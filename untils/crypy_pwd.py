import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES,PKCS1_v1_5

class CryptPwd:
    # 用于加密和解密
    def __init__(self):
        self.key = "juren"
        self.mode = AES.MODE_ECB

    @staticmethod
    def add_to_16(value):
        while len(value) % 16 != 0:
            value +='\n'
        return value.encode('utf-8')

    def encrypt_pwd(self,pwd):
        # 对密码进行加密
        # param pwd:密码
        # retuen 加密后的密码
        # type pwd: str
        # rtype :str
        aes = AES.new(self.add_to_16(self.key),self.mode)
        encrypt_aes = aes.encrypt(self.add_to_16(pwd))
        encrypt_pwd = str(base64.b64encode(encrypt_aes),encoding='utf-8')
        return encrypt_pwd

    def decrypt_pwd(self,):
