motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)


# NEED TO MAKE THE VALUE LIST 
too_expensive = motorcycles[3]
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
