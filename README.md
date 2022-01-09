# Dia mount scan

A utility script to facilitate batch scanning of [diapositives](https://en.wikipedia.org/wiki/Reversal_film) on flatbed scanners that provide loading frames to fix multiple slides on the glass plate at repeatable locations. Tested with the Epson GT-X980 ([Perfection V850 Pro](https://www.epson.be/products/scanners/consumer-scanners/perfection-v850-pro)).

Heavily uses [SANE drivers](http://sane-project.org/) and [scanimage](http://sane-project.org/man/scanimage.1.html).

# Usage


```
python3 batch_mount_scan.py DEVICE_NAME DESTINATION_FOLDER
```
```
python3 batch_mount_scan.py "epson2:libusb:003:015" /home/michael/Pictures/my_1982_holiday
```

Determining the device name of your scanner: `scanimage -L | grep -E "epson2:libusb:[0-9]{3}:[0-9]{3}"`

# Background

Initial web-searches [cast dark shadows](https://forums.linuxmint.com/viewtopic.php?t=335995) on the possibilities of doing dia digitization in Linux with an Epson Perfection V850 pro (one of the more available prosumer slide scanners on the Belgian market in dec. 2021). Therefore, upon acquiring the machine, I set off installing a Windows 10 VM on my Fedora machine through Gnome Boxes. This in itself went quite smooth for a first experience. The scanner comes with [SilverFast® SE Plus 8](https://www.silverfast.com/scanner-software/), a Windows & Mac scanning software. Reading in to Silverfast, I was somewhat disappointed in Epson providing software dating from 2011 with a 2021 acquired scanner, but proceeded installing it. After successfully fiddling with license registration procedures, I set off to test. The feature which seemed most useful to me, the automatic frame detection, made the program crash when trying to select frames for a second round of scanning. On top of that, the auto colour-correcting features don't seem available in batch-mode in SF 8 plus. As I understand it, you need the "[jobmanager](https://www.silverfast.com/highlights/jobman/en.html)" in SilverFast AI for that. Considering the aforementioned shortcomings and the general inconveniences of working with VM's, I decided to look for alternatives.  
I knew about SANE drivers, but the XSANE frontend is quite outdated, which makes it not out-of-the box compatible with a modern Linux distro. Being preconceived about the fact that I'd need a GUI tool for scanning, made that I discovered "scanimage" CLI tool only later in the process. Silverfast's auto-frame selection not being perfect (the crashing aside), meant that I'd have to use additional post-editing software for cropping anyway. [Darktable](https://www.darktable.org/), another great piece of open source software works great for that.



