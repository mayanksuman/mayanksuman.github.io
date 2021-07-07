---
layout: post
title: Pass-through to VM on Linux Host
date: 2021-07-07
category: Virtual Machine
tag: windows_vm
---

Before enabling pass-through we need to enable IOMMU
([input–output memory management unit](https://en.wikipedia.org/wiki/Input–output_memory_management_unit))
by adding following kernel parameters in `/etc/default/grub`.

* For intel systems: `intel_iommu=on`
* For AMD system, IOMMU is by default enabled.

Additionally add `iommmu=pt` parameter to prevent linux kernel from touching
devices which cannot be passed through.
Update grub by `sudo update-grub` command and
reboot the system. After reboot, check that the device to be pass-throughed
(usually GPU) has separate IOMMU group by inspecting the output
of following shell script.

```
#!/bin/bash
shopt -s nullglob
for g in `find /sys/kernel/iommu_groups/* -maxdepth 0 -type d | sort -V`; do
    echo "IOMMU Group ${g##*/}:"
    for d in $g/devices/*; do
        echo -e "\t$(lspci -nns ${d##*/})"
    done;
done;
```

Sometimes, a number of sub-devices can be attached to a device in that case,
please ensure that all of sub-devices belong to same IOMMU group and all of
them should be pass-throughed together.

Sample output:
```
IOMMU Group 8:
	01:00.0 VGA compatible controller [0300]: NVIDIA Corporation TU116M [GeForce GTX 1660 Ti Mobile] [10de:2191] (rev a1)
	01:00.1 Audio device [0403]: NVIDIA Corporation TU116 High Definition Audio Controller [10de:1aeb] (rev a1)
	01:00.2 USB controller [0c03]: NVIDIA Corporation TU116 USB 3.1 Host Controller [10de:1aec] (rev a1)
	01:00.3 Serial bus controller [0c80]: NVIDIA Corporation TU116 USB Type-C UCSI Controller [10de:1aed] (rev a1)
IOMMU Group 9:
	02:00.0 Network controller [0280]: Intel Corporation Wi-Fi 6 AX200 [8086:2723] (rev 1a)
```

For enabling pass-through on the device, note its vendorID:productID and add
`vfio-pci` parameter to kernel parameters. For instance to forward
Network controller from the above example the parameter should be

```
vfio-pci.ids=8086:2723
```
If you want to pass-through IOMMU Group 8, then add following parameter
```
vfio-pci.ids=10de:2191,10de:1aeb,10de:1aec,10de:1aed
```

Then add `vfio-pci` module to initramfs by adding to
`/etc/initramfs-tools/modules` file. Regenerate the initramfs by
`sudo update-initramfs -u` command and regenerate the grub configuration by
`sudo update-grub`. Reboot the system.

After reboot, ensure that the concerned device have `vfio-pci` as active
module by `lspci -nnk -d vendorID:productID`. For instance, the correct output
for NVIDIA GPU card from IOMMU group 8 should be (output of `lspci -nnk -d 10de:2191`)

```
01:00.0 VGA compatible controller [0300]: NVIDIA Corporation TU116M [GeForce GTX 1660 Ti Mobile] [10de:2191] (rev a1)
	Subsystem: ASUSTeK Computer Inc. TU116M [GeForce GTX 1660 Ti Mobile] [1043:17ef]
	Kernel driver in use: vfio-pci
	Kernel modules: nvidia
```

Now, we are ready to pass this device to virtual machine (VM). Open properties
of VM in `virt-manager` and add 'PCI Host Device' hardware for the NVIDIA GPU
and its sub-devices. Turn on VM to enjoy NVIDIA GPU with it.

**Note**: The host linux system will not use any device with `vfio-pci` module.
To get the access to device, please remove the `vfio-pci` related kernel
parameter. You can keep IOMMU on as it has [added advantage](https://en.wikipedia.org/wiki/Input-output_memory_management_unit#Advantages).

