import requests
from bs4 import BeautifulSoup
import time
import random
import hashlib
from datetime import datetime, timezone
from fake_useragent import UserAgent

class BaseScraper:
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url
        self.ua = UserAgent()

    def get_headers(self):
        return {"User-Agent": self.ua.random}

    def generate_id(self, link):
        return hashlib.md5(link.encode()).hexdigest()

    def random_sleep(self):
        time.sleep(random.uniform(1, 3))

class FLScraper(BaseScraper):
    def __init__(self):
        super().__init__("FL.ru", "https://www.fl.ru/projects/")

    def scrape(self):
        try:
            self.random_sleep()
            response = requests.get(self.base_url, headers=self.get_headers(), timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            projects = []
            # Логика поиска блоков на FL.ru
            for post in soup.find_all('div', class_='b-post'):
                title_link = post.find('a', class_='b-post__link')
                if title_link:
                    link = "https://www.fl.ru" + title_link['href']
                    projects.append({
                        "id": self.generate_id(link),
                        "title": title_link.get_text(strip=True),
                        "link": link,
                        "source": self.name
                    })
            return projects
        except Exception as e:
            print(f"Error {self.name}: {e}")
            return []

class FreelanceRuScraper(BaseScraper):
    def __init__(self):
        super().__init__("Freelance.ru", "https://freelance.ru/project/search/pro/")

    def scrape(self):
        try:
            self.random_sleep()
            response = requests.get(self.base_url, headers=self.get_headers(), timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            projects = []
            for box in soup.find_all('div', class_='project-list-item'):
                title_link = box.find('a', class_='description')
                if title_link:
                    link = "https://freelance.ru" + title_link['href']
                    projects.append({
                        "id": self.generate_id(link),
                        "title": title_link.get_text(strip=True),
                        "link": link,
                        "source": self.name
                    })
            return projects
        except Exception as e:
            print(f"Error {self.name}: {e}")
            return []

class WeblancerScraper(BaseScraper):
    def __init__(self):
        super().__init__("Weblancer", "https://www.weblancer.net/jobs/")

    def scrape(self):
        try:
            self.random_sleep()
            response = requests.get(self.base_url, headers=self.get_headers(), timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            projects = []
            for row in soup.find_all('div', class_='row-projects'):
                title_link = row.find('a', class_='project-title')
                if title_link:
                    link = "https://www.weblancer.net" + title_link['href']
                    projects.append({
                        "id": self.generate_id(link),
                        "title": title_link.get_text(strip=True),
                        "link": link,
                        "source": self.name
                    })
            return projects
        except Exception as e:
            print(f"Error {self.name}: {e}")
            return []
