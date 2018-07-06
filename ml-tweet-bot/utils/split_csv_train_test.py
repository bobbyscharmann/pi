"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python split_csv_train_test.py --csv_input=data/labels.csv
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
import pandas as pd
import numpy as np
import os
import io
import pandas as pd
import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
FLAGS = flags.FLAGS

def main():

    df = pd.read_csv(FLAGS.csv_input)

    msk = np.random.rand(len(df)) <= 0.8

    train = df[msk]
    test = df[~msk]
    train.to_csv('train_labels.csv', index=False)
    test.to_csv('test_labels.csv', index=False)
	
    print('Successfully split into train and test set.')


if __name__ == '__main__':
    main()
