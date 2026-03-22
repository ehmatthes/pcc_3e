apps = {"FIRST_APP": "instagram", "SECOND_APP": "SNAPCHAT"}
# extra_apps = apps[:] 
extra_apps = apps.copy()


print(extra_apps.keys())
print(apps.get("FIRST_APP"), "\n")