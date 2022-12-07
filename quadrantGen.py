import openai
from PIL import Image, ImageDraw, ImageFont
import os
import requests
from io import BytesIO
from dotenv import load_dotenv

# Set the OpenAI API key
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Prompt the user for input
prompt = input("Enter a prompt to generate images: ")

# Use the OpenAI API to generate four images based on the user's input
response = openai.Image.create(
    prompt=prompt,
    n=4,
    size="1024x1024",
    response_format="url"
)

# Print the URLs of the generated images
print("Generated images:")
for i, image in enumerate(response["data"]):
    print(f"{i + 1}. {image['url']}")

#Get the URLs of the generated images
image_urls = [image["url"] for image in response["data"]]

images = []
for image_url in image_urls:
    # Open the image using the requests library
    response = requests.get(image_url)

    # Create a Pillow Image object from the image data
    images.append(Image.open(BytesIO(response.content)))

# Show the images
for image in images:
    image.show()