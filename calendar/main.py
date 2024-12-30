from utils.month import monthCal
from utils.year import yearCal
def main():
    while True:
        print("------- MENU---------")
        print("1.To print specific month calender:")
        print("2.To print specific year calender:")
        print("3.Exit:")

        ch=int(input("Enter your choice:"))
        if(ch==1):
            year=int(input("Enter year: "))
            month=int(input("Enter month :"))
            monthCal(year,month)

        elif(ch==2):
            year=int(input("Enter year: "))
            yearCal(year)
        else:
            exit()

if __name__ == "__main__":
    main()
