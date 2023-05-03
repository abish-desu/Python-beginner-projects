from tkinter import *
import os

shut_down = Tk()                    # Tk class  
shut_down.title("Shutdown App")
shut_down.geometry("500x500")
shut_down.config(bg="black")

def restart():
    os.system("shutdown /r /t 1 ")
def restart_time():
    os.system("shutdown/r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")

restart_button = Button(shut_down,text="Restart",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus")
restart_button.place(x=150,y=70,height=50,width=200,command=restart)

restart_time = Button(shut_down,text="Restart with time",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus")
restart_time.place(x=150,y=170,height=50,width=200,commadn=restart_time)

log_out_button = Button(shut_down,text="Log Out",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus")
log_out_button.place(x=150,y=270,height=50,width=200,command=logout)

shutdown_button = Button(shut_down,text="Shut Down",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus")
shutdown_button.place(x=150,y=370,height=50,width=200,command=shutdown)



shut_down.mainloop()                # main loop function