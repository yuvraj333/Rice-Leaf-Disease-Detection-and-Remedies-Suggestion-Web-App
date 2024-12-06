# Rice Leaf Disease Detection and Remedies Suggestion Web App

This web application provides a solution for detecting diseases in rice leaves and suggesting remedies using machine learning models. The app allows users to upload images of rice leaves, and it identifies potential diseases using deep learning techniques like Convolutional Neural Networks (CNN), ResNet50, VGG19, and VGG16. Based on the detected disease, the app also suggests remedies for the user.

## Technologies Used

- **Frontend**: 
  - HTML5
  - CSS3
  - JavaScript

- **Backend**:
  - Python with Flask
  - RESTful API for communication

- **Machine Learning Models**:
  - Convolutional Neural Networks (CNN)
  - ResNet50
  - VGG19
  - VGG16

- **Mobile App**:
  - Flutter
  - Firebase
  - API Integration for Web App Communication

## Features

- **Disease Detection**: Users can upload images of rice leaves, and the app detects diseases using deep learning models (CNN, ResNet50, VGG19, VGG16).
- **Remedies Suggestion**: Based on the detected disease, the app provides remedies and solutions to treat the diseases.
- **User-friendly Interface**: Simple and responsive design for both mobile and web users.
- **Mobile App Integration**: The mobile app, built with Flutter and Firebase, is fully integrated with the web app via API calls.

## Installation

### Web Application

1. Clone this repository:
   ```bash
   git clone https://github.com/yuvraj333/rice-leaf-disease-detection-web-app.git


# Rice Leaf Disease Detection and Remedies Suggestion Web App

## Installation

### Web Application

1. Navigate to the project directory:
   ```bash
   cd rice-leaf-disease-detection-web-app
   ```

2. Install the necessary Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

### Mobile App (Flutter)

1. Clone the mobile app repository:
   ```bash
   git clone https://github.com/yourusername/rice-leaf-disease-detection-mobile.git
   ```

2. Navigate to the mobile app directory:
   ```bash
   cd rice-leaf-disease-detection-mobile
   ```

3. Install Flutter dependencies:
   ```bash
   flutter pub get
   ```

4. Run the app:
   ```bash
   flutter run
   ```

## How It Works

### Frontend (Web App)

The web app interface allows users to upload images of rice leaves. The image is then processed and sent to the backend via API. The backend, powered by Flask and the trained machine learning models (ResNet50, VGG19, VGG16), processes the image and returns the predicted disease. The frontend displays the result along with suggested remedies.

### Backend (Flask API)

The backend leverages deep learning models (CNN, ResNet50, VGG19, VGG16) to process the uploaded image. The models are pre-trained on a dataset of rice leaf diseases and can detect common diseases like bacterial blight, leaf blast, and more. Once the disease is detected, the backend fetches the corresponding remedy and returns it to the frontend.

### Mobile App

The mobile app built with Flutter connects to the web app’s API, allowing users to interact with the disease detection and remedy suggestion features. Firebase is used for user authentication, data storage, and push notifications.

## API Documentation

The API allows communication between the mobile and web applications. Below is a sample of the endpoints:

### 1. **POST /upload**

- **Description**: Upload a rice leaf image for disease detection.
- **Request Body**:
  - `image`: (required) Base64-encoded image of the rice leaf.
  
- **Response**:
  ```json
  {
    "disease": "Bacterial Blight",
    "remedies": "Use copper-based fungicides and remove infected leaves."
  }
  ```

### 2. **GET /diseases**

- **Description**: Get a list of known diseases.
- **Response**:
  ```json
  {
    "diseases": ["Bacterial Blight", "Leaf Blast", "Rice Sheath Blight"]
  }
  ```

## Contributing

If you'd like to contribute to the project, follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Special thanks to the developers of the ResNet50, VGG19, and VGG16 models for their contributions to the field of computer vision.
- Thanks to the community for providing datasets for rice leaf diseases that helped train the models.
