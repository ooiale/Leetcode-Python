'''
  use a hashMap to encode/decode the urls. so start with a baseUrl and append to it the encoded string. in this case we are encoding by the length of the encodeMap hashMap. if we limit ourselves to 5 digits max in the tinyUrl this grants us 10^5 different urls. if we want more we could for example add chars to it resulting in  62^5 different urls
'''

class Codec:
    def __init__(self):
        self.base = "http://tinyurl.com/"
        self.encodeMap = {} #longUrl => shortUrl
        self.decodeMap = {} #shortUrl => longUrl

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeMap:
            shortUrl = self.base + str(len(self.encodeMap))
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        
        return self.encodeMap[longUrl]        

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))