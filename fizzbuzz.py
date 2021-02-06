# shortest
# for i in range(1,101):
#     print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)

# readable
def isDivisible(a, b):
    return a % b == 0

for i in range(1,101):
    output = "Fizz" if isDivisible(i,3) else ""
    output += "Buzz" if isDivisible(i,5) else ""
    print(output or i)