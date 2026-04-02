list_test = ["Hello","World","!"]
for _ in range(0,3): # '_' just to iterate
    if "Hello" in list_test:
        take = list_test.pop(0)
        print(take)
    if "World" in list_test:
        del list_test[0]
    if "!" in list_test:
        list_test.remove("!")
    
print(list_test)
