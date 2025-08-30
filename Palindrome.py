def palindrome_check(word):
  a = word.lower()
  b = a.replace(" " , "")
  rev = b[::-1]
  if b == rev:
    print('Yes, it is a palindrome')
  else:
    print('No, it is not a palindrome')
word = str(input('Please type a word '))
palindrome_check(word)