---
hide:
  - footer
title: "Solutions: Chapter 14"
---

# Solutions - Chapter 14

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

## 14-1: Press P to Play

Because *Alien Invasion* uses keyboard input to control the ship, it would be useful to start the game with a keypress. Add code that lets the player press P to start. It might help to move some code from `_check_play_button()` to a `_start_game()` method that can be called from `_check_play_button()` and `_check_keydown_events()`.

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_14/ex_14_1_p_to_play)

## 14-2: Target Practice

Create a rectangle at the right edge of the screen that moves up and down at a steady rate. Then on the left side of the screen, create a ship that the player can move up and down while firing bullets at the rectangular target. Add a Play button that starts the game, and when the player misses the target three times, end the game and make the Play button reappear. Let the player restart the game with this Play button.

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_14/ex_14_2_target_practice)

## 14-3: Challenging Target Practice

Start with your work from Exercise 14-2 (page 283). Make the target move faster as the game progresses, and restart the target at the original speed when the player clicks Play.

[Solution](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_14/ex_14_3_challenging_tp)


