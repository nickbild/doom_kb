# The Doomsday Button

![](https://raw.githubusercontent.com/nickbild/doom_kb/refs/heads/main/media/logo.jpg)

There is no quicker way to get your retro gaming fix than by pressing The Doomsday Button. One press of this big red button launches a game of *Doom* on a nearby vintage PC.

This project was inspired by John Park's [Doom keyboard](https://www.hackster.io/news/keyboard-warriors-060948232ef6), which launches a source port of *Doom* on a modern computer.

## How It Works

One of the large programmable buttons on an 8BitDo Retro Mechanical Keyboard was set to a specific combination of key presses. A [python script](https://github.com/nickbild/doom_kb/blob/main/doom_kb.py) listens for that combination, and when it is detected, a [Bash script](https://github.com/nickbild/doom_kb/blob/main/ftp.sh) FTPs a zero-byte file to an FTP server running on a vintage Windows 95 PC.

A QBasic program running on the vintage PC checks for the presence of that zero-byte file in a loop. When it is found, it launches *Doom*.

## Media

[Demo video on YouTube]()

A game of *Doom*, anyone?

![](https://raw.githubusercontent.com/nickbild/doom_kb/refs/heads/main/media/doom_intro_sm.png)

![](https://raw.githubusercontent.com/nickbild/doom_kb/refs/heads/main/media/doom_playing_sm.png)

QBasic in all it's glory:

![](https://raw.githubusercontent.com/nickbild/doom_kb/refs/heads/main/media/qbasic_sm.png)

The Win95 setup:

![](https://raw.githubusercontent.com/nickbild/doom_kb/refs/heads/main/media/win95_sm.png)

My Packard Bell PC:

![](https://raw.githubusercontent.com/nickbild/doom_kb/refs/heads/main/media/packard_bell.png)

## Bill of Materials

- 1 x Modern PC
- 1 x 8BitDo Retro Mechanical Keyboard
- 1 x Vintage PC (Packard Bell 5340 running Win95 used here)

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
