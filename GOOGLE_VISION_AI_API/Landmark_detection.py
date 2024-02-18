import os
from google.cloud import vision
from google_vision_ai import VisionAI
from google_vision_ai import prepare_image_local,prepare_image_web,draw_boundary,draw_boundary_normalized
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\C C++\PROJECTS\GOOGLE_VISION_AI_API\client_google_api.json'
client = vision.ImageAnnotatorClient()
image_path="D:\C C++\PROJECTS\GOOGLE_VISION_AI_API\images\download (5).jpg"
image= prepare_image_local(image_path)
va = VisionAI(client,image)
landmarks = va.landmark_detection()
for landmark in landmarks:
    print(landmark.description)
    print(landmark.score)
