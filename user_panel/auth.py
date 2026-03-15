from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret123"
ALGORITHM = "HS256"


def create_access_token(data):

    expire = datetime.utcnow() + timedelta(hours=2)

    data.update({"exp": expire})

    encoded = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return encoded