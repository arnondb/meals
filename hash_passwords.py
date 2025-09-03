import streamlit_authenticator as stauth

# Define your credentials with plain text passwords
credentials = {
    'usernames': {
        'user1': {
            'name': 'User One',
            'password': 'abc123',
            'email': 'user1@example.com'
        },
        'user2': {
            'name': 'User Two',
            'password': 'def456',
            'email': 'user2@example.com'
        }
    }
}

# Hash the passwords
hashed_credentials = stauth.Hasher.hash_passwords(credentials)

# Print the hashed credentials
print(hashed_credentials)
