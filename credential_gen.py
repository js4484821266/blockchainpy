from Crypto.PublicKey import RSA
r = RSA.generate(2048)
if __name__ == '__main__':
    with open('public.pem', 'wb') as f:
        f.write(r.publickey().export_key())
    with open('private.pem', 'wb') as f:
        f.write(r.export_key(
            pkcs=8,
            protection='PBKDF2WithHMAC-SHA1AndAES256-CBC',
            passphrase=input('Enter passphrase: ')
        ))