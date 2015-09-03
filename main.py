import csv
import mechanize
import sys

def log_in(browser, email, password, league_id, team_id):
  
  url = "http://www.fleaflicker.com/nfl/leagues/{}/teams/{}/settings/rankings".format(league_id, team_id)

  browser.open(url)
  browser.select_form(nr=0)
  browser.form["email"] = email
  browser.form["password"] = password
  browser.submit()

  return browser

def submit_rankings(browser, ranking_file_name):
  browser.select_form(nr=1)
  browser.form.find_control("playerIds").readonly = False
  
  player_ids = get_ranking(ranking_file_name)
  
  browser.form["playerIds"] = player_ids
  browser.submit()

  return browser  

def get_ranking(ranking_file_name):
  players = get_players()
  player_ids = []
  with open(ranking_file_name, 'rb') as ranking_file:
    for ranking in ranking_file:
      player_name = ranking.strip()
      try:
        player_ids.append(players[player_name])
      except KeyError:
        print("Could not find player: {}. Make sure your spelling matches the spelling on fleaflicker".format(player_name))
  return "|".join(player_ids)

def get_players():
  players = {}
  with open('players.csv', 'rb') as csvfile:
    playersreader = csv.reader(csvfile)
    for row in playersreader:
      player_name = row[1]
      fleaflicker_id = row[0]
      players[player_name] = fleaflicker_id 
  return players


if __name__ == '__main__':
  league_id = sys.argv[1]
  team_id = sys.argv[2]
  email = sys.argv[3]
  password = sys.argv[4]
  ranking_file_name = sys.argv[5]

  browser = mechanize.Browser()

  browser = log_in(browser, email, password, league_id, team_id)
  submit_rankings(browser, ranking_file_name)