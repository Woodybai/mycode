import pygame as p
import os
import sqlite3
import pandas as pd
import tkinter as tk
root=tk.Tk()
m=[]
x=0
play=True
def conn():
    conn=sqlite3.connect("sound.db")
    return conn
def createtable(conn):
    cursor=conn.cursor()
    #cursor=conn.cursor()
    cursor.execute("CREATE TABLE songs3(id integer primary key,songname text,songpath text)")
    conn.commit()
def ins(conn):
    cursor=conn.cursor() 
    for a,b,c in os.walk("d://"):
        for file in c:
            if file.endswith(".mp3"):
                file2=file.strip(".")
                file3=file2[0]
                file1=os.path.join(a,file)
                cursor.execute("INSERT INTO songs3(songname,songpath)values(?,?)",(file3,file1))
    conn.commit()
def sech(conn):
    global m
    #p.init()
     
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM songs3")
    rows=cursor.fetchall()
    for row in rows:
        m.append(row[2])
        print(m)
"""     
def music():
    p.init()
    p.mixer.init()
    p.mixer.music.load(m[x])
    p.mixer.music.play(0)
    que()

def que():
    global x, m
    pos = p.mixer.music.get_pos()
    if int(pos) == -1:
        x += 1
        p.mixer.music.load(m[x])
        p.mixer.music.play(0)

    root.after(1, que)           
         
       
"""
conn=conn()
createtable(conn)
ins(conn)
sech(conn)
#music()
#root.mainloop()
