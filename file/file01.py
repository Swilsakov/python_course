file = open('directories.txt', 'w')
file.write('''bin@    dev/   lib@    libx32@      mnt/   root/  snap/     sys/  var/
boot/   etc/   lib32@  lost+found/  opt/   run/   srv/      tmp/
cdrom/  home/  lib64@  media/       proc/  sbin@  swapfile  usr/''')

print(file)