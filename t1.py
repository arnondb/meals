def main():
  number = int(input("Number: "))
  if 0 <= number <= 9:
    print('Number of donuts:' , number)
  elif 10 <= number:
    print ('Number of donuts: many')
if __name__ == '__main__':
  main()
