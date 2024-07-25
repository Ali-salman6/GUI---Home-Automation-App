# Import the required libraries
from tkinter import *
from tkinter import ttk, messagebox
import datetime, time, pygame, cv2, webbrowser
from threading import Thread
from PIL import Image, ImageTk

# Create the main application window
App = Tk()
App.geometry("650x600") #Set the dimensions of the App
App.title("Home Application Simulation") # Set GUI's title
App.iconbitmap("C:\\Users\\pc\\Desktop\\Project\\home.ico")#Set GUI's icon 

# Load and display the image for the application window GUI
mobile = Image.open("C:\\Users\\pc\\Desktop\\Project\\mobile-in-hand.png")
newsize = (600, 600)
Appm = mobile.resize(newsize)
Appm = ImageTk.PhotoImage(Appm)
App_Lab = Label(image=Appm)
App_Lab.image = Appm
App_Lab.place(x=0, y=0)


                                ### iphone camera ####
camera = PhotoImage(file = "C:\\Users\\pc\\Desktop\\Project\\camera.png")
#camera.iconbitmap("C:\\Users\\Dell\\OneDrive\\Desktop\\Project\\garg.ico")
camera = camera.subsample(8, 8) 

def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

open_camera_button = Button(App, image=camera, command=open_camera)
open_camera_button.place(x=370, y=35)
        
    
# Initialize the Pygame mixer for audio playback
pygame.mixer.init()

##### music function for "Living room" ####
def play():
    pygame.mixer.music.load("C:\\Users\\pc\\Desktop\\Project\\theme.mp3")
    pygame.mixer.music.play(loops=0)

def music1(): ## bed room alarm 
    pygame.mixer.music.load("C:\\Users\\pc\\Desktop\\Project\\mixkit-classic-alarm-995.mp3")
    pygame.mixer.music.play(loops=0)
    
def stop():
    pygame.mixer.music.stop()
    
##################

                                  ### Buttons Functions:
                            ############ Kitchen Button ##############

# Function for Kitchen Button
def kitchen():
    global kit_Img
    kit = Toplevel() # Create a new window for the kitchen
    kit.title("Kitchen")
    kit.iconbitmap("C:\\Users\\pc\\Desktop\\Project\\cooking.ico")

    # Resize the image to fit the screen
    screen_width = 450
    screen_height = 350
    original_image = Image.open("Kitchentk.png")
    resized_image = original_image.resize((screen_width, screen_height), Image.LANCZOS)
    kit_Img = ImageTk.PhotoImage(resized_image)
    
    # Label to indicate the status of the switch
    label = Label(kit, text="The Switch Is On!", fg="green", font=("Helvetica", 32))
    label.pack(pady=0)

    # Button to toggle the switch
    is_on = True
    def Switch():
        nonlocal is_on
        if is_on:
            button.config(image=off)
            label.config(text="Switch to Off", fg="grey")
            is_on = False
        else:
            button.config(image=on)
            label.config(text="Switch to On", fg="green")
            is_on = True

    # Load the original images for the switch
    original_on = PhotoImage(file="C:\\Users\\pc\\Desktop\\Project\\blub1.png")
    original_off = PhotoImage(file="C:\\Users\\pc\\Desktop\\Project\\blub2.png")

    # Resize the images for the switch
    on = original_on.subsample(5, 5) 
    off = original_off.subsample(2, 3)

    button = Button(kit, image=on, bd=0, command=Switch, width=100, height=100)
    button.pack(pady=0) 

    Kit_Lab = Label(kit, image=kit_Img)  # Image label
    Kit_Lab.pack()

    # Button to go back
    btn1 = Button(kit, text="Back", command=kit.destroy)
    btn1.pack()

    
                            ############ BedRoom Button ##############
