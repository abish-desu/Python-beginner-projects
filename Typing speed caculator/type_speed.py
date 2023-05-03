from time import *
import random as r

def mistake(paragraph,user_text):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != user_text[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed(time_i,time_e,user_text):
    time_delay = time_e - time_i
    time_roundup = round(time_delay,2)
    speed = len(user_text)/time_roundup
    return round(speed)

if __name__ == '__main__':              # Doesn't run if imported as module
    while True: 
        check = input("ready to test : yes/ no : ")
        if check == "yes":
    
            texts = ["Hello, My name is Abish Magar","I am a computer science student","Data is the fuel of the future"]
            texts_1 = r.choice(texts)     # random text from texts
            print("*****Typing speed*****")
            print(texts_1)
            print()
            print()
            time_1 = time()
            text_input = input("Enter : ")
            time_2 = time()

            print("speed: " ,speed(time_1,time_2,text_input),'clicks/sec')
            print("error: ", mistake(texts_1,text_input))
        elif check == "no":
            print("Thank you")
            break
        else:
            print("Wrong input")




