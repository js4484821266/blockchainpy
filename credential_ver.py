from Crypto.PublicKey import RSA
if __name__ == '__main__':
    with open('public.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())
    with open('private.pem', 'rb') as f:
        private_key = RSA.import_key(f.read(), passphrase=input('Enter passphrase: '))
    print(public_key.export_key().decode())
    print(private_key.export_key().decode())