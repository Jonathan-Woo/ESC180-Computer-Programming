#Problem 1
print ("Hello, Python")

#Problem 2
strName1, strName2 = "Luna Wu", "Jonathan Woo"

print ("Hello,", strName1)
print ("Hello,", strName2)

#Rename variables (Problem 4)
strName1, strName2 = "Prof. Cluett", "Prof. Thywissen"

#Problem 3
print(f'Hello, {strName1} and {strName2}. Your names are {strName2} and {strName1}. Hi there. Your names are still {strName1} and {strName2}.')

#Problem 5
greetee = input("What's your name? \n")
if greetee.upper() == "LORD VOLDEMORT":
    print("I'm not talking to you.")
else:
    print(f'Hello {greetee}')
