<a href="url"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160643.jpg" align="left" height="100" width="100" ></a>
<a href="url"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160713.jpg" align="left" height="100" width="100" ></a>
<a href="url"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160719.jpg" align="left" height="100" width="100" ></a>
<a href="url"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160725.jpg" align="left" height="100" width="100" ></a>


------------
# What is this?
Its a python app that is used to controll industrial Radwag scale. It use tkinter gui to display mass obtained by serial communication with scale. User is obligated to use controller connected to usb port to "SEND" result to server, "TARE" the scale and "WITHDRAW" the result from server. 

##  Why You need this?
If You want to send results from your scale directly to MySQL database its now possible. 

## Modules used
- pySerial
- Requests
- time

## How to use?
1. Connect scale to USB port wia R232 --> usb dongle... or DIY one
2. Check if Arduino IDE sees your scale. Try to write "normal" communicates to it first. You need to learn how to speak to your Scale. 
3. Adapt my code. 

### Related
[Remote controller for this scale](https://github.com/MarcinanBarbarzynca/Pilot-do-komputera-Arduino-NANO "Remote controller for this scale")
[How to read serial from scale](https://github.com/MarcinanBarbarzynca/Read-two-Arduino-serial-with-PYSerial "How to read serial from scale")
[Scale emulator](https://github.com/MarcinanBarbarzynca/Emulator-wagi-radwag-arduino "Scale emulator")

#### Contact to me :)
Write 10 mails to p_ir@o2.pl


# BUGS! and how to deal with them
- It works slow. 
- Its crashing when it cannot open serial port
- It need some clearence. 
