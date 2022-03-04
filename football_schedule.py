from datetime import datetime
from bs4 import BeautifulSoup
import requests

URL = "https://www.goal.com/en-in/fixtures/"
date_today = datetime.now().strftime("%Y-%m-%d")


def get_schedule(date=date_today):
    """
    Provide date in YYYY-MM-DD format as a string.
    If no argument is provided, it defaults to today's date
    """

    response = requests.get(URL + date)
    response.raise_for_status()
    goal_text = response.text

    soup = BeautifulSoup(goal_text, "html.parser")

    all_competitions = soup.find_all(name="div", class_="competition-matches")

    if all_competitions:
        schedule_list = []
        scheduled_matches = False
        for competition in all_competitions:
            competition_name = competition.select_one("div.competition-wrapper a span").get_text()
            all_matches = competition.select("div.match-row__data")

            if all_matches:
                scheduled_matches = True
                matches_list = []
                for match in all_matches:
                    match_time = match.select_one("div.match-row__status span").get_text()
                    home_team = match.select_one("table.match-row__teams tr td.match-row__team-home a span").get_text()
                    away_team = match.select_one("table.match-row__teams tr td.match-row__team-away a span").get_text()
                    matches_list.append(
                        {
                            "time": match_time,
                            "home_team": home_team,
                            "away_team": away_team,
                        }
                    )

                schedule_list.append(
                    {
                        "competition": competition_name,
                        "matches": matches_list
                    }
                )

        if scheduled_matches:
            return schedule_list
        else:
            return "No matches scheduled on that day"
