import string
import random

if __name__ == '__main__':
    len =int(input("Enter Password Length\n"))
    pun =input("Enter True if you want to include characters\n")
    
    lets=string.ascii_letters
    nums=string.digits
    char=string.punctuation
    pswd=[]
    pswd.extend(list(nums))
    pswd.extend(list(lets))
    if pun == "True":
        pswd.extend(list(char))
   
        
          
    print ("Your Password is")
    print("".join(random.sample(pswd,len))) 



        
    