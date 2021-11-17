import hashlib


def main():
    digester = hashlib.md5()
    with open("python-3.9.7.tar.xz", "rb") as file:
        for data in iter(lambda: file.read(1024), b""):
            digester.update(data)
    print(digester.hexdigest())


if __name__ == '__main__':
    main()
