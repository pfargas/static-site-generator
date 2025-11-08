import os
from generate_page import generate_pages_recursive

def remove_files_in_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            remove_files_in_directory(item_path)
    os.rmdir(directory)

def copy_full_directory(src, dest):
    os.makedirs(dest, exist_ok=True)
    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        print(f"Copying {item_path} to {dest_path}")
        if os.path.isdir(item_path):
            os.makedirs(dest_path, exist_ok=True)
            copy_full_directory(item_path, dest_path)
        else:
            with open(item_path, 'rb') as fsrc:
                with open(dest_path, 'wb') as fdst:
                    fdst.write(fsrc.read())


def main():
    if os.path.exists("./public"):
        remove_files_in_directory("./public")

    copy_full_directory("./static", "./public")

    print("Current working directory:", os.getcwd())

    generate_pages_recursive("content/",
                  "./src/template.html",
                  "./public/")



if __name__ == "__main__":
    main()