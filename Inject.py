from PIL import Image
import os
import sys

def hide_data(image_path, data_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Open and read the binary file
    with open(data_path, 'rb') as file:
        binary_data = file.read()

    # Convert binary data to a list of integers
    binary_values = list(binary_data)

    # Flatten the pixel values into a one-dimensional list
    pixels = list(img.getdata())

    # Ensure there's enough space in the image to hide the data
    if len(binary_values) > len(pixels):
        raise ValueError("Insufficient space in the image to hide the data")

    # Iterate through each pixel and hide the data in the LSB
    for i in range(len(binary_values)):
        # Modify the least significant bit of each color channel
        pixels[i] = tuple(value & 0xFE | ((binary_values[i] >> shift) & 1) for value, shift in zip(pixels[i], (0, 1, 2)))

    # Create a new image with the modified pixel values
    encoded_img = Image.new('RGB', img.size)
    encoded_img.putdata(pixels)

    # Save the new image
    try:
        encoded_img.save(output_path)
        print("Image saved successfully.")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    # Paths to the original image, binary file to be hidden, and output image
    if len(sys.argv) < 4:
        print("Usage: python3 Inject.py <image_path> <data_path> <output_path>")
        sys.exit(1)

    script_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = sys.argv[1]
    data_path = sys.argv[2]
    output_path = sys.argv[3]

    try:
        hide_data(image_path, data_path, output_path)
        print("Hiding data complete.")
    except Exception as e:
        print(f"Error: {e}")
