import jwt
from src.utils.utils import getEnv

class Auth:
    def decodeToken(self, token):
        return jwt.decode(token, self.getSecretKey(),algorithms=['HS256'])

    def generateToken(self, data):
        key = self.getSecretKey()
        return jwt.encode(data,key,algorithm="HS256")

    def getSecretKey(self):
        return getEnv('secretkey')


