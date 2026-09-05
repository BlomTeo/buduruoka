from flask import Flask
from flask import render_template
from flask import request
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        title = request.form["title"]
        ingredients = request.form["ingredients"]
        instructions = request.form["instructions"]
        price = request.form["price"]
        servings = request.form["servings"]

        connection = sqlite3.connect("database.db")

        connection.execute(
            """
            INSERT INTO recipes
            (title, ingredients, instructions, price, servings)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, ingredients, instructions, price, servings)
        )

        connection.commit()
        connection.close()

    return render_template("add.html")

