from flask import Flask
from flask import render_template
from flask import request
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row

    recipes = connection.execute(
        "SELECT * FROM recipes ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return render_template("index.html", recipes=recipes)

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

@app.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row

    recipe = connection.execute(
        "SELECT * FROM recipes WHERE id = ?",
        (recipe_id,)
    ).fetchone()

    connection.close()

    return render_template("recipe.html", recipe=recipe)
