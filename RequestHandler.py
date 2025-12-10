import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

class RequestHandler:

    @staticmethod
    def getChatbotMessages():
        pass

    @staticmethod
    def identifyMushroom(image, predictor, index_to_name):
        print("identifyMushroom")
        image_path = image.GetImageLink()

        img = load_img(image_path, target_size=(224, 224))
        x = img_to_array(img) / 255.0
        x = np.expand_dims(x, axis=0)

        prediction = predictor.predict(x)[0]

        top3_index = prediction.argsort()[-3:][::-1]
        top3_probs = prediction[top3_index]

        results = []
        for idx, prob in zip(top3_index, top3_probs):
            results.append({
                "name": index_to_name[idx],
                "score": float(prob)
            })

        return {"results": results}
    
    @staticmethod
    def test(image, predictor):
        # predictor = predictor
        image_path = image.GetImageLink()
        prediction = predictor.predict([image_path])
        return prediction[0]
    
    @staticmethod
    def dummy(image):
        image_path = image.GetImageLink()
        if image_path:
            return "imagen recibida"
        else:
            return "error"

    @staticmethod
    def askChatbot(message):
        pass

    @staticmethod
    def trainModel():
        pass