#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    ones = [i for i, n in enumerate(nums) if n == 1]
    for one in ones:
        if (one + 2 < len(nums)
        and nums[one + 1] == 2 
        and nums[one + 2] == 3):
            return True
    return False


print("True")
print(arrayCheck([1,1,2,3,1]))
print("False")
print(arrayCheck([1,1,2,4,1]))
print("True")
print(arrayCheck([1,1,2,1,2,3]))

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def string_bits(str):
    out_str = ""
    for i in range(len(str)):
        if i%2 == 0:
            out_str += str[i]
    return out_str


print("Hlo")
print(string_bits("Hello"))
print("H")
print(string_bits("Hi"))
print("Hello")
print(string_bits("Heeololeo"))

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    if len(a) > len(b):
        longer_str = a
        shorter_str = b
    else:
        longer_str = b
        shorter_str = a
    return longer_str[-len(shorter_str):].lower() == shorter_str.lower()


print("True")
print(end_other("Hiabc", "abc"))
print("True")
print(end_other("AbC", "HiaBc"))
print("True")
print(end_other("abc", "abXabc"))

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    out_str  = ""
    for char in str:
        out_str += 2*char;
    return out_str


print("TThhee")
print(double_char("The"))
print("AAAAbbbb")
print(double_char("AAbb"))
print("HHii--TThheerree")
print(double_char("Hi-There"))
#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
    
def fix_teen(n):
    if (n not in range(13,20)
            or (n == 15 or n == 16)):
        return n
    else:
        return 0

print('6')
print(no_teen_sum(1, 2, 3))
print('3')
print(no_teen_sum(2, 13, 1))
print('18')
print(no_teen_sum(2, 1, 15))

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    evens = list(filter(lambda x: x%2 == 0, nums))
    return len(evens)

print('3')
print(count_evens([2, 1, 2, 3, 4]))
print('3')
print(count_evens([2, 2, 0]))
print('0')
print(count_evens([1, 3, 5]))
