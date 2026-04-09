import hashlib

def file_hash(filename):
    h = hashlib.sha256()

    with open(filename, "rb") as f:
        data = f.read()
        h.update(data)

    return h.hexdigest()