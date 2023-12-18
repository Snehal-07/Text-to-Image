#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
import base64

def text_to_image():
    # Replace with your Stability AI API key
    api_key = "YOUR_ACTUAL_API_KEY"

    # API endpoint for text-to-image
    api_endpoint = "https://platform.stability.ai/sandbox/text-to-image"

    # Request headers
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Request parameters
    params = {
        "steps": 40,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
                "text": "A picture of a sky with beautiful clouds and pinkish sky and a long road",
                "weight": 1,
            },
            {
                "text": "blurry, bad",
                "weight": -1,
            },
        ],
    }

    # Make the API request using GET method
    response = requests.get(api_endpoint, headers=headers, params=params)

    # Print the entire response text
    print(response.text)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            response_json = response.json()
            # Save each generated image
            for index, image in enumerate(response_json["artifacts"]):
                image_data = base64.b64decode(image["base64"])
                with open(f"./out/txt2img_{image['seed']}.png", "wb") as file:
                    file.write(image_data)
            print("Images generated successfully.")
        except Exception as e:
            print(f"Error parsing JSON response: {e}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Call the function to generate images
text_to_image()


# In[ ]:





# In[ ]:




