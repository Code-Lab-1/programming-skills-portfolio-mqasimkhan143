##exercise 5:
sandwich_order = ["chicken sandwich ","pastrami","beef sandwich","pastrami","cheese sandwich","pastrami"]
finished_sandwiches = []
print("Your order is:",sandwich_order)
print("we sre out of ingredients for pastrami")
for i in range(0, 3):
  if sandwich_order != "pastrami":
    finished_sandwiches.append(sandwich_order.pop(0))
    finished_sandwiches.sort()
    print("Your order is done")
    print(finished_sandwiches)
    sandwich_order.remove("pastrami")
  else:
    print("out of ingredients for pastrami")  
sandwich_order.append("pastrami")    
sandwich_order.append("pastrami") 
sandwich_order.append("pastrami")    
print("Your finished sandwiches:")    
print(finished_sandwiches) 
print("not made sandwich:")
print(sandwich_order) 
