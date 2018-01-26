import os
import sys
import random
import struct
import os.path
import hashlib
from Crypto.Cipher import AES

import Settings

class AES256:
    
    key = ""
    blockSize = 0

    def __init__(self, pwd):
        if Settings.PasswordHashFunction == 'SHA256':
            self.blockSize = 32 # Block size a 32 byte ovvero a 256 bit. Usiamo AES256
            self.key = hashlib.sha256(pwd).digest(); # Da una password di dimensione variabile ne ottendo una fissa a 32 caratteri

    def encryptFolder(self, filepath):
        if os.path.isdir(filepath):
            for filename in listdir(filepath):
                if os.path.isdir(filename):
                    self.encryptFolder(filename)
                else:
                    self.encryptFile(os.path.join(filepath,filename))
        else:
            self.encryptFile(filepath)

    def decryptFolder(self, filepath):
        if os.path.isdir(filepath):
            for filename in os.listdir(filepath):
                if os.path.isdir(filename):
                    self.decryptFolder(filename)
                else:
                    ext = os.path.splitext(filename)[1]
                    if ext == Settings.EncryptedExtension:
                        self.decryptFile(os.path.join(filepath,filename))
        else:
            self.decryptFile(filepath)
            
    def encryptFile(self, in_filename, out_filename=None, chunksize=64 * 1024):
        if not out_filename:
            out_filename = in_filename + Settings.EncryptedExtension

        # Inizializzazione
        iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
        encryptor = AES.new(self.key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(in_filename)

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)

                # Cifratura
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' ' * (16 - len(chunk) % 16)

                    outfile.write(encryptor.encrypt(chunk))
        #Rimozione file originale
        infile.close()
        outfile.close()
        os.unlink(in_filename)

    def decryptFile(self,in_filename, out_filename=None, chunksize=24 * 1024):
        if not out_filename:
            out_filename = os.path.splitext(in_filename)[0]+".dec"

        with open(in_filename, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(self.key, AES.MODE_CBC, iv)

            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))

                outfile.truncate(origsize)

            infile.close()
            outfile.close()