# Exercise 3-1. Names:
names = ['sara', 'anam' , 'faiza' , 'zainab']

print(names[2].title())
print(names[-1].title())
print(names[0].title())
print(names[-3].title())

# Exercise 3-2. Greetings:

message_1 = "Hello " + str(names[0]) +" !" +" welcome to python class. "
message_2 = "Hello " + str(names[1]) +" !" +" welcome to python class. "
message_3 = "Hello " + str(names[2]) +" !" +" welcome to python class. "
message_4 = "Hello " + str(names[-1]) +" !" +" welcome to python class. "
message = message_1+"\n"+message_2+"\n"+message_3+"\n"+message_4

print("\n"+message.title())

# Exercise 3-3. Your Own List:

trans_name = ['Toyota' , 'Subaru' , 'Audi' , 'Lexus', 'Acura']

trans_name_p = trans_name[0]+"\n"+trans_name[1]+"\n"+trans_name[2]+"\n"+trans_name[-2]+"\n"+trans_name[-1]
new_message_1 = "'"+"I would like to own a "+trans_name[0].upper()+" car."+"'"
new_message_2 = "'"+"I would like to own a "+trans_name[1].upper()+" car."+"'"
new_message_3 = "'"+"I would like to own a "+trans_name[2].upper()+" car."+"'"
new_message_4 = "'"+"I would like to own a "+trans_name[3].upper()+" car."+"'"
new_message_5 = "'"+"I would like to own a "+trans_name[4].upper()+" car."+"'"
new_message = new_message_1+"\n"+new_message_2+"\n"+new_message_3+"\n"+new_message_4+"\n"+new_message_5


print("\n"+trans_name_p)
print("\n"+new_message)
print("\n"+new_message.lower())
print("\n"+new_message.upper()+"\n")
print(trans_name)

# Exercise 3-4. Guest List:

guests = ['zara' , 'sara' , 'zoya' , 'sana']

for guest in guests:
    print("Hi " + guest.title() + ", Please join us for dinner party on this weekend.")

# Exercise 3-5. Changing Guest List:

pop_guest = guests.pop(-1)

print("\n"+pop_guest.title()+" can't make the dinner with us on this weekend.")

# Exercise 3-5. Modify List... Replace the name with newone :

guests.insert(-1,'tania')

print("\n"+str(guests).title()+"\n")

# Exercise 3-5. Print new list:

for guest in guests:
    print("Hi " + guest.title() + ", Please join us for dinner party on this weekend.")

# Exercise 3-6. More Guests:
print("\n")

guests.insert(0,'anam')
guests.insert(3,'rumaila')
guests.append('zaib')

print(guests)

print("\n")
for guest in guests:
    print("Hi " + guest.title() + ", Please join us for dinner party on this weekend... as we get a big table and more space :)"+"\n")

# Exercise 3-7. Shrinking Guest List:

for guest in guests:
    print("Hi "+ guest.title() +", I regret to inform you... Dinner table found only have two person space can't invite you.")

remove_guest_1=guests.pop()
print("\n"+"Hi "+ remove_guest_1.title() +", I regret to inform you... Dinner table found only have two person space can't invite you.")

remove_guest_2= guests.pop()
print("\n"+"Hi "+ remove_guest_2.title() +", I regret to inform you... Dinner table found only have two person space can't invite you.")

remove_guest_3= guests.pop()
print("\n"+"Hi "+ remove_guest_3.title() +", I regret to inform you... Dinner table found only have two person space can't invite you.")

remove_guest_4= guests.pop()
print("\n"+"Hi "+ remove_guest_4.title() +", I regret to inform you... Dinner table found only have two person space can't invite you.")

remove_guest_5= guests.pop()
print("\n"+"Hi "+ remove_guest_5.title() +", I regret to inform you... Dinner table found only have two person space can't invite you.")


print("\n"+str(guests))

for guest in guests:
    print("Hi " + guest.title() + ", Please join us for dinner party on this weekend..."+"\n")

del guests[0]
del guests[0]
print(guests)

# Exercise 3-8. Seeing the World:

places  = ['makkah','switzerland' ,'austin', 'madina' , 'neelum valley', 'kashmir']

print("\n")
print(places)
print("\n")

print(sorted(places))

print("\n")
print(places)
print("\n")


print(sorted(places, reverse=True))
print("\n")

print(sorted(places))
print("\n")

print(places)
print("\n")


places.reverse()
print(places)

places.reverse()
print(places)
print("\n")

places.sort()
print(places)
print("\n")

places.sort(reverse=True)
print(places)
print("\n")

# Exercise 3-9. Dinner Guests:

print(len(pop_guest))

# Exercise 3-10. Every Function:

funlist = ['english', 'urdu', 'math', 'science', 'computer']



print(funlist[0].title()+"\n"+funlist[-4].title()+"\n"+funlist[2].title()+"\n"+funlist[3].title()+"\n"+funlist[-1].title())

