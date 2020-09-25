"""
Midi Color Piano
Author: Dan Wallace
Website: www.brick.technology
Email: danwallaceasu@gmail.com
Vist settings.py to change reaction types or colors
<< Last Update: 9/25/2020 >>
"""

import re
import pygame.midi
from pygame.locals import *
from settings import *
from functions import *

## Set up pygame
pygame.init()
pygame.fastevent.init()
pygame.midi.init()
pygame.midi.get_init()
event_get = pygame.fastevent.get

print("Press any key on your midi controller to change the window color!")

## open a specific midi device
userInput = pygame.midi.Input(1)

## Set screen size and window title
screen = pygame.display.set_mode((myWidth, myHeight), RESIZABLE, 100)
pygame.display.set_caption(myTitle)

## Set running to true and start the main loop
running = True
while running:
    
    ## Sets running to false on window closeand ends the loop/program
    events = event_get()
    for event in events:
        if event.type in [QUIT]:
            running = False
        if event.type in [KEYDOWN]:
            running = False
            
    ## Checks for incoming midi data and executes if true
    if userInput.poll():
                          
        ## Read the raw input from midi device:
        raw = userInput.read(16)

        ## Parse raw midi data into usable information:
        OnOff = raw[0][0][0]                                            # Returns the value 144 (key press) or 128 (key release)
        midiNumber = raw[0][0][1]                                       # Returns a number representative of the key you pressed
        note = pygame.midi.midi_to_ansi_note(midiNumber)                # Takes midNumber and converts it to a note/octive value (ex: F#2, A-1, B0 etc)
        noteSplit = re.split("[0-9]\Z|[-]", note)                       # Splits "note" and creates a list containing the note name and octave value
        justNote = noteSplit[0]                                         # Returns the first value created by noteSplit. [0] = note name, [1] = octave number
        noteColor = color[justNote]                                     # Matches "justNote" to the dict "color" and grabs the correct RGB color value

        ## Key press/release events:
        if OnOff == 144:                                                # Checks to see if the key is currently pressed down
            printData(OnOff, justNote, raw)
            screen.fill(noteColor)                                      # Changes screen color to the new color from color dict
            pygame.display.update()                                     # Updates the display 

        else:                                                           # Checks to see if there is no input, or key if key released
            printData(OnOff, justNote, raw)
            
            if userSetting == "both":                                   # If userSetting is set to both, the screen is set to black when the key is not pressed
                screen.fill([0, 0, 0])                                  # Changes the screen to black  
                pygame.display.update()   
                
            else:                                                       # If userSetting is set to "press", the screen will not change on key release 
                pass

## End midi/exit program
userInput.close()
pygame.midi.quit()
pygame.quit()
exit()

## <(^_^<)end(>^_^)>
