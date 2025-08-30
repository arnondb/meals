def main():
  s = str(input("string: "))
  for char in s:
    if s.count(char) > 1:
        # Replace only the second occurrence
        first_index = s.find(char)
        second_index = s.find(char, first_index + 1)
        s = s[:second_index] + "*" + s[second_index + 1:]
        
  print(s)
if __name__ == '__main__':
  main()