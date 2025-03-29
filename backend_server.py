from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(_name_)
app.config["JWT_SECRET_KEY"] = "panconwebito" 

jwt = JWTManager(app)

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if _name_ == "_main_":
    app.run(port=5001, debug=True)