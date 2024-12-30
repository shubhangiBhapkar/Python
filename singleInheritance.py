class Company:
    def __init__(self,name,proj):
        self.name=name
        self.proj=proj

    def show(self,x):
        self.code=x
        print("company location is {x}")

    
class Emp(Company):
    def __init__(self,ename,sal,cname,proj):
        Company.__init__(self,cname,proj)
        self.ename=ename
        self.__sal=sal

    def show_salary(self):
        print(f"Salary of {self.name}is{self.__sal}")
c=Company("jio Ind","6G")
e=Emp("Ashish",5000,c.name,c.proj)
