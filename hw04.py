# ------------------------------------------------------
#        Name: (put your name here)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1

def check_text():
    #docstring
    while True:
         text = str(input("Give me a sentence: "))
         if secret_word in text:
             print("You used the secret word!")
             break
         if  "dog" in text or "Dog" in text:
             print("You used the word \"dog\" or the word \"Dog\"!")
             break
         else:
            print("Try again")
            continue

# Task 2

def check_greater():
    #Add your docstring
    while True:
        int1 = int(input("give me an integer: "))
        int2 = int(input("give me another integer: "))
        if int1>int2:
            print("First is Greater")
            break
        if int2>int1:
            print ("Second is Greater")
            break
        else:
            print ("Try again")
            continue

# Task 3
def get_special_numbers():
    #Add your docstring 
    x = 1
    while x in range (1,41):
        if x%2 == 0 or  x%3 != 0 or x%5 == 0:
            x+=1
            continue
        else:
            print(x)
            x+=1 

# Task 4.a
def my_for_loop():
    #Add your docstring
    while True:
        string = str(input("give me a string: "))
        if len(string) not in range (2,6):
            print("bad word")
            return
        if " " in string:
              print("bad word")
              return
        else:
            for char in string:
                if char in "aeiouAEIOU":
                    print(f"letter {char} is a vowel")
                else:  
                    print(f"letter {char} is a consonant")
            break
            
# Task 4.b
def my_while_loop():
    while True:
        letter=str(input("choose one option: a, b, or c: "))
        if letter == "a":
            continue
        elif letter == "b":
            print("Goodbye")
        elif letter == "c":
            exit()
        else:
            print("try again")
            continue
        break
        
# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
