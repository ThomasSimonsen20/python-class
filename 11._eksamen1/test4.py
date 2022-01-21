
def myFunction(**kwargs):
    return ("Firstname: " + kwargs["fname"] + " Lastname: " + kwargs["lname"])

#print(myFunction(fname = "Thomas", lname = "Simonsen"))

#Tuple
tupleFruits = ("apple", "banana", "orange", "lime")

#print(tupleFruits)
#print(len(tupleFruits))
#print(type(tupleFruits))

#Set
setFruits = {"apple", "banana", "orange", "lime"}

#setFruits.add(25)
#setFruits.remove("apple")
#print(setFruits)

#Dictionary
myDict = {"fname": "Thomas", "lname": "Simonsen"}

myDict.update({"fname": "Mikkel"})
myDict["Age"] = 25
myDict.keys()
myDict.values()

#List
listFruits = ["apple", "banana", "orange", "lime"]

listFruits.pop(1)
listFruits.remove("apple")
listFruits.insert(1, "watermelon")