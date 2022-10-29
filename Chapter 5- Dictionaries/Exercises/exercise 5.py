##exercise 5:
list = []
an1 = {"animal":"cat",
       "owner":"malez"}
list.append(an1)
an1 = {"animal":"dog",
       "owner":"qasim"}
list.append(an1)
an1 = {"animal":"parrot",
       "owner":"ahmed"}
list.append(an1)
an1 = {"animal":"goldfish",
       "owner":"shahryar"}
list.append(an1)
an1 = {"animal":"hamster",
       "owner":"saif"}
list.append(an1)
print(list)
for an1 in list:
  print("\nbelow are the animal and their owner:")
  for key, value in an1.items():
    print(f"\t{key}: {value}")