def BedRoom():
    global bed_Img
    bed = Toplevel()
    bed.title("BedRoom")
    bed.iconbitmap("C:\\Users\\pc\\Desktop\\Project\\bed.ico")
    
    hour = StringVar()
    min = StringVar()
    sec = StringVar()
    
    # Resize the image to fit the screen
    screen_width = 650
    screen_height = 550
    original_image1 = Image.open("childrenbed.png")
    resized_image1 = original_image1.resize((screen_width, screen_height), Image.LANCZOS)
    bed_Img = ImageTk.PhotoImage(resized_image1)
    bed_Lab = Label(bed, image=bed_Img).pack()
    
    addTime = Label(bed, fg="red", text="Hour      Min        Sec", font='arial 12 bold').place(x=440, y=270)
    setYourAlarm = Label(bed, text="Set Time(24hrs): ", bg="grey", font="arial 11 bold").place(x=300, y=300)

    # make the time input fields
    hourTime = Entry(bed, textvariable=hour, relief=RAISED, width=4, font=(20)).place(x=440, y=300)
    minTime = Entry(bed, textvariable=min, width=4, font=(20)).place(x=500, y=300)
    secTime = Entry(bed, textvariable=sec, width=4, font=(20)).place(x=560, y=300)

    def start_alarm():
        t1 = Thread(target=alarm)
        t1.start()

    def alarm():
        while True:
            set_alarm_time = f"{hour.get()}:{min.get()}:{sec.get()}"
            time.sleep(1)

            # Get current time
            actual_time = datetime.datetime.now().strftime("%H:%M:%S")
            FMT = '%H:%M:%S'

            # get time remaining
            time_remaining = datetime.datetime.strptime(
                set_alarm_time, FMT) - datetime.datetime.strptime(actual_time, FMT)

            # displays current time
            CurrentLabel = Label(
                bed, text=f'Current time: {actual_time}', fg='black')
            CurrentLabel.place(relx=0.2, rely=0.8, anchor=CENTER)

            # displays alarm time
            AlarmLabel = Label(
                bed, text=f'Alarm time: {set_alarm_time}', fg='black')
            AlarmLabel.place(relx=0.2, rely=0.9, anchor=CENTER)

            # displays time remaining
            RemainingLabel = Label(
                bed, text=f'Remaining time: {time_remaining}', fg='red')
            RemainingLabel.place(relx=0.7, rely=0.8, anchor=CENTER)

            if actual_time == set_alarm_time:
                music1()
                
    music_stop = Button(bed, text="Stop Alarm", command=stop)
    music_stop.place(x=320, y=260)
    
    submit = Button(bed, text="Set Your Alarm", fg="red", width=15,
                    command=start_alarm, font=("arial 20 bold")).place(x=290, y=370)

    btn2 = Button(bed, text="Back", command=bed.destroy).pack()
    
    
                            ############ Garage Button ##############

def Garage():
    global Garg_Img
    Gg = Toplevel()
    Gg.title("Garage Window")
    Gg.iconbitmap("C:\\Users\\pc\\Desktop\\Project\\garg.ico")
    
    # Resize the image to fit the screen
    screen_width = 500
    screen_height = 450
    original_image2 = Image.open("\\Users\\pc\\Desktop\\Project\\preview.png")
    resized_image2 = original_image2.resize((screen_width, screen_height), Image.LANCZOS)
    Garg_Img = ImageTk.PhotoImage(resized_image2)
    Garg_Lab = Label(Gg, image=Garg_Img).pack()
    
    def show():
        myLabel = Label(Gg, text=var.get()).pack()
    
    var = StringVar()
    
    c = Checkbutton(Gg, text= "Check to Open",variable=var, onvalue="Opening", offvalue="Closing")
    c.deselect()
    c.place(x=185, y=170)
    
    myButton = Button(Gg, image=door, command=show)
    myButton.place(x=190, y=200)

    btn3 = Button(Gg, text="Back", command=Gg.destroy).pack()

    
                            ############ Water-tank level Button ##############

def WatLevel():
    global WatLevl_Img
    Watlevl = Toplevel()  # Create a new top-level window for water-level display
    Watlevl.title("Water-Level Window")  # Set the window title
    Watlevl.iconbitmap("C:\\Users\\pc\\Desktop\\Project\\wat.ico")  # Set the window icon

    # Create a frame to hold the image on the left
    image_frame = Frame(Watlevl)
    image_frame.pack(side=LEFT, padx=20, pady=20)

    # Resize the image to fit the frame
    screen_width = 500
    screen_height = 500
    original_image3 = Image.open("C:\\Users\\pc\\Desktop\\Project\\water-storage.png")
    resized_image3 = original_image3.resize((screen_width, screen_height), Image.LANCZOS)
    WatLevl_Img = ImageTk.PhotoImage(resized_image3)  
    WatLevl_Lab = Label(image_frame, image=WatLevl_Img)  
    WatLevl_Lab.pack()  # Pack the image label into the image_frame

    # Create a frame to hold the progress bar on the right
    progress_frame = Frame(Watlevl)
    progress_frame.pack(side=RIGHT, padx=20, pady=20)
    
    def set_custom_style():
        style = ttk.Style()
        style.theme_use('default')
        style.configure("red.Horizontal.TProgressbar", background='red')


    def step():
        # Function to increment the progress bar value and show a warning if it reaches 100
        for x in range(5):
            my_progress['value'] += 20  
            Watlevl.update_idletasks()  
            time.sleep(0.5)  
            
            if my_progress['value'] == 100:
                set_custom_style()
                my_progress["style"] = "red.Horizontal.TProgressbar"
                messagebox.showwarning("Water Sensor", "Tank is full of water !!")  
                    
    # Create a vertical progress bar widget in the progress_frame
    my_progress = ttk.Progressbar(progress_frame, orient=VERTICAL, mode='determinate', length=200)
    my_progress.pack()

    # Create a button with an image named Water_Sensor, associated with the step() function
    my_button = Button(progress_frame, image=Water_Sensor, command=step).pack()

    #Create a "Back" button with a command to close the window when clicked
    btn4 = Button(Watlevl, text="Back", command=Watlevl.destroy)
    btn4.place(x=582, y=100)

    
                            ############ Living_Room Button ##############
