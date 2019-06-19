import json

def retrieve_ranked_elements(browser):
    """
    Extracts div elements for ranked submissions
    from a selenium browser. Skips adverts and announcements.

    Parameters:
    ---
    broswer: selenium.webdriver object eg. selenium.webdriver.chrome.webdriver.WebDriver

    Returns:
    ---
    List of selenium elements - - selenium.webdriver.remote.webelement.WebElement object
    """
    wildcard_sel = '//*[contains(@id, "thing")]'
    els = browser.find_elements_by_xpath(wildcard_sel)
        # If the element doesn't have a data-rank we want to skip it
    ranked_elements = [el for el in els if el.get_attribute('data-rank')]
    return ranked_elements

def retrieve_submissions_data(element):
    """
    Extract text, and metadata for a reddit 
    submission from a web selenium web element.
    Returns a dictionary for storage in json.
    Parameters:
    ---
    element: selenium.webdriver.remote.webelement.WebElement object

    Returns:
    ---
    dict(
        'text':text,
        'age': age,
        'timestamp': timestamp,
        'score': score,
        'num_comments': num_comments)
    """
    title_sel = 'a.title.may-blank.outbound'
    time_sel = 'time.live-timestamp'
    title_element = element.find_element_by_css_selector(title_sel)      
    time_element = element.find_element_by_css_selector(time_sel)        
    data = {}
    data['text'] = title_element.text  
    data['age'] = time_element.text
    data['timestamp'] = time_element.get_attribute('title')
    data['score'] = element.get_attribute('data-score')
    data['num_comments'] = element.get_attribute('data-comments-count')
    return data

def store_page_to_json(browser, fp):
    """
    Transfer submission data + metadata on a reddit(old.reddit) page to json.
    Input args: selenium browser and filepath. Returns: None. 

    Parameters:
    ---
    broswer: selenium.webdriver object eg. selenium.webdriver.chrome.webdriver.WebDriver
    fp: opened file object - - <_io.TextIOWrapper name='test.json' mode='r' encoding='UTF-8'>
    """
    submission_elements = retrieve_ranked_elements(browser=browser)
    for element in submission_elements:
        data = retrieve_submissions_data(element)
        json.dump(data, fp)
        fp.write('\n') 

def go_back(browser):
    """
    Go to the previous page. There is not an archive for every 
    day of old.reddit.com/r/worldnews 
    but its okay, we just need to get enough datapoints.

    Parameters:
    ---
    broswer: selenium.webdriver object eg. selenium.webdriver.chrome.webdriver.WebDriver
    """
    shadow_section = browser.execute_script(
    '''return document.querySelector("div").shadowRoot''')
    #nav_buttons = browser.find_elements_by_css_selector(sel)
    #prev_button = nav_buttons[1]
    prev_button = shadow_section.find_element_by_css_selector(
    ('#wm-ipp-inside > div:nth-child(1) > table > tbody > tr:nth-child(1)'
    ' > td.n > table > tbody > tr.d > td.b > a'))
    prev_button.click()