import time
from subprocess import call

while True:
   with open("signal", "r+") as file:
      contents = file.read(1)
      if contents == '\1':
         call(["killall", "mpg123"])
         file.seek(0)
         file.write("\0")

   time.sleep(.5)
