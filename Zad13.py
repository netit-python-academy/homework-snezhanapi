# Ask for enter the number from the use
number = int(input("Enter the integer number: "))
number2 = number
# Initiate value to null
revs_number = 0

# reverse the integer number using the while loop

while (number > 0):
    # Logic
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

# Display the result
print(f"The reverse number is : {revs_number}")

res = [int(x) for x in str(number2)]
res.reverse()
res2 = [str(integer) for integer in res]
# printing result
res2 = int("".join(res2))
print("The list from number is ", res2)