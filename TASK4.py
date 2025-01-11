import os
import shutil

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

# Function to organize files
def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    category_folder = os.path.join(directory, category)
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved '{filename}' to '{category}' folder.")
                    break

if __name__ == "__main__":
    directory_to_organize = input("Enter the directory path to organize: ")
    organize_files(directory_to_organize)
    print("File organization complete!")
