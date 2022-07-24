# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

# two methods to solve this problem.
# These both work, except when the integer ends in zeros
# Neither prints 0001 if 1000 is input. Both print 1

def reverse_integer(num):
    # check if int is negative or positive
    if num<0:
        isNegative = True
        num = abs(num)
    else:
        isNegative = False

    stringInt = str(num)    # convert the integer into a string
    reversedString = stringInt[::-1]
    print("Reversed string is: ", reversedString)

    reversedInt = int(reversedString)


    if isNegative:
        return -abs(reversedInt)
    else:
        return reversedInt

#--------------------------------------------------
def reverse_integer_slices(num):

    string = str(num)

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])
#--------------------------------------------------


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Number is:", 123, "Reversed number is: ", reverse_integer(123))
    print("Number is:", -246, "Reversed number is: ", reverse_integer(-246))
    print("Number is:", 10000, "Reversed number is: ", reverse_integer(10000))

    print("Number is:", 123, "Reversed number is: ", reverse_integer_slices(123))
    print("Number is:", -246, "Reversed number is: ", reverse_integer_slices(-246))
    print("Number is:", 10000, "Reversed number is: ", reverse_integer_slices(10000))

    print("Slices testing here:")
    a=[1,3,5,7,9]
    print(a[0:3])   # prints [1, 3, 5]
    print(a[2])     # prints 5

