---
layout: post
date: 2021-08-28
title: Hardware-Accelerated Window capture (NVIDIA FBC) in OBS-Studio
Category: Software
Tags: obs-studio, nvidia, window-capture
---

For getting hardware-accelerated window capture on obs-studio, first we need to patch the nvidia-driver in using [https://github.com/keylase/nvidia-patch](https://github.com/keylase/nvidia-patch). Please note that before applying the patch, please ensure that your driver version is supported. The installed driver version can be seen by issuing `nvidia-smi` command.

Next, we need to install a obs-studio plugin for Nvidia FBC API. The source code for the plugin is available at [https://gitlab.com/fzwoch/obs-nvfbc](https://gitlab.com/fzwoch/obs-nvfbc). Download the source code and build it. The compiled `nvfbc.so` file is copied to `plugins/nvfbc/` folder.

In OBS-Studio, a new source will appear for NVIDIA FBC. Enjoy the hardware-accelerated window capture.
