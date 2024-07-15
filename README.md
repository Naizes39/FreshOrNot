![default](https://github.com/user-attachments/assets/21d3f8ed-1bed-44ba-a99b-80c0cfa37326)

# Fruit and Vegetables Classifier Web Application

This project utilizes a TensorFlow model for image classification through a Django web application. Users can upload images, classify them using a model served by TensorFlow Serving, and view if uploaded image show rotten or healthy object.

## Project Structure

The project consists of the following components:

-  api: Contain fastapi and tfserving files.
-  models: Contain trained tensorflow model.
-  web_app: Contain django web app using tensorflow model.
-  fresh_or_not.ipynb: Jupyter Notebook with model training.

## Installation

## To run the project locally, follow these steps:

## Clone the repository:
  - git clone https://github.com/Naizes39/FreshOrNot.git
  - cd FreshOrNot/web_app
  
## Intsall requirements.txt:
  - pip install -r requirements.txt

## Run the Django server:
  - cd FreshOrNot/web_app
  - python manage.py runserver
# Open a web browser and go to http://127.0.0.1:8000 to access the application.

## Usage
  - Drag and drop or select an image file that you want to classify.
  - Click on the "Check" button.
  - View the classification results, including whether the object is fresh or not.

## Credits

The dataset used for training contains images of various fruits and vegetables in two categories: healthy and rotten.
It was sourced from Kaggle, specifically the Fruit and Vegetable Disease dataset by MUHAMMAD SUBHAN.
https://www.kaggle.com/datasets/muhammad0subhan/fruit-and-vegetable-disease-healthy-vs-rotten/data
