#!/usr/bin/env python

from subprocess import call

with open("signal", "w") as file:
   file.write("\1")

