import os
import shutil

def change_photo_extension(input_directory, output_directory, new_extension='.jpg'):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a photo (you can add more extensions if needed)
        if filename.endswith(('.png', '.jpeg', '.gif', '.bmp', '.tif', '.jpg')):
            # Get the current file extension
            _, old_extension = os.path.splitext(filename)
            # Generate the new filename with the new extension
            new_filename = os.path.splitext(filename)[0] + new_extension
            # Copy the file to the output directory with the new filename and extension
            shutil.copy(os.path.join(input_directory, filename), os.path.join(output_directory, new_filename))
            print(f"Copied {filename} to {os.path.join(output_directory, new_filename)}")

# Specify the input directory containing the photos
input_directory_path = '/home/darkstorm/Desktop/new'

# Specify the output directory where the new images will be saved
output_directory_path = '/home/darkstorm/Desktop/newnew'

# Call the function to change the extension and save the new images in the output directory
change_photo_extension(input_directory_path, output_directory_path)
