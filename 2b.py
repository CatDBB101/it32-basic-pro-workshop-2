name = input("name : ")
age = int(input("age : "))
height = int(input("height(cm) : "))
power = int(input("power(1-10) : "))
money = int(input("money : "))

# Pass or not dicision

isPass = True
print("=" * 50)
if age >= 18:
    print("\tAge must more than or equal 18.")
    isPass = False
if power < 2:
    print("\tPower must be full only, We need productivity.")
    isPass = False

if isPass:
    print("WELCOME TO OUR CORP.")
else:
    print("YOU SHALL NOT PASS !!!")
    exit()

# Position dicision

if age >= 20 and power < 5:
    print("Your position is \"Gunner\".")
elif power >= 5 and power <= 8:
    print("Your position is \"Guard\".")
elif power >= 9:
    print("Your position is \"Giant Guard\".")
elif money >= 10_000_000:
    print("Your position is \"Boss\".")
else:
    print("Your positon is \"Janitor\".")
