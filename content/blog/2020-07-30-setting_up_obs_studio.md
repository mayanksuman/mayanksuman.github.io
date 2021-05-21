---
layout: post
title: Setting up droidcam and obs-studio cam in Debian
---

Currently, most of the population is working from home, so having a good video conferencing setup has become important. I have setup droidcam for getting video input from phone/ipad and obs-studio for managing different audio/video source in Debian using the following steps:

1. At first install `droidcam` in PC using software from [here](https://www.dev47apps.com/droidcam/linux/). `droidcam` should also be installed on phone/ipad using app store.
2. Install obs-studio by the command `sudo apt install obs-studio`.

For using the output of obs-studio into video-conferencing software, `obs-v4l2sink` should be installed and properly configured.

1. Install `v4l2loopback` kernel module by `sudo apt install v4l2loopback-dkms`
2. Install deb file for `obs-v4l2sink` downloaded from [their release page](https://github.com/CatxFish/obs-v4l2sink/releases).
3. Make a link for `obs-v4l2sink` plugin in right folder by `sudo ln -s /usr/lib/obs-plugins/v4l2sink.so /usr/lib/x86_64-linux-gnu/obs-plugins/v4l2sink.so`
4. Open `/etc/modprobe.d/droidcam.conf` and edit it so that content looks like
```conf
options v4l2loopback_dc width=1280 height=720 card_label="Droidcam"
options v4l2loopback width=1280 height=720 devices=1 video_nr=10 card_label="obs_studio_cam"  exclusive_caps=1
options snd-aloop enable=1,1 index=3,4
```
5. Add `v4l2loopback` to autoload modules by editing `/etc/modules-load.d/droidcam.conf`, so that its content is
```conf
videodev
v4l2loopback_dc
v4l2loopback
snd-aloop
```
6. Update initramfs by `sudo update-initramfs -u`.
7. Reboot the system and enjoy video output from obs-studio in your video conferencing session.

Update (20/04/2021): Camera functionality is now built into `obs-studio` 26.1+. Out of box, it works with almost all popular video conferencing systems. However, for `skype`, please limit the camera output resolution to 1280x720.

