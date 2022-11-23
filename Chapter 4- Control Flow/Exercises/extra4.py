n = int(input("enter an integer value: "))
flag = False
for i in range(2, n):
  if (n % i) == 0:
    flag = True
    break
if flag:
  print("not prime number")    
else:
  print("prime number") 