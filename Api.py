import json
from RequestHandler import RequestHandler
# from Connection import connection as db
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

# Configurar el modelo de IA
chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# if db.connection is None:
#     db.initConnection()

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

@app.route("/test/", methods = ["POST"])
def test():
    data = req.file["file"]
    return jsonify(RequestHandler.test(data, predictor))

@app.route("/dummy/", methods = ["POST"])
def dummy():
    data = req.form.to_dict()
    return jsonify(RequestHandler.test(data))

@app.route("/ask-chatbot/", methods=["POST"])
def ask_chatbot():
    message = req.get_data(as_text=True).strip()  # Get plain text from the body

    if not message:
        return "Message is required", 400  # Return plain text error message

    # Pass the message to the RequestHandler to get a response from the chatbot
    chatbot_response = RequestHandler.askChatbot(message, chat_model)

    # Return the response as plain text
    return chatbot_response

@app.route("/get-mushroom-info/", methods=["POST"])
def get_mushroom_info():
    data = req.get_json()
    mushroom_name = data.get("mushroom_name")
#    language = data.get("language", "es")  # Default to Spanish if not specified

    if not mushroom_name:
        return jsonify({"error": "Mushroom name is required"}), 400

    return jsonify(RequestHandler.getMushroomInfo(mushroom_name, chat_model))

@app.route("/train-model/", methods=["PATCH"])
def trainModel():
    return jsonify(RequestHandler.trainModel())

@app.route("/")
def home():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # Obtén el puerto de Render, por defecto 5000 para pruebas locales
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' es obligatorio para que Render pueda enrutar
    app.run(host="0.0.0.0", port=port)