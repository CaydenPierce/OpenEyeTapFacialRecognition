#Follow these guidelines to disable the screensaver in PIXEL

Install:
```
 sudo apt-get install x11-xserver-utils
```
Open config:
```
nano ~/.xinitrc
```

Paste in:
```
xset s off         # don't activate screensaver
xset -dpms         # disable DPMS (Energy Star) features.
xset s noblank     # don't blank the video device

exec /etc/alternatives/x-session-manager      # start lxde
```
Save

Screensaver is now disable!
