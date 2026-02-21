from flask import Flask, jsonify
from concurrent.futures import ThreadPoolExecutor
from scrapers import FLScraper, FreelanceRuScraper, WeblancerScraper
import os

app = Flask(__name__)

# Initialize scrapers once
scrapers = [
    FLScraper(),
    FreelanceRuScraper(),
    WeblancerScraper()
]

@app.route('/', methods=['GET'])
def index():
    return 'OK'

@app.route('/get_all', methods=['GET'])
def get_all():
    results = []
    # Use ThreadPoolExecutor to run scrapers concurrently
    with ThreadPoolExecutor(max_workers=len(scrapers)) as executor:
        future_to_scraper = {executor.submit(s.scrape): s for s in scrapers}
        for future in future_to_scraper:
            try:
                data = future.result()
                if data:
                    results.extend(data)
            except Exception as e:
                print(f"Scraper {future_to_scraper[future].name} failed: {e}")
    
    return jsonify(results)

if __name__ == "__main__":
    # Render сам назначит порт через переменную окружения PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
