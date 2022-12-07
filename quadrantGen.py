import openai
from PIL import Image, ImageGrid
import os
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

print("Generated images:")
for i, image in enumerate(response["data"]):
    # Print the URLs of the generated images
    print(f"{i + 1}. {image['url']}")
    # Open the images urls using the pillow library 
    ims = Image.open(image['url'])

# Create an ImageGrid instance with the images and the desired grid size
grid = ImageGrid(ims, nrows=2, ncols=2)

# Prompt the user to choose an image
#selected_image = int(input("Choose an image (1-4): "))

# Use the selected image as the prompt for the next round of image generation
#selected_prompt = response["data"][selected_image - 1]["prompt"]
#response = openai.Image.create(
    #prompt=selected_prompt,
    #n=4,
    #size="512x512",
    #response_format="url"
#)

## Print the URLs of the second round of generated images
#print("Generated images:")
#for i, image in enumerate(response["data"]):
    #print(f"{i + 1}. {image['url']}")
