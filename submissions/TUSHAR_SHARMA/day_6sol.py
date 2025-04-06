#day 6 sol
while True:
    choice =input("which path do you choose(left/right)").strip().lower()
    if choice == "left":
        print("you found a hidden tunnel: you 're safe")
        break
    elif choice == "right":
        print("oh no! the glitch's trap was here! try again ")
        break
    else:
        print ("Invalid choice. please enter 'left' or 'right'.")