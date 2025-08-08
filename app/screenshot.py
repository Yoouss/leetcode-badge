from playwright.sync_api import sync_playwright

def capture_badge(url="http://127.0.0.1:5000/", output_file="badge_screenshot.png"):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        badge = page.query_selector("div.badge")
        if badge:
            badge.screenshot(path=output_file)
            print(f"Screenshot saved as {output_file}")
        else:
            print("Something went wrong... Maybe the API isn't working :(")
        browser.close()

if __name__ == "__main__" :
    capture_badge()