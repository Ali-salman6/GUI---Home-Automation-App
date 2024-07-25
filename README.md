# GUI - Home-Automation-App

<p align="center">
  <img src="https://github.com/user-attachments/assets/9a9c6be7-d42c-46ce-a206-8d96b1c3a9e1" width="600" height="600">
</p>

<p> This project is a home automation simulation application developed using Python and the Tkinter library. </p>
<p> The application simulates a GUI-based home automation system with functionalities for controlling various home appliances and systems.</p> 

## Features

- **Kitchen Control**: Toggle the switch for the kitchen.
- **Bed Room Control**: Set and manage alarms in the bedroom.
- **Garage Control**: Open and close the garage door.
- **Water Level Monitoring**: Monitor the water tank level with a progress bar.
- **Living Room Control**: Play and stop music, and open Netflix in the default web browser.
- **Camera Feed**: Open the live feed from the webcam.
- **Current Local Time**: Showing the user's local time at the App button.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/home-automation-app.git
    cd home-automation-app
    ```

2. Install the required libraries:
    ```sh
    pip install pillow opencv-python pygame
    ```

3. Make sure you have the following `files` in the same directory as the script:
    - `home.ico`
    - `mobile-in-hand.png`
    - `camera.png`
    - `theme.mp3`
    - `mixkit-classic-alarm-995.mp3`
    - `cooking.ico`
    - `Kitchentk.png`
    - `blub1.png`
    - `blub2.png`
    - `bed.ico`
    - `childrenbed.png`
    - `garg.ico`
    - `preview.png`
    - `water-storage.png`
    - `waSen.png`
    - `liv.ico`
    - `livingroom.png`
    - `Kitchen.png`
    - `bedroom.png`
    - `garage.png`
    - `door.png`
    - `water.png`
    - `download.png`
    - `music.png`
    - `Netflix.png`

## Usage

1. Run the main application script:
    ```sh
    python home_automation_app.py
    ```

2. The application window will open with various buttons representing different home systems. Click on the buttons to interact with the respective systems.

## Code Overview

```python
# Import the required libraries
from tkinter import *
from tkinter import ttk, messagebox
import datetime, time, pygame, cv2, webbrowser
from threading import Thread
from PIL import Image, ImageTk

# Create the main application window
App = Tk()
App.geometry("650x600")  # Set the dimensions of the App
App.title("Home Application Simulation")  # Set GUI's title
App.iconbitmap("C:\\Users\\pc\\Desktop\\Project\\home.ico")  # Set GUI's icon 

# Load and display the image for the application window GUI
mobile = Image.open("C:\\Users\\pc\\Desktop\\Project\\mobile-in-hand.png")
newsize = (600, 600)
Appm = mobile.resize(newsize)
Appm = ImageTk.PhotoImage(Appm)
App_Lab = Label(image=Appm)
App_Lab.image = Appm
App_Lab.place(x=0, y=0)

More code follows...
```


## Important Note

Make sure to adjust the paths to the images and other resources according to your project structure and file locations.





