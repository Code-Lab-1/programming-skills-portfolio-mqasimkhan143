##exercise 5:
sandwich_order = []
finished_sandwiches = []
n = int(input("Enter the amount of sandwiches:"))
for i in range(0, n):
  ele = str(input("Enter your order:"))
  sandwich_order.append(ele)
  print("You have ordered:",ele)
while 'pastrami' in sandwich_order:
  sandwich_order.remove('pastrami')
for i in range(0, n-3):
    finished_sandwiches.append(sandwich_order.pop(0))
    finished_sandwiches.sort()
    print("Your order is done")
    print(finished_sandwiches)
print("Your finished sandwiches:")    
print(finished_sandwiches) 
print("now pending orders:")
print(sandwich_order) 