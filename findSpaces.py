import sqlite3
conn = sqlite3.connect('temp.db')
c = conn.cursor()
f = open("readFile.txt", "r")

rl = f.readline()
len1 = len(rl)
x = rl.find(" ")
l1 = rl[0:x]
fline1 = l1
x+=1
line1 = l1
l2 = rl[x:len1]
fline2 = l2

rl = f.readline()
len1 = len(rl)
x = rl.find(" ")
l1 = rl[0:x]
fline3 = l1
x+=1
line2 = l1
l2 = rl[x:len1]
fline4 = l2

rl = f.readline()
len1 = len(rl)
x = rl.find(" ")
l1 = rl[0:x]
fline5 = l1
x+=1
line2 = l1
l2 = rl[x:len1]
fline6 = l2

rl = f.readline()
len1 = len(rl)
x = rl.find(" ")
l1 = rl[0:x]
fline7 = l1
x+=1
line2 = l1
l2 = rl[x:len1]
fline8 = l2

rl = f.readline()
len1 = len(rl)
x = rl.find(" ")
l1 = rl[0:x]
fline9 = l1
x+=1
line2 = l1
l2 = rl[x:len1]
fline10 = l2

data = "CREATE TABLE sample (" + fline1 + " " + fline2 + "," + fline3 + " " + fline4 + "," + fline5 + " " + fline6 + "," + fline7 + " " +fline8 + "," + fline9 + " " + fline10 + ")"



final = """sql =" """ + data + """ " """
print(final)

#c.execute(final)

h = open("sql.txt", "w")
g = open("saveFile.txt", "w")
# saves final file
h.write(final)


# save file to database
import sqlite3
conn = sqlite3.connect('findSpaces.db')
c = conn.cursor()
# title
# fileContents


insertStatement =  "INSERT INTO findSpaces VALUES (title, contents) VALUES (?, ?) ('sample', final)"

print(insertStatement)

c.execute(insertStatement)
c.close()

g.write(data)
j = open("saveFile.txt", "r")
rl = j.readlines()
print("------------")
#730am
print(f.readlines())
print(j.readlines())
g.close()
quit()


#------------------------------'
#c.execute("""CREATE TABLE ) """)print("")
print(l1)
print(l2)
ln = len(txt)
l2 = f.readline()
print(l1+l2)
quit()

string = "full name"
txt = "firstName TEXT"
ln = len(txt)
#print(ln)
x = txt.find(" ")
add = x + 1
n1 = txt[0:x]
n2 = txt[add:ln]
print(n1, "-->first find")
print(n2, "-->second find")






quit()
# Python3 code to demonstrate working of
# Check for spaces in string
# Using regex
import re
  
# initializing string 
test_str = "Geeks  forGeeks"
  
# printing original string 
print("The original string is : " + test_str)
  
# Using regex
# Check for spaces 
res = bool(re.search(r"\s", test_str))
  
# printing result 
print("Does string contain spaces ? " + str(res))
