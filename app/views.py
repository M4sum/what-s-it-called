from app import app
import numpy as np
from flask import Flask, flash, render_template, redirect, request, send_file, url_for
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import os

UPLOAD_FOLDER = "app/uploads"

NEURAL_NET_MODEL_PATH = "app/model/model_weights.h5"
NEURAL_NET = tf.keras.models.load_model(NEURAL_NET_MODEL_PATH)

brands = {0:'Honda', 1:'Hyundai', 2:'Lexus', 3:'Toyota', 4:'Volkswagon'}
img_x=img_y=70

@app.route("/", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":
        if request.files:
            image_file = request.files["image"]
            if image_file:
                passed = False
            try:
                filename = image_file.filename
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                image_file.save(filepath)
                passed = True

            except Exception:
                passed = False
                print(passed)
            if passed:
                return redirect(url_for('predict', filename=filename))
    return render_template("upload_image.html")

def load_and_prepare(filepath):

    image = np.array(Image.open(filepath).convert('RGB')).flatten()
    image = image.astype(float) / 255
    image = image.reshape(-1,70,70,3)
    return image

@app.route('/predict/<filename>')
def predict(filename):
    
    prediction = ''
    image_url = url_for('images', filename=filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image_data = load_and_prepare(image_path)
    preds = NEURAL_NET.predict(image_data)
    for i in range(len(preds[0])):
        if np.around(preds[0][i]) == 1:
            prediction = brands[i]

    return render_template(
        'predict.html',
        prediction = prediction
    )

@app.route('/images/<filename>')
def images(filename):

    """ Route for serving uploaded images """
    if is_allowed_file(filename):
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        flash("File extension not allowed.")
        return redirect(url_for('home'))