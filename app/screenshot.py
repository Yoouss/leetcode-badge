from playwright.sync_api import sync_playwright
import time

def waiting_for_the_website_to_load(page, refresh=360, refresh_cooldown=15) :
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
        refresh_count += 1
        print("Loading the website... Next refresh in {} seconds... ({} refresh/{})".format(refresh_cooldown, refresh_count, refresh))
        badge = page.query_selector("div.badge")
        time.sleep(refresh_cooldown)

    if badge :
        print("Website successfully loaded !")
    else :
        print("Failed to load the website :(")

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
        page.goto(url)

        badge = waiting_for_the_website_to_load(page)

        if badge :
            badge.screenshot(path=output_file)
            print("Screenshot saved as {} - Job succeed :)".format(output_file))
        else:
            print("Something went wrong... if the website loaded, Maybe the API isn't working or the website has some issues :(")
        browser.close()

if __name__ == "__main__" :
    capture_badge()
