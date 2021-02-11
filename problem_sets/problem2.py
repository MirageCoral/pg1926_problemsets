import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{,3}$'
x = int(input("@ işaretinden sonraki uzunluğu: "))
email = input("Email: ")


def check(email):
    if re.search(regex, email):
        return True
    else:
        return False




if check(email):
    print("Mail adresiniz doğrudur.")
else:
    print("Mail adresiniz yanlıştır.")