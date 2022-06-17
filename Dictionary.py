dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict1["brand"])

dict1.setdefault("Km",50000)
dict1.pop("brand")
print(dict1)

for  key,value in dict1.items():
  print(key,":",value)