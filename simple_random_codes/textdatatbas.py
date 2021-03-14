import os,sqlite3
import pandas as pd
a=pd.read_excel(r"c://Users\sherwood\AppData\Local\Programs\Python\Python38-32\output.xlsx")
b=a.columns[2]
print(a)
conn=sqlite3.connect("learn.db")
c=conn.cursor()
c.execute("CREATE TABLE (id integer primary key,%s text, physics text,chemistry text,algebra text)"%b

c.execute("select * from sqlite_master where type='table'")
print(c.fetchall())
 
c.execute("select physics from daisy")
print(c.fetchall())
