#ask for two numbers and add the up


check=True

turns=3

while turns>2:

    number1=input("Give me your first number: ")
    number2=input("Give me your second number: ")


    try:
        int(number1)
        check=True

    except ValueError:
        input("Give me a number: ")
        check=False


    else:
        sum= number1 + number2
        print("sum: ", sum)
        print(sum)

    turns+=1







# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# sum = a + b
# print("sum:", sum)

 



# else:
#     print(len(userInput)) 
# for i in userInput:
#     print(i)

# if len(userInput>3):
#     print(userInput[3])
