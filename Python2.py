#!/usr/bin/env python
# coding: utf-8

# # Functions, Scoping, Data Collections 1 & List Comprehensions

# ## Tasks Today:
# 
# <i>Monday Additions (or, and ... if statements)</i>
# 
# 1) String Manipulation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) strip() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) title() <br>
# 2) Working With Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) min() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) max() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) sum() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) sort() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Copying a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) 'not in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Checking an Empty List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Removing Instances with a Loop <br>
# 3) List Comprehensions <br>
# 4) Tuples <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) sorted() <br>
# 5) Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) User-Defined vs. Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Accepting Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Default Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Making an Argument Optional <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Keyword Arguments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) Returning Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) *args <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Docstring <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Using a User Function in a Loop <br>
# 6) Scope

# ### String Manipulation

# ##### .lstrip()

# In[6]:


# string.lstrip()
name = "      Alex R"
print(name.lstrip())


# ##### .rstrip()

# In[8]:


# string.rstrip()
name = " Alex R       "
print(name.rstrip())


# ##### .strip()

# In[9]:


# string.strip()
name = "   Alex   "
print(name.strip())


# ##### .title()

# In[12]:


# string.title()
name = "alex" " trevor"
print(name.title())


# ### String Exercise <br>
# <p>Strip all white space and capitalize every name in the list given</p>

# In[34]:


names = ['    coNNor', 'max', ' EVan ', 'JORDAN']
# HINT: You will need to use a for loop for iteration
new_names = [item.strip() for item in names]
upper = [name.upper() for name in new_names]
print(upper)

    


# ### Working With Lists

# ##### min()

# In[35]:


# min(list)
list = [1,3,2,4,5]
print(min(list))


# ##### max()

# In[36]:


# max(list)

print(max(list))


# ##### sum()

# In[37]:


# sum(list)
print(sum(list))


# ##### sorted()

# In[38]:


# sorted(list)
new_list = sorted(list)
print(new_list)


# ##### .sort() <br>
# <p>Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list</p>

# In[41]:


# list.sort()
list.sort()
print(list)

# use sorted when you don't want to alter original list, use .sort() when you want to alter original list


# ##### Copying a List

# In[42]:


# [:] copies a list, doesn't alter original
list_2 = list [:]


# ##### 'in' keyword

# In[53]:


people = ['chris','kara','alex','travis','trevor']
if 'alex' in people:
    print('hes in there')


# ##### 'not in' keyword

# In[54]:


if 'zack' not in people:
    print('hes not in there')


# ##### Checking an Empty List

# In[ ]:


# if l_1: or if l_1 = []


# ##### Removing Instances with a Loop

# In[55]:


# while, remove
list_3 = []
if list_3 == []:
    print('its empty')


# ### List Exercise <br>
# <p>Remove all duplicates<br><b>Extra: Create a program that will remove any duplicates from a given list</b></p>

# In[76]:


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
new_names = []
# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier
for name in names:
    if name not in new_names:
        new_names.append(name)




print(new_names)


# ### List Comprehensions <br>
# <p>Creating a quickly generated list to work with<br>*result*  = [*transform*    *iteration*         *filter*     ]</p>

# ##### In a list comprehension we have a few pieces:
# 1. The first is the counter/ variable - IN this the variable is x
# 2. then we have a transform for the variable
# 3. The finale part of a list comp is called the condition
# 
# ```python
#     [variable, transform, condition]
# ```

# In[ ]:


# number comprehension

# With a regular for loop
nums = []

for i in range(100):
    nums.append(i)
print(nums)

# IN a list comprehension we have a few pieces:
# The first is the counter/ variable - IN this the variable is x
# Then we have a transform for the variable 
# The finale part of a list comp is called the condition
#[variable, transform, condition]




# There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.
# 
# Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.
# 
# Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# In[ ]:


# square number comprehension


# In[ ]:


# string comprehension




# In[ ]:





# In[ ]:





# ### Tuples <br>
# <p><b>Defined as an immutable list</b></p><br>Seperated by commas using parenthesis

# In[80]:


tuple = ('alex', 'hi','aaron')
print(tuple)


# ##### sorted()

# In[81]:


tup2 = sorted(tuple)
print(tup2)


# ##### Adding values to a Tuple

# In[84]:


tup 3 = ('trevor','travis','max')
new_tup = (tup 3 , + tup 2)
print(new_tup)


# ## Functions

# ##### User-Defined vs. Built-In Functions

# In[85]:


def sayHello():
    return 'Hello World'
sayHello()


# ##### Accepting Parameters

# In[87]:


def my_range(stop, start=0, step=1):
    for i in range(start,stop,step):
        print(i)
        
        
my_range(20,8,4)


# ##### Default Parameters

# In[ ]:





# ##### Making an Argument Optional

# In[ ]:





# ##### Keyword Arguments

# In[ ]:


# last_name='Max', first_name='Smith' in the function call

# see above


# # Creating a start, stop, step function

# In[ ]:


def my_range(stop, start=0, step=1):
    for i in range(start,stop,step):
        print(i)
        
        
my_range(20,8,4)


# ##### Returning Values

# In[88]:


def addNums(num1, num2):
    return num1 + num2 
addNums (5,2)


# ##### *args

# In[93]:


#stands for arguments and takes ANY number of arguments as parameters
#must be last if multiple parameters are present
def printArgs(num1, *args, **kwargs):
    print(num1)
    print(args)
    print(kwargs)
    
    for arg in args:
        print(arg)
        
    for kwarg in kwargs:
        print(kwarg)
printArgs(36, 'Dragonzord','vanilla', 2,3,testing='joel')


# ##### Docstring

# In[95]:


def printNames(list_1):
    '''
        printNames(list_1)
        Function requires a list to be passed as a parameter 
        and will print hte contents of the list. Expcecting a list of names(strings) 
        to be passed
        
    '''
    for name in list_1:
        print(name)
printNames(['George','Ramon','Peter'])
help(printNames)


# ##### Using a User Function in a Loop

# In[97]:


def printInput(answer):
    print(answer)
response = input('are you ready to quit')
while True:
    ask = input('what do you want to do?')
    printInput(ask)
    
    response = input('ready yet?')
    if response.lower() == 'quit':
        break


# ## Function Exercise <br>
# <p>Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names</p>

# In[ ]:


first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']
def fullName():
    for name in first_name:
        if name not in fullName
        


# ## Scope <br>
# <p>Scope refers to the ability to access variables, different types of scope include:<br>a) Global<br>b) Function (local)<br>c) Class (local)</p>

# In[ ]:





# # Exercises

# ## Exercise 1 <br>
# <p>Given a list as a parameter,write a function that returns a list of numbers that are less than ten</b></i></p><br>
# <p> For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]</p>

# In[2]:


list_1 = [1,11,14,5,8,9]

def underten(list_1):
    for number in list_1:
        if number < 10:
            return number

print(underten([1,11,14,5,8,9]))
        
#im sorry i spent 6 hours on this and this is as close as i can get.
#its easy unless i use a def function then its just impossible for me.
    




# ## Exercise 2 <br>
# <p>Write a function that takes in two lists and returns the two lists merged together and sorted<br>
# <b><i>Hint: You can use the .sort() method</i></b></p>

# In[1]:


l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
# add the two lists together, then sort them

def list (*lists):
    lists = l_1 + l_2 
    
    return sorted(lists)

print(list())


# In[ ]:

