# Append exercises
#1)
list_of_classes=["1class","2class","3class","4class","5class"]#i made a list 
list_of_classes.append("6class")#i add a "6class" in the list
print(list_of_classes)#and  printed already a new list 
#2)
list_of_fruits=[]#i made a empty list 
list_of_fruits.append("banana")#added banana 
list_of_fruits.append("apple")#added apple 
list_of_fruits.append("orange")#added orange  
print(list_of_fruits)#printed the list
#3)
letters_1=["a","b","c"]#created a list 
letters_2=["d","x","z"]#created another list 
for item in letters_2:#using for loop i make every item i the letter_2 move to the variable " item " and added to the letter_1 
    letters_1.append(item)
print (letters_1)#printed the renewed letter_1
#4)
row1=[]#i made a list 1
row2=[]# made list 2
Matrix=[row1,row2]#another list where is nested that two lists which i made previous time 
row1.append(1)#here i added numbers in first two lists 
row1.append(2)
row1.append(3)
row2.append(4)
row2.append(5)
row2.append(6)
print(Matrix)#and then printed the main list Matrix
#5)
number=[]# i made a main list 
num=input("please enter a first number:")#made  varaibles  
num1=input("please enter a second number:")
num2=input("please enter a third number:")

number.append(num)#added that variable meanings to the main list 
number.append(num1)
number.append(num2)

print(number)# and printed the list 



#Clear exercises
#1)
list8=["beagle","Doberman","Georgian shephard","German shephard"]#made a list 
list8.clear()#cleard the list 
print(list8)#printed the list
#2)
Surenames=["Abramishvili","Burduli","Janiashvili"]#made a list 
Surenames.clear()#cleard the list 
print(Surenames)#printed the list
#3)
Phone_Brands =["Iphone","Saumsung","Nokia","LG"]#made a list 
Phone_Brands.clear()#cleard the list 
print(Phone_Brands)#printed the list
#4)
Car_brands =["BMW","Mersedes","Porsche","Pagani"]#made a list 
Car_brands.clear()#cleard the list 
print(Car_brands)#printed the list
#5)
Names=["nikoloz", "Xato","giorgi", "gabrieli"]#made a list 
Names.clear()#cleard the list 
print(Names)#printed the list


#Copy exercises
#1)
children_names=["rati","cotne","gigi","nika"]#made list
children_names_copy=children_names.copy()#copyed list
print(children_names_copy)#printed copyed list 
#2)
Teachers_names=["Tariko","Mari","Tamuna","Nata","Asmati"]#made list 
Teachers_names_copy=Teachers_names.copy()#copyed list 
print(Teachers_names_copy)#printed copyed list 
#3)
Countrys_names=["Spain","Englad","Georgia","France","USA"]#made list 
Countrys_names_copy=Countrys_names.copy()#copyed list 
print(Countrys_names_copy)#printed copyed list 
#4)
Georgian_Footballers_list=["Kvaratsqhelia","Miqautadze","Witeishvili","Qochorashvili","Kakabadze","..."]#made list 
Georgian_Footballer_list_copy=Georgian_Footballers_list.copy()#copyed list 
print(Georgian_Footballer_list_copy)#printed copyed list 
#5)
Citys_list=["Tbilissi","Madrid","Paris","Kutaisi","Barcelona"]#made list 
City_names_copy=Citys_list.copy()#copyed list 
print(City_names_copy)#printed coped list 



#Count exercises
#1)
children_names=["rati","cotne","gigi","nika"]#made list
print(children_names.counter("nika"))#printed and counted the element

#2)
Teachers_names=["Tariko","Mari","Tamuna","Nata","Asmati"]#made list 
print(Teachers_names.count("Mari"))#printed and counted the element 

#3)
Countrys_names=["Spain","Englad","Georgia","France","USA"]#made list 
print(Countrys_names.counter("Georgia"))#printed and counted the element

#4)
Georgian_Footballers_list=["Kvaratsqhelia","Miqautadze","Witeishvili","Qochorashvili","Kakabadze","..."]#made list 
print(Georgian_Footballers_list.count("Kvaratsqelia"))#printed and counted the element 

#5)
Citys_list=["Tbilissi","Madrid","Paris","Kutaisi","Barcelona","Paris",]#made list 
print(Citys_list.count("Paris"))#printed and counted the element 



#Extend exercises
#1)
children_names=["rati","cotne","gigi","nika"]#made list 
print(children_names.extend("Xato"))#printed and extended the list 

