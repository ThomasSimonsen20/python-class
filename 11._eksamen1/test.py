
def argsFunction(*args):
    print("last parameter " + args[-1])
    
#argsFunction("thomas", "mikkel", "mads")

def kwargsFunction(**kwargs):
    print("Firstname: " + kwargs["fname"]  + " Lastname: " + kwargs["lname"])

#kwargsFunction(fname = "Thomas", lname = "Simonsen")


#List
fruits = ["Apple", "Banana", "Pineapple", "Orange"]

#Vise pop, remove insert, append
#Pop fjerner på index, remove fjerner på navn

#Tuple
tupleFruits = ("Apple", "Banana", "Pineapple", "Orange")

#evt. bruge .len her
#print(len(tupleFruits))
#print(type(tupleFruits))

#Dictionary
firstDic = {"fname": "Thomas", "lname": "Simonsen", "age": 25}

#x = firstDic.keys() - giver alle keys
#x = firstDic.values() - giver alle values
#firstDic.update({"age": 27}) - updates
#thisdict["color"] = "red" -> tilføjer
#thisdict.pop("model") -> Fjerner

#Set
mySet = {"apple", "banana", "pineapple", "orange"}

#A set is a collection which is unordered, but you can remove items and add new items*, and unindexed.
#A set can contain different data types:
#thisset.add("orange")
#thisset.remove("banana")









