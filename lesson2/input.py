print("What is your name?")
name = input()
print("Your name is " + name)
print("What is your age?")
age = input()
if (age.isdigit()):
   nextage = int(age) + 1
   print("You will be " + str(nextage) + " on your next birthday")
else:
   print("Sorry, " + age + " is not a whole number")


