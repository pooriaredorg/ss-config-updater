import requests
from urllib.parse import urlparse
import os
import sys
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def fetch_config(url):
    # Convert ssconf:// to https://
    https_url = url.replace('ssconf://', 'https://')
    logger.info(f"Fetching config from: {https_url}")
    
    try:
        response = requests.get(https_url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        content = response.text.strip()
        if content.startswith('ss://'):
            logger.info(f"Successfully fetched config from {https_url}")
            return content
        else:
            logger.error(f"Invalid config format from {https_url}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching {https_url}: {str(e)}")
        return None

def main():
    logger.info("Starting config fetch process")
    
    # List of config URLs
    urls = [
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-1.csv",
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-2.csv",
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-3.csv",
        "ssconf://ainita.s3.eu-north-1.amazonaws.com/AinitaServer-4.csv"
    ]
    
    # Fetch and store configs
    configs = []
    for url in urls:
        logger.info(f"Processing URL: {url}")
        config = fetch_config(url)
        if config:
            configs.append(config)
    
    if not configs:
        logger.error("No configs were successfully fetched!")
        sys.exit(1)
    
    # Write configs to file
    try:
        with open('configs.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(configs))
        logger.info(f"Successfully wrote {len(configs)} configs to configs.txt")
    except Exception as e:
        logger.error(f"Error writing to file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()