import zipfile

def crack_zip(zip_file, wordlist):
    with zipfile.ZipFile(zip_file) as zf:
        with open(wordlist, 'r', errors='ignore') as f:
            for line in f:
                password = line.strip()
                try:
                    zf.extractall(pwd=password.encode())
                    print(f"Password found: {password}")
                    return
                except:
                    pass
    print("Password not found")

crack_zip("secret.zip", "rockyou.txt")