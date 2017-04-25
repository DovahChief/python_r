import pymysql as db

con =  db.connect(host = 'localhost', user= 'accusr',
password = 'accusr', db = 'red_social')

a = con.cursor()

sql = "select user_first, user_email, user_nickname from users"


#a.execute(sql2)

count =a.execute(sql)

dat  = a.fetchall()


print("-------------------------------------------")

for e in dat: #vamos a sacar los elementos e imprimir correos
    print(e[0],"\t->\t", e[2],"\t->\t" ,e[1])
    print("-------------------------------------------")

print("fin")
