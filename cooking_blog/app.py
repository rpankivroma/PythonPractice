from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User, Recipe, Comment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()

# Головна сторінка
@app.route("/")
def index():
    recipes = Recipe.query.order_by(Recipe.created_at.desc()).all()
    return render_template("index.html", recipes=recipes)

# Реєстрація
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        password = generate_password_hash(request.form["password"])
        user = User(username=request.form["username"], password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

# Логін
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("profile"))
    return render_template("login.html")

# Профіль
@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", recipes=current_user.recipes)

# Створення рецепту
@app.route("/recipe/new", methods=["GET", "POST"])
@login_required
def new_recipe():
    if request.method == "POST":
        recipe = Recipe(
            title=request.form["title"],
            content=request.form["content"],
            author=current_user
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("profile"))
    return render_template("recipe_form.html")

# Деталі рецепту + коментарі
@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe_detail(id):
    recipe = Recipe.query.get_or_404(id)
    if request.method == "POST":
        comment = Comment(text=request.form["comment"], recipe=recipe)
        db.session.add(comment)
        db.session.commit()
    return render_template("recipe_detail.html", recipe=recipe)

# Видалення рецепту
@app.route("/recipe/delete/<int:id>")
@login_required
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    if recipe.author == current_user:
        db.session.delete(recipe)
        db.session.commit()
    return redirect(url_for("profile"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
