from sys import intern
from typing import final
import pandas
import tvDatafeed as tv
import talib
from talib import abstract
from tvDatafeed import main
from tvDatafeed import Interval
import datetime as dt
from datetime import datetime
import time

#crypto_list = ["btcusdt","ethusdt","ltcusdt","adausdt","soluusdt","bnbusdt","xrpusdt"]

data_error_message =  "An error occured when I was trying to get data. Check the details you've sent."

def return_time(time):
    try:
       if time == "1h":
           return Interval.in_1_hour
       elif time =="15m":
           return Interval.in_15_minute
       elif time == "30m":
           return Interval.in_30_minute
       elif time == "1m":
           return Interval.in_1_minute
       elif time == "5m":
           return Interval.in_5_minute
       elif time == "4h":
           return Interval.in_4_hour
       elif time == "2h":
           return Interval.in_2_hour
       elif time == "3h":
           return Interval.in_3_hour
       elif time == "3m":
           return Interval.in_3_minute
       elif time == "45m":
           return Interval.in_45_minute
       elif time == "1d":
           return Interval.in_daily
       elif time == "1w":
           return Interval.in_weekly
       elif time == "1M":
           return Interval.in_monthly

    except:
        return "Unknown time format"
    

#def check_if_it_is_crypto(stock_name):
    
    #if stock_name in crypto_list:
     #   return "Binance"
    

def get_data(stock_name, market, time_frame):

    #if market == "":
    #    market = check_if_it_is_crypto(stock_name)

    #if market == "binance":
    #    market = "Binance"


    try:
        
    
        client = tv.TvDatafeed(chromedriver_path=None)
        
 
        data = client.get_hist(
            stock_name, market, interval=time_frame ,n_bars=50)
     
      
        
        return data
    except:
        return data_error_message


def analyzer(stock_name, data,time_frame):
    try:
           buy_pattern_names = []
           sell_patterns_names = []
        
           buy_patterns_count = 0
           sell_patterns_count = 0
        
           whattodo = ""
        
           for pattern in talib.get_function_groups()["Pattern Recognition"]:

               function = abstract.Function(pattern)

               result = function(data["open"], data["high"],
                                 data["low"], data["close"])

               yesterday_result = int(result[-1])
               

               if yesterday_result == 100:
                   buy_pattern_names.append(pattern)
                   buy_patterns_count += 1
               if yesterday_result == -100:
                   sell_patterns_names.append(pattern)
                   sell_patterns_count += 1

               if buy_patterns_count > sell_patterns_count:
                  whattodo = "Suggest to Buy"
               elif buy_patterns_count < sell_patterns_count:
                   whattodo = "Suggest to Sell"
               else: 
                whattodo = "No suggestion" 
            
        
           return(f"*** Final result for {str(stock_name).upper()} {str(time_frame).upper()} ***\n"
            f"Buy  Patterns : {str(buy_patterns_count)} \n"
            f"Sell Patterns : {str(sell_patterns_count)} \n" 
            f"Condition : {whattodo}\n"
            f"Buy pattern's names : {buy_pattern_names}\n"
            f"Sell pattern's names : {sell_patterns_names}\n"
             "THIS IS NOT A FINANCIAL ORDER\n"
             "DO NOT trade based on this message and check your strategy.")

    except:
        
       return "Sorry! A error occured while processing data. Try again. "


def calculate(stock_name,market,time_frame):
     
    print(f"{stock_name} - {market} - {time_frame}")
    
    returned_time_frame = return_time(time_frame)
    if returned_time_frame == "Unknown time format":
        return "Unknown time format"

    data = get_data(stock_name,market,returned_time_frame) 

    
    if isinstance(data, str):
         if data == data_error_message:
             return(data_error_message)
    else:
         final_result = analyzer(stock_name, data,time_frame)
         now = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
         
      
         with open(f"{stock_name}_{market}_{time_frame}_{now}.txt","a") as f:
             f.write(final_result)
             f.close()
         return final_result








    
