from itertools import count


class Player: 
    # initialize the player class
    def __init__(self, name):#, goals, assists, pens_made, pens_att, shots_total, shots_on_target, cards_yellow, cards_red, touches, pressures, tackles, interceptions, blocks, xg, npxg, xa, sca, gca, passes_completed, passes, passes_pct, progressive_passes, carries, progressive_carries, dribbles_completed, dribbles, passes_total_distance, passes_progressive_distance, passes_completed_short, passes_short, passes_pct_short, passes_medium, passes_pct_medium, passes_completed_medium, passes_completed_long, passes_long, passes_pct_long, assisted_shots, passes_into_final_third, passes_into_penalty_area, crosses_into_penalty_area, passes_live, passes_dead, passes_free_kicks, through_balls, passes_pressure, passes_switches, crosses, corner_kicks, corner_kicks_in, corner_kicks_out, corner_kicks_straight, passes_ground, passes_low, passes_high, passes_left_foot, passes_right_foot, passes_head, throw_ins, passes_offsides, passes_oob, passes_intercepted, passes_blocked, tackles_won, tackles_def_3rd, tackles_mid_3rd, tackles_att_3rd, dribble_tackles, dribbles_vs, dribble_tackles_pct, dribbled_past, pressure_regains, pressure_regain_pct, pressures_def_3rd, pressures_mid_3rd, pressures_att_3rd, blocked_shots, blocked_shots_saves, blocked_passes, tackles_interceptions, clearances, errors, touches_def_pen_area, touches_def_3rd, touches_mid_3rd, touches_att_3rd, touches_att_pen_area, touches_live_ball, dribbles_completed_pct, players_dribbled_past, nutmegs, carry_distance, carry_progressive_distance, carries_into_final_third, carries_into_penalty_area, miscontrols, dispossessed, pass_targets, passes_received, passes_received_pct, progressive_passes_received, cards_yellow_red, fouls, fouled, offsides, pens_won, pens_conceded, own_goals, ball_recoveries, aerials_won, aerials_lost, aerials_won_pct):
        self.name = name
        #self.team = team
        '''
        self.goals = goals
        self.assists = assists
        self.pens_made = pens_made
        self.pens_att = pens_att
        self.shots_total = shots_total
        self.shots_on_target = shots_on_target
        self.cards_yellow = cards_yellow
        self.cards_red = cards_red
        self.touches = touches
        self.pressures = pressures
        self.tackles = tackles
        self.interceptions = interceptions
        self.blocks = blocks
        self.xg = xg
        self.npxg = npxg
        self.xa = xa
        self.sca = sca
        self.gca = gca
        self.passes_completed = passes_completed
        self.passes = passes
        self.passes_pct = passes_pct
        self.progressive_passes = progressive_passes
        self.carries = carries
        self.progressive_carries = progressive_carries
        self.dribbles_completed = dribbles_completed
        self.dribbles = dribbles
        self.passes_total_distance = passes_total_distance
        self.passes_progressive_distance = passes_progressive_distance
        self.passes_completed_short = passes_completed_short
        self.passes_short = passes_short
        self.passes_pct_short = passes_pct_short
        self.passes_medium = passes_medium
        self.passes_pct_medium = passes_pct_medium
        self.passes_completed_medium = passes_completed_medium
        self.passes_completed_long = passes_completed_long
        self.passes_long = passes_long
        self.passes_pct_long = passes_pct_long
        self.assisted_shots = assisted_shots
        self.passes_into_final_third = passes_into_final_third
        self.passes_into_penalty_area = passes_into_penalty_area    
        self.passes_live = passes_live
        self.passes_dead = passes_dead
        self.passes_free_kicks = passes_free_kicks
        self.through_balls = through_balls
        self.passes_pressure = passes_pressure
        self.passes_switches = passes_switches
        self.crosses = crosses
        self.corner_kicks = corner_kicks
        self.corner_kicks_in = corner_kicks_in
        self.corner_kicks_out = corner_kicks_out
        self.corner_kicks_straight = corner_kicks_straight
        self.passes_ground = passes_ground
        self.passes_low = passes_low
        self.passes_high = passes_high
        self.passes_left_foot = passes_left_foot
        self.passes_right_foot = passes_right_foot
        self.passes_head = passes_head
        self.throw_ins = throw_ins
        self.passes_offsides = passes_offsides
        self.passes_oob = passes_oob
        self.passes_intercepted = passes_intercepted
        self.passes_blocked = passes_blocked
        self.tackles_won = tackles_won
        self.tackles_def_3rd = tackles_def_3rd
        self.tackles_mid_3rd = tackles_mid_3rd
        self.tackles_att_3rd = tackles_att_3rd
        self.dribble_tackles = dribble_tackles
        self.dribbles_vs = dribbles_vs
        self.dribble_tackles_pct = dribble_tackles_pct
        self.dribbled_past = dribbled_past
        self.pressures = pressures
        self.pressure_regains = pressure_regains
        self.pressure_regain_pct = pressure_regain_pct
        self.pressures_def_3rd = pressures_def_3rd
        self.pressures_mid_3rd = pressures_mid_3rd
        self.pressures_att_3rd = pressures_att_3rd
        self.blocked_shots = blocked_shots
        self.blocked_shots_saves = blocked_shots_saves
        self.blocked_passes = blocked_passes
        self.tackles_interceptions = tackles_interceptions
        self.clearances = clearances
        self.errors = errors
        self.crosses_into_penalty_area = crosses_into_penalty_area
        self.touches_def_pen_area = touches_def_pen_area
        self.touches_def_3rd = touches_def_3rd
        self.touches_mid_3rd = touches_mid_3rd
        self.touches_att_3rd = touches_att_3rd
        self.touches_att_pen_area = touches_att_pen_area
        self.touches_live_ball = touches_live_ball
        self.dribbles_completed_pct = dribbles_completed_pct
        self.players_dribbled_past = players_dribbled_past
        self.nutmegs = nutmegs
        self.carry_distance = carry_distance
        self.carry_progressive_distance = carry_progressive_distance
        self.carries_into_final_third = carries_into_final_third
        self.carries_into_penalty_area = carries_into_penalty_area
        self.miscontrols = miscontrols
        self.dispossessed = dispossessed
        self.pass_targets = pass_targets
        self.passes_received = passes_received
        self.passes_received_pct = passes_received_pct
        self.progressive_passes_received = progressive_passes_received
        self.cards_yellow_red = cards_yellow_red
        self.fouls = fouls
        self.fouled = fouled
        self.offsides = offsides
        self.pens_won = pens_won
        self.pens_conceded = pens_conceded
        self.own_goals = own_goals
        self.ball_recoveries = ball_recoveries
        self.aerials_won = aerials_won
        self.aerials_lost = aerials_lost
        self.aerials_won_pct = aerials_won_pct
'''
    # add attributes to the class

