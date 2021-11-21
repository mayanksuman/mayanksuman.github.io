---
layout: post
title: Create Encrypted Volume inside File
date: 2021-11-21
category: Software
tag: filesystem
---

Prerequisite: The system should have `cryptsetup` installed. On debian this can be
achieved by `sudo apt install cryptsetup`.

At first creat the file that will act as encrypted drive/volume. Please ensure that 
the file should be >=100MB in size. The file will then be formatted with 
`cryptsetup`. This step will demand either a passphrase or key file (following 
example commands are for passphrase case).
```bash
fallocate -l 100M encrypted_volume.enc
sudo cryptsetup -y luksFormat encrypted_volume.enc
```
In case, if you want to use key file, you can generate a key-file with random bits 
using `head -c 4kB /dev/urandom > key_file_path;sync` or 
`dd if=/dev/urandom of=key_file_path bs=1000 count=4;sync`. 
Next while doing `luksFormat` with `cryptsetup` command, 
add `--key-file key_file_path` in the command. For security, save the key file at a
safe location with proper permission (for example `chmod 400 key_file_path`), because 
losing or modifying key-file will mean loss of data in encrypted volume.

It should be noted additional passphrase or key-files can be added to
`encrypted_volume.enc` with `cryptsetup luksAddKey` command. 

Now, open the volume inside file with cryptsetup and format it with `ext4` partition. 
```bash
sudo cryptsetup luksOpen encrypted_volume.enc encrypted_vol 
sudo mkfs -t ext4 /dev/mapper/encrypted_vol
```
You can go with other filesystem or even with `lvm2`. The volume can be mounted in any
folder by using `mount` command.
```bash
sudo mount -t ext4 /dev/mapper/encrypted_vol target_folder
```

After accessing the data in the volume, the volume should be unmounted and the mapping
should be closed
```bash
sudo umount /dev/mapper/encrypted_vol
sudo cryptsetup luksClose encrypted_vol 
```

## Additional Tips
1. To get information about existing encrypted device, use the command 
`cryptsetup luksDump device_path`.
2. If you do not want to enter passphrase everytime you open an encrypted drive, add a
key-file to it using `cryptsetup luksAddKey` command, get the UUID for the encrypted 
device by `sudo blkid` (or `cryptsetup luksDump` or `cryptsetup luksUUID`), and then 
put following line in `/etc/crypttab`:
```bash
device_mapper_name UUID=encrypted_drive_UUID   key_file_path    luks
```
3. For added safety, you can backup LUKS Header of encrypted drive. Backed up LUKS Header
can come handy in cases when header in actual encrypted drive is corrupted or missing. 
For backing and restoring header, following commands are used.
```bash
cryptsetup luksHeaderBackup <device> --header-backup-file <file>
cryptsetup luksHeaderRestore <device> --header-backup-file <file>
```
4. After taking backup of LUKS Header, all pass-phrases and key-files can be removed from 
encrypted device by `cryptsetup luksErase`. However, this operation will render the device 
unusable, so it is highly recommended that a backup of header is taken before. Such a 
device can then be opened using `cryptsetup luksOpen --header=header_file_path` command.
5. For an encrypted device, the command `cryptsetup -v isLuks <device_path>` give 
`command successful` message (hence, it reveals that device is encrypted with LUKS). If 
you want to avoid detection, take a backup of header and then run 
`wipefs -a <device_path>` to remove all information about filesystem in encrypted 
device. After this step, the encrypted drive can only be opened using 
`cryptsetup luksOpen --header=header_file_path` command.
