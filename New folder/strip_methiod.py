name,char = input("enter comma separated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"charater count : {name.lower().count(char.lower())}")
