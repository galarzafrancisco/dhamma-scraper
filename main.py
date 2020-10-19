# ========================================
#
# Definitions
#
# ========================================

url = 'https://www.dhamma.org/en/schedules/schbhumi'
lookup_location = 'Blackheath'
lookup_dates = '27 Jan - 07 Feb' # test
# lookup_dates = '09 Feb - 20 Feb'
sleep_period = 10 # Time in seconds between pings



# ========================================
#
# Imports
#
# ========================================

# Parsing
import requests
from bs4 import BeautifulSoup

# General
import os, time
from datetime import datetime




def get_row_text(lookup_dates, lookup_location):
    '''
    Function to scrape the website.
    Looks for rows with the dates & location defined above (ie: '27 Jan - 07 Feb' and 'Blackheath')
    and returns the text of the row
    '''
    # Ping the url
    response = requests.get(url)

    # Parse the HTML response
    html = response.content
    soup = BeautifulSoup(html, features='html.parser')

    # Find the row we're interested on
    rows = [row.text.replace('\n', ' ') for row in soup.findAll('tr')]
    rows = [row for row in rows if lookup_dates in row and lookup_location in row]
    row_text = rows[0]

    return row_text




if __name__ == '__main__':
    '''
    This is the main function. This gets executed when you run 'python main.py'
    '''

    # Get the first response from the website
    text = get_row_text(lookup_dates, lookup_location)

    # Loop forever
    while True:
        # Sleep to avoid pinging the url too frequently
        time.sleep(sleep_period)
        ping_timestamp = datetime.now()
        # Check the website again
        new_text = get_row_text(lookup_dates, lookup_location)
        
        # Check if the application is open or not. Proxy for this is the text 'applications accepted starting...'
        if 'applications accepted starting' in new_text.lower():
            status = 'closed'
        else:
            status = '>>> OPEN!!! <<<'
        
        # Check if the website has changed since the last time. This may be an indication that the applications are now open.
        if new_text == text:
            print("{} - {} - Website hasn't changed".format(ping_timestamp, status))
        else:
            print('\n\n\n----------------------------------\n')
            print("{} - {} - Website has changed!!!!".format(ping_timestamp, status))
            print(new_text)
            text = new_text
            print('\n----------------------------------\n')
            with open('log.txt', 'a') as f:
                ping_timestamp = datetime.now()
                f.write("{} - Website has changed!!!!\n".format(ping_timestamp))

