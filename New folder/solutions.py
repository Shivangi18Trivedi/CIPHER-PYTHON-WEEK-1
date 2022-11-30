name = input("enter your name: ")
print(f"reverse of your your name is {name[-1::-1]}")

while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]}  : {name.count(name[i])")
        
