from pathlib import Path
import json


username = input("What is your name? ")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")