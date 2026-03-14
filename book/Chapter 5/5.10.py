current_users = ["alice006", "bob_smith", "charlie89", "david_jones", "eve_adams"]
copy_users = [user.lower() for user in current_users]
new_users = ["Frank99", "alice006", "GeorgeK", "bob_smith", "Hannah_1"]
for new_user in new_users:
    if new_user.lower() in copy_users:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")