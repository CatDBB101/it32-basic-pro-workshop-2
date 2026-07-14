name = input("name :")
age = int(input("age :"))
height = int(input("height(cm) :"))
power = int(input("power(1-10) :"))
money = int(input("money :"))

isPass = True

if age < 18:
    print("Age must more than or equal 18.")
    isPass = False
if power < 10:
    print("Power must be full only, We need productivity.")
    isPass = False

if isPass:
    print("WELCOME TO OUR CORP.")
else:
    print("YOU SHALL NOT PASS !!!")
