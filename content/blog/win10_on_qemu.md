---
layout: post
title: Windows 10 guest on QEMU
date: 22-01-2021
category: Virtual Machine
tag: win10, qemu
---

I use Linux (Debian) as my daily driver. However, for some softwares only available on the Windows platform, I use `Windows 10 VM` in `QEMU` (managed using `virt-manager`). There is a myth about the `Windows 10` guest under `QEMU` that they are slow compared to other virtualization techniques/softwares (VirtualBox, VMWare, and others). Surely, the default values in `virt-manager` do not result in the most performant Windows virtual machine out of box. Still, with the following tips one can get a very performant virtual machine setup (with low computational load additionally):

1. Please ensure that the disk file to be created for the virtual machine is not on a `BTRFS` partition. Furthermore, at the last step of new virtual machine wizard in `virt-manager`, click **Customize configuration before install**.
	![Create VM Wizard]({static}../images/new_vm_last_step.png)
2. In the next dialog box, change the disk bus of `SATA Disk 1` and device model of Network Interface Card (`NIC`) to `VirtIO`. `Windows` do not have `VirtIO` drivers, so attach a new `SATA CDROM` with the latest `VirtIO` iso file downloaded from [virtio-archive](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/). At this stage, please ensure video setting is QXL. After doing all these setting, start the installation. During installation, `Windows` will notify about missing disk, which can be troubleshot by navigating to the appropriate disk driver file in `viostor` folder in the `VirtIO` driver iso.
	![VirtIO Option Selection]({static}../images/virtio_selection.png)
	![New CDROM drive]({static}../images/new_cdrom.png)
3. After installation, install additional drivers from `VirtIO` driver disk. Additionally, install other [`SPICE` drivers](https://www.spice-space.org/download.html), specially `spice-guest-tools` and `Spice WEBDAV Daemon`.
4. Debloat it with [Windows 10 Debloater](https://github.com/Sycnex/Windows10Debloater) and enhance your privacy with [O&O ShutUp10](https://www.oo-software.com/en/shutup10). Please ensure that before running `Windows10Debloater`, execution policy in `Powershell` (Administrator) is unrestrictive (`Set-ExecutionPolicy Unrestricted`). Don't forget to change the execution policy afterward (`Set-ExecutionPolicy restricted`).
5. Additional Tip: For sharing files from Linux host, you have two options a) by USB redirection of attached pen drive b) by WebDAV. For using WebDAV, `Spice WebDAV Daemon` should be installed in Windows guest. Add a new channel hardware with target name `org.spice-space.webdav.0`. Start the Windows guest and connect it with `remote-viewer` (`remote-viewer spice://127.0.0.1:5900`) and then use `File > Preferences` to select the folder to be shared. If this does not work, ensure that on the host machine (Linux), the user is a member of `libvirt` or other appropriate groups (`sudo usermod -a -G libvirt $USER`; you may need to restart linux host), and on the guest virtual machine (Windows), `Spice WebDAV` service is running.
