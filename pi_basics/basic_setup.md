## First time powering on your pi!

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

