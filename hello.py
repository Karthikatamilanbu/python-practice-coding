#ask user for their name
name=input("what's your name? ").strip().title()

#split user's name into first and last
first,last=name.split(" ")

#say hello to user
print(f"hello,{first}")
    