import os,pygame,random
pygame.mixer.init()
music=[]
for a,b,c in os.walk("c://"):
    for file in c:
        if file.endswith(".mp3"):
            try:
                        file1=os.path.join(a,file)
                        file2=os.path.abspath(file1)
                        file3=r"%s"%file2
                        pygame.mixer.music.load(random.choice(file3))
                        pygame.mixer.music.play()
    
                        music.append(file3)
            except:
                        print("no")

"""print(music)

pygame.mixer.music.load(random.choice(music))
pygame.mixer.music.play()"""
    
                        
