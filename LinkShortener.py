class LinkShortener:
    # The id used here is required to map the shortened urls. In our case, we will
    # maintain a dictionary to store url and their corresponding shortened url
    def __init__(self):
        self.url_id = 10000000000 # setting the initial id for the first url
        self.url = {}             # dict {url: encoded_id} for encoding
        self.decoder_url = {}     # dict {id: url} for decoding
        self.base62_char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # base62 conversion string

    def shorten_url(self, current_url):
        if current_url in self.url:
            shortened_url =  self.url[current_url]
        else:
            self.decoder_url[self.url_id] = current_url
            shortened_url = self.base62_encoder(self.url_id)
            self.url[current_url] = shortened_url
            self.url_id += 1

        return "https://link-short-light.herokuapp.com/" + shortened_url

    # we apply base 62 encoding so we can compress base10 to base62
    # base62 supports 56800 times more url than base10
    def base62_encoder(self, _id):
        base = len(self.base62_char)
        result_list = []
        while _id>0:
            val = _id%base
            result_list.append(self.base62_char[val])
            _id = int(_id/base)
        # reverse the final result before returning it
        return "".join(result_list[::-1])

    def base62_decoder(self, _id):
        decoder_id = 0
        k = len(_id) - 1 # k represents the exponent for 62 in terms of index (Ex: 62 ** 2)
        for i in _id:
            if(i in "0123456789"):
                decoder_id += int(i) * pow(62, k)
            else:
                index = self.base62_char.index(i)
                decoder_id += int(index) * pow(62, k)
            k -= 1
        return self.decoder_url[decoder_id]
    
