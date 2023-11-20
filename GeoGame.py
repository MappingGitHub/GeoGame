from tkinter import *
window=Tk()
window.title("Welcome to GeoGame for Los Angeles County GIS DAY 2024")

#the font parameter can be passed to any widget to change its font,
#thus it applies to more than just labels.
lbl = Label(window, text="Welcome to Los Angeles County GIS Day ""\n\nPlease Register your Name", font=("Arial Bold", 30))
lbl.grid(column=200,row=100)


#dding the button to the window
#change the foreground of a button or any other widget using the fg property
#change the background color of any widget using the bg property.
btn1 = Button(window, text="Register", bg="orange", fg="red")
btn1.grid(column=1, row=0)
btn2 = Button(window, text="Print final Resualts", bg="orange", fg="red")
btn2.grid(column=2, row=0)


#set the default window size using the geometry function
window.geometry('1100x700')

#the mainloop function calls the endless
# loop of the window,so the window will 
#wait for any user interaction till we close it.
window.mainloop()
