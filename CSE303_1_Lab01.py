# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
print("Welcome to Python programming")
##using format specifier:
name = 'John'
age = 23
print("%s is %d years old." % (name, age))

#%%
##reading input from keyboard
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"{name} is {age} years old")
print(type(age))

#%%variable declaration- Integer
x = 5
print(x)
print(type(x))

#%% Variable declaration- String
x = "Hello"
print(x)
print(type(x))

#%%Variable declaration- Floating point numbers
import math
print(format(math.pi, '0.12g'))
print(format(math.pi, '0.6f'))

#%%
2**52 <= 2**56 //10 < 2**53

#%%
x = 2
score = ""
if x > 5:
    score = "high"
else:
    score = "low"
print(score)
#%%
##Now write a program in python 
##which will do the grade computation
#%%Data Structures
#Creating list
x = [3, "hello", 1.2]
print(x)
x.append("A")
print(x)

#creating tuple
x = (3.0, "hello")
print(x)


#String
st = "Rain starts"
print(st)
print(st.split(" "))

#Creating set
text = 'SDS in python'
print(set(text))
print(set(text.split(" ")))

##Creating Dictionaries
phonebook = {"John": 88017190000, 
             "Jack": 88017100000, 
             "Najiba": 8801719663546, 
             "Khusbu": 8801916971463}
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d"%(name, number))

for i in x:
    print(i)
#%%List Comprehension






