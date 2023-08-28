
#Length:

Subjects = ["C","C++","Java","Python","Php","R","Java-Script"]

print(len(Subjects))


#Lastly add in the list:

Subjects = ["C","C++","Java","Python","Php","R","Java-Script"]
Subjects.append("Swift")

print(Subjects)


#Insert:

Subjects = ["C","C++","Java","Python","Php","R","Java-Script"]
Subjects.insert(3,"Ios")

print(Subjects)


#Remove:

Subjects = ["C","C++","Java","Python","Php","R","Java-Script"]
Subjects.remove("Php")

print(Subjects)


#Copy:

Subjects = ["C","C++","Java","Python","Php","R","Java-Script"]
Subjects2 = Subjects.copy()

print(Subjects2)


#Sort:

Subjects = ["C","C++","Java","Python","Php","R","Java-Script"]
Subjects.sort()

print(Subjects)


#Reverse:

Subjects = ["C","C++","Java","Python","Php","R","Java-Script"]
Subjects.reverse()

print(Subjects)


#Pop:

Subjects = ["C","C++","Java","Python","Php","R","Java-Script"]
Subjects.pop(3)

print(Subjects)


#Clear:

Subjects = ["C","C++","Java","Python","Php","R","Java-Script"]
Subjects.clear()

print(Subjects)


#Index Position Check:

Subjects = [20,25,30,40]
pos = Subjects.index(30)

print(pos)


#Count:

Subjects = [2,2,2,2,3,4,6,78,9]
pos = Subjects.count(2)

print(pos)


