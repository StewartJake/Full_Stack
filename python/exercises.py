#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print("d")
print(s[0])
# 'o'
print("o")
print(s[-1])
# 'djan'
print("djan")
print(s[:4])
# 'jan'
print("jan")
print(s[1:4])
# 'go'
print("go")
print(s[-2:])

# Bonus: Use indexing to reverse the string
reversed = s[::-1] 
print(reversed)

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
print("goodbye")
l[2][2] = "goodbye"
print(l[2][2])

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:
print("hello * 3")
d1 = {'simple_key':'hello'}
print(d1["simple_key"])
d2 = {'k1':{'k2':'hello'}}
print(d2["k1"]["k2"])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3["k1"][0]["nest_key"][1][0])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"
print("Hello my dog's name is {name} and he is {age} years old"
        .format(age=4, name="Sammy"));
# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
