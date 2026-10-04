import os
import shutil

# Step 1: Define the folder you want to organize on your laptop
folder_path = "C:/Users/HP/Downloads"

# Step 2: Set up categories for different file types
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".html", ".cpp"],
    "Videos": [".mp4", ".mkv"],
    "Zip Files": [".zip", ".rar"]
}

# Step 3: Loop through every file inside the folder
for filename in os.listdir(folder_path):
    file_extension = os.path.splitext(filename)[1].lower()
    
    # Step 4: Check which category the file belongs to
    for category, extensions in file_types.items():
        if file_extension in extensions:
            # Create the folder if it doesn't exist yet
            target_folder = os.path.join(folder_path, category)
            os.makedirs(target_folder, exist_ok=True)
            
            # Move the file into its matching folder
            shutil.move(os.path.join(folder_path, filename), os.path.join(target_folder, filename))
            print(f"Moved {filename} -> {category}/")