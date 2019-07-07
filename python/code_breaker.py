import random
import sys
import pdb


def build_num():
    """
    Fn: creates the number for the user to guess
    Args: None
    Ret: a tuple of three numbers
    """
    out_num = set()
    while len(out_num) < 3:
        num = random.randint(0,9)
        out_num.add(num)
    return tuple(out_num)


def parse_input(user_str):
    """
    Fn: takes input and turns into a tuple for comparisons
        if there are not 3 characters, prints a warning
    Arg: a string received from user
    Ret: a tuple of the str characters
    ***: on error will exit function
    """
    try:
        if len(user_str) == 3:
            # list comprehension into a tuple
            return tuple([int(n) for n in user_str]) 
        else:
            print('Invalid Input!')
            return tuple()
    except ValueError:
        print("Your input must be integers")
        sys.exit()

def sanitize_input(user_tpl):
    """
    Fn: checks if every character is an integer
    Arg: 1 tuple
    Ret: a boolean; true if all chars are ints
    """
    input_fine = True
    for char in user_tpl:
        if type(char) != int:
            input_fine = False
    return input_fine


def compare_user_comp(user_tpl, cmp_tpl):
    """
    Fn: checks two tuples for simililarities
    Arg: 2 tuples
    Ret: a string that interprets the relationship between the two
    """
    msgs = ('close ', 'match ', 'nope')
    out_msg = ""
    for item in user_tpl:
        if (item in cmp_tpl
                and user_tpl.index(item) != cmp_tpl.index(item)):
            out_msg += msgs[0]
            break
    for item in user_tpl:   
        if (item in cmp_tpl
                and user_tpl.index(item) == cmp_tpl.index(item)):
            out_msg +=  msgs[1]
            break
    if out_msg == "":
        out_msg += msgs[2]
    if user_tpl == cmp_tpl:
        out_msg = msgs[3]
    return out_msg

def get_input():
    """
    Fn: gets, converts, and checks user input
    Arg: None
    Ret: a tuple representing user guess
    """
    choice = input("What is your guess?\n"
            + "Please type in 3 integers, eg. [456]\n")
    choice_tpl = parse_input(choice)
    if sanitize_input:
        return choice_tpl
    return ()


def check_winner(user, comp, num_tries):
    """
    Fn: checks if user has exact match
    Arg: user & comp as tuple, num_tries as integer
    Ret: None, on success exits function
    """
    if user == comp:
        print("GENIUS! You've outsmarted me.\n"
                + "Only took you "
                + str(num_tries) + " tries to do it.")
        sys.exit()

def game():
    """
    Fn: Actually play the game
    Arg: None
    Ret: None
    ***: contains an infinite loop
    """
    code_to_guess = build_num()
    tries = 0
    while True: 
        user_guess = get_input()
        tries += 1
        check_winner(user_guess, code_to_guess, tries)
        print(compare_user_comp(user_guess, code_to_guess))


game()

