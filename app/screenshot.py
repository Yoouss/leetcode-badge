from playwright.sync_api import sync_playwright
import time
import os

def waking_up_the_website(browser, url, request_cooldown=60, loading_time=90) :
    """
        Pre : browser and url are provided by the function capture_badge()
              request_cooldown is the time in second (int) to wait before making another request to the url
              loading_time is the time in second (int) it takes to try to wake the website up
        Post : If we succeeded, we return the page, otherwise False
    """
    print("The website is probably sleeping... Waiting until it wakes up...")
    for request in range(1, loading_time+1) :
        try :
            page = browser.new_page()
            page.goto(url)
            return page
        except :
            print("Attempt {} : The website is still sleeping, {} seconds cooldown...".format(request, request_cooldown))
            page.close()
            time.sleep(request_cooldown)
    return False

def waiting_for_the_webite_to_load(page, refresh=360, refresh_cooldown=15) :
    """
        Pre : page is provided by the function capture_badge()
              refresh is the number of time we'll refresh the page (int)
              refresh_cooldown is the time in second (int) before refreshing the page
        Post : in both scenario, we return bagde, however badge can be "True" or False
    """
    badge = page.query_selector("div.badge")
    refresh_count = 0
    while not badge and refresh_count < refresh : # We keep trying for max 1h30
        page.reload()
        badge = page.query_selector("div.badge")
        time.sleep(refresh_cooldown)
        refresh_count += 1
    return badge   
        
def capture_badge(url="https://leetcode-badge.onrender.com/", output_file="app/static/badge.png") :
    """
        Pre : url is the website where the LeetCode badge is hosted
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
            page.close()
            page = waking_up_the_website(browser, url)
            if page == False :
                print("Failed to wake the website up... screenshot failed")
                browser.close()
                return

        badge = waiting_for_the_webite_to_load(page)

        if badge :
            if os.path.exists(output_file) :
                os.remove(output_file)
            badge.screenshot(path=output_file)
            print(f"Screenshot saved as {output_file}")
        else:
            print("Something went wrong... Maybe the API isn't working or the website has some issues :(")
        browser.close()

if __name__ == "__main__" :
    capture_badge()
