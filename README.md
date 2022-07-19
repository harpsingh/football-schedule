# football-schedule
A simple web scraper to get football match schedules from www.goal.com site.

# Usage
1. Clone repository `git clone https://github.com/harpsingh/football-schedule.git`
2. Change to the cloned directory `cd football-schedule`
3. Create python virtual environment `python -m venv venv`
4. Install packages `pip install -r requirements.txt`
5. Provide date as a string argument in `main.py` and run it - `python main.py`.
  `
    [{'competition': 'Premier League',
    'matches': [{'away_team': 'Newcastle United',
                 'home_team': 'Everton',
                 'time': '18/03/22 (1:15 AM IST)'}]},
   {'competition': 'Serie A',
    'matches': [{'away_team': 'Spezia',
                 'home_team': 'Sassuolo',
                 'time': '18/03/22 (11:15 PM IST)'}]},
   {'competition': 'UEFA Europa League',
    'matches': [{'away_team': 'Real Betis',
                 'home_team': 'Eintracht Frankfurt',
                 'time': '18/03/22 (1:30 AM IST)'},
                {'away_team': 'Porto',
                 'home_team': 'Olympique Lyonnais',
                 'time': '18/03/22 (1:30 AM IST)'},
                {'away_team': 'Sevilla',
                 'home_team': 'West Ham United',
                 'time': '18/03/22 (1:30 AM IST)'}]}]
  `
