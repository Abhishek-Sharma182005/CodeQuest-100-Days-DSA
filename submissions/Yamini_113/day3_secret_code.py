user_name=input("Enter your name:")
print("Original Name:",user_name)
print("Secret Code:",(user_name[::-1]).upper())