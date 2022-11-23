##exercise 2:
audience = []
n = int(input("Enter the amount of people in your group:"))
for i in range(0, n):
  ele = int(input("Enter your age:"))
  audience.append(ele)
  if audience[i] < 3:
    print("your ticket is free!")
  elif audience[i] >= 3 and audience[i]<= 12:
    print("your ticket price is 10 dollars!")
  elif audience[i] > 12:
    print("your ticket price is 15 dollars!")
  else:
    print("wrong entry")