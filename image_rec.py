import ast
import pprint
import pandas
import json
import torch
from api_call import encode_base_64, generate_response_to_animal_image


class ImageRec():

    def __init__(self, animal_image_location):
        self.animal_image_location = self.path_heading(animal_image_location)

    def path_heading(self, path):
        return "animal_images/" + path

    def set_animal_image(self, animal_image_location):
        self.animal_image_location = self.path_heading(animal_image_location)

    def recognise(self):

        print("RECOGNISING ANIMAL")
        print(".")
        print("..")
        print("...")

        if not self.animal_image_location:
            print("Animal location not set")
            return

        encoded_image = encode_base_64(self.animal_image_location)
        response = generate_response_to_animal_image(encoded_image)

        print("ANIMAL RECOGNISED")
        print()

        dict = ast.literal_eval(response.content.decode('utf-8'))

        message = dict['choices'][0]['message']['content']

        info_list = message.split("\n")

        for info_string in info_list:
            print(info_string)
            print()



