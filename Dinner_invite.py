import time
#Who would i invite to dinner exercise
list_of_people = ["my mom","my dad","my pet"]
salute = f"hey! {list_of_people[0],list_of_people[1], list_of_people[2]}! welcome to my dinner"
print(salute)
time.sleep(1)
print("My pet can't make it")
del list_of_people[2]
time.sleep(1)
list_of_people.append("New Person")
print(f"hey!{list_of_people}")
time.sleep(1)
print("I just found a bigger table")
time.sleep(1)
list_of_people.insert(3,"Grandma")
list_of_people.insert(4,"Grandpa")
list_of_people.append("Finale Persone")
print(f"new people {list_of_people}")



