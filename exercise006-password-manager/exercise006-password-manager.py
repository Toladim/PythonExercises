pwd = input("What is your master password? ")
while True:
    mode = input("Would you like to add a new password or view existing ones (view,add)? Press 'q' to quit ").lower()
    
    if mode == "q":
        break
    elif mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue