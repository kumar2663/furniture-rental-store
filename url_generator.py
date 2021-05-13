from itsdangerous import URLSafeTimedSerializer


def generate_confirmation_token(email, secret_key, password_salt):
    serializer = URLSafeTimedSerializer(secret_key)
    return serializer.dumps(email, salt=password_salt)


def confirm_token(token, secret_key, password_salt, expiration=100000):
    serializer = URLSafeTimedSerializer(secret_key)
    try:
        email = serializer.loads(
            token,
            salt=password_salt,
            max_age=expiration
        )
    except:
        return False
    return email
