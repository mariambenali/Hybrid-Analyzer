import bcrypt


password= "mariam123"

def hashed_password(password:str):
    password_bytes = password.encode('utf-8')


    salt = bcrypt.gensalt()

    hashed_password_bytes = bcrypt.hashpw(password_bytes, salt)

    return hashed_password_bytes.decode('utf-8')

hashed_password_utilisateur = hashed_password(password)
print(hashed_password_utilisateur)
