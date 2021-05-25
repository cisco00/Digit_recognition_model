from PIL import Image
import numpy as np
from tensorflow.keras.applications.imagenet_utils import decode_predictions
import tensorflow as tf


def load_models():
    models = tf.keras.applications.load_model("test_model.h5")
    print("model loaded successfully")
    return models


def predict(image: Image.Image):
    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0

    result = decode_predictions(load_models.predict(image), 2)[0]

    response = []

    for i, res in enumerate(result):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2] * 100:0.2f} %"

        response.append(resp)

    return response
