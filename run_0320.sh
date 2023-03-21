python3 preprocess_diginetica.py --remove_items 4
python3 main.py --n_epochs 50 --loss_type TOP1
python3 main.py --n_epochs 50 --loss_type TOP1-max
python3 main.py --n_epochs 50 --loss_type BPR
python3 main.py --n_epochs 50 --loss_type BPR-max
python3 main.py --n_epochs 50 --loss_type CrossEntropy
