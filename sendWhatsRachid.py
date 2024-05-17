
import pywhatkit as whatsapp

whatsapp.sendwhatmsg("+33622068899","Hi python.hub",22,1)
# Same as above but Closes the Tab in 2 Seconds after Sending the Message
whatsapp.sendwhatmsg("+33622068899", "Hi", 22,3, 2, True, 2)

# Send an Image to a Group with the Caption as Hello
whatsapp.sendwhats_image("AB1", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
whatsapp.sendwhats_image("+33622068899", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
whatsapp.sendwhatmsg_to_group("AB1", "Hey All!", 22, 3)

# Play a Video on YouTube
whatsapp.playonyt("PyWhatKit")