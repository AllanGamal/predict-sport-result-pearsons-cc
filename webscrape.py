# check how many times a class of html tag with the tag value is found in the html
# function that checks a website for a specific class of html tag
import requests
from bs4 import BeautifulSoup
# connect another py file to this one
# import objects as obj
import objects as obj 

# find the player stats table for the specific team
from calendar import c


def team_stats_table(tags, team):# find the spicific player stats table for the specific team
    table_tag = ''
    
    for tag in tags: 
        if team + ' Player Stats Table' in str(tag): 
            table_tag = tag
            break
    return table_tag



def n_rows(children): # find the number of rows in the table
    count = 0
    for child in children:
        count += 1
    return count
    

def check_html_tag(url, element, tag, team, row):
    
    # get the html
    html = requests.get(url)
    # parse the html
    soup = BeautifulSoup(html.text, 'html.parser')
    # find the tag
    tags = soup.findAll(element)
    
    # find the player stats table for the specific team
    caption_tag = team_stats_table(tags, team) 
    print(caption_tag)
    table_tag = caption_tag.findNext('tbody') 

    player = table_tag.findChildren("tr")
    player = player[row:row+1]
    

    n_players = n_rows(player) # find the number of players in the table of a team
    # go to the third row of children
    
    

    minutes = int(soup.select('td[data-stat="minutes"]')[row].text) # find the minutes of a player
    name = player[0].find('th').get('csk') # find the name of a player
    minutes = int(player[0].find_all_next('td', {"data-stat": 'minutes'})[0].text) # find the minutes of a player
    
    
    
    player_stats = soup.findAll("th", {"csk": name})
    return player_stats
    if minutes < 75:
        # return the tag value of children
        return player_stats
        
    else:
        return 0



    

url = 'https://fbref.com/en/matches/81074285/Hellas-Verona-Sassuolo-August-21-2021-Serie-A'

player_stats = check_html_tag(url, 'caption', 'NONE', 'Sassuolo', 1)
play_att_list = ['name', 'team', 'goals', 'assists', 'pens_made', 'pens_att', 'shots_total', 'shots_on_target', 'cards_yellow', 'cards_red', 'touches', 'pressures', 'tackles', 'interceptions', 'blocks', 'xg', 'npxg', 'xa', 'sca', 'gca', 'passes_completed', 'passes', 'passes_pct', 'progressive_passes', 'carries', 'progressive_carries', 'dribbles_completed', 'dribbles', 'passes_total_distance', 'passes_progressive_distance', 'passes_completed_short', 'passes_short', 'passes_pct_short', 'passes_medium', 'passes_pct_medium', 'passes_completed_medium', 'passes_completed_long', 'passes_long', 'passes_pct_long', 'assisted_shots', 'passes_into_final_third', 'passes_into_penalty_area', 'crosses_into_penalty_area', 'passes_live', 'passes_dead', 'passes_free_kicks', 'through_balls', 'passes_pressure', 'passes_switches', 'crosses', 'corner_kicks', 'corner_kicks_in', 'corner_kicks_out', 'corner_kicks_straight', 'passes_ground', 'passes_low', 'passes_high', 'passes_left_foot', 'passes_right_foot', 'passes_head', 'throw_ins', 'passes_offsides', 'passes_oob', 'passes_intercepted', 'passes_blocked', 'tackles_won', 'tackles_def_3rd', 'tackles_mid_3rd', 'tackles_att_3rd', 'dribble_tackles', 'dribbles_vs', 'dribble_tackles_pct', 'dribbled_past', 'pressure_regains', 'pressure_regain_pct', 'pressures_def_3rd', 'pressures_mid_3rd', 'pressures_att_3rd', 'blocked_shots', 'blocked_shots_saves', 'blocked_passes', 'tackles_interceptions', 'clearances', 'errors', 'touches_def_pen_area', 'touches_def_3rd', 'touches_mid_3rd', 'touches_att_3rd', 'touches_att_pen_area', 'touches_live_ball', 'dribbles_completed_pct', 'players_dribbled_past', 'nutmegs', 'carry_distance', 'carry_progressive_distance', 'carries_into_final_third', 'carries_into_penalty_area', 'miscontrols', 'dispossessed', 'pass_targets', 'passes_received', 'passes_received_pct', 'progressive_passes_received', 'cards_yellow_red', 'fouls', 'fouled', 'offsides', 'pens_won', 'pens_conceded', 'own_goals', 'ball_recoveries', 'aerials_won', 'aerials_lost', 'aerials_won_pct']
# make a function that removes every double and single quotation mark from the string and backslashes from the string

