from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from datetime import timedelta

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret_key"  
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)

jwt = JWTManager(app)

fake_users_db = {
    "usuario1": "password123"
}

@app.route("/token", methods=["POST"])
def generate_token():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Validación de usuario y contraseña
    if fake_users_db.get(username) == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Credenciales inválidas"}), 401

if __name__ == "__main__":
    app.run(port=5000, debug=True)
