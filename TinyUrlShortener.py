# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
import string
class Codec:
    alphabet = string.ascii_letters + '0123456789'
    BASE_URL = "http://tinyurl.com/"
    urlDict = {}
    CODE_LENGTH = 6
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while True:
            # Generate code
            code = ''.join(random.choice(self.alphabet) for i in range(self.CODE_LENGTH))
            if code not in self.urlDict:
                self.urlDict[code] = longUrl
                break
        return self.BASE_URL + code
            

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[len(self.BASE_URL)::]
        return self.urlDict[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))