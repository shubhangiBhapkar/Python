class Access:
    def __init__(self,x,y):
        self._pro_var=x
        self.__pri_var=y
    
    def access(self):
        return self.__pri_var


obj=Access(10,5)
print(f"private variable value:{obj.access()}")