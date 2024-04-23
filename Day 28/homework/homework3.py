# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
def reverse_words(text):
  lst= []
  for text in text.split(' '):
      lst.append(text[::-1])
  return ' '.join(lst)