import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from langchain_core.messages import HumanMessage

class RequestHandler:

    @staticmethod
    def getChatbotMessages():
        pass

    @staticmethod
    def identifyMushroom(image, predictor, index_to_name):
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
    def askChatbot(message, chat_model):
        response = chat_model.invoke(message)
        
        return {"response": response.content}
    
    @staticmethod
    def getMushroomInfo(mushroom_name, chat_model):
        prompt = f"""Eres un experto en micología. Para el hongo llamado '{mushroom_name}', 
        proporciona la siguiente información EXCLUSIVAMENTE en formato JSON:

        INFORMACIÓN REQUERIDA:
        1. ¿Cuál es su nombre común? (Breve respuesta)
        2. ¿Es comestible? (Respuesta: "sí", "no")
        3. ¿Dónde suelen crecer? (Breve descripción, máximo 20 palabras)
        4. ¿Es venenoso? (Respuesta: "sí", "no" o "parcialmente")
        5. ¿Cómo se suele cocinar/preparar? (Breve descripción, máximo 40 palabras)
        6. Advertencias importantes sobre consumo (si aplica)

        REGLAS IMPORTANTES:
        - El json debe tener estos campos:
          "nombre_cientifico":
          "nombre_comun":
          "es_comestible":
          "donde_crecen":
          "venenoso":
          "como_cocinar":
          "advetencias":
        - Si no conoces el hongo, déjalo claro en el inicio de la respuesta
        - Sé preciso y basado en hechos científicos
        """
        
        response = chat_model.invoke(prompt)

        return {"response": response.content}

    @staticmethod
    def trainModel():
        pass