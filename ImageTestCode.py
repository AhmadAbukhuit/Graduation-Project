import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the saved model
model = load_model("malware_classification_model.keras")

# Define a function to preprocess the image
def preprocess_image(image_path, target_size):
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Path to the image you want to test
test_image_path = "/home/darkstorm/Desktop/TestDataset/Class_7/Malware_7_676.jpg"
# Adjust target_size if needed
target_size = (256, 256)

# Preprocess the image
test_image = preprocess_image(test_image_path, target_size)

# Make predictions
predictions = model.predict(test_image)

# Get the class labels
class_labels = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Non-malware"]

# Get the predicted class index
predicted_class_index = np.argmax(predictions)
# Get the predicted class label
predicted_class_label = class_labels[predicted_class_index]
# Get the probability of the predicted class
predicted_probability = predictions[0][predicted_class_index]

# Print the predicted class and probability
print("Predicted class:", predicted_class_label)
print("Probability:", predicted_probability)

# Provide feedback based on the prediction
# If the prediction is correct, you can provide positive feedback
# If the prediction is incorrect, you can provide constructive feedback

