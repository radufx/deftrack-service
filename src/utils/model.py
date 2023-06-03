import requests
import tensorflow as tf
import numpy as np
from PIL import Image


class PredictionModel():
    def __init__(self) -> None:
        self.__model = tf.keras.models.load_model(
            "assets/models/u-net/model")
        self.__threshold_value = 0.6

    def getVegetationRate(self, image):
        predicted = self.__model.predict(image)
        predicted = np.where(predicted > self.__threshold_value, 1, 0)
        vegetation_pixels = np.count_nonzero(
            predicted <= self.__threshold_value)

        return vegetation_pixels / predicted.size

    def getImageVegetationRate(self, url):
        requested_image = requests.get(url, stream=True)
        image = Image.open(requested_image.raw)
        image = np.array(image) / 255
        image = image.reshape(1, 512, 512, 3)

        image = image.astype("float32")

        return self.getVegetationRate(image)

    def getImageVegetationRates(self, urls):
        rates = []
        for url in urls:
            rates.append(self.getImageVegetationRate(url))

        return rates


prediction_model = PredictionModel()
