
nums = {1:"One", 2:"Two", 3:"Three" ,4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight",\
        9:"Nine", 0:"Zero", 10:"Ten", 11:"Eleven", 12:"Tweleve" , 13:"Thirteen", 14:"Fourteen", \
        15: "Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty",\
        60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety", 100:"Hundred"}
num = int(input("Enter a number: "))
# To convert three digit number into words
if 101 <= num < 1000:
    a = num // 100
    b = num % 100
    c = b // 10
    d = b % 10
    if c == 1 :
        print (nums[a] + " hundred" , nums[b])
    elif c == 0:
        print (nums[a] + " hundred" , nums[d])
    else:
        c *= 10
        if d == 0:
            print( nums[a] + "hundred", nums[c])
        else:
            print(nums[a] + "hundred", nums[c], nums[d])
    # to convert two digit number into words
elif 0 <= num <= 100:
    a = num // 10
    b = num % 10
    if a > 1 and a < 10 and b!=0:
        a *= 10
        print(nums[a], nums[b])
    else:
        print(nums[num])

