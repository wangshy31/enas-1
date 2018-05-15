#!/bin/bash

export PYTHONPATH="$(pwd)"
fixed_arc="0 3 0 2 0 2 0 0 1 4 0 2"
fixed_arc="$fixed_arc 1 2 1 3 1 4 1 2 0 0 2 3"
python src/textcls/main.py \
  --data_format="NCHW" \
  --search_for="micro" \
  --reset_output_dir \
  --data_path="/ssd/ijcai18/data/agnews" \
  --output_dir="textcls/agnews/maxout/8810" \
  --batch_size=256 \
  --num_epochs=72 \
  --log_every=50 \
  --eval_every_epochs=1 \
  --child_use_aux_heads \
  --child_fixed_arc="${fixed_arc}" \
  --child_num_layers=4 \
  --child_out_filters=16 \
  --child_num_branches=5 \
  --child_num_cells=3 \
  --child_keep_prob=0.80 \
  --child_drop_path_keep_prob=0.60 \
  --child_l2_reg=1e-4 \
  --child_lr_cosine \
  --child_lr_max=0.05 \
  --child_lr_min=0.0005 \
  --child_lr_T_0=10 \
  --child_lr_T_mul=2 \
  --nocontroller_training \
  --controller_search_whole_channels \
  --controller_entropy_weight=0.0001 \
  --controller_train_every=1 \
  --controller_sync_replicas \
  --controller_num_aggregate=10 \
  --controller_train_steps=50 \
  --controller_lr=0.001 \
  --controller_tanh_constant=1.50 \
  --controller_op_tanh_reduce=2.5 \
  "$@"

