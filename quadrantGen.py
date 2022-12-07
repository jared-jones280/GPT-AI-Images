import openai
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
    size="512x512",
    response_format="url"
)

# Print the URLs of the generated images
print("Generated images:")
for i, image in enumerate(response["data"]):
    print(f"{i + 1}. {image['url']}")

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
