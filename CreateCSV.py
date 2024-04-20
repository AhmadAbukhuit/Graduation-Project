import csv
import os

# Define the directory where your dataset is located
dataset_dir = '/home/darkstorm/Desktop/TestDataset'

# Initialize an empty list to store image paths and labels
data = []

# Each class have folder in the dataset directory
for class_name in range(1, 12):
    class_dir = os.path.join(dataset_dir, f'Class_{class_name}')
    print(f"Checking folder: {class_dir}")
    if os.path.isdir(class_dir):
        # Go through each image in the class folder
        for image_name in os.listdir(class_dir):
            if image_name.endswith('.jpg') :
                image_path = os.path.join(class_dir, image_name)
                print(f"Found image: {image_path}")
                # Append image path and class label to the data list
                data.append([image_path, f'Class_{class_name}'])
            else:
                print(f"Ignored file: {image_name}")
    else:
        print(f"Class folder not found: {class_dir}")

# Define the path for the CSV file
csv_file = 'dataset.csv'

# Write data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Image_Path', 'Class_Label'])
    # Write data
    writer.writerows(data)

print("CSV file created successfully!")
