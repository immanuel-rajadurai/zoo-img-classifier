import base64
import requests

# OpenAI API Key
api_key = ""

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
# image_path = "peacock.jpg"

# Getting the base64 string
def encode_base_64(image_path):
  base64_image = encode_image(image_path)
  return base64_image


def generate_response_to_animal_image(base64_image):

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": """You are a zookeeper and you are given the task of giving information about animals found within an image. Given an image of an animal, classify the animal in the image correctly and give the information about the animal in the following order: {"Specie": ___ , "Habitat": ___ , "Diet": ___, "Behaviour":___}"""
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  return response

