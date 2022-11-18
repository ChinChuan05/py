import random

Range = eval(input("Give me number range (about50): "))
element = eval(input("Give me list length (about10): "))

MyList1 = list()
MyList2 = list()
MyList3 = list()

for i in range(element):
    rand = random.randrange(Range)
    MyList1.append(rand)
    MyList2.append(rand)
    MyList3.append(rand)


element -= 1
for i in range(element):
    for j in range(element):
        if MyList2[j] > MyList2[j+1]:
            buffer = MyList2[j]
            MyList2[j] = MyList2[j+1]
            MyList2[j+1] = buffer

i = j = 0
for i in range(element):
    for j in range(element):
        if MyList3[j] < MyList3[j+1]:
            buffer = MyList3[j]
            MyList3[j] = MyList3[j+1]
            MyList3[j+1] = buffer

print(f"\nMylist 1 is {MyList1}")
print(f"Mylist 2 (small to big) is {MyList2}")
print(f"Mylist 3 (big to small) is {MyList3}\n")

element += 1
count = 0
for i in range(element):
    if MyList2[i] % 2 != 0:
        count += 1
        mark = i
        print(MyList2[i], end=', ')

print(f"\nWe have {count} odd number(s), max odd number is: {MyList2[mark]}")

