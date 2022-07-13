---
layout: post
title: Enable battery level reporting for bluetooth devices on linux
date: 2022-07-10
category: Software
tag: filesystem
---

This is an experimental feature of BlueZ bluetooth stack. To enable the feature edit `bluetooth.service` and put the `ExecStart` to be `/usr/libexec/bluetooth/bluetoothd --experimental`.

The file `bluetooth.service` is present in `/lib/systemd/system/` on debian. Otherwise, the file can be edited by issuing command `sudo systemctl edit bluetooth.service`.

After this change restart the bluetooth service by `sudo systemctl daemon-reload && sudo systemctl restart bluetooth`. The power status for the device connected via bluetooth should be now visible in power pane of GNOME Settings application.
