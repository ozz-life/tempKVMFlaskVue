#!/usr/bin/env bash

# Это просто старый скрипт, который хочу видеть в этой папке, под рукой

New_Volume_Label="B9KNRPMF"
Path="/dev/sdk"

parted ${Path} --script mklabel gpt
parted ${Path} --script mkpart ${New_Volume_Label} ext4 0% 100%

mkfs.ext4 -L ${New_Volume_Label} -i 67108864 -I 128 -b 4096 -m 0 ${Path}1

#mkfs.ext4 \
#       -t ext4 \ # -t fs-type
#-L ${New_Volume_Label} \ # -L new-volume-label
#-i 1073741824          \ # -i bytes-per-inode
#-I 256                 \ # -I inode-size
#-b 4096                \ # -b block-size
#-m 0                   \ # -m reserved-blocks-percentage
#${Path}1
tune2fs -o journal_data_writeback ${Path}1
fsck ${Path}1

echo "LABEL=${New_Volume_Label}          /mnt/${New_Volume_Label}       ext4            defaults,noatime,data=writeback,barrier=0,nobh,errors=remount-ro        0 0" | tee -a /etc/fstab
mkdir /mnt/${New_Volume_Label}
mount -a
rmdir /mnt/${New_Volume_Label}/lost+found
