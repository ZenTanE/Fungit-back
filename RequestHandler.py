from autogluon.multimodal import MultiModalPredictor
class RequestHandler:
    
    MODEL_PATH = "../data/"
    
    @staticmethod
    def getChatbotMessages():
        pass

    @staticmethod
    def identifyMushroom(image):
        predictor = MultiModalPredictor.load("f{MODEL_PATH}mushroom_model")
        image_path = image.GetImageLink()
        prediction = predictor.predict([image_path])
        return prediction[0]
    
    @staticmethod
    def test(image, predictor):
        # predictor = predictor
        image_path = image.GetImageLink()
        prediction = predictor.predict([image_path])
        return prediction[0]

    @staticmethod
    def askChatbot(message):
        pass

    @staticmethod
    def trainModel():
        pass