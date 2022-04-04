# -*- coding: utf-8 -*-
"""preprocessing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14HBGaFUtT0iuXTbUZrQxpkyJvNypR_nB
"""

import argparse
import os
import sys

def main(read_file_name):
  print("clear", read_file_name)
  index = read_file_name.rfind(".")
  write_file_name = read_file_name[:index]+"_clear.txt"
  file_write = open(write_file_name, "w");
  file_write.write("type address size block_address\n") # write header
  file_write.close()

  file_write = open(write_file_name, "a");
  with open(read_file_name) as f:
      for line in f:
        if (line.startswith('read') or line.startswith('write')):
          data_line = line.split()
          data_line.pop()
          block_address = int(str(data_line[1]), 16)
          data_line.append(str(block_address))
          file_write.write(" ".join(data_line)+"\n")
  file_write.close()

def is_valid_file(parser, arg):
  if not os.path.exists(arg):
      parser.error("The file %s does not exist" % arg)
  else:
      return arg


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description = 'remove timestamp and calculate block address')
  parser.add_argument("-i", dest="filename", required=True,
                    help="input raw trace data",
                    type=lambda x: is_valid_file(parser, x))
  args = parser.parse_args()
  main(args.filename)
