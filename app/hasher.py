import bcrypt




def hashed_password(password:str):
    password_bytes = password.encode('utf-8')


    salt = bcrypt.gensalt()

    hashed_password_bytes = bcrypt.hashpw(password_bytes, salt)

    return hashed_password_bytes.decode('utf-8')



def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )
    