play_att_list = ['name', 'name', 'team', 'goals', 'assists', 'pens_made', 'pens_att', 'shots_total', 'shots_on_target', 'cards_yellow', 'cards_red', 'touches', 'pressures', 'tackles', 'interceptions', 'blocks', 'xg', 'npxg', 'xa', 'sca', 'gca', 'passes_completed', 'passes', 'passes_pct', 'progressive_passes', 'carries', 'progressive_carries', 'dribbles_completed', 'dribbles', 'passes_total_distance', 'passes_progressive_distance', 'passes_completed_short', 'passes_short', 'passes_pct_short', 'passes_medium', 'passes_pct_medium', 'passes_completed_medium', 'passes_completed_long', 'passes_long', 'passes_pct_long', 'assisted_shots', 'passes_into_final_third', 'passes_into_penalty_area', 'crosses_into_penalty_area', 'passes_live', 'passes_dead', 'passes_free_kicks', 'through_balls', 'passes_pressure', 'passes_switches', 'crosses', 'corner_kicks', 'corner_kicks_in', 'corner_kicks_out', 'corner_kicks_straight', 'passes_ground', 'passes_low', 'passes_high', 'passes_left_foot', 'passes_right_foot', 'passes_head', 'throw_ins', 'passes_offsides', 'passes_oob', 'passes_intercepted', 'passes_blocked', 'tackles_won', 'tackles_def_3rd', 'tackles_mid_3rd', 'tackles_att_3rd', 'dribble_tackles', 'dribbles_vs', 'dribble_tackles_pct', 'dribbled_past', 'pressure_regains', 'pressure_regain_pct', 'pressures_def_3rd', 'pressures_mid_3rd', 'pressures_att_3rd', 'blocked_shots', 'blocked_shots_saves', 'blocked_passes', 'tackles_interceptions', 'clearances', 'errors', 'touches_def_pen_area', 'touches_def_3rd', 'touches_mid_3rd', 'touches_att_3rd', 'touches_att_pen_area', 'touches_live_ball', 'dribbles_completed_pct', 'players_dribbled_past', 'nutmegs', 'carry_distance', 'carry_progressive_distance', 'carries_into_final_third', 'carries_into_penalty_area', 'miscontrols', 'dispossessed', 'pass_targets', 'passes_received', 'passes_received_pct', 'progressive_passes_received', 'cards_yellow_red', 'fouls', 'fouled', 'offsides', 'pens_won', 'pens_conceded', 'own_goals', 'ball_recoveries', 'aerials_won', 'aerials_lost', 'aerials_won_pct']
# check how many times an element appears in a list
def count_elements(list, element):
    count = 0
    for i in list:
        if i == element:
            count += 1
    return count


for i in play_att_list:
    if count_elements(play_att_list, i) > 1:
        print(i)
        break

# function to make a list of strings of every word in a string while ignoring every comma
def get_words(string):
    words = []
    word = ""
    for char in string:
        if char == " ":
            words.append(word)
            word = ""
        elif char == ",":
            pass
        else:
            word += char
    words.append(word)
    return words


# print(play_att_list)

