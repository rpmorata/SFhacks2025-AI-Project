import os
import re
import time
import argparse
from urllib.parse import urlparse, parse_qs, urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import requests

def extract_dataset_name(url):
    """Extract dataset name from Roboflow URL."""
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')
    
    # Find the dataset name in the URL path
    for part in path_parts:
        if part and not part.startswith('browse') and not part.startswith('universe'):
            return part
    
    return "roboflow_dataset"  # Default name if not found

def create_folder(folder_name):
    """Create a folder if it doesn't exist."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def download_image(url, folder_path):
    """Download an image from URL and save it to the specified folder."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://universe.roboflow.com/',
        }
        response = requests.get(url, stream=True, headers=headers)
        if response.status_code == 200:
            # Extract filename from URL or use a timestamp
            filename = url.split('/')[-1]
            if not filename or '?' in filename:
                filename = f"image_{int(time.time())}.jpg"
            
            # Clean up filename to only keep the extension
            if '.' in filename:
                ext = filename.split('.')[-1].lower()
                if ext in ['png', 'jpg', 'jpeg']:
                    filename = f"image_{int(time.time())}.{ext}"
                else:
                    filename = f"image_{int(time.time())}.jpg"
            else:
                filename = f"image_{int(time.time())}.jpg"
            
            file_path = os.path.join(folder_path, filename)
            
            # Save the image
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Downloaded: {filename}")
            return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
    return False

def download_roboflow_images(url):
    """Main function to download images from Roboflow dataset using Selenium."""
    # Extract dataset name and create folder
    dataset_name = extract_dataset_name(url)
    folder_path = create_folder("../dataset/" + dataset_name)
    print(f"Created folder: {folder_path}")
    
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Navigate to the URL
        print(f"Navigating to {url}...")
        driver.get(url)
        
        # Wait for the page to load
        time.sleep(5)  # Give the page time to load
        
        # Initialize variables for pagination
        total_downloaded = 0
        page = 1
        
        while True:
            print(f"Processing page {page}...")
            
            # Wait for images to load
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "img"))
                )
            except TimeoutException:
                print("Timeout waiting for images to load. Trying to continue...")
            
            # Scroll down to load all images
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for images to load after scrolling
            
            # Find all image elements
            image_elements = driver.find_elements(By.TAG_NAME, "img")
            
            # Filter and download images
            page_downloaded = 0
            for img in image_elements:
                src = img.get_attribute("src")
                if src:
                    # Check if it's an image file
                    if any(src.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
                        if download_image(src, folder_path):
                            page_downloaded += 1
                            total_downloaded += 1
            
            print(f"Downloaded {page_downloaded} images from page {page}.")
            
            # If we didn't find any images on this page, we're probably done
            if page_downloaded == 0:
                print("No more images found on this page.")
                break
            
            # Try to click the "Next" button if it exists
            try:
                next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next') or contains(@class, 'next')]")
                if next_button.is_enabled():
                    next_button.click()
                    page += 1
                    time.sleep(3)  # Wait for the next page to load
                else:
                    print("Next button is disabled. Reached the last page.")
                    break
            except NoSuchElementException:
                print("No next button found. Reached the last page.")
                break
        
        print(f"\nDownload complete! Downloaded {total_downloaded} images to {folder_path}")
        
    except Exception as e:
        print(f"Error processing URL: {str(e)}")
    finally:
        # Close the browser
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Download images from a Roboflow dataset URL')
    parser.add_argument('url', nargs='?', help='The Roboflow dataset URL')
    args = parser.parse_args()
    
    # Get URL from command line argument or prompt if not provided
    url = args.url
    if not url:
        url = input("Enter the Roboflow dataset URL: ")
    
    download_roboflow_images(url) 