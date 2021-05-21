---
layout: post
title: Access data in lvm2 drive
date: 10-01-2021
category: Software
tag: filesystem
---

Prerequisite: The system should have `lvm2` installed. On debian this can be
achieved by `sudo apt install lvm2`.

For mounting a `lvm2` drive, we need to activate the associated LVM group. The following command can list all available LVM group:
```bash
sudo vgscan
```
Scanning will show the name of different LVM volumes. More details about any of
LVM volume can be obtained by `vgs` or `vgdisplay` commands.
A particular LVM volume can be activated by `vgchange` command. Successful
activating of LVM volume with make device files in `/dev` for each drive in
the volume.
```bash
sudo vgchange -ay <lvm_volume_name>
```
The required drive can be mounted in any folder by using `mount` command.
```bash
sudo mount /dev/<lvm_volume_name>/<lvm_drive_name> target_folder
```

After accessing the required file, the drive can be unmounted by
`sudo umount target_folder`. The LVM group is deactivated with
following command:
```bash
sudo vgchange -an
```
LVM group should always be deactivated before removing the concerned removable drive.
