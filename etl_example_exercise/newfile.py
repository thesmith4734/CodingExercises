### Create a list of all elements between 1 and 5000, keep only elements where sum of all digits is a multiple of 3 (12)
'''
- create a list
- range(1, 5000)

- list of each number in range
- list comprehension to return:
    - Splitting the number into individial digits
    - Cheking if the sum of those digits % 3 = 0

'''

def sumDigits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum


number_list = list(range(1, 5000))

three_list = [x for x in number_list if (sumDigits(x) % 3) == 0]

print(three_list)