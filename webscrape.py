# check how many times a class of html tag with the tag value is found in the html
def check_html_tag_count(url, element, tag, tag_value):
    import requests
    from bs4 import BeautifulSoup
    # get the html
    html = requests.get(url)
    # parse the html
    soup = BeautifulSoup(html.text, 'html.parser')
    # find the tag
    tag = soup.find_all(element, {tag: tag_value})
    # return the tag
    return len(tag)

url = 'https://fbref.com/en/matches/81074285/Hellas-Verona-Sassuolo-August-21-2021-Serie-A'
test = check_html_tag_count('https://fbref.com/en/matches/81074285/Hellas-Verona-Sassuolo-August-21-2021-Serie-A', 'tr', 'data-row', '0')
print(test)