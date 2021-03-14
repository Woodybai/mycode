import os
for root,subdir,files in os.walk("c://"):
    for file in files:
        if ".txt" in file:
            print(file)
