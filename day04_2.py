import hashlib


INPUT = "yzbqklnj"


def md5_hash(input_str):
    encoder = hashlib.md5()
    encoder.update(input_str.encode())
    return encoder.hexdigest()


num = 1
while True:
    input_str = INPUT + str(num)
    if md5_hash(input_str).startswith("000000"):
        print(num)
        break
    num += 1
