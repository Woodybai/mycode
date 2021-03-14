import sqlite3,os,pandas as pd
conn=sqlite3.connect("sales.db")
cc=conn.cursor()
cc.execute("create table bai(id primary key,filename text,folder text)")
#conn.commit()
for a,b,c in os.walk("c://"):
    for file in c:
            if file.endswith(".jpg"):
                            file1=os.path.join(a,file)
                            file2=file1.split(".")[-2]
                            cc.execute("insert into bai (filename,folder)values(?,?)",(file2,file1))

conn.commit()
