# Import necessary libraries
from flask import Flask, render_template, request,jsonify
import numpy as np
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from keras.models import load_model

# Define a list of model paths
model_paths = [
    "model/new.h5",
    "model/trained_modelResNet50Transferandfine.h5",
    "model/trained_modelVGG19Transferandfinetuning.h5"
]

# Load multiple models
models = []
model_names = []  # Store the model names
for model_path in model_paths:
    model = load_model(model_path)
    models.append(model)
    model_names.append(os.path.basename(model_path))
print('@@ Models loaded')

def predict_with_models(models, rice_plant):
    test_image = load_img(rice_plant, target_size=(150, 150))
    print("@@ Got Image for prediction")
    test_image = img_to_array(test_image) / 255
    test_image = np.expand_dims(test_image, axis=0)
    
    results = []
    for model in models:
        result = model.predict(test_image).round(2)
        results.append(result)
    print('@@ Raw results =', results)
    
    pred_index = np.argmax(np.mean(results, axis=0))  # Take the index with the highest average probability
    
    if pred_index < len(model_names):  # Check if the index is within the range of model_names
        selected_model = model_names[pred_index]  # Get the name of the selected model
    else:
        selected_model = "new.h5 "
    
    if pred_index == 0:
        return 'Diseased Rice Plant', 'BrownSpot_plant.html', selected_model
    elif pred_index == 1:
        return 'Healthy Rice Plant', 'healthy_plant_leaf.html', selected_model
    elif pred_index == 2:
        return 'Disease Rice Plant', 'Hispa.html', selected_model
    else:
        return "Disease Rice Plant", 'LeafBlast.html', selected_model

# Create flask instance
app = Flask(__name__)

# Render index.html page
@app.route("/", methods=['GET', 'POST'])
def home1():
    return render_template('index1.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

# Get input image from client, then predict class and render respective .html page for the solution
@app.route("/predict", methods=['GET', 'POST'])
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        filename = file.filename
        print("@@ Input posted =", filename)

        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class...")
        pred, output_page, selected_model = predict_with_models(models, rice_plant=file_path)

        return render_template(output_page, pred_output=pred, user_image=file_path, selected_model=selected_model, model_names=model_names)
        #Return the URL of the rendered HTML file
        #html_file_url = request.host_url + output_page
        #return jsonify({'html_file_url': html_file_url})

# For local system & cloud
if __name__ == "__main__":
    #app.run(threaded=False)
    app.run(app.run(host='192.168.43.11', port=5000))


