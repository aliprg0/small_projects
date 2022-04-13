from tvDatafeed import TvDatafeed, Interval
import talib
from talib import abstract
from time import sleep

def download_db(symbol,name_of_the_market,time_frame):
    #username,password = get_username_password() There are some problem I'll solve...
    # ...later so for now we have some limitation but it won't bother us    
    tv = TvDatafeed()
    data = tv.get_hist(symbol=symbol,exchange=name_of_the_market,interval=time_frame,n_bars=100)
    return data

def analyze_the_data(data,symbol,time_frame):
    buy_patterns = []
    sell_patterns = []

    for pattern in talib.get_function_groups()["Pattern Recognition"]:

        function = abstract.Function(pattern)
        result = function(data["open"], data["high"],
        data["low"], data["close"])
        last_candle_result = result[-1]

        if last_candle_result == -100:
            sell_patterns.append(pattern)
        elif last_candle_result == 100:
            buy_patterns.append(pattern)
        
        if len(buy_patterns) > len(sell_patterns):
            suggest = "Buy 📈"
        elif len(buy_patterns) < len(sell_patterns):
            suggest = "Sell 📉"    
        else:
            suggest = "Neutral"

    result = f"""📊 Result For {symbol} {time_frame}:
 🟢 Buys: {len(buy_patterns)} | 🔴Sells: {len(sell_patterns)}
 🟩 Buy Patterns: {buy_patterns} 
 🟥Sell Patterns: {sell_patterns}
 🔎  Suggestion: {suggest}
"""
    return result


#This is the Main method 
# USE this
    
def full_analyzer(symbol,market):
 results = []
 for time_frame in Interval:
    data = download_db(symbol,market,time_frame)
    analyzation_result = analyze_the_data(data,symbol,time_frame=time_frame)
    results.append(analyzation_result)
    sleep(3)
 return results



if __name__ == "__main__":

    data = full_analyzer("btcusdt","binance")
    print(data)