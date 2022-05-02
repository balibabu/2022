def user(password):
    msg="Welcome to system" if password=="jerry" else "password mismatch"
    return msg
print(user("jerry"))
    
