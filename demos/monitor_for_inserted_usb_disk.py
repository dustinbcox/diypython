#!/usr/bin/env python2.7

"""This was part of https://www.meetup.com/Central-Florida-RPi-Users-Group/events/234221747/
Go headless with Nate Jennings, play with Python with Dustin Cox!

Using python2.7 we (poll) monitor for new USB disks on a Raspberry Pi and add a 1,000 empty files called "THIS_IS_A_VIRUS_xxxx"
to simulate a security attack where someone can insert a disk and write malware to the USB within a few seconds. These are 
just empty files, however.

Some of the basics of Linux were covered: serial terminals, daemons, forking, screen, tmux, ascii art (aalib, bb, caca-utils,
toilet/figlet), Python 2.7 vs 3.x, bpython.

This script ran on a Raspberry Pi which had an automounter and was tested with two different FAT formatted USB disks."""

import subprocess
import time
import os.path

def lsblk():
    return subprocess.check_output(['lsblk'])

def deliver_exploit(path):
    for i in range(1000):
        subprocess.call(['touch', os.path.join(path, 'THIS_IS_A_VIRUS_{0}'.format(i))])

def get_mount_point(output):
    """Get the mount point from subprocess return list of mount points"""
    mount_points = []
    for index, line in enumerate(output.splitlines()):
        if index != 0:
            mount_point = line[41:] # this is a hack
            if len(mount_point) > 0 and '/media' in mount_point and 'mmcblk' not in line:
                mount_points.append(mount_point)
    return mount_points

if __name__ == "__main__":
    print "Let's see when a disk is inserted"

    output = lsblk()
    while True:
        new_output = lsblk()

        if output != new_output:
            new_disk = False
            mounts = get_mount_point(new_output)
            for mount in mounts:
                print "Mounted on ", mount
                new_disk = True
                deliver_exploit(mount)
                print "Sploiting!!!!"
                print subprocess.check_output(['ls', mount])
                if new_disk:
                    print subprocess.check_output(['toilet', 'NEW DISK!!!'])
            output = new_output
        else:
            output = new_output

        time.sleep(.5)
