import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def login_authenticator():
    with open('src\credentials\credentials.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    return authenticator.login('Login', 'main')