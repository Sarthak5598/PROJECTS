import io
import os
from google.cloud import vision
from google_vision_ai import VisionAI
from google_vision_ai import prepare_image_local,prepare_image_web,draw_boundary,draw_boundary_normalized
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_google_api.json'
client = vision.ImageAnnotatorClient()

image_path = 'D:\C C++\PROJECTS\GOOGLE_VISION_AI_API\images\download (3).jpg'
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

response = client.label_detection(image=image)
for label in response.label_annotations:
    print(label.description)
