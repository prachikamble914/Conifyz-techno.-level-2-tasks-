print("*****Password strenght checker program*****")
import re
# password should be at least 8 character long
password = input("Enter your password: ")
if len(password) < 8:
    print("Password must be at least 8 charcters long.")
    # password should be at least one uppercase letter.
elif not re.search("[A-Z]",password):
    print("Password must contain at least one uppercase letter.")
     # password should be at least one lowercase letter.
elif not re.search("[a-z]",password):
    print("password must contain at least one lowercase letter.")
     # password should be at least one number.
elif not re.search("[0-9]",password):
    print("password must contain at least one number.")
else:
    print("Password is strong")