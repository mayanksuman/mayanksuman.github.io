---
layout: post
title: Setting up Skype for web in Debian
---

I do not prefer having closed source software on my Debian machine.
However, due to the popularity of Skype, the package `skypeforlinux` was installed on my Debian system.
Finally, I am able to get rid of the binary blob by using the web version of the service.
If you also want to get rid of the binary software and still want to have the convenience offered by it, the steps are listed below:

1. Get rid of `skypeforlinux` package by `sudo apt purge skypeforlinux` command.
2. Make a text file named `skype_web.desktop` in `~/.local/share/applications` with following content.
```conf
[Desktop Entry]
Name=Skype Web
Comment=Skype Web application in a Chrome profile
Exec=sh -c "mkdir -p $HOME/.local/share/skypeweb && GDK_BACKEND=x11 chromium --kiosk --user-data-dir=$HOME/.local/share/skypeweb https://web.skype.com 1>/dev/null 2>/dev/null &"
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Network;Application;
```
3. In the activities panel of gnome-shell, select `Skype Web` to start it.
4. Login with your credentials and select to remain logged in.

Enjoy Skype from the web interface.
Further, it also frees me from worry that skype might be running in the background.
If chromium is closed, the skype is no longer running.
