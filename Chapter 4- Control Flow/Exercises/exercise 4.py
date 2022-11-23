##exercise 4:
age = int(input("enter your age:"))
if age>=0 and age<2:
  print("you are a baby")
elif age>=2 and age<4:
  print("you are a toddler")
elif age>=4 and age<13:
    print("you are a kid")
elif age>=13 and age<20:
  print("you area a teenager")
elif age>=20 and age<65:
  print("you are an adult")
else:
  print("elder")