#2)
Teachers_names=["Tariko","Mari","Tamuna","Nata","Asmati"]#made list 
print(Teachers_names.extend("Mari"))#printed and extended the list 

#3)
Countrys_names=["Spain","Englad","Georgia","France","USA"]#made list 
print(Countrys_names.extend("Egypt"))#printed and extended the list 

#4)
Georgian_Footballers_list=["Kvaratsqhelia","Miqautadze","Witeishvili","Qochorashvili","Kakabadze","..."]#made list 
print(Georgian_Footballers_list.extend("Kvaratsqelia"))#printed and extendedd the list 

#5)
Citys_list=["Tbilissi","Madrid","Paris","Kutaisi","Barcelona","Paris",]#made list 
print(Citys_list.extend("Varshava"))#printed and extended the list 



#Index exerscise
#1)
children_names=["rati","cotne","gigi","nika","Xato"]#made list 
print(children_names.index("Xato"))#printed the element index

#2)
Teachers_names=["Tariko","Mari","Tamuna","Nata","Asmati"]#made list 
print(Teachers_names.index("Mari"))#printed the element index 

#3)
Countrys_names=["Spain","Englad","Georgia","France","USA"]#made list 
print(Countrys_names.index("Georgia"))#printed the element index

#4)
Georgian_Footballers_list=["Kvaratsqhelia","Miqautadze","Witeishvili","Qochorashvili","Kakabadze","..."]#made list 
print(Georgian_Footballers_list.index("Kvaratsqelia"))#printed the elemet index

#5)
Citys_list=["Tbilissi","Madrid","Paris","Kutaisi","Barcelona","Paris",]#made list 
print(Citys_list.index("Paris"))#printed the element index


#Insert exercises
#1)
children_names=["rati","cotne","gigi","nika"]#made list 
children_names.insert(0,"nata")#inserted the element
print(children_names)#printed the list 

#2)
Teachers_names=["Tariko","Mari","Tamuna","Nata","Asmati"]#made list 
print(Teachers_names.insert(3,"Mari"))#printed and inserted the element 

#3)
Countrys_names=["Spain","Englad","Georgia","France","USA"]#made list 
print(Countrys_names.insert(3,"Brazil"))#printed and inserted the element 

#4)
Georgian_Footballers_list=["Kvaratsqhelia","Miqautadze","Witeishvili","Qochorashvili","Kakabadze","..."]#made list 
print(Georgian_Footballers_list.insert(2,"Kvaratsqelia"))#printed and inserted the element 

#5)
Citys_list=["Tbilissi","Madrid","Paris","Kutaisi","Barcelona","Paris",]#made list 
print(Citys_list.insert(3,"Brazil"))#printed and inserted the element



#Pop exercises
#1)
children_names=["rati","cotne","gigi","nika","Xato"]#made list 
print(children_names.pop("gio"))#printed and subtracted the element  

#2)
Teachers_names=["Tariko","Mari","Tamuna","Nata","Asmati"]#made list 
print(Teachers_names.pop("Asmati"))#printed and substracted the element

#3)
Countrys_names=["Spain","Englad","Georgia","France","USA"]#made list 
print(Countrys_names.pop("USA"))#printed and subtracted the element 

#4)
Georgian_Footballers_list=["Kvaratsqhelia","Miqautadze","Witeishvili","Qochorashvili","Kakabadze","..."]#made list 
print(Georgian_Footballers_list.pop("Kvaratsqelia"))#printed and subtracted the element  

#5)
Citys_list=["Tbilissi","Madrid","Paris","Kutaisi","Barcelona","Paris",]#made list 
print(Citys_list.pop("Paris"))#printed and subtracted the element 



#Remove exercises
#1)
children_names=["rati","cotne","gigi","nika","Xato"]#made list 
print(children_names.remove("gio"))#printed and subtracted the element 

#2)
Teachers_names=["Tariko","Mari","Tamuna","Nata","Asmati"]#made list 
print(Teachers_names.remove("Asmati"))#printed and subtracted the element 

#3)
Countrys_names=["Spain","Englad","Georgia","France","USA"]#made list 
print(Countrys_names.remove("USA"))#printed and subtracted the element 

#4)
Georgian_Footballers_list=["Kvaratsqhelia","Miqautadze","Witeishvili","Qochorashvili","Kakabadze","..."]#made list 
print(Georgian_Footballers_list.remove("Kvaratsqelia"))#printed and subtracted the element 

#5)
Citys_list=["Tbilissi","Madrid","Paris","Kutaisi","Barcelona","Paris",]#made list 
print(Citys_list.removej("Paris"))#printed and subtracted the element 