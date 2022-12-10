from pathlib import Path

path = Path('guest.txt')

name = input("What's your name? ")
path.write_text(name)