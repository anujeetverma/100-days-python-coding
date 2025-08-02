import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))

random_selector = random.randint(0,4)
print(f"{friends[random_selector]}")