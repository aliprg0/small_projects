from flask import request,Flask,jsonify
from db_methods import get_all_books,search_in_db,add_in_db

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/search",methods=["Get"])
def search_a_book():
    if "id" in request.args:
        id = request.args.get("id")
        result = search_in_db(id)
        return jsonify(result)
    else:
        return "Sorry, Something went wrong"

@app.route("/",methods=["Get"])
def home_page():
    return "Hey! This is the main page"


@app.route("/books/",methods=["Get"])
def return_all_books():
    books = get_all_books()
    return jsonify(books)

@app.route("/add/book",methods=["Post"])
def add_a_book():
    if "id" and "name" in request.args:
        id = request.args.get("id")
        name = request.args.get("name")
        result = add_in_db(id,name)
        return result
    else:
        return "Something went wrong!"
app.run()


