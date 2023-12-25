import sys

try:
    import zipfile
except ImportError:
    print("zipfile module not found. Installing...")
    try:
        from pip._internal import main as pipmain
    except ImportError:
        from pip import main as pipmain

    pipmain(['install', 'zipfile'])
    import zipfile

def crack_password(password_list, zip_file):
    with open(password_list, 'rb') as password_list_file:
        passwords = password_list_file.read().splitlines()

    with zipfile.ZipFile(zip_file) as archive:
        attempt_count = 0
        for idx, password in enumerate(passwords, start=1):
            attempt_count += 1
            try:
                archive.extractall(pwd=password)
                print(f"Password found at line {idx}")
                print(f"Password is {password.decode()}")
                print(f"Number of attempts: {attempt_count}")
                return True
            except Exception as e:
                continue

    print(f"Number of attempts: {attempt_count}")
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py PASSWORD_FILE ZIP_FILE")
        sys.exit(1)

    password_list = sys.argv[1]
    zip_file = sys.argv[2]

    print(f"Testing passwords from {password_list} on {zip_file}")

    if not crack_password(password_list, zip_file):
        print("Password not found in this file")
