import requests
import tensorflow as tf
import numpy as np
from PIL import Image


class PredictionModel():
    def __init__(self) -> None:
        self.__model = tf.keras.models.load_model(
            "assets/models/u-net/model")
        self.__threshold_value = 0.6

    def get_vegetation_rate(self, image):
        predicted = self.__model.predict(image)
        predicted = np.where(predicted > self.__threshold_value, 1, 0)
        vegetation_pixels = np.count_nonzero(
            predicted <= self.__threshold_value)

        return vegetation_pixels / predicted.size

    def get_image_vegetation_rate(self, url: str):
        requested_image = requests.get(url, stream=True)
        image = Image.open(requested_image.raw)
        image = image.resize((512, 512))

        if image.mode == 'RGBA':
            image = image.convert('RGB')

        image = np.array(image) / 255
        image = image.reshape(1, 512, 512, 3)

        image = image.astype("float32")

        return self.get_vegetation_rate(image)

    def get_images_vegetation_rates(self, urls):
        rates = []
        for url in urls:
            rates.append(self.get_image_vegetation_rate(url))

        return rates
