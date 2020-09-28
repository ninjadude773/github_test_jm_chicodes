# Question 1 - Write a function to print "Hello_USERNAME"

def hello_name(user_name):
    print("Hello" + user_name.upper()+ "!")

hello_name('Carlos')

#Question 2 - Print first odd numbers 1 and 100
def odd_numbers():
    for i in range(0, 101, 2):
        print(i)

# Question 3 - Write a function that returns the max number in a given list:
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([2,3,5,8,9])
print(max_num_in_list([2,3,5,8,9]))

#Question 4 - Write a function to return if the given year is a leap year

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year}) is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
is_leap_year(2020
)      

#Write a function to find all consecutive numbers inside of a list

