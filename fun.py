import calendar as cal
print("----------------calendar program in python------------------")
print("Enter 'x' to exit")
y=input("Enter year:")
if y=='x':
    exit()
else:
    m=input("Enter month:")
    yy=int(y)
    mm=int(m)
    print("\n",cal.month(yy,mm))