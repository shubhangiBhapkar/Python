num=12
if num>0:
    print("number is positive",num)
elif num<0:
    print("number is negative: ",num)
else:
    print("it is zero")
    

for i in range (1,5):
    print(i)
print("------------------")
for i in range(5,1,-1):
    print(i)
print("------------------")
count=1
while count<=5:
    print(count)
    count=count+1
print("------------------")
count=5
while count>=1:
    print(count)
    count=count-1
print("------------------")

for i in range(1,10):
    if i==5:
        print("applay break at ",i)
        break
    print(f"loop iterate: {i}")

    print("------------------")

    for i in range(1,10):
        if i%2==0:
            # print("skip even")
            continue
        print(i)

print("------------------")

for i in range(1,5):
    pass

print("------------------")

def greet():
    print("hello")
greet()

def add(x,y):
    return x+y
print(add(2,4))