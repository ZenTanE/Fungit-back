from flask import Flask, jsonify, request as req

app = Flask(__name__)

@app.route("/chatbot-messages/", methods = ["GET"])
def getChatbotMessages():
    pass

@app.route("/identify-mushroom/", methods = ["POST"])
def identifyMushroom():
    pass

@app.route("/ask-chatbot/", methods=["POST"])
def askChatbot():
    pass

@app.route("/train-model/", methods=["PATCH"])
def trainModel():
    pass