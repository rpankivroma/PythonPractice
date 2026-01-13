# Gourmet Share - Modern Cooking Blog

A full-stack culinary platform where home cooks and professional chefs can share, discover, and manage recipes. Built with Flask (Python) backend and vanilla JavaScript frontend.

## 🚀 Features

- **User Authentication**: Secure registration and login system with password hashing.
- **Recipe Management**: Create, read, update, and delete (CRUD) your own recipes.
- **Recipe Discovery**: Browse recipes shared by the community with filtering by author.
- **Detailed Profiles**: Manage your personal profile, update username/password, and view your contributed recipes.
- **Rich Recipe Editor**: Add ingredients, cooking steps, difficulty levels, and cooking times.
- **Responsive Design**: Modern, mobile-friendly interface with light/dark mode readiness.

## 🛠️ Tech Stack

### Backend
- **Python (Flask)**: Lightweight WSGI web application framework.
- **JSON Database**: Simple file-based persistence for Users (`users.json`) and Recipes (`recipes.json`).
- **Werkzeug Security**: Secure password hashing using scrypt.
- **Flask-CORS**: Handling Cross-Origin Resource Sharing.

### Frontend
- **HTML5 & CSS3**: Custom responsive styling using modern CSS variables.
- **Vanilla JavaScript**: Lightweight client-side logic for API interactions and DOM manipulation.
- **Fetch API**: Asynchronous communication with the backend.

## 📂 Project Structure

```
├── app.py                # Main Flask application entry point
├── users.json            # JSON database for user credentials
├── recipes.json          # JSON database for recipes
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Global styles and responsive design
│   └── js/
│       └── auth.js       # Authentication logic and API wrapper
├── templates/            # HTML Templates
│   ├── index.html        # Homepage and recipe feed
│   ├── profile.html      # User profile and recipe management
│   └── recipe.html       # Single recipe view
└── README.md             # Project documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/rpankivroma/PythonPractice/tree/3a9dbcb57759e7f16d4c3fb531867100b2baeaf5/cooking_blog
   ```

2. **Install Dependencies**
   Ensure you have Python 3.8+ installed.
   ```bash
   pip install flask flask-cors werkzeug
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```
   The server will start at `http://localhost:5000`.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/register` | Register a new user |
| `POST` | `/api/login` | Authenticate user |
| `GET` | `/api/me` | Get current user info |
| `PATCH` | `/api/me` | Update profile (username/password) |
| `GET` | `/api/recipes` | Get all recipes (or filter by `?username=`) |
| `POST` | `/api/recipes` | Create a new recipe |
| `GET` | `/api/recipes/<id>` | Get specific recipe details |
| `PUT` | `/api/recipes/<id>` | Update a recipe (Author only) |
| `DELETE` | `/api/recipes/<id>` | Delete a recipe (Author only) |

## 🛡️ Security Note
This project uses JSON files for data persistence which is excellent for prototypes and learning. For production environments, it is recommended to migrate to a robust database system like PostgreSQL or SQLite.

## 📄 License
This project is open source and available under the [MIT License](LICENSE).