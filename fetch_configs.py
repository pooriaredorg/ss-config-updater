import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

HEADERS = """//profile-title: base64:8J+lt1BPT1JJQV9SRUQo2b7Ys9ixLdii2LHbjNin24zbjCk=
//profile-update-interval: 1
//subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531
//support-url: https://t.me/BXAMbot
//profile-web-page-url: https://github.com/4n0nymou3"""

def fetch_config(url, server_number):
    https_url = url.replace('ssconf://', 'https://')
    logger.info(f"Fetching config from: {https_url}")
    
    try:
        response = requests.get(https_url, timeout=10)
        response.raise_for_status()
        content = response.text.strip()
        if content.startswith('ss://'):
            content = f"{content}#Server-{server_number}"
            logger.info(f"Successfully fetched config from {https_url} and added server number")
            return content
        else:
            logger.error(f"Invalid config format from {https_url}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching {https_url}: {str(e)}")
        return None

def main():
    logger.info("Starting config fetch process")

    urls = [
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-1.csv",
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-2.csv",
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-3.csv",
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-4.csv"
    ]

    configs = []
    for index, url in enumerate(urls, 1):
        logger.info(f"Processing URL: {url}")
        config = fetch_config(url, index)
        if config:
            configs.append(config)
    
    if not configs:
        logger.error("No configs were successfully fetched!")
        exit(1)

    try:
        with open('configs.txt', 'w', encoding='utf-8') as f:
            f.write(HEADERS)
            f.write('\n\n')
            f.write('\n\n'.join(configs))
        logger.info(f"Successfully wrote {len(configs)} configs to configs.txt with headers")
    except Exception as e:
        logger.error(f"Error writing to file: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
