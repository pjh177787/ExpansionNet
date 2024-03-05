python data_generator.py \
    --save_model_path ./github_ignore_material/raw_data/swin_large_patch4_window12_384_22k.pth \
    --output_path ./github_ignore_material/raw_data/features.hdf5 \
    --images_path ../COCO2014/ \
    --captions_path ./github_ignore_material/raw_data/ &> log.txt &