print("\n"+"I love to read "+"'"+funlist[0].title()+"' novels."+"\n")

funlist[2] = 'statistics'

print("updated \n"+str(funlist))

funlist.append('math')
print(funlist)

print("\n")
funlist.insert(3,'chemistry')
print(funlist)

print("\n")

funlist.remove('urdu')
print(funlist)

print("\n")

del funlist[-2]
print(funlist)

print("\n")

funlist_new = funlist.pop(2)
print(funlist_new)
print(funlist)

funlist_new_1 = funlist.pop()
print(funlist_new_1)
print(funlist)


funlist.sort()
print(funlist)

print("\n")
funlist.sort(reverse=True)
print(funlist)

print("\n")

print(sorted(funlist))
print("\n")

print(sorted(funlist,reverse=True))
print("\n")


funlist.reverse()
print(funlist)
print("\n")

print(len(funlist))
print("\n")

#Exercise 3-11. Intentional Error:

#funlist[4] = 'computer'
print(funlist)
# there is no No.4 index position in list

funlist[-1] = 'computer'
print(funlist)

# Exercise 4-1. Pizzas:

print("\n"+"Chapter no.4 (Loop) ".upper()+"\n")

pizzas = ['fajita','Chicken Alfredo','supreme max','creamy cheese','pepperoni']

for pizza in pizzas:
    print(pizza.title())

print("\n"+"Modify list with sentence".upper()+"\n")

for pizza in pizzas:
    print("I like '"+pizza.title()+"'"+" pizza.")

print("\n"+"I like Fajita pizza!"+"\n"+"I love the flavour ....."+"\n"+"I eat twice a month.")
print("\n"+"I really love pizza!"+"\n")

# Exercise 4-2. Animals:

animals = ['cat','parrot','dog','horse']

for animal in animals:
    print(animal.title())

print("\n"+"Modify animals list with sentence".upper()+"\n")

for animal in animals:
    print("A "+animal.upper()+" would make a great pet.")

print("\n"+"Add line in animals list with sentences".upper()+"\n")

for animal in animals:
    print(animal.upper()+" is loyal pet.\nThey eat vegetables and also play with humans."+"\n")

print(animal.title()+" would make a great pet.")


# Exercise 4-3. Counting to Twenty:

for count in range(1,21):
    print(count)

numbers= list(range(1,21))
print(numbers)

# Exercise 4-4. One Million:

print("\n")

#for list in range(1,1000001):
 #   print(list)

# Exercise 4-5. Summing Million:

mill_numbers = list(range(1,1000001))

print(min(mill_numbers))
print(max(mill_numbers))
print(sum(mill_numbers))

# Exercise 4-6. Odd Numbers:
print("\n")

for odd in range (1,20,2):
    print(odd)

# Exercise 4-7. Three:
print("\n")

for multiples in range(3,30,3):
    print(multiples)

# Exercise 4-8. cubes:
print("\n")

cubes=[]

for value in range(1,10):
    cube= value**3
    cubes.append(cube)
print(cubes)

# Exercise 4-9. cube comprehension:
print("\n")

cubes_comp = [value**3 for value in range(1,10)]

print(cubes_comp)

# Exercise 4-10. Slices:

print("\n")


for animal in animals:
    print(animals[0:3])
    print("My friend's favourite pet is '" + animal.title() + "'")
    print("\n")

print("Three item from the start of the list are: ")
print(pizzas[:3])

print("\n")

print("Three item from the middle of the list are: ")
print(pizzas[1:4])

print("\n")


print("Three item from the last of the list are: ")
print(pizzas[-4:])

print("\n")


# Exercise 4-11. My Pizzas, Your Pizzas:

friend_pizzas = pizzas[:]

pizzas.append('cheesy chicken tikka')
print(pizzas)
print("\n")

friend_pizzas.insert(0,'chicken tandoori')
print(friend_pizzas)
print("\n")


print(pizzas)
print(friend_pizzas)
print("\n")

for pizza in pizzas:
    print("My favorite pizzas are:\n'"+pizza+"'.")

print("\n")

for fren_pizza in friend_pizzas:
    print("My friend'sfavorite pizzas are:\n'"+fren_pizza+"'.")
print("\n")

# Exercise 4-12. More Loops:

my_foods = ['pizza','falafel','carrot cake']

friend_foods = my_foods[:]


print("My food list: \n")
for myfood in my_foods:
    print(myfood)

print("\nMy Friend food list: \n")

for food in friend_foods:
    print(food)
print("\n")

# Exercise 4-12. Buffet:

buffet_food = ('biryani','stew','nihari','tikka boti','charga')

for foody in buffet_food:
    print(foody.title())

#buffet_food[3] = 'beef boti'
print(buffet_food)

print("\n")
print("\nRevised Menu:\n")

buffet_food =('biryani','quorma','nihari','bihari boti','charga')

for foody in buffet_food:
    print(foody.title())