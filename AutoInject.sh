#!/bin/bash

# Directory containing the script
script_directory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Directory containing the image and binary files
malware_directory="/home/darkstorm/Desktop/Malwares"
images_directory="/home/darkstorm/Desktop/mdataset"

# Output directory for encoded images
output_directory="/home/darkstorm/Desktop/MDataset"

# Number of images and files
num_images=30000
num_files_per_image=10

# Iterate over each image
for ((image_index = 1; image_index <= num_images; image_index++)); do
  image_file="Img_${image_index}.jpg"

  # Determine the file index for the current image
  file_index=$(( (image_index - 1) / 100 + 1 ))

  # Iterate over each binary file for the current image
  for ((current_file = 1; current_file <= num_files_per_image; current_file++)); do
    binary_file="Malware_${file_index}.exe"
    output_file="MImg_${file_index}_${image_index}.jpg"

    # Build full paths
    image_path="$images_directory/$image_file"
    binary_path="$malware_directory/$binary_file"
    output_path="$output_directory/$output_file"

    # Check if the files exist
    if [ -f "$image_path" ] && [ -f "$binary_path" ]; then
      # Run the Python script to encode the image
      python3 "$script_directory/Inject.py" "$image_path" "$binary_path" "$output_path"
      echo "Encoding complete for $output_file."
    else
      echo "Image or file not found for $output_file."
    fi
  done
done