def LivingR():
    global LivRoom_Img
    LivR = Toplevel()
    LivR.title("Living Room Window")
    LivR.iconbitmap("C:\\Users\\pc\\Desktop\\Project\\liv.ico")
    
    # Resize the image to fit the screen
    screen_width = 500
    screen_height = 450
    original_image4 = Image.open("C:\\Users\\pc\\Desktop\\Project\\livingroom.png")
    resized_image4 = original_image4.resize((screen_width, screen_height), Image.LANCZOS)
    LivRoom_Img = ImageTk.PhotoImage(resized_image4)
    LivRoom_Lab = Label(LivR, image=LivRoom_Img).pack()
    
    music_but = Button(LivR, image=music, command=play)
    music_but.place(x=50, y=50)
    
    music_stop = Button(LivR, text="Stop Music", command=stop)
    music_stop.place(x=60, y=18)
    
    btn4 = Button(LivR, text="Back", command=LivR.destroy).pack()
    
    def open_url():
        url = 'https://www.netflix.com'
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        webbrowser.get(chrome_path).open(url)
    
    open_button = Button(LivR, image= Netflix, command=open_url)
    open_button.place(x=255, y=175)

    
    
#BUTTON Images:
### Kitchen Button ### 
KitPhoto = PhotoImage(file = "C:\\Users\\pc\\Desktop\\Project\\Kitchen.png")
KitPhoto = KitPhoto.subsample(30, 35) 

kit = Button(App, image = KitPhoto, command=kitchen)
kit.pack()
kit.place(x=280, y=200)

lable1=Label(App,text=' Kitchen', foreground = 'Red', width=8).place(x=295,y=180) 

### BedRoom ### 
bedPhoto = PhotoImage(file = "C:\\Users\\pc\\Desktop\\Project\\bedroom.png").subsample(6, 7) 

bed = Button(App, image = bedPhoto,  command = BedRoom) 
bed.pack()
bed.place(x=421, y=100)

lable2=Label(App,text='Bed Room', foreground = 'orange', width=8) 
lable2.place(x=428,y=80)

### Garage ###
GaragePhoto = PhotoImage(file = "\\Users\\pc\\Desktop\\Project\\garage.png")
GaragePhoto = GaragePhoto.subsample(7, 10)

Gar = Button(App, image = GaragePhoto, command = Garage)
Gar.pack()
Gar.place(x=280, y=100)

lable3=Label(App,text=' Garage', foreground = 'Black', width=8) 
lable3.place(x=288,y=80) 

door = PhotoImage(file = "C:\\Users\\pc\\Desktop\\Project\\door.png")
door = door.subsample(5, 4) 

### Water Level ###
WaterPhoto = PhotoImage(file = "C:\\Users\\pc\\Desktop\\Project\\water.png")
WaterPhoto = WaterPhoto.subsample(3, 3) 

WAT = Button(App, image = WaterPhoto, command = WatLevel)
WAT.pack()
WAT.place(x=420, y=200)

lable4=Label(App,text='Water Level', foreground = 'blue', width=9)
lable4.place(x=422,y=180) 

Water_Sensor = PhotoImage(file = "C:\\Users\\pc\\Desktop\\Project\\waSen.png")
Water_Sensor = Water_Sensor.subsample(3, 3) 

### Living Room ###
LivingPhoto = PhotoImage(file = "C:\\Users\\pc\\Desktop\\Project\\download.png") 
LivingPhoto = LivingPhoto.subsample(4, 3) 

living=Button(App, image = LivingPhoto, command = LivingR)
living.pack()
living.place(x=350, y=320) 

lable5=Label(App,text='Living Room', foreground = 'green', width=10)
lable5.place(x=350,y=300)

music = PhotoImage(file = "C:\\Users\\pc\\Desktop\\Project\\music.png")
music = music.subsample(6, 5) 

Netflix = PhotoImage(file = "C:\\Users\\pc\\Desktop\\Project\\Netflix.png")
Netflix = Netflix.subsample(18, 12) 

# Update clock display time
def time_update():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, time_update)
    
# clock canvas
clock = Label(App, font=("times", 20, "italic"), bg="white")
clock.place(x=335, y=400)

time_update()
mainloop()