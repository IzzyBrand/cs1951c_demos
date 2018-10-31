## Background

The Raspberry Pi is a little computer. Unlike the arduino, which can only run a single program, the Raspberry Pi can run numerous programs at the same time, and supports other regular computer stuff like web browsing, file storage, cameras, etc.

The "hard drive" for this computer is a microSD card. Everything you put on the Raspberry Pi gets saved on the microSD. This means you can take your microSD out of one PI and put it in another, and everything will still work.

## Setting up the Pi

We need to put an operating system image on the microSD card before we can use the Pi. This is well documented on [the raspberrypi.org page.](https://www.raspberrypi.org/documentation/installation/installing-images/)

Once you've followed this tutorial, insert the microSD card into the PI. You can power the Pi via a microUSB cable.

## First boot!

(This assumes you have a screen/keyboard/mouse connected).
Connect to a wifi network using the menu in the top right corner.

Open up a terminal. You can press ctrl+alt+t to do this. Enter the following commands

```
sudo apt update
sudo apt upgrade
sudo pip install pip --upgrade
```

These will take a moment. You should enter `Y` when prompted.

Now run `sudo raspi-config` and do the following things

 * change your password under `Change User Password`
 * change your device name under `Network Options > Hostname`
 * enable ssh under `Interfacing Options > SSH > yes`
 * reboot your pi

You can also reboot from the commandline with `sudo reboot`.
Log back into your pi with the new password.
