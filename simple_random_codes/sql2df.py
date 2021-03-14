import pygame as p
import os
import sqlite3
import pandas as pd
import tkinter as tk
con=sqlite3.connect("sound.db")
c=con.cursor()
ss="select * from songs3"
df1=pd.read_sql(ss,con)
print(df1)
