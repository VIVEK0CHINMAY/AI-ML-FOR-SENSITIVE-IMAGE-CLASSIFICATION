import numpy as np
import tensorflow as tf
from PIL import Image

# Load your saved model
model_path = r'E:/violence_classification_model.h5'
try:
    model = tf.keras.models.load_model(model_path)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Define classes for prediction
classes = ['non-sensitive', 'sensitive']


def classify_image(image_path):
    try:
        # Load and preprocess the image
        image = Image.open(image_path)

        # Display the image
        image.show()

        image = image.resize((224, 224))  # Resize to match model's expected sizing
        image = np.array(image) / 255.0  # Normalize
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Perform prediction
        prediction = model.predict(image)
        predicted_class = classes[int(np.round(prediction)[0][0])]

        # Show result
        print(f"The image is classified as: {predicted_class}")
    except Exception as e:
        print(f"Error classifying image: {e}")


# Example usage
if __name__ == "__main__":
    image_path = r'D:\c.webp'
    print(f"Classifying image: {image_path}")
    classify_image(image_path)
