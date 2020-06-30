import pyperclip
import secrets
import string


ALPHABET = string.ascii_lowercase + string.ascii_uppercase + string.digits

def pw_generator(n):
    while True:
        password = "".join(secrets.choice(ALPHABET) for i in range(n))
        if (any(c.islower() for c in password) 
            and any(c.isupper() for c in password) 
            and sum(c.isdigit() for c in password) >= 1):
            pyperclip.copy(password)
            return password


def main():
    print("クリップボードにコピーしました:", pw_generator(int(input("文字数を入力してください:"))), sep="")


if __name__ == "__main__":
    main()
