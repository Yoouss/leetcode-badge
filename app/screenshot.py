from playwright.sync_api import sync_playwright
import time
import os

def waking_up_the_website(page, url, request_cooldown, loading_time) :
    """
        Pre : page and url are provided by the function capture_badge()
              request_cooldown is the time in second (int) to wait before making another request to the url
              loading_time is the time in second (int) it takes to try to wake the website up
        Post : If we succeeded, we return True, otherwise False
    """
    print("The website is probably sleeping... Waiting until it wakes up...")
    for request in range(1, loading_time+1) :
        try :
            page.goto(url)
            return True
        except :
            print("Attempt {} : The website is still sleeping, {} seconds cooldown...".format(request, request_cooldown))
            time.sleep(request_cooldown)
    return False
            
        
def capture_badge(url="https://leetcode-badge.onrender.com/", output_file="app/static/badge.png") :
    """
        Pre : url is the website where the LeetCode badge is heberged
              => I used Render so the website can be in a sleeping mode if there aren't visitors (I anticiped this case)
              output_file is the emplacement and name the screenshot will have
        Post : If we succeeded, the screenshot will be taken, otherwise it won't
    """
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        try :
            page.goto(url)
        except :
            if not waking_up_the_website(page, url, 60, 90) :
                print("Failed to wake the website up... screenshot failed")
                browser.close()
                return

        badge = page.query_selector("div.badge")
        if badge:
            if os.path.exists(output_file): # We delete the previous screenshot if there's one
                os.remove(output_file)
            badge.screenshot(path=output_file)
            print(f"Screenshot saved as {output_file}")
        else:
            print("Something went wrong... Maybe the API isn't working :(")
        browser.close()

if __name__ == "__main__" :
    capture_badge()
