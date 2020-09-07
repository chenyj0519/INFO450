def check_users(current_users, new_users):
    pass

current_users=['Chen','Zhang','Zhao','Qian','Sun']
new_users=['Li','Sun','Zhou','Wu','Zheng']

current_users_lower = [user.lower() for user in current_users]

for username in new_users:
    if username in current_users:
        print("Existing user name.Need to enter a new username.")
    else:
        print("Username is available.")
