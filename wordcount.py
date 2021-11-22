#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Quang Le - Techmaster.vn - 09/2021
from collections import Counter

"""Wordcount exercise

Hàm main() đã được định nghĩa hoàn chỉnh ở dưới. Bạn phải viết hàm get_words()
và get_top_words() mà sẽ được gọi từ main().

1. Với đối số --count, viết hàm get_words(filename) đếm số lần xuất hiện của mỗi từ 
trong file đầu vào và trả list các tuple theo định dạng sau:
[(word1, count1), 
(word2, count2)
...]

Trả ra danh sách trên theo thứ tự từ điển các từ (python sẽ sắp xếp dấu câu đứng trước
các chữ cái nên cũng không thành vấn đề). Lưu tất cả các từ dưới dạng chữ thường,
vì vậy 'The' và 'the' được tính là cùng một từ.

2. Với đối số --topcount, viết hàm get_top_words(filename) tương tự như get_words()
nhưng chỉ trả ra 20 từ thông dụng nhất sắp xếp theo từ thông dụng nhất ở trên cùng.

Tùy chọn: định nghĩa một hàm helper để tránh lặp lại code trong các hàm 
get_words() và get_top_words().

"""

import sys

# +++your code here+++
def get_words(filename):
  # print(filename.readlines())
  split_string = filename.read().split()
  string_dict = dict()

  for word in split_string:
    if word in string_dict:
      string_dict[word] += 1
    else:
      string_dict[word] = 1
  return string_dict

def get_top_words(filename):
  split_string = filename.read().split()
  string_dict2 = dict()

  for word in split_string:
    if word in string_dict2:
      string_dict2[word] += 1
    else:
      string_dict2[word] = 1
  c = Counter(string_dict2)
  most_common = c.most_common(20)
  return most_common

###

# This basic command line argument parsing code is provided and
# calls the get_words() and get_top_words() functions which you must define.
def main():
  print("Đếm từ trong file")
  filename = open("small.txt",'r')
  ans = []
  ans = get_words(filename)
  print(ans)
  print("====================================================")
  print("Top 20 từ thông dụng nhất")
  filename1 = open("alice.txt",'r')
  ans1 = get_top_words(filename1)
  print(ans1)

if __name__ == '__main__':
  main()
