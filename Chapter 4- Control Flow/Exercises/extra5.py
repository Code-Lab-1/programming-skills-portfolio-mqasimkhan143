time = int(input("Enter time: "))##in 0000 format
if time >= 0000 and time < 1200:
  print("its A.M")
elif time >= 1200 and time < 2400:
  print("its P.M")
else:
  print("wrong entry") 