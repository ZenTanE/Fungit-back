from RequestHandler import RequestHandler
from Connection import connection as db
from flask import Flask, jsonify, request as req
from entities.images import Image
from autogluon.multimodal import MultiModalPredictor

MODEL_PATH = "../data/"
app = Flask(__name__)

if db.connection is None:
    db.initConnection()

@app.route("/chatbot-messages/", methods = ["GET"])
def getChatbotMessages():
    return jsonify(RequestHandler.getChatbotMessages())

@app.route("/identify-mushroom/", methods = ["POST"])
def identifyMushroom():
    data = req.form.to_dict()
    image = Image(data)
    return jsonify(RequestHandler.identifyMushroom(image))

@app.route("/test/", methods = ["POST"])
def test():
    data = req.form.to_dict()
    predictor = MultiModalPredictor.load("f{MODEL_PATH}mushroom_model")
    return jsonify(RequestHandler.test(data, predictor))

@app.route("/dummy/", methods = ["POST"])
def dummy():
    data = req.form.to_dict()
    return jsonify(RequestHandler.test(data))

@app.route("/ask-chatbot/", methods=["POST"])
def askChatbot():
    data = req.form.to_dict()
    return jsonify(RequestHandler.askChatbot(data))

@app.route("/train-model/", methods=["PATCH"])
def trainModel():
    return jsonify(RequestHandler.trainModel())