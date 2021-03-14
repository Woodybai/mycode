import os
import time
for root, dirs, files in os.walk(".", topdown=False):
      print(root)
      time.sleep(1)
       
