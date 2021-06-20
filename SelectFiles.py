import sqlite3
conn = sqlite3.connect('commands.db')
sl = "commands"
count = 0
c = conn.cursor()
sql = """SELECT id, title FROM commands ORDER BY title"""
#sql = """SELECT id, title FROM commands"""
c.execute(sql)
result = c.fetchall();
for x in result:
    count +=1
    n = x[0]
    t = x[1]
    print(n, t[0:22])

conn.close()
print("")
print(count)
"""
# it created the database file if it doesn't exits'
conn = sqlite3.connect('comxxxmnands.db')


#c.execute('DROP TABLE temp1' ) 
"""
