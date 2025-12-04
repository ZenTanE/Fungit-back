from RequestHandler import RequestHandler
from flask import Flask, jsonify, request as req

app = Flask(__name__)

@app.route("/chatbot-messages/", methods = ["GET"])
def getChatbotMessages():
    return jsonify(RequestHandler.getChatbotMessages())

@app.route("/identify-mushroom/", methods = ["POST"])
def identifyMushroom():
    return jsonify(RequestHandler.identifyMushroom())

@app.route("/ask-chatbot/", methods=["POST"])
def askChatbot():
    return jsonify(RequestHandler.askChatbot())

@app.route("/train-model/", methods=["PATCH"])
def trainModel():
    return jsonify(RequestHandler.trainModel())