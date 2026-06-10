import json
import random
import time
import os
import csv

class Url:
    
    def __init__(self, long_url):
        self.long_url = long_url
        self.short_code = None
        self.visit_counter = None
        self.created_at = time.ctime()
        
    def store_data(self):
        '''Saves the long_url, short_code, created_at in a dictionary'''
        data = {
            "long_url": self.long_url,
            "short_code": self.short_code,
            "created_at": self.created_at
        }
        return data

    def visit(self):
        '''implements thenotion of clicking on the url'''
        self.visit_counter = 0
        while True:
            user_response = input("Do you want to visit the short URL?(yes/no): ").strip().lower()
            if user_response in ("yes", "no"):
                break
        if user_response == "yes":
            self.visit_counter += 1
            return self.visit_counter
        else:
            return
        
    def most_clicked(self, url):
        '''Stores the click counter with its long url in a csv file'''
        if not self.visit():
            report_data = []
            if os.path.exists("clicked_report.csv"):
                with open("clicked_report.csv") as data_file:
                    reader = csv.DictReader(data_file)
                    for row in reader:
                        report_data.append(row)
                for row_data in report_data:
                    if row_data['url'].strip() == url:
                        row_data['clicks'] = str(int(row_data['clicks']) + 1)
                with open("clicked_report.csv", "w", newline = "") as edit_file:
                    file_writer = csv.DictWriter(edit_file, fieldnames = ["url", "clicks"], lineterminator = "\n")
                    file_writer.writeheader()
                    file_writer.writerows(report_data)
                return
            with open("clicked_report.csv", "a", newline = "") as report_file:
                writer = csv.DictWriter(report_file, fieldnames = ["url", "clicks"], lineterminator = "\n")
                writer.writeheader()
                writer.writerow({"url": url, "clicks": self.visit_counter})
        

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
                self.visit()
                self.most_clicked(self.long_url)
                return 

        self.generate_code()
        print(f"bit.ly/{self.short_code}")
        self.visit()
        self.most_clicked(self.long_url)
        #Save to file
        data[self.short_code] = self.store_data()
        store_urls(data)



def main():
    while True:
        user_input = input("Enter URL: ").strip()
        if user_input.startswith("https://") or user_input.startswith("http://"):
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