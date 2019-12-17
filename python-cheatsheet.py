from sys import argv
from os.path import exists

############# Print Statements  #############
print("hello World")

### Multi-line prints
print("""
Alight, so you said you like food ad
you just figuted out how to do multi-line prints
Nice!
""")

############# Operators
### Mdoulo
remainder = 10%3
print(remainder)

### Addition
num1 = 1
num1 += 1 #num1 = num1 + 1

### Comparators
print("is 2 greater than 5", 2>=5)

############# Formatting #############
### Float
float = float(5/2)
num = 3
print(num+float)

### F string
type_of_people = 10
x = f"There are {type_of_people} types of people."
print (x)

### format
hilarious = True
joke_evaluation = "Isn't this fun? {}"
print(joke_evaluation.format(hilarious)) #Converts value to string then concatinates to string its being called by

### Concatination
end1 = "H"
end2 = "i"
print(end1 + end2)

### New Line
print("Jan\nFeb\nMar")

### Escape characters \
backlash_cat = "I'm \\ a \\ cat."
print(backlash_cat)

### Round function
float_num = 3.4444444444
print(round(float_num,2))

############# Inputs #############
bill = float(input("Tell me, how much was the bill? $"))

### Multi-line input
print("How much do you weigh?", end=' ')
weight = input()

### Inputs with printf
answer = input(f"So your {weight}. Is that right? ")

### sys and argv (inputs from cmd line)
script, first = argv # make sure to import argv from sys
print(f"The script is called {script}")
print(f"Your first variable is {first}")

############# If/Elif/Else Statements #############
answer = input("Am I smart?")

if answer == "yes" or answer == "Yes" or answer == "y" or answer == "Y":
    print("ヽ(´▽｀)ノ \n Whoooohoooooo! \n I'm smart")
#Or you could do
# if answer in ['y','Y', 'yes','Yes']:

elif answer == "no" or answer == "No" or answer == "n" or answer == "N":
    print("*flips table* \n(╯°□°）╯  ┻━┻ \n You gotta be kidding me!")

############# Files #############
##### Opening a file
txt = input("Please enter the filename :")
file = open(filename) # default read

### Opening a file for write
file = open(filename, 'w')

### Exists
if exists(filename) == False:
    print("It does not exist")
### Writing to a file
file.write("Hello World")

### Opening a file for read
file = open(filename, 'r')

### Erasing an entire filen
file.truncate()

### Reading a file (ouputting it)
print(f"Here's your file {txt}:")
print(file.read())

### Sets the position of the file to the first character
file.seek(0)

### Prints the current line that is pointed to
# consecutive readlines() move the pointer to the next line (like a for loop)
# seek can also change the line of the pointer
print(file.readline(), end ='') # end = '' removes the \n character that is returned

### Closing a file
file.close()

############# Functions #############\
###nT Taking all arguements as a list
def print_two(*args): #don't use numbers in function names
    arg1, arg2 =args
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two("Indya", "Dodson")

### Normal Functions
def print_two_again(arg1, arg2): # standard is to have five arguements or less
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two_again("Indya", "Dodson")

def print_none():
    print("I got nothing.")

print_none()

# Returning values
def add(num1, num2):
    return num1 + num2

print(f"1 + 2 = {add(2, 1)}")

# Function Looping
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding,errors)
        return main(language_file, encoding,errors)

# Function tuple and Format
def test(a, b, c):
    return a, b, c

formula_test = test(1,2,3)
print("We'd have {} beans, {} jars and {} crates.".format(*formula_test))

# sotring values from  returned values
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

beans, cans, boxes = secret_formula(100)

############# Encoding  #############
#a ”byte” a sequence of 8 bits (1s and 0s).
# ASCII. This standard maps a number to a letter.
# Unicode 32-bit numbe 2^33 or 4,294,967,295 characters
# utf-8 means Unicode Transformation Format 8 Bits
# f you have raw bytes, then you must use .decode() to get the string
# encode() function is used from string to raw_bytes
# ”DBES” mnemonic. ”Decode Bytes, Encode Strings”

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors=errors) #encode strings, this turns it into bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) #decode bytes, this turns it into strings
    print(raw_bytes, "<=========>", cooked_string)

############# Encoding  #############

split
