from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Global configuration and initialization.
app = Flask(__name__)
MODEL_PATH = "best_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Chosen in the 3rd cell of the notebook file.
IMG_SIZE = (64, 64)

def preprocess_input(img_bytes: bytes) -> np.ndarray:
    """
    Convert raw uploaded image bytes into a normalized NumPy array
    ready to be input to our best model.
    """
    # Decode raw bytes into an RGB image from memory.
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    
    # Resize the image to the same shape as our training data.
    img = img.resize(IMG_SIZE)
    
    # Convert image into NumPy array of the same shape (H, W, 3) and normalize.
    arr = np.array(img) / 255.0
    
    # Add a batch dimension so model. predict can handle it (1, H, W, 3).
    # i.e., a batch of one image.
    return arr.reshape(1, IMG_SIZE[0], IMG_SIZE[1], 3)
    
@app.route("/summary", methods=["GET"])
def summary():
    """
    A model summary endpoint (GET /summary) providing metadata about the model.
    """
    # get model metadata
    metadata = {
        "model_name": MODEL_PATH,
        "input_shape": model.input_shape,
        "output_shape": model.output_shape,
        "parameters": model.count_params(),
        "image_size": IMG_SIZE,
        "framework": "TensorFlow/Keras",
        "author": "Tav"
    }

    # Return metadata as JSON with 200 OK
    return jsonify(metadata), 200


@app.route("/inference", methods=["POST"])
def inference():
    # Ensure the POST request contains the image.
    if "image" not in request.files:
        return '{"error": "Invalid request: Must pass binary image file as a multi-part form under the image key."}'
    
    # Otherwise, get the data.
    data = request.files["image"]
    img_bytes = data.read()
    
    # Preprocess the input so it's an array of numeric values.
    input_arr = preprocess_input(img_bytes)
    
    # Return the model's prediction.
    # model.predict() returns a NumPy array: e.g. [[pred], dtype=float32].
    pred = model.predict(input_arr)[0][0]
    # Test server either wants "damage" or "no_damage". Per our load_and_preprocess() function in our notebook,
    # 0 maps to "no_damage" and 1 maps to "damage".
    label = "damage" if pred > 0.5 else "no_damage"
    return jsonify({"prediction": label}), 200
    
# Start server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
