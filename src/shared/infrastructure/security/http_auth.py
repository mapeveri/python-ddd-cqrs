import os

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


auth = HTTPBasicAuth()
USER_DATA = {
    os.environ.get('METRICS_ENDPOINT_USER'): generate_password_hash(os.environ.get('METRICS_ENDPOINT_PASSWORD'))
}


@auth.verify_password
def verify(username: str, password: str) -> bool:
    password_hash = USER_DATA.get(username)
    if username is None or password is None or password_hash is None:
        return False

    return check_password_hash(password_hash, password)
