---
hide:
  - footer
title: What's new?
---

# What's new in the third edition?

Python is a mature language, but like every programming language it continues to evolve. The third edition incorporates some of the latest features in Python, without becoming bloated with every new feature that's been introduced in recent years. The new edition uses the latest versions of all third-party libraries in the projects section.

## Overall changes

Here is a summary of the changes that have been made to the book overall:

- This new edition uses Python 3.11. (The second edition was written using Python 3.7.)
- This edition uses VS Code instead of Sublime Text. VS Code is fully open, and it's seen widespread adoption in the Python world in recent years.
- Code listings are less cluttered and easier to follow throughout the book.
- The new edition uses updated libraries throughout, and updated workflows for each library.

## Specific changes

### Chapter 1

- Recommends VS Code as a text editor for readers who don't already have a preference. (You can use any editor that's properly configured to run Python code.)

### Chapter 2

- This chapter introduces `removeprefix()` and `removesuffix()`, two new methods that are helpful when working with files and URLs.
- Chapter 2 also includes Python's newly-improved error messages, which provide much more specific information to help you troubleshoot your code when something goes wrong.

### Chapters 3-9

- Many explanations have been clarified, and code listings have been simplified. (There were some annotations in shorter listings that weren't really necessary.)

### Chapter 10

- Uses the `pathlib` module for working with files. This is a much simpler approach to reading from and writing to files. It's also in keeping with how most major libraries are working with files now.

### Chapter 11

- Uses the third party-library `pytest` instead of the standard library's `unittest`.
- `pytest` is now the main testing library in the Python world. It's accessible to beginners, but powerful enough to serve professional testing needs as well.
- This chapter shows how to install third-party libraries, instead of introducing the topic in several different projects in the second half of the book.

### Alien Invasion (Chapters 12-14)

- The game uses an FPS (frames per second) setting, to make it run more consistently across all systems.
- The approach to building the alien fleet is simpler and easier to understand.
- The code listings are presented in an order that's easier to follow.

### Data Visualization (Chapters 15-17)

- Matplotlib has changed some of its default style settings; all figures in the new edition match the current default styles.
- Plotly has introduced Plotly Express, a module that focuses on building an initial plot quickly, and then making styling choices. The third edition uses this new approach.
- The random walk project has a small improvement that increases the accuracy of the plots, which means you'll see a wider variety of patterns emerge each time you generate a new walk.
- The weather and earthquake projects use updated data sets.
- The GitHub data used in Chapter 17 is fully updated.

### Web Applications (Chapters 18-20)

- The Learning Log project is built using Django 4.1.
- Some parts of the project have been renamed to make it easier to understand the overall layout of a Django project.
- The project is styled using Bootstrap 5.
- The deployment process has been updated. The project is now deployed to Platform.sh, a modern hosting service for Django projects. The deployment process is controlled by YAML configuration files, which give you a great deal of control over how your project is deployed. This approach is consistent with how professional programmers deploy modern Django projects.

### Appendices

- Appendix A includes updated supplementary installation and setup instructions, for readers who run into any issues installing Python.
- Appendix B discusses customizations you can make to VS Code to make it more useful for writing and maintaining Python code. It also includes a number of shortcuts you can use to work more efficiently in VS Code.
- Appendix C includes an updated set of resources for getting help online.
- Appendix D uses the new `git restore` command for rolling back changes in a project, and the `git switch` command for getting back to the main branch in a project.
- Appendix E expands on the deployment process for web applications; it is entirely new. Deployment is a complex process when it doesn't go perfectly. This appendix provides some guidance on how to troubleshoot deployments when they don't work the first time you try them.

### Index

- The new edition has been entirely re-indexed, to help you find what you need quickly after you've worked through the book.