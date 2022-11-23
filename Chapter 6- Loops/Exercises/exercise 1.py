##exercise 1:
toppings = []
n = int(input("ENTER THE AMOUNT OF TOPPINGS:"))
for i in range(0, n):
  ele = str(input("You are about to add:"))
  toppings.append(ele)
print("There are your toppingd below:")
print(toppings)  