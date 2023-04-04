# import requests
# from bs4 import BeautifulSoup

# # Set the API endpoint and key for ImgBB
# api_url = 'https://api.imgbb.com/1/upload'
# api_key = 'a431b34dd132a00c26e44d1988330ac0'

# # Open the image file to upload
# with open('ritesh1.jpg', 'rb') as f:
#     # Send a POST request to the ImgBB API endpoint with the image data and API key
#     response = requests.post(
#         api_url, data={'key': api_key, 'image': f.read(), 'name': "img1.jpg"})
# if(response.json()['status_code'] == 200):
#     print(response.json()['data']['url_viewer'])
# else:
#     print("Errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
#     print(response.json())
# Parse the JSON response from ImgBB to get the image URL and delete URL
# data = response.json()['data']
# image_url = data['url']
# delete_url = data['delete_url']

# # Send a GET request to the ImgBB HTML page to get the download link
# html_response = requests.get(image_url)
# soup = BeautifulSoup(html_response.text, 'html.parser')
# download_url = soup.select_one('.download')['href']

# # Print the download link
# print(f"Download link: {download_url}")


import requests
import base64

api_url = 'https://api.imgbb.com/1/upload'
api_key = 'a431b34dd132a00c26e44d1988330ac0'

with open('1.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')

response = requests.post(api_url, data={
    'key': api_key,
    'image': image_data,
    'name': 'image.jpg'
})

if response.status_code == 200:
    print(response.json()['data']['url'])
else:
    print("Error: ", response.json()['error'])
