import string
import random

PasswordHashFunction = "SHA256"
EncryptedExtension = '.enc'

# Cross platform cryptographically secure PRNG methods
# *nix -> /dev/urandom 
# win -> CryptGenRandom()
def genRndPsw(len = 16):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits ) for _ in range(len))
