from flask import Flask
from api.user import user_service

app = Flask(__name__)

# Register blueprints
app.register_blueprint(user_service, url_prefix="/api/user")

if __name__ == "__main__":
    app.run(debug=True)
