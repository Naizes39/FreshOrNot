
from django.shortcuts import render
from django.http import JsonResponse
import requests
import numpy as np
from PIL import Image
from io import BytesIO

TF_SERVING_URL = 'http://localhost:8501/v1/models/fresh_or_not:predict'

CLASS_NAMES = ['Apple__Healthy', 'Apple__Rotten', 'Banana__Healthy', 'Banana__Rotten', 'Bellpepper__Healthy', 'Bellpepper__Rotten', 'Carrot__Healthy', 'Carrot__Rotten',
               'Cucumber__Healthy', 'Cucumber__Rotten', 'Grape__Healthy', 'Grape__Rotten', 'Guava__Healthy', 'Guava__Rotten', 'Jujube__Healthy', 'Jujube__Rotten',
               'Mango__Healthy', 'Mango__Rotten', 'Orange__Healthy', 'Orange__Rotten', 'Pomegranate__Healthy', 'Pomegranate__Rotten',
               'Potato__Healthy', 'Potato__Rotten', 'Strawberry__Healthy', 'Strawberry__Rotten', 'Tomato__Healthy', 'Tomato__Rotten']

def classify_image(image):
    img_batch = np.expand_dims(image, 0)
    json_data = {"instances": img_batch.tolist()}
    response = requests.post(TF_SERVING_URL, json=json_data)
    prediction = np.array(response.json()["predictions"][0])
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = float(np.max(prediction))
    predicted_class = predicted_class.split("__")
    p_class = predicted_class[0]
    p_state = predicted_class[1]
    return p_class, p_state, int(confidence * 100)

def classify(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        image = Image.open(image_file)
        image_np = np.array(image)
        predicted_class, predicted_state, confidence = classify_image(image_np)
        result = {
            'class': predicted_class,
            'state': predicted_state,
            'confidence': confidence
        }
        return render(request, 'upload_form.html', {'result': result})
    return render(request, 'upload_form.html')
