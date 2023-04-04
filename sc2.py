import requests
import urllib.request

# URL to make the API request
url = "https://quickchecktech.vercel.app/api/teacher/students"

# Make the API request
response = requests.get(url)
data = response.json()

for student in data:
    # Check if the student has an avatar image
    if "avatar" in student:
        image_url = student["avatar"]
        filename = student["name"] + student["rollno"] + ".jpg"

        # Download the image
        try:
            urllib.request.urlretrieve(image_url, filename)
            print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")
    else:
        print(f"No avatar image found for {student['name']} ({student['rollno']})")
