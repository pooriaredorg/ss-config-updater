import requests
from urllib.parse import urlparse
import os

def fetch_config(url):
    https_url = url.replace('ssconf://', 'https://')
    
    try:
        response = requests.get(https_url, timeout=10)
        if response.status_code == 200:
            return response.text.strip()
    except Exception as e:
        print(f"Error fetching {https_url}: {str(e)}")
    return None

def main():
    urls = [
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-1.csv",
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-2.csv",
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-3.csv",
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-4.csv"
    ]
    
    configs = []
    for url in urls:
        config = fetch_config(url)
        if config:
            configs.append(config)
    
    with open('configs.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(configs))

if __name__ == "__main__":
    main()
