import json
import random
import time
import os

class Url:
    
    def __init__(self, long_url):
        self.long_url = long_url
        self.short_code = None
        self.created_at = time.ctime()
        
    def store_data(self):
        '''Saves the long_url, short_code, created_at in a dictionary'''
        data = {
            "long_url": self.long_url,
            "short_code": self.short_code,
            "created_at": self.created_at
        }
        return data

    def generate_code(self):
        urls = retrieve_urls()
        ls = "abcdefghijklmnopqrstuvwxyz0123456789"
        while True:
            code = "" 
            for _ in range(6):
                code += random.choice(ls)
            if code not in urls:
                self.short_code = code
                return self.short_code
    
    def shorten_url(self):
        data = retrieve_urls()
        for code,info in data.items():
            if info['long_url'] == self.long_url:
                self.short_code = info['short_code']
                print(f"URL already exists: bit.ly/{self.short_code}")
                return 

        self.generate_code()
        print(f"bit.ly/{self.short_code}")
        #Save to file
        data[self.short_code] = self.store_data()
        store_urls(data)



def main():
    while True:
        user_input = input("Enter URL: ").strip()
        if user_input in ("https://", "http://"):
            break
    url = Url(user_input)
    url.shorten_url()
    


def store_urls(url_data):
    with open("urls.json", "w") as file:
        json.dump(url_data, file, indent = 4)

def retrieve_urls():
    if os.path.exists("urls.json"):
        with open("urls.json") as urls_file:
            return json.load(urls_file)
    else:
        return {}


if __name__ == "__main__":
    main()