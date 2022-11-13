from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def generate_keys():
    private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public = private.public_key()
    return private, public


def sign(message, private):
    message = bytes(str(message), 'utf-8')  # converting message to bytes
    signature = private.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def verify(message, signature, public):
    message = bytes(str(message), 'utf-8')  # converting message to bytes
    try:
        public.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    except:
        print("Error executing public key")
        return False


if __name__ == '__main__':
    pr, pu = generate_keys()  # A
    pr1, pu1 = generate_keys() # B
    print(pr)
    print(pu)

    message = "Hi I am Parmanand Yadav"
    sig = sign(message, pr)
    print(sig)
    correct = verify(message, sig, pu1)
    if correct:
        print("Successful")
    else:
        print("Failed")
