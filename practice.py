Solve these Questions using loops and recursion
 
1.	Find Sum of numbers from 1 to n 
find out the sum of numbers from 1 to n like 1 + 2 + 3 + 4 +, etc


2.	Reverse a string 

3. Adding all numbers in a list 


Python Practice Questions

1.# we need to write a python program to find the power of a number using recursion
# input : num = 2, power= 3
# output : 8

def power(N,P):
    if P== 0:
        return 1
        return(N*power(N, P-1))
        if __name__'main':
            N = 2
            P = 3
            Print(power(N,P))


2.Assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)

display_student("AASHA", 26)


3.Python Program to Print All Odd Numbers in a Range

Start,end=4,19
for num in range(start ,end+1):
    if num% 2!=0:
        print(num,end = "")

4.Python Program to Check Whether a Given Number is Even or Odd using Recursion

def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))
n=int(input("Enter number:"))
if(check(n)==True):
      print("Number is even!")
else:
      print("Number is odd!")

5.Python Program to Check whether a Number is Prime or Not using Recursion

def check(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Number not prime")
            return False
        else:
            return check(n, div-1)
    else:
        print("Number is prime")
        return 'True'
n=int(input("Enter number: "))
check(n)
6.Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

# input the maximum number to
# which you want to send
max_num = 20
 
# starting numbers from 0
n = 1
 
# run until it reaches maximum number
print("Numbers not divisible by 2 and 3")
while n <= max_num:
     
    # check if number is divisible by 2 and 3
    if n % 2 != 0 and n % 3 != 0:
        print(n)
     
    # incrementing the counter
    n = n+1

7.Python Program to Check if a Number is a Palindrome

# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
8.Python Program to Count the Number of Vowels in a String

string=raw_input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)
9.Python Program to Remove Odd Indexed Characters in a string

def modify(string):  
  final = ""   
  for i in range(len(string)):  
    if i % 2 == 0:  
      final = final + string[i]  
  return final
string=raw_input("Enter string:")
print("Modified string is:")
print(modify(string))

10.Python Program to Remove the nth Index Character from a Non-Empty String

# index to remove character at
n = 4
 
# declaring an empty string variable for storing modified string
modified_str = ''
 
# iterating over the string
for char in range(0, len(str)):
 
    # checking if the char index is equivalent to n
    if(char != n):
        # append original string character
        modified_str += str[char]
 
print("Modified string after removing ", n, "th character ")
print(modified_str)
11.Python Program to Replace Every Blank Space with Hyphen in a String

string=raw_input("Enter string:")
string=string.replace(' ','-')
print("Modified string:")
print(string)

12.Python Program to Calculate the Length of a String Without using Library 

string=raw_input("Enter string:")
count=0
for i in string:
      count=count+1
print("Length of the string is:")
print(count)

13. Python Program to Count Number of Lowercase Characters in a String

string=raw_input("Enter string:")
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)

14.Python Program to Count the Number of Vowels in a String

string=raw_input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)

15.Python Program to Count Number of Uppercase and Lowercase Letters in a String
string=raw_input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)



16.Python Program to Find Common Characters in Two Strings
s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)

17.String Palindrome Program in Python

string=raw_input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")

18.Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively

def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
string=raw_input("Enter string:")
ch=raw_input("Enter character to check:")
print("Count is:")
print(check(string,ch))






