print("Welcome to Quiz game..")
game = input("Do you want to play? ")
score = 0

if game.lower()!= "yes":
   print("See You Again!!!")
   quit()
else:
    print("let's play!!!")

question = input("Long form of RAM? ")
if question.lower() !="random access memory":
    print("Incorrect")
    score = score - 1

else:
    print("correct!!!")
    score = score + 1


question = input("long form of ROM? ")

if question.lower() == "read only memory":
    print("correct!!!")
    score = score + 1

else:
    print("Incorrect!!")
    score = score - 1

print(f"score: {score}")
print(f"percentage: {score/2 * 100}")
