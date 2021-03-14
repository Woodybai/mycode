import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
#sql = """
"""DROP TABLE IF EXISTS users;
CREATE TABLE users (
           id integer unique primary key autoincrement,
           name text
);
"""
#c.execute("INSERT INTO USERS values(?,?)",(33,"xioazhuang"))
for x in range(100):
    c.executemany("insert into users(name) values(?)",['a','b','c'])
c.execute("select * from users")
conn.commit()
print (c.lastrowid)
for  x in c.fetchall():
    print(x)
conn.close()
