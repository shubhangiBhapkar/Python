float_varr=12.5
string_var="hello"
bool_var=True

# LIST

# list_var=[44,32,67,'hello',1.1]
# print(f"list={list_var}");print(f"list ={list_var[1]}")
# print(f"list={list_var[:]}");print(f"list={list_var[1:4]}")
# print(f"list last index={list_var[-1]}")
# print(f"list last to 2nd: {list_var[-1:-5:-1]}")

# list_var[1]=2.5

# list_var[1:5]=12,45,76,89,22
# print(f"list :{list_var}")

# list_var.append(7)
# print(f"list :{list_var}")
# list_var.extend([99,88,45,99])
# print(f"list :{list_var}")
# list_var.insert(2,75)
# print(f"list :{list_var}")
# list_var.remove(75)
# print(f"list :{list_var}")
# list_var.pop(2)
# print(f"list :{list_var}")

# list_var.sort()
# print(f"list :{list_var}")
# list_var.reverse()
# print(f"list :{list_var}")

# ***********************TOUPLE**********************
# -immutable
# -but we can add new touple at end

# touple_var=(11,77,22,44)
# print(touple_var+(12,55))
# -this are not applicaple to touple
# print(touple_var.append(7))
# print(touple_var.extend(7,23,11))
# print(touple_var.insert(2,34))
# print(touple_var.remove(77))
# print(touple_var.pop(1))

# ********************** SET **********************
# -it does not have index

# set_var={44,88,22}
# print(f"set_var= {set_var}")
# print(f"type of set_var= {type(set_var)}")
# set_var.add(4)
# print(f"after add set_var= {set_var}")
# set_var.discard(88)
# print(f"after discard set_var= {set_var}")
# union_set=set_var.union({1,6,9})
# print(f"after union set_var= {union_set}")
# set_difference=set_var.difference(union_set)
# print(f"difference = {set_difference}")

# ************ DICTIONARY ****************
# -key value pair
# -key is immutable, value is mutable
# -not follow indexing but follow key

# dict_var={1:'A','B':2}
# print(f"Dictionary ={dict_var}")
# dict_var['c']=3
# print(f"Added value ={dict_var}")
# dict_var[1]=22
# print(f"updated value ={dict_var}")
# dict_var.pop('c')
# print(f"remove c value ={dict_var}")
# keys=dict_var.keys()
# print(f"keys ={keys}")
# values=dict_var.values()
# print(f"values ={values}")
# items=dict_var.items()
# print(f"items ={items}")

# ************** AIRTHMATIC OPERATORS ***********************
a,b=20,50
print(f"{a}+{b}={a+b}");print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}");print(f"{a}/{b}={a/b}")
print(f"{a}%{b}={a%b}")

#  COMPARISON 
print(f"{a}=={b}={a==b}");print(f"{a}!={b}={a!=b}")
print(f"{a}>{b}={a>b}");print(f"{a}<{b}={a<b}")
print(f"{a}>={b}={a>=b}");print(f"{a}<={b}={a<=b}")

#  LOGICAL
t,f=True,False
print(f"t and f={t and f}");print(f"t or f={t or f}")
print(f"not f={not f}")

#  BITWISE

print(f"t & f={t & f}");print(f"t | f={t | f}")
a=5
print(a<<2)
