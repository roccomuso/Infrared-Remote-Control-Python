# Infrared-Remote-Control-Python
Project to control the VLC Player through a standard IR remote controller and Arduino

Developed in Python 3.2

To make the project work all you need is:
- VLC Player installed
- The USB Arduino Driver installed
- Arduino board
- IR Receiver

Then make sure to have the Telnet interface activated in VLC.

Entering in the VLC telnet server through PUTTY or any other telnet client allows you to launch the 'help' command and have the list of standard commands for the VLC player.

You can now start the python script that will ask you to prompt the local ip address of the computer running VLC.

Obviously, don't forget to upload the .pde sketch to your arduino board and make the right circuits connections: With the serial monitor of arduino you'll get all the IR code of your remote controller. Then you should map the IR serial codes in the python script.


Here's the link to the italian docs explaining circuit connection in details:

- http://www.hackerstribe.com/2013/vlc-hacking-infrared-remote-py-control-2-0/

Feel free to contribute.
