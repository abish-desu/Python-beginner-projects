# creating madlibs using string concatenation
# string concatenation (put strings together)
# example
""" word = "Hello"
print(word + " Abish")
print("{} Abish".format(word))
print(f"{word} Abish") 
Output of all three : Hello Abish"""

# program
_1 = input("Animal : ")
_3 = int(input("enter odd number : "))                  
_4 = int(input("enter binary code number : "))                  
_2 = int(input("enter even number : "))                  

sentence = f"{_1} is domestic animal.{_2} is even number.\
{_3} is odd number.{_4} is a binary code"
print(sentence)

