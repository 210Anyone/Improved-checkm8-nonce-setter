#!/usr/local/bin/python

import os
import commands
from termcolour import colored

pwd = os.getcwd()

output = commands.getoutput(pwd + "/lsusb")


shsh = input("Enter the SHSH.");

while len(shsh) <> 16:
        shsh = input("Enter the SHSH.");


while "DFU MODE" not in output:
    if "Recovery Mode" in output:
        print("Device in Recovery Mode found!\n")
        print("Please connect device in DFU Mode")


print("Device in DFU Mode detected, continuing...")
