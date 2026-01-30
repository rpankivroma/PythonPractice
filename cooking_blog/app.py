from flask import Flask, request, jsonify, session, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
app.secret_key = 'super-secret-key-for-session'
CORS(app, supports_credentials=True)

# MySQL Configuration using SQLAlchemy with PyMySQL driver
# Format: mysql+pymysql://username:password@localhost/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/CookingBlog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models matching your SQL structure
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    bank_name = db.Column(db.String(255), nullable=True)
    card_number = db.Column(db.String(255), nullable=True)
    card_holder_name = db.Column(db.String(255), nullable=True)

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    ingredients = db.Column(db.JSON)
    steps = db.Column(db.JSON)
    cooking_time = db.Column(db.Integer)
    difficulty = db.Column(db.String(50))
    chapter = db.Column(db.String(100))
    image_url = db.Column(db.Text)
    author = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    for_sale = db.Column(db.Boolean, default=False)
    price = db.Column(db.Float, nullable=True)

class Deal(db.Model):
    __tablename__ = 'deals'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='created')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page>.html')
def render_page(page):
    return render_template(f'{page}.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400
    
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "User already exists"}), 400
    
    new_user = User(
        username=username,
        email=email,
        password=generate_password_hash(password)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        session['user'] = user.username
        session.permanent = True
        return jsonify({"message": "Logged in", "username": user.username}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400
        
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "No user found with this email"}), 404
        
    user.password = generate_password_hash(password)
    db.session.commit()
    return jsonify({"message": "Password updated successfully"}), 200

@app.route('/api/logout', methods=['POST'])
def logout_route():
    session.pop('user', None)
    return jsonify({"message": "Logged out"}), 200

@app.route('/api/me', methods=['GET'])
def get_me():
    if 'user' in session:
        user = User.query.filter_by(username=session['user']).first()
        if user:
            return jsonify({
                "username": user.username,
                "email": user.email,
                "bankName": user.bank_name,
                "cardNumber": user.card_number,
                "cardHolderName": user.card_holder_name
            }), 200
    return jsonify({"error": "Not authenticated"}), 401

@app.route('/api/me', methods=['PATCH'])
def update_me():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()
    old_username = session['user']
    user = User.query.filter_by(username=old_username).first()
    
    if not user:
        return jsonify({"error": "User not found"}), 404

    new_username = data.get('username')
    if new_username and new_username != old_username:
        if User.query.filter_by(username=new_username).first():
            return jsonify({"error": "Username already taken"}), 400
        
        Recipe.query.filter_by(author=old_username).update({Recipe.author: new_username})
        user.username = new_username
        session['user'] = new_username

    new_password = data.get('password')
    if new_password:
        user.password = generate_password_hash(new_password)
    
    if 'bankName' in data:
        user.bank_name = data.get('bankName')
    if 'cardNumber' in data:
        user.card_number = data.get('cardNumber')
    if 'cardHolderName' in data:
        user.card_holder_name = data.get('cardHolderName')
        
    db.session.commit()
    return jsonify({"message": "Profile updated", "username": session['user']}), 200

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    username = request.args.get('username')
    chapter = request.args.get('chapter')
    
    query = Recipe.query
    if username:
        query = query.filter_by(author=username)
    if chapter:
        query = query.filter(Recipe.chapter.ilike(chapter))
        
    recipes = query.all()
    
    return jsonify([{
        "id": r.id,
        "title": r.title,
        "description": r.description,
        "ingredients": r.ingredients,
        "steps": r.steps,
        "cookingTime": r.cooking_time,
        "difficulty": r.difficulty,
        "chapter": r.chapter,
        "imageUrl": r.image_url,
        "author": r.author,
        "forSale": r.for_sale,
        "price": r.price
    } for r in recipes])

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        return jsonify({
            "id": recipe.id,
            "title": recipe.title,
            "description": recipe.description,
            "ingredients": recipe.ingredients,
            "steps": recipe.steps,
            "cookingTime": recipe.cooking_time,
            "difficulty": recipe.difficulty,
            "chapter": recipe.chapter,
            "imageUrl": recipe.image_url,
            "author": recipe.author,
            "forSale": recipe.for_sale,
            "price": recipe.price
        })
    return jsonify({"error": "Recipe not found"}), 404

