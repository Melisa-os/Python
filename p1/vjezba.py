list = []
for i in range(10):
    list.append(int(input("Enter a number: ")))
for i in list:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

while  True:
    try:
        num = int(input("Enter a number: "))
        if num == 0:
            break
        list.append(num)
    except ValueError:
        print("Invalid input")
print(list)