def add_object(stats_tag, list): 
    if stats_tag == 0:
        return 0
    for stat in stats_tag:
        # make an object from webscrape.py
        raw_stats = stat.parent
        name = raw_stats.find('th').get('csk')
        p1 = obj.Player(name)
        print(p1.name)
        break
    templist = list
    
    for tag in stats_tag:
        raw_stats = tag.parent
        for att in reversed(templist):
            if att in str(raw_stats):
                att_stat = raw_stats.find_all_next('td', {"data-stat": att})[0].text
                if att_stat == '':
                    att_stat = 0
                att_stat = float(att_stat)
                p1.att = att_stat
                print(p1.name)
                print(att)
                print(p1.att)
                print('\n')
                templist.remove(att)

#add_object(player_stats, play_att_list)

def check_n_players(url, element, team):
    # get the html
    html = requests.get(url)
    # parse the html
    soup = BeautifulSoup(html.text, 'html.parser')
    # find the tag
    tags = soup.findAll(element)
    
    # find the player stats table for the specific team
    caption_tag = team_stats_table(tags, team) 
    print(caption_tag)
    table_tag = caption_tag.findNext('tbody') 

    player = table_tag.findChildren("tr")
    

    n_players = n_rows(player) # find the number of players in the table of a team
    return n_players
test = check_n_players(url, 'caption', 'Sassuolo')
print(test)

def collect_game_data(stats_tag, list, url, win, loss):
    n_players = check_n_players(url, 'caption', 'Sassuolo')
    if stats_tag == 0:
        return 0
    for stat in stats_tag:
        # make an object from webscrape.py
        raw_stats = stat.parent
        name = raw_stats.find('th').get('csk')
        print(name)
    templist = list

    
collect_game_data(player_stats, play_att_list, url, 0, 0)

url_team = 'https://fbref.com/en/comps/11/schedule/Serie-A-Scores-and-Fixtures'

# check teams
def win_loss2(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    tags = soup.find('caption')
    tag = tags.find_next('tbody')
    table = tag.findNext("tr")
    squad_a = ''
    squad_b = ''
    for tabl in table:
        if "squad_a" in str(tabl):
            squad_a=tabl.text
        if "squad_b" in str(tabl):
            squad_b=tabl.text
    print(squad_a + '\n' + squad_b)
    # print next line
    print('\n')


def get_game_tag(url): # get the game tag
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    tags = soup.find('caption')
    tag = tags.find_next('tbody')
    
    return tag
  
        
#print(get_game_tag(url_team))

def win_loss(tag): # return winner/loser
    
    tag = tag.findNext("tr")

    for tabl in tag:
        
        if "squad_a" in str(tabl):
            if "bold" in str(tabl):
                return 1
            
        if "squad_b" in str(tabl):
            if "bold" in str(tabl):
                return 2
            
    return 0
#print(win_loss(get_game_tag(url_team)))

def get_game_link(tag, game_row): # get the link to the game
    
    tag_link = tag.find_all_next('td', {"data-stat": 'score'})[game_row]
    
    if tag_link.text == "":
        return 0
    else:
        # return the link
        return "https://fbref.com/" + str(tag_link.find_all_next('a')[0].get('href'))   


#print(get_game_link(get_game_tag(url_team), 419))



# function that checks how many times a class of html tag with the tag value is found in the html
def check_html_tag_n(url, element, tag, team, row):
    # get the html
    html = requests.get(url)
    # parse the html
    soup = BeautifulSoup(html.text, 'html.parser')
    # find the tag
    tags = soup.findAll(element)
    # find the player stats table for the specific team
    caption_tag = team_stats_table(tags, team) 
    table_tag = caption_tag.findNext('tbody') 

