import time
import random
import hashlib
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from urllib.parse import urljoin
import requests
from fake_useragent import UserAgent

class BaseScraper(ABC):
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url
        self.ua = UserAgent()
        self.session = requests.Session()

    def get_headers(self):
        return {
            'User-Agent': self.ua.random,
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': self.base_url
        }

    def random_sleep(self):
        time.sleep(random.uniform(0.5, 2.0))

    def generate_id(self, link):
        return hashlib.md5(link.encode()).hexdigest()

    @abstractmethod
    def scrape(self):
        pass

class FLScraper(BaseScraper):
    def __init__(self):
        super().__init__("FL.ru", "https://www.fl.ru")

    def scrape(self):
        try:
            self.random_sleep()
            # Placeholder for actual parsing logic
            # In a real scenario, we would parse the HTML here
            return [{
                "id": self.generate_id("https://www.fl.ru/projects/1"),
                "title": "Example Project on FL.ru",
                "link": "https://www.fl.ru/projects/1",
                "description": "This is a placeholder description.",
                "source": self.name,
                "timestamp": datetime.now(timezone.utc).isoformat()
            }]
        except Exception as e:
            print(f"Error scraping {self.name}: {e}")
            return []

class FreelanceRuScraper(BaseScraper):
    def __init__(self):
        super().__init__("Freelance.ru", "https://freelance.ru")

    def scrape(self):
        try:
            self.random_sleep()
            return [{
                "id": self.generate_id("https://freelance.ru/projects/2"),
                "title": "Example Project on Freelance.ru",
                "link": "https://freelance.ru/projects/2",
                "description": "Another placeholder description.",
                "source": self.name,
                "timestamp": datetime.now(timezone.utc).isoformat()
            }]
        except Exception as e:
            print(f"Error scraping {self.name}: {e}")
            return []

class WeblancerScraper(BaseScraper):
    def __init__(self):
        super().__init__("Weblancer", "https://www.weblancer.net")

    def scrape(self):
        try:
            self.random_sleep()
            return [{
                "id": self.generate_id("https://www.weblancer.net/projects/3"),
                "title": "Example Project on Weblancer",
                "link": "https://www.weblancer.net/projects/3",
                "description": "Final placeholder description.",
                "source": self.name,
                "timestamp": datetime.now(timezone.utc).isoformat()
            }]
        except Exception as e:
            print(f"Error scraping {self.name}: {e}")
            return []
