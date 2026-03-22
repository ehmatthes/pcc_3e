banned_users = ['andrew', 'carolina', 'david']
user = 'david'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else: 
    print(f"{user.title()}, can't post")