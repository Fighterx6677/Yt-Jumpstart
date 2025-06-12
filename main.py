from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import traceback
import os
import tempfile

VIDEO_URL = "https://www.youtube.com/shorts/5VD1KjZ9cs0"

def watch_video():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124")
    temp_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_dir}")

    while True:
        driver = None
        try:
            print("Attempting to initialize ChromeDriver...")
            driver = webdriver.Chrome(options=options)
            print("ChromeDriver initialized successfully")
            try:
                driver.get(VIDEO_URL)
                print(f"Watching: {driver.title}")
                time.sleep(60)
                driver.refresh()
            finally:
                if driver:
                    driver.quit()
                    print("ChromeDriver closed")
        except Exception as e:
            print(f"Setup Error: {e}")
            print(traceback.format_exc())
            if driver:
                driver.quit()
                print("ChromeDriver closed after error")
        finally:
            try:
                os.rmdir(temp_dir)
            except:
                pass
            time.sleep(300)

if __name__ == "__main__":
    watch_video()
