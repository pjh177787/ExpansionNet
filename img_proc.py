import json
import os
import random
import shutil

# Now, the contents of the JSON file are stored in the 'data' dictionary
# # Specify the path to the JSON file
# file_path = './github_ignore_material/raw_data/dataset_coco.json'
# # Read the JSON file
# with open(file_path, 'r') as file:
#     data = json.load(file)
# # Now, the contents of the JSON file are stored in the 'data' dictionary

# # Pretty print the data dictionary
# coco_keys = data["images"]
# print(json.dumps(coco_keys[0], indent=2))
# print()
# print(data["dataset"])

# Specify the directory path
directory = "../yh_img_cap/image-caption"

# Initialize an empty dictionary
file_dict = {}

# Walk through the directory and get the file names and paths
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".jpg"):
            file_path = os.path.join(root, file)
            file_name = os.path.splitext(file)[0]
            parent_folder = os.path.basename(os.path.dirname(file_path))
            key = parent_folder + '_' + file_name
            json_file = file_name + '.json'
            json_path = os.path.join(root, json_file)
            if os.path.exists(json_path):
                file_dict[key] = {
                    'path': file_path,
                    'anno': json_path
                }
            

yh_dict = {}
yh_dict["images"] = []
yh_dict["dataset"] = "coco"
# Read the JSON file for each entry in file_dict

# {
#   "image_name": "00104_c7s0_18.jpg",
#   "region": [],
#   "global": [
#     {
#       "label": "Description",
#       "value": "A boy sits on the living room couch watching TV, and there's a couple of velvet dolls and a back-back on the couch"
#     }
#   ],
#   "file": {
#     "fid": "1710903284469125130",
#     "src": "jinglianwen_biaoqian/imagecaption/Single_users_compound_event/data/p104/Watch.TV/c7s0/00104_c7s0_18.jpg",
#     "name": "00104_c7s0_18.jpg",
#     "scaleHistory": [],
#     "isSeen": true,
#     "isChange": false
#   }

for key, value in file_dict.items():
    file_path = value['path']
    json_path = value['anno']
    if os.path.exists(json_path):
        with open(json_path, 'r') as file:
            json_data = json.load(file)

        # Randomly assign the split       
        rand_num = random.random()
        if rand_num < 0.8:
            split = "train"
            folder = "train2024"
        elif rand_num < 0.9:
            split = "test"
            folder = "val2024"
        else:
            split = "val"
            folder = "val2024"
        
        activity = file_path.split(os.sep)[-2]
        new_path = '../YH2024' + os.sep + folder + os.sep + 'img'
        new_filename = activity + '_' + json_data['image_name']
        
        # Create the new path if it doesn't exist
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        # Copy the jpg file to the new path
        shutil.copy(file_path, new_path + os.sep + new_filename)

        # Organize the entries into the same format as data
        entry = {
            'filepath': folder,
            'sentids':[0],
            'filename': new_filename,
            'imgid': json_data['file']['fid'],
            'split': split,
            'sentences': [
                {
                    'tokens': json_data['global'][0]['value'].split(),
                    'raw': json_data['global'][0]['value'],
                    'imgid': json_data['file']['fid'],
                    'sentid': 0
                }
            ],
            'cocoid': json_data['file']['fid']
        }
        yh_dict["images"].append(entry)

# Pretty print the first entry in the yh_dict
# print(json.dumps(yh_dict["images"][0], indent=2))
        
# Write the yh_dict to a JSON file
with open('github_ignore_material/raw_data/yh_anno.json', 'w') as file:
    json.dump(yh_dict, file, indent=2)

train_count = 0
val_count = 0
for entry in yh_dict["images"]:
    if entry["filepath"] == "train2024":
        train_count += 1
    else:
        val_count += 1

print(f"Number of images in YH2024/train2024: {train_count}")
print(f"Number of images in YH2024/val2024: {val_count}")