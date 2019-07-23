#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 17:04
# @Author  : Stodgers
# @Site    : 
# @File    : date_train.py
# @Software: PyCharm



'''
python data_utils.py --bsz_per_host=32 --num_core_per_host=16 --seq_len=512 --reuse_len=256 --input_glob=test.txt --save_dir=${SAVE_DIR} --num_passes=20 --bi_data=True --sp_path=spiece.model --mask_alpha=6 --mask_beta=1 --num_predict=85



python train_gpu.py --record_info_dir=$SAVE_DIR/tfrecords --train_batch_size=2048 --seq_len=512 --reuse_len=256 --mem_len=384 --perm_size=256 --n_layer=24 --d_model=1024 --d_embed=1024 --n_head=16 --d_head=64 --d_inner=4096 --untie_r=True --mask_alpha=6 --mask_beta=1 --num_predict=85


'''