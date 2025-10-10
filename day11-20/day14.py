num = int(input("Enter a number: "))

if(num>0):
  print("Number is positive")
  if(num>18):
    print("Your number is greater than 18")
  elif(num==18):
    print("Your number is equal to 18")
  else:
    print("Your number is less than 18")
else:
  print("Your number is negative")