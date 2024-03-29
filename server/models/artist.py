import json

class Artist:
    def __init__(self, url, name, image, num_followers, genres):
        self.url = url
        self.name = name
        self.image = image
        self.num_followers = num_followers
        self.genres = genres
    
    def to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))