import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Minimal config for testing
config = {
    'credentials': {
        'usernames': {
            'user1': {
                'name': 'User One',
                # hashed password for 'abc123'
                'password': '$2b$12$U3l4D6oJZNJ35cEBGvRPLuqAMDD3OepPaNasxGCdjK85CQ05TfUs6'
            },
            'user2': {
                'name': 'User Two',
                # hashed password for 'def456'
                'password': '$2b$12$5aydDINk8VSKAECLgSqFR.g0guBbJI8IX3MXMDjXfd2PLIDqIGq8S'
            }
        }
    },
    'cookie': {
        'name': 'test_cookie',
        'key': 'some_random_secret_key',
        'expiry_days': 30
    }
}

# Initialize authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Login form
authentication_status = authenticator.login(location='main')

if authentication_status:
    name = authenticator.get_name()
    username = authenticator.get_username()
    st.success(f"Welcome {name} ({username})!")
    authenticator.logout('Logout', 'sidebar')

elif authentication_status is False:
    st.error("Username/password is incorrect")

elif authentication_status is None:
    st.info("Please enter your username and password")
