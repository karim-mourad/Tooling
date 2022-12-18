#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# e.g. ['aa', 'xx'] and ['bb', 'cc', 'zz'] => ['aa', 'bb', 'cc', 'xx', 'zz']
def linear_merge(list1, list2):
  # +++your code here+++
  s = list1 + list2
  s.sort()
  return s

# F. Given a string and length of word n, return a list that contain only words 
# of length n or greater of the given string.
# e.g. long_words(3,"ITI is the best") -> ['ITI' , 'the' , 'best']
# Hint: Check string methods.
def long_words(n, string):
  new = []
  new = string.split(' ')
  srs = []
  for s in new:
    if len(s) >= n:
      srs.append(s)
  return srs


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print ('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])

  print ()
  print ('long_words')
  test(long_words(3,"Hi This is Python list test"), ['This', 'Python', 'list' , 'test'])
  test(long_words(4,"ITI is the best organization"), ['best', 'organization'])
  test(long_words(1,"a bb ccc dddd eeee"), ['a', 'bb' , 'ccc' , 'dddd' , 'eeee'])

if __name__ == '__main__':
  main()
