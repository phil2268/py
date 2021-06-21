from _importVars import l
fm = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
cn = {
  "brand": "Chevrolet",
  "model": "Nova",
  "year": 1971
}
mz = {
  "brand": "Mazda",
  "model": "RX7",
  "year": 1979
}
ty = {
  "brand": "Toyota",
  "model": "Carolla",
  "year": 1977
}
x = 0
while x < 4:
    x += 1
    l()
    if x == 1:
        print(fm)
        print(fm["brand"])
        print(fm["model"])
        print(fm["year"])
    elif x == 2:
        print(cn)
        print(cn["brand"])
        print(cn["model"])
        print(cn["year"])
    elif x == 3:
        print(mz)
        print(mz["brand"])
        print(mz["model"])
        print(mz["year"])
    elif x == 4:
        print(ty)
        print(ty["brand"])
        print(ty["model"])
        print(ty["year"])
        
l()
x = fm.items()
print(x)
print(fm)
l()
# outputs keys
for y in fm:
    print(y)
    
# convert library to list
print(fm.items)
l()
x = list(fm.items())
print(x)
# loop through items
l()
for y in x:
    print(y)
