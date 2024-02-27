"""
Server status checker
"""
import requests

class WebsiteChecker:
    def __init__(self, url):
        self.url = url
        self.status = {
            200: "Website is operational",
            301: "Permanent Redirect",
            404: "Website not found",
            500: "Internal Server Error"
        }

    def get_url(self):
        return self.url
    
    def set_url(self, url):
        self.url = url
        return self.url

    def check_url(self):
        try:
            web_response = requests.get(self.url)
            return (self.url, self.status[web_response.status_code])
        except Exception as e:
            return (f"Error checking {self.url}: {e}")

if __name__ == "__main__":
    url = input("Please enter the URL of the website you want to check")
    checker = WebsiteChecker(url)
    print(checker.check_url())

    