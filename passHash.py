from hashlib import sha256

# description: hash stuff; parameters: (string) password; returns: (string) hex representation of hash
def passHash(password):
    return sha256(password.encode()).hexdigest()

def test():
    x = "pass123"
    y = passHash(x)
    print(x)
    print(y)

test()