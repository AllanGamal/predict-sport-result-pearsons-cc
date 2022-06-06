# check how many times a class of html tag with the tag value is found in the html
# function that checks a website for a specific class of html tag

# find the player stats table for the specific team
from calendar import c


def team_stats_table(tags, team):# find the spicific player stats table for the specific team
    table_tag = ''
    
    for tag in tags: 
        if team + ' Player Stats Table' in str(tag): 
            table_tag = tag
            print(table_tag)
            break
    return table_tag

def n_rows(children): # find the number of rows in the table
    count = 0
    for child in children:
        count += 1
    return count
    

def check_html_tag(url, element, tag, team, row):
    import requests
    from bs4 import BeautifulSoup
    # get the html
    html = requests.get(url)
    # parse the html
    soup = BeautifulSoup(html.text, 'html.parser')
    # find the tag
    tags = soup.findAll(element)
    
    # find the player stats table for the specific team
    caption_tag = team_stats_table(tags, team) 
    table_tag = caption_tag.findNext('tbody') 
    

    player = table_tag.findChildren("tr")
    player = player[row:row+1]
    n_players = n_rows(player) # find the number of players in the table of a team
    # go to the third row of children

    minutes = int(soup.select('td[data-stat="minutes"]')[row].text) # find the minutes of a player
    name = soup.select('th[csk]')[row].get('csk') # find the name of a player

    
    
    if minutes < 75:
        # return the tag value of children
        return name
        
    else:
        return 0
    

url = 'https://fbref.com/en/matches/81074285/Hellas-Verona-Sassuolo-August-21-2021-Serie-A'

tag_string = check_html_tag(url, 'caption', 'data-label', 'Hellas Verona', 0)
print(tag_string)


