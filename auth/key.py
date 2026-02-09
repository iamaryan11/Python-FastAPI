import secrets

SECRET_KEY=secrets.token_urlsafe(32)
print(SECRET_KEY)

# run above file as: python key.py to get a random secret string