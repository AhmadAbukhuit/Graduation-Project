from PIL import Image
import os

# Directory containing your JPEG images
input_dir = "/home/darkstorm/Desktop/Dataset"

# Directory to save resized images
output_dir = "/home/darkstorm/Desktop/DataSet"

# Ensure the output directory exists, if not create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # Open the image file
        with Image.open(os.path.join(input_dir, filename)) as img:
            # Resize the image to 256x256
            resized_img = img.resize((256, 256))

            # Save the resized image to the output directory
            resized_img.save(os.path.join(output_dir, filename))
            print(f"Resized {filename} successfully.")

print("All images resized and saved.")
