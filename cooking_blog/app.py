from flask import Flask, request, jsonify, session, render_template, send_from_directory
from flask_cors import CORS
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
app.secret_key = 'super-secret-key-for-session'
CORS(app, supports_credentials=True)

DB_FILE = 'users.json'
RECIPES_DB_FILE = 'recipes.json'

def load_db():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def load_recipes_db():
    if not os.path.exists(RECIPES_DB_FILE):
        return []
    try:
        with open(RECIPES_DB_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_recipes_db(data):
    with open(RECIPES_DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

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
    
    users = load_db()
    if any(u['username'] == username or u['email'] == email for u in users):
        return jsonify({"error": "User already exists"}), 400
    
    new_user = {
        "username": username,
        "email": email,
        "password": generate_password_hash(password)
    }
    users.append(new_user)
    save_db(users)
    return jsonify({"message": "User registered"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    username = data.get('username')
    password = data.get('password')
    
    users = load_db()
    user = next((u for u in users if u['username'] == username), None)
    
    if user and check_password_hash(user['password'], password):
        session['user'] = user['username']
        session.permanent = True
        return jsonify({"message": "Logged in", "username": user['username']}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    new_password = data.get('password')
    
    if not email or not new_password:
        return jsonify({"error": "Missing email or password"}), 400
        
    users = load_db()
    user_idx = next((i for i, u in enumerate(users) if u['email'] == email), None)
    
    if user_idx is None:
        return jsonify({"error": "No user found with this email"}), 404
        
    users[user_idx]['password'] = generate_password_hash(new_password)
    save_db(users)
    return jsonify({"message": "Password updated successfully"}), 200

@app.route('/api/logout', methods=['POST'])
def logout_route():
    session.pop('user', None)
    return jsonify({"message": "Logged out"}), 200

@app.route('/api/me', methods=['GET'])
def get_me():
    if 'user' in session:
        users = load_db()
        user = next((u for u in users if u['username'] == session['user']), None)
        if user:
            return jsonify({
                "username": user['username'],
                "email": user['email']
            }), 200
    return jsonify({"error": "Not authenticated"}), 401

@app.route('/api/me', methods=['PATCH'])
def update_me():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()
    users = load_db()
    user_idx = next((i for i, u in enumerate(users) if u['username'] == session['user']), None)
    
    if user_idx is None:
        return jsonify({"error": "User not found"}), 404
        
    user = users[user_idx]
    old_username = user['username']
    
    # Update username
    new_username = data.get('username')
    if new_username and new_username != old_username:
        if any(u['username'] == new_username for u in users):
            return jsonify({"error": "Username already taken"}), 400
        user['username'] = new_username
        session['user'] = new_username
        
        # Update author in recipes
        recipes = load_recipes_db()
        for r in recipes:
            if r['author'] == old_username:
                r['author'] = new_username
        save_recipes_db(recipes)

    # Update password
    new_password = data.get('password')
    if new_password:
        user['password'] = generate_password_hash(new_password)
        
    save_db(users)
    return jsonify({"message": "Profile updated", "username": user['username']}), 200

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = load_recipes_db()
    username = request.args.get('username')
    chapter = request.args.get('chapter')
    
    filtered_recipes = recipes
    if username:
        filtered_recipes = [r for r in filtered_recipes if r['author'] == username]
    
    if chapter:
        filtered_recipes = [r for r in filtered_recipes if r.get('chapter', '').lower() == chapter.lower()]
        
    return jsonify(filtered_recipes)

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipes = load_recipes_db()
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({"error": "Recipe not found"}), 404

@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Invalid recipe data"}), 400

    recipes = load_recipes_db()
    new_id = 1
    if recipes:
        new_id = max(r['id'] for r in recipes) + 1

    new_recipe = {
        "id": new_id,
        "title": data.get('title'),
        "description": data.get('description', ''),
        "ingredients": data.get('ingredients', []),
        "steps": data.get('steps', []),
        "cookingTime": data.get('cookingTime', 0),
        "difficulty": data.get('difficulty', 'Medium'),
        "chapter": data.get('chapter', 'Meals'),
        "imageUrl": data.get('imageUrl', ''),
        "author": session['user']
    }
    recipes.append(new_recipe)
    save_recipes_db(recipes)
    return jsonify(new_recipe), 201

@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()
    recipes = load_recipes_db()
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    
    if recipe['author'] != session['user']:
        return jsonify({"error": "You can only edit your own recipes"}), 403
        
    recipe.update({
        "title": data.get('title', recipe['title']),
        "description": data.get('description', recipe['description']),
        "ingredients": data.get('ingredients', recipe['ingredients']),
        "steps": data.get('steps', recipe['steps']),
        "cookingTime": data.get('cookingTime', recipe['cookingTime']),
        "difficulty": data.get('difficulty', recipe['difficulty']),
        "chapter": data.get('chapter', recipe.get('chapter', 'Meals')),
        "imageUrl": data.get('imageUrl', recipe['imageUrl'])
    })
    save_recipes_db(recipes)
    return jsonify(recipe)

@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    recipes = load_recipes_db()
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
        
    if recipe['author'] != session['user']:
        return jsonify({"error": "You can only delete your own recipes"}), 403
        
    recipes = [r for r in recipes if r['id'] != recipe_id]
    save_recipes_db(recipes)
    return jsonify({"message": "Recipe deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
