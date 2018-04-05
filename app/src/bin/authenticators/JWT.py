import hashlib
import base64
import hmac

class JWT():
    def __init__(self, secret):
        self.secret = secret

    def _hash(self, msg):
        return base64.urlsafe_b64encode(hmac.new(self.secret, msg, hashlib.sha256).digest())

    def _compare(self, msg, hash_str):
        x = str(self._hash(msg))
        y = str(hash_str)
        print (x, y)
        if len(x) != len(y):
            return False
        return x == y

    def encode(self, payload):
        header = base64.urlsafe_b64encode(json.dumps({ 'typ': 'JWT', 'alg': 'SHA256' }))
        payload = base64.urlsafe_b64encode(json.dumps(payload))
        signature = self._hash(header + '.' + payload)
        return header + '.' + payload + '.' + signature

    def decode(self, token):
        header, payload, signature = token.split('.')
        if self._compare(header + '.' + payload, signature):
            return json.loads(base64.urlsafe_b64decode(str(payload)))
        return None
