##exercise 5:
party = []
n = int(input("enter the amount of people to invite:"))
for i in range(0, n):
  ele = str(input())
  party.append(ele)
for i in range(len(party)):
  print("Dear",party[i],",You have been invited to the party")
print("\n")
print(party[1],"cannot make it")
party[1] = str(input())
print(party)