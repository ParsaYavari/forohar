
from instagrapi import Client
import random
from urllib.parse import urlparse

names = [
    "ali", "mmdgang", "hossein", "reza", "fateme", "sina", 
    "armin", "sahar", "nilo", "mohsen", "sogand", "shahin"
]

def generate_fake_username():
    base = random.choice(names)
    suffix = str(random.randint(1000, 99999))
    return base + suffix

def extract_username_from_link(link):
    path = urlparse(link).path
    username = path.strip('/').split('/')[0]
    return username if username else None

def get_sessionid_from_login(username, password):
    cl = Client()
    cl.login(username, password)
    return cl.get_settings()["authorization_data"]["sessionid"]

def login_with_sessionid(sessionid):
    cl = Client()
    cl.login_by_sessionid(sessionid)
    return cl

def main():
    print('''
    ████████████████████████████████████████████████████████
    █▄─▄█▄─▀█▄─▄█─▄▄▄▄█─▄─▄─██▀▄─██▄─▄─▀█▄─▄▄▀█▄─██─▄█─▄─▄─█
    ██─███─█▄▀─██▄▄▄▄─███─████─▀─███─▄─▀██─▄─▄██─██─████─███
    ▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀
    ''')
    print('Username hesab asli:')
    username = input(" ↪ ").strip()
    print('Password hesab asli:')
    password = input(" ↪ ").strip()
    print('Link profil hadaf:')
    link = input(" ↪ ").strip()

    target_username = extract_username_from_link(link)
    if not target_username:
        print("[✗] Link eshtebah ast.")
        return

    fake_user = generate_fake_username()
    print(f"[+] Fake name: {fake_user}")

    try:
        sessionid = get_sessionid_from_login(username, password)
        cl = login_with_sessionid(sessionid)
        user = cl.user_info_by_username(target_username)
        cl.user_follow(user.pk)
        print(f"[✓] {fake_user} -> {target_username} follow shod (az tarighe link)")
    except Exception as e:
        print(f"[✗] Error: {e}")

if __name__ == "__main__":
    main()
