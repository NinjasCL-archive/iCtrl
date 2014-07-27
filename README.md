# iCtrl
Creates a Web Server that sends key commands for controlling presentations with any device capable of web browsing.

In order to be able to control your presentations with you iPhone, Android or similar device, the presentation server and the device must be in the same network. And the presentation must be the current active window in the presentation server.

# License
By Camilo Castro <camilo@cervezapps.cl>

26/07/2014

Version 1.0

From Chile with love

Project Under the MIT License, see LICENSE file


# Installation
In order to properly use this application you need to install python 2.7.x

## Windows
Install [Active Python](http://www.activestate.com/activepython) it haves all the components (*win32api, win32com*) that the server needs.

## Linux
You probably already have Python installed, but the server relies on [xdotool](http://www.semicomplete.com/projects/xdotool/) for sending commands. Please check if you got it in your machine.

## Mac
Already have all the components installed. (tested on Mac OSX Mavericks)

# Usage
First you need to have at least 2 files, *keys.html* and *server-** (depends on your operating system).

Second, you must open the server file inside a terminal with *python server-<os>.py*, for example:


```

python server-mac.py


```

> Probably double clicking the file should work as well, but I prefer the command line way.

When the server shows *"Serving at localhost:8080"*, you need to check what is the ip address for the machine that host the presentation.

Linux and Mac can use *ifconfig* (in terminal), Windows need to use *ipconfig* (in cmd).

You will get something like


```

192.168.0.114

```

Finally open the web browser in your Android, iPhone or similar device and go to 192.168.0.xxx:8080.

Check that your presentation server have the presentation as the active window, so the server can control the presentation.

# Available Keys
The server can send the following keystrokes

* Up
* Down
* Left
* Right
* Space

But you can easily add more if you need them :)

# Testing
You can test the server with the awesome *reveal.js* presentation framework, check it out at http://lab.hakim.se/reveal-js