import os

image_dir = os.path.expanduser('~/Git/yh_img_cap')
image_files = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith(('.jpg', '.jpeg', '.png')):
            image_files.append(os.path.join(root, file))

print(image_files)