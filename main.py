from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import traceback

VIDEO_URL = "https://www.youtube.com/shorts/5VD1KjZ9cs0"

def watch_video():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124")

    while True:
        driver = None
        try:
            print("Attempting to initialize ChromeDriver...")
            driver = webdriver.Chrome(options=options)
            print("ChromeDriver initialized successfully")
            try:
                driver.get(VIDEO_URL)
                print(f"Watching: {driver.title}")
                time.sleep(5)  # Wait for page load
                # Simulate user interaction (scrolling)
                ActionChains(driver).move_by_offset(0, 500).perform()
                # Watch for a random duration (mimicking user behavior)
                watch_duration = random.uniform(30, 60)
                print(f"Watching for {watch_duration:.2f} seconds")
                time.sleep(watch_duration)
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
            time.sleep(300)  # Wait before retrying

if __name__ == "__main__":
    watch_video()
