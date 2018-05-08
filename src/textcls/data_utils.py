import os
import sys
import cPickle as pickle
import numpy as np
import tensorflow as tf

dim_embed = 300

def _read_data(data_path, data_file, label_file, num_words = 320):
  """Reads text format data.

  Returns:
    images: np tensor of size [N, 1, H, W]
    labels: np tensor of size [N]
  """
  text, labels = [], []
  #read text data
  with open(data_path + '/' + data_file) as f:
      for line in f:
          line = np.array(line.strip('\n').split(' ')[0:-1], dtype=np.int)
          length = line.shape[0]
          if length >= num_words:
              line = line[0:num_words]
          else:
              if length==0:
                  line = np.zeros((num_words), dtype=np.int)
              else:
                  num_tile = num_words // length + 1
                  line = np.tile(line, [num_tile])
                  line = line[0:num_words]
          text.append(line)

  text = np.reshape(text, [-1, 1, num_words])
  #read text label
  labels = open(data_path + '/' + label_file).read().split('\n')
  labels = labels[1:-1]
  labels = np.array(labels, dtype=np.int32)
  return text, labels


def read_data(data_path, num_valids=50000):
  print "-" * 80
  text, labels = {}, {}
  #read word dict
  print "Reading dict..."
  dic = open(data_path + '/local_dic_index.txt').read().split('\n')
  dic = dic[0:-1]
  for i in range(len(dic)):
      dic[i] = np.array(dic[i].split(' '), dtype = np.float32)
  print ('len of dict: ')
  print len(dic)
  dic = np.array(dic)

  print "Reading data..."
  print data_path
  text["train"], labels["train"] = _read_data(data_path, \
                                                'train_index.txt',\
                                                'train_label.txt')

  if num_valids:
    text["valid"] = text["train"][-num_valids:]
    labels["valid"] = labels["train"][-num_valids:]

    text["train"] = text["train"][:-num_valids]
    labels["train"] = labels["train"][:-num_valids]
  else:
    text["valid"], labels["valid"] = None, None

  text["test"], labels["test"] = _read_data(data_path, \
                                                'test_index.txt',\
                                                'test_label.txt')

  return text, labels, dic
