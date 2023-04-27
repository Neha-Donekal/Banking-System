import pymysql

con = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='Neha_41s',
    db='new_schema',
    charset='utf8'
)

cur = con.cursor()
sql2 = 'insert into stu values(4,"Jerry", 12, 8);'
cur.execute(sql2)
con.commit()

sql1 = 'select * from stu'
cur.execute(sql1)
data = cur.fetchall()
cur.close()
con.close()

for i in data:
    print(str(i))