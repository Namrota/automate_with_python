'''
Website Screenshot Tool:

Captures full-page screenshot of an URL using the Playwright browser automation library.

WHAT TO FIGURE OUT:
- How do you automate a web browser with Python?
- How do you take screenshots programmatically?
- How do you wait for a page to fully load?
- How do you generate unique filenames with timestamps?
- How do you extract domain names from URLs?

Steps:
First, get the URL from the user and add https:// if needed.
Then launch a headless browser and navigate to the URL.
Finally, take a full-page screenshot and save it.

Information:
Playwright automates real browsers (Chrome/Firefox/Safari).
Use sync_playwright() to create a browser automation context.
browser.new_page() creates a new browser tab.
page.goto() navigates to a URL.
page.screenshot() captures the page as an image.
full_page=True captures the entire scrollable page.

'''

# Import necessary libraries
# playwright for browser automation, datetime for timestamps, and re for URL parsing

from playwright.sync_api import sync_playwright
from datetime import datetime
from urllib.parse import urlparse

# Print header
print("====Website Screenshot Tool==== \n")

# Get URL input from the use
website= input("Enter website URL: ")

# Add https:// if the URL doesn't start with it
'''
startswith() method returns True if the string starts with the specified prefix, otherwise False.
# string.startswith(value, start, end)
# value: Required. The value to check if the string starts with it
    # This value parameter can also be a tuple,
    # then the method returns true if the string starts with any of the tuple values.
# start and end is Optional, they specify the at which position to start and end the search.
    # Default is 0 and len(string) respectively.
 
'''
if not website.startswith("https://"):
	website = "https://" + website
	
# Extract domain name for filename using regex
parsed= urlparse(website)
domain= parsed.netloc
filename= domain.replace(".", "_")

#Create a timestamp for the filename to make it unique
dt= datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
# Create a filename
filename = f"{filename}_{dt}.png"
# Saving file to a dedicated folder
filename = f"screenshots/{filename}"

# Print status message
print(f"Taking screenshot of {website} and saving as {filename}")

# Launch browser and take screenshot
# (use sync_playwright context manager)
    # Launch Chromium browser for headless mode
    # Create a new page with viewport size
    # Navigate to the URL and wait until the page is fully loaded
    # Take a full-page screenshot and save it with the generated filename
    # Close the browser
'''
goto:
Returns the main resource response. In case of multiple redirects, the navigation will resolve with the first non-redirect response.

The method will not throw an error when any valid HTTP status code is returned by the remote server,
including 404 "Not Found" and 500 "Internal Server Error".
'''
with sync_playwright() as playwright:
    chrome= playwright.chromium
    browser = chrome.launch(headless=True)
    '''
    Browser.new_page:Creates a new page in a new browser context. Closing this page will close the context as well.
    After we instantiate the browser, we create a new page (tab) in the browser.
    We can also specify the viewport size for the page, which determines the dimensions of the screenshot.

    goto() method tells the browser to navigate to the specified URL.
    In case of multiple redirects, it returns the final non-direct response.
    -> wait_until parameter specifies when the navigation is considered finished.
    -> wait_until : Union["commit", "domcontentloaded", "load", "networkidle", None]
    networkidle means that there are no network connections for at least 500 ms. This is best suited for:
    - SPAs (Single Page Applications) that load content dynamically.
    - Pages with heavy AJAX requests that may continue after the initial load.

    '''
    page = browser.new_page(viewport={"width": 1280, "height": 1080})
    page.goto(website, wait_until="networkidle")
    page.screenshot(path=filename, full_page=True)
    browser.close()

# Print success message with filename

print(f"Screenshot saved as {filename} successfully!")
