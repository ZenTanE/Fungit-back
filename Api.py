import json
from RequestHandler import RequestHandler
import Connection as db
from flask import Flask, jsonify, request as req
from flask_cors import CORS
from entities.images import Image
from tensorflow.keras.models import load_model
from langchain_google_genai import ChatGoogleGenerativeAI
import os

MODEL_PATH = "data/"
app = Flask(__name__)
CORS(app)

with open(f"{MODEL_PATH}mushroom_model_labels.json", "r", encoding="utf-8") as f:
    class_dict = json.load(f)

index_to_name = {v: k for k, v in class_dict.items()}

predictor = load_model(f"{MODEL_PATH}mushroom_model_current.keras")

chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

if db.connection is None:
    db.initConnection()

@app.route("/chatbot-messages/", methods = ["GET"])
def getChatbotMessages():
    return jsonify(RequestHandler.getChatbotMessages())

@app.route("/identify-mushroom/", methods = ["POST"])
def identifyMushroom():
    if "file" not in req.files:
        return jsonify({"error": "No file provided"}), 400

    os.makedirs("tmp", exist_ok=True)

    file = req.files["file"]
    path = f"./tmp/{file.filename}"
    file.save(path)

    image = Image(path)
    return jsonify(RequestHandler.identifyMushroom(image, predictor, index_to_name))

@app.route("/ask-chatbot/", methods=["POST"])
def ask_chatbot():
    data = req.get_json()
    message = data.get("message")

    if not message:
        return "Message is required", 400  
    
    return jsonify(RequestHandler.askChatbot(message, chat_model))

@app.route("/get-mushroom-info/", methods=["POST"])
def get_mushroom_info():
    data = req.get_json()
    mushroom_name = data.get("mushroom_name")

    if not mushroom_name:
        return jsonify({"error": "Mushroom name is required"}), 400

    return jsonify(RequestHandler.getMushroomInfo(mushroom_name, chat_model))

@app.route("/train-model/", methods=["PATCH"])
def trainModel():
    return jsonify(RequestHandler.trainModel())

@app.route("/login/", methods=["POST"])
def login():
    userInfo = req.get_json()
    return jsonify(RequestHandler.login(userInfo))

@app.route("/signup/", methods=["POST"])
def signup():
    userInfo = req.get_json()
    return jsonify(RequestHandler.signup(userInfo))

@app.route("/")
def home():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)