info = ('Alice', 21, 'Student', 'Texas', 3.9)
print(info[1:2])
"""a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a^b) #symmetric difference is 1,2,5,6

Int1 = {1,2}
Int2 = {3,4}
print(Int1|Int2) #combined outputs

H = {1,2}
A = {1,4}
print(H&A)
    
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a ^ b #1,2,5,6
d = a & b #3,4
print(len(c | d)) #1,2,5,6,3,4

totient_seq = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20]
totient_set = set(totient_seq)
totient_set.add(1)
print(totient_set)

nums = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
odd_count = 0
seen = set()

for num in nums:

    if num not in seen:
        if nums.count(num) % 2 == 0: #odd
            odd_count += 1


        
    seen.add(num)


print(odd_count,seen)

inventory = {
    "The Simpsons: Krusty Burger": 5,
    "Sherlock Holmes: Book Nook": 3,
    "Lord of the Rings: Balrog Book Nook": 4,
    "Japanese Red Maple Bonsai Tree": 6,
    "Bluey's Family House": 7,
    "Durrr Burger Restaurant": 2,
    "Hogwarts Express Book Nook": 3,
    "The Fauna Collection: Tiger": 5,
    "Klombo": 4,
    "Minifigure Vending Machine": 2
}

# 1. Check inventory and quantity for "Bluey's Family House".

stock = inventory.get("Bluey's Family House")


print(f"Bluey's Family House (available quantity): {stock}")

# 2. Check which sets are ready for summer launch.

set_names = inventory.keys()


print(f"Launch Sets: {set_names}")

# 3. Print out inventory / quantities for final check.

for set_name, quantity in inventory.items():


    print(f"{set_name}: {quantity} units")"""