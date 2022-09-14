from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)