---
hide:
  - footer
title: "Solutions: Chapter 13"
---

# Solutions - Chapter 13

There are a few things that can be helpful to know as you work on the exercises for Chapters 12-14:

- The solutions for Chapters 12-14 are kept in the [solution_files directory](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files), because every exercise is a mini project. These pages contain links to individual solutions in the repository.
- If you make a mistake when working through the project and can't get it back to a working state, it can be really frustrating to start over from scratch. There are some resources that can help with this:
    - In the [online resources](https://github.com/ehmatthes/pcc_3e), there's a complete version of the Alien Invasion project as it looks at the end of each main section in Chapters 12-14.
    - For example if you're working on getting the ship to move and everything stops working, you can look at the [versions from Chapter 12](https://github.com/ehmatthes/pcc_3e/tree/main/chapter_12), then click on the [adding_ship_image](https://github.com/ehmatthes/pcc_3e/tree/main/chapter_12/adding_ship_image) folder, and you'll have a working copy of the project as it looks at the beginning of the section about making the ship move.
    - If you want to compare your files to what they should look like at the end of the Piloting the Ship section, click on the [piloting_the_ship](https://github.com/ehmatthes/pcc_3e/tree/main/chapter_12/piloting_the_ship) folder.
    - If you want to know how to make snapshots of a project like this, make time to work through Appendix D, Using Git for Version Control. It will be well worth your time, and it's something you'll use your whole life as a programmer.
- If you haven't already seen the [cheat sheets](https://ehmatthes.github.io/pcc_2e/cheat_sheets/cheat_sheets/), there's a sheet that focuses on Pygame which might be helpful when working on these exercises. *(These will be fully updated to match the third edition shortly, but the Pygame sheets will not change much.)*
- It can be helpful to look through some of the [Pygame documentation](https://www.pygame.org/docs/) as you work on these exercises. There are also direct links to specific pages in the documentation that are helpful for certain exercises.

---

## 13-1: Stars

Find an image of a star. Make a grid of stars appear on the screen.

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_13/ex_13_1_stars)

## 13-2: Better Stars

You can make a more realistic star pattern by introducing randomness when you place each star. Recall from Chapter 9 that you can get a random number like this:

```python
from random import randint
random_number = randint(-10, 10)
```

This code returns a random integer between −10 and 10. Using your code in Exercise 13-1, adjust each star’s position by a random amount.

***Note:** This is a basic solution that shows working code to solve this exercise. If you want, you can experiment with different size stars, different spacing values, and different values for the amount of randomness in each star's position. From my experimentation this effect seems to work better with a relatively dense field of smaller stars.*

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_13/ex_13_2_better_stars)

***Note:** Here's an entirely different approach to creating a random field of stars. Instead of making a grid with some offsets, each star is randomly placed somewhere on the screen, up to a total number of stars.*

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_13/ex_13_2_better_stars_alternate)

## 13-3: Raindrops

Find an image of a raindrop and create a grid of raindrops. Make the raindrops fall toward the bottom of the screen until they disappear.

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_13/ex_13_3_raindrops)

## 13-4: Steady Rain

Modify your code in Exercise 13-3 so when a row of raindrops disappears off the bottom of the screen, a new row appears at the top of the screen and begins to fall.

***Note:** This is a simple working solution as well, and has not been optimized. If you like this exercise I encourage you to experiment with different size drops, different approaches to defining the starting position for each drop, and different approaches to creating new rows of raindrops.*

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_13/ex_13_4_steady_rain)

## 13-5: Sideways Shooter Part 2

We’ve come a long way since Exercise 12-6, *Sideways Shooter*. For this exercise, try to develop *Sideways Shooter* to the same point we’ve brought *Alien Invasion* to. Add a fleet of aliens, and make them move sideways toward the ship. Or, write code that places aliens at random positions along the right side of the screen and then sends them toward the ship. Also, write code that makes the aliens disappear when they’re hit.

***Note:** This is a solution to the version that sends individual aliens across the screen at random intervals.*

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_13/ex_13_5_sideways_shooter_2)

## 13-6: Game Over

In *Sideways Shooter*, keep track of the number of times the ship is hit and the number of times an alien is hit by the ship. Decide on an appropriate condition for ending the game, and stop the game when this situation occurs.

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_13/ex_13_6_game_over)