@app.route('/api/recipes/<int:recipe_id>/author-bank', methods=['GET'])
def get_recipe_author_bank(recipe_id):
    if 'user' not in session:
        return jsonify({"error": "Please log in to view payment details"}), 401
    
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    
    if not recipe.for_sale:
        return jsonify({"error": "This recipe is not for sale"}), 400
    
    author = User.query.filter_by(username=recipe.author).first()
    if not author:
        return jsonify({"error": "Author not found"}), 404
    
    return jsonify({
        "recipeTitle": recipe.title,
        "price": recipe.price,
        "authorName": author.username,
        "bankName": author.bank_name,
        "cardNumber": author.card_number,
        "cardHolderName": author.card_holder_name
    })

@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Invalid recipe data"}), 400

    new_recipe = Recipe(
        title=data.get('title'),
        description=data.get('description', ''),
        ingredients=data.get('ingredients', []),
        steps=data.get('steps', []),
        cooking_time=data.get('cookingTime', 0),
        difficulty=data.get('difficulty', 'Medium'),
        chapter=data.get('chapter', 'Meals'),
        image_url=data.get('imageUrl', ''),
        author=session['user'],
        for_sale=data.get('forSale', False),
        price=data.get('price') if data.get('forSale') else None
    )
    db.session.add(new_recipe)
    db.session.commit()
    
    return jsonify({"id": new_recipe.id, "message": "Recipe created"}), 201

@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()
    recipe = Recipe.query.get(recipe_id)
    
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    
    if recipe.author != session['user']:
        return jsonify({"error": "You can only edit your own recipes"}), 403
        
    recipe.title = data.get('title', recipe.title)
    recipe.description = data.get('description', recipe.description)
    recipe.ingredients = data.get('ingredients', recipe.ingredients)
    recipe.steps = data.get('steps', recipe.steps)
    recipe.cooking_time = data.get('cookingTime', recipe.cooking_time)
    recipe.difficulty = data.get('difficulty', recipe.difficulty)
    recipe.chapter = data.get('chapter', recipe.chapter)
    recipe.image_url = data.get('imageUrl', recipe.image_url)

    if 'forSale' in data:
        recipe.for_sale = data.get('forSale', False)
        recipe.price = data.get('price') if data.get('forSale') else None
    db.session.commit()
    return jsonify({"message": "Recipe updated"})

@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    recipe = Recipe.query.get(recipe_id)
    
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
        
    if recipe.author != session['user']:
        return jsonify({"error": "You can only delete your own recipes"}), 403
        
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Recipe deleted"}), 200

@app.route('/api/deals', methods=['POST'])
def create_deal():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()
    recipe_id = data.get('recipe_id')
    
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
        
    buyer = User.query.filter_by(username=session['user']).first()
    author = User.query.filter_by(username=recipe.author).first()
    
    if not buyer or not author:
        return jsonify({"error": "User not found"}), 404
        
    new_deal = Deal(
        recipe_id=recipe.id,
        buyer_id=buyer.id,
        author_id=author.id,
        price=recipe.price,
        status='created'
    )
    
    db.session.add(new_deal)
    db.session.commit()
    
    return jsonify({"message": "Deal created", "id": new_deal.id}), 201

@app.route('/api/deals/<int:deal_id>', methods=['PATCH'])
def update_deal(deal_id):
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    data = request.get_json()
    status = data.get('status')
    
    print(f"DEBUG: Updating deal {deal_id} with status: '{status}'")
    
    deal = Deal.query.get(deal_id)
    if not deal:
        return jsonify({"error": "Deal not found"}), 404
    
    if status is not None:
        deal.status = status
        db.session.commit()
        print(f"DEBUG: Deal {deal_id} status updated to: '{deal.status}'")
        
    return jsonify({"message": "Deal updated"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)