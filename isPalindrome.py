#1 ere solution
def isPalindrome(string:str)->bool:
    return string == "".join(list(reversed(string)))
#2 eme solution
def isPalindrome2(string:str)->bool:
    return string == string[::-1]
# il y a plein d'autre solution que je ne couvrirais pas ici.
  
  
