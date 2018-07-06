Repository to hold Raspberry Pi related development.

python object_detection/train.py --logtostderr --train_dir=C:\Users\scharmann\Desktop\pi\ml-tweet-bot\checkpoint --pipeline_config_path=C:\Users\scharmann\Desktop\pi\ml-tweet-bot\training\ssd_mobilenet_v1_pets.config


python object_detection/eval.py --logtostderr --checkpoint_dir=C:\Users\scharmann\Desktop\pi\ml-tweet-bot\checkpoint --pipeline_config_path=C:\Users\scharmann\Desktop\pi\ml-tweet-bot\training\ssd_mobilenet_v1_pets.config --eval_dir=C:\Users\scharmann\Desktop\pi\ml-tweet-bot\checkpoint

tensorboard --logdir=foo:C:\Users\scharmann\Desktop\pi\ml-tweet-bot

# To split training and testing data
python utils/split_csv_train_test.py --csv_input=training/basket_labels.csv

# To generate test and training records
python utils/generate_tfrecord.py --csv_input=training/train_labels.csv  --output_path=train.record
python utils/generate_tfrecord.py --csv_input=training/test_labels.csv  --output_path=test.record