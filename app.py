from flask import Flask, render_template, request, session
from flask import redirect, url_for
from flask import render_template
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
app = Flask(__name__)
app.secret_key = "change-this-later"

@app.route("/")
def index():
    query = request.args.get("query")

    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row

    if query:
        recipes = connection.execute(
            """
            SELECT * FROM recipes
            WHERE title LIKE ? OR ingredients LIKE ? OR instructions LIKE ?
            ORDER BY id DESC
            """,
            (f"%{query}%", f"%{query}%", f"%{query}%")
        ).fetchall()
    else:
        recipes = connection.execute(
            "SELECT * FROM recipes ORDER BY id DESC"
        ).fetchall()

    connection.close()

    return render_template("index.html", recipes=recipes)

@app.route("/add", methods=["GET", "POST"])
def add():

    if "user_id" not in session:
        return redirect(url_for("login"))

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
            (title, ingredients, instructions, price, servings, user_id)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (title, ingredients, instructions, price, servings, session ["user_id"])
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

@app.route("/recipe/<int:recipe_id>/edit", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row

    recipe = connection.execute(
        "SELECT * FROM recipes WHERE id = ?",
        (recipe_id,)
    ).fetchone()

    if recipe is None:
        connection.close()
        return "Reseptiä ei löytynyt"

    if recipe["user_id"] != session["user_id"]:
        connection.close()
        return "Et voi muokata tätä reseptiä"

    if request.method == "POST":
        title = request.form["title"]
        ingredients = request.form["ingredients"]
        instructions = request.form["instructions"]
        price = request.form["price"]
        servings = request.form["servings"]

        connection.execute(
            """
            UPDATE recipes
            SET title = ?, ingredients = ?, instructions = ?, price = ?, servings = ?
            WHERE id = ?
            """,
            (title, ingredients, instructions, price, servings, recipe_id)
        )

        connection.commit()
        connection.close()

        return redirect(url_for("recipe", recipe_id=recipe_id))

    connection.close()

    return render_template("edit_recipe.html", recipe=recipe)

@app.route("/recipe/<int:recipe_id>/delete", methods=["POST"])
def delete_recipe(recipe_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row

    recipe = connection.execute(
        "SELECT * FROM recipes WHERE id = ?",
        (recipe_id,)
    ).fetchone()

    if recipe is None:
        connection.close()
        return "Reseptiä ei löytynyt"

    if recipe["user_id"] != session["user_id"]:
        connection.close()
        return "Et voi poistaa tätä reseptiä"

    connection.execute(
        "DELETE FROM recipes WHERE id = ?",
        (recipe_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        password_hash = generate_password_hash(
        password,
        method="pbkdf2:sha256"
    )

        connection = sqlite3.connect("database.db")

        connection.execute(
            """
            INSERT INTO users (username, password_hash)
            VALUES (?, ?)
            """,
            (username, password_hash)
        )

        connection.commit()
        connection.close()

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        connection = sqlite3.connect("database.db")
        connection.row_factory = sqlite3.Row

        user = connection.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return "Kirjautuminen onnistui"

        return "Väärä käyttäjänimi tai salasana"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))







