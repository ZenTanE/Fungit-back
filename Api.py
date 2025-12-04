from RequestHandler import RequestHandler
from Connection import connection as db
from flask import Flask, jsonify, request as req

app = Flask(__name__)

if db.connection is None:
    db.initConnection()

@app.route("/chatbot-messages/", methods = ["GET"])
def getChatbotMessages():
    return jsonify(RequestHandler.getChatbotMessages())

@app.route("/identify-mushroom/", methods = ["POST"])
def identifyMushroom():
    data = req.form.to_dict()
    return jsonify(RequestHandler.identifyMushroom(data))

@app.route("/ask-chatbot/", methods=["POST"])
def askChatbot():
    data = req.form.to_dict()
    return jsonify(RequestHandler.askChatbot(data))

@app.route("/train-model/", methods=["PATCH"])
def trainModel():
    return jsonify(RequestHandler.trainModel())