---
layout: post
title: Access files in qcow2 drive
---

The qcow2 (or QEMU copy-on-write) is a virtual disk image format primarly used by QEMU for guest systems. In many circustances, such as reseting passwords, editting or recovering files etc., mouting a qcow2 disk images without running a guest system is required. This can be acheived by `Network Block Device` module (or `nbd`) on host linux system. At first, we need to define maximum number of partitions expected for the qcow2 disk and then the disk can be mouted with following commands:

```
modprobe nbd max_part=8   # maximum partition = 8
qemu-nbd --connect=/dev/nbd0 /var/lib/vz/images/100/vm-100-disk-1.qcow2
fdisk /dev/nbd0 -l	# For finding virtual machine partitions
mount /dev/nbd0p1 /mnt/somepoint/    #mount partition on /mnt/somepoint
```

The disk image can be unmounted with following commands:

```
umount /mnt/somepoint/
qemu-nbd --disconnect /dev/nbd0
rmmod nbd
```

Depending upon system configuration, you may need to run either one or all commands as root user.
