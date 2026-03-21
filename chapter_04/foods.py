# FOODS SECTION
MY_FOODS = ['pizza', 'falafel', 'carrot cake'.upper()]
FRIEND_FOOD = MY_FOODS[:] # THIS WILL CREATE TRUE INDEPENDENT LIST WITH SAME VALUE OF THE FIRST LIST (MY_FOODS)

MY_FOODS.append('bariani'.upper()) # HERE IT ADD THIS VALUE IN THE END OF THE LIST
FRIEND_FOOD.append('katsu kari'.upper()) 

print("My favorite foods are:")
print(MY_FOODS)



print("\nMy friend's favorite foods are:")
print(FRIEND_FOOD, "\n")

print(2 * "=============" * 2)

my_fruits = ["apple", "orange", "banana"]
friend_fruits = my_fruits.copy() # ALSO THIS WAY OF COPYING A LIST WORKS LIKE SAME FOODS LINE 2 => FRIEND_FOOD = MY_FOODS[:]
friend_fruits.insert(0, "cherry")

print(friend_fruits)