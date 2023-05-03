from cProfile import label
import speedtest as st
from tkinter import *

def speed_check():
    sp = st.Speedtest()
    sp.get_servers()
    down_load = str(round(sp.download()/(10**6),3)) + " Mbps"               # round(....,3) gives rounding of ....
    up_load = str(round(sp.upload()/(10**6),3)) + " Mbps" 
    lab_download.config(text=down_load)
    lab_up.config(text=up_load)


speed =  Tk()                       #Tk class in variable
speed.title("Internet speed test")
speed.geometry("500x500")
speed.config(bg = "Black")

# Label
lab = Label(speed, text="Internet speed test",font = ("Time New Roman",30,"bold"),bg = "Black",\
            fg = "White")
# position
lab.place(x=60,y=20,height=50,width=380 )   


lab = Label(speed, text="Download speed",font = ("Time New Roman",25,"bold"),bg = "white", fg = "black")
lab.place(x=60,y=100,height=50,width=380 )

lab_download = Label(speed, text="000",font = ("Time New Roman",25,"bold"),bg = "Black",fg = "White")
lab_download.place(x=60,y=160 ,height=50,width=380)

lab = Label(speed, text="Upload speed",font = ("Time New Roman",25,"bold"),bg = "white", fg = "black")
lab.place(x=60,y=220,height=50,width=380)

lab_up = Label(speed, text="000",font = ("Time New Roman",25,"bold"),bg = "Black",fg = "White")
lab_up.place(x=60,y=280,height=50,width=380 )

button_check = Button(speed, text="Check speed",font = ("Time New Roman",25,"bold"),bg = "red",fg = "Black",relief = RAISED,command=speed_check)
button_check.place(x=60,y=360,height=50,width=380)


speed.mainloop()









