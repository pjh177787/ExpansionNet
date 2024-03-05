# Phase 1
# python train.py --N_enc 3 --N_dec 3  \
#     --model_dim 512 --seed 775533 --optim_type radam --sched_type custom_warmup_anneal  \
#     --warmup 10000 --lr 1e-4 --anneal_coeff 0.8 --anneal_every_epoch 2 --enc_drop 0.3 \
#     --dec_drop 0.3 --enc_input_drop 0.3 --dec_input_drop 0.3 --drop_other 0.3  \
#     --batch_size 16 --num_accum 1 --num_gpus 1 --ddp_sync_port 11317 --eval_beam_sizes [3]  \
#     --save_path ./github_ignore_material/saves/ --save_every_minutes 5 --how_many_checkpoints 1  \
#     --is_end_to_end False --features_path ./github_ignore_material/raw_data/features_yh.hdf5 --partial_load False \
#     --print_every_iter 100000 --eval_every_iter 999999 \
#     --reinforce False --num_epochs 100 &> train_log.txt &

# Phase 2
python train.py --N_enc 3 --N_dec 3  \
    --model_dim 512 --optim_type radam --seed 775533   --sched_type custom_warmup_anneal  \
    --warmup 100 --lr 2e-5 --anneal_coeff 0.55 --anneal_every_epoch 1 --enc_drop 0.3 \
    --dec_drop 0.3 --enc_input_drop 0.3 --dec_input_drop 0.3 --drop_other 0.3  \
    --batch_size 8 --num_accum 3 --num_gpus 1 --ddp_sync_port 11317 --eval_beam_sizes [3]  \
    --save_path ./github_ignore_material/saves/ --save_every_minutes 60 --how_many_checkpoints 1  \
    --is_end_to_end True --images_path ../YH2024/ --partial_load True \
    --backbone_save_path ./github_ignore_material/raw_data/swin_large_patch4_window12_384_22k.pth \
    --body_save_path ./github_ignore_material/saves/p1_2403051045.pth \
    --print_every_iter 50000 --eval_every_iter 999999 \
    --reinforce False --num_epochs 100 &> train_p2_log.txt &
