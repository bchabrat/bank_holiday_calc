import pandas as pd
from datetime import datetime


class BH(object):
    DAY_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    rota_schedule = pd.read_csv("rota_schedule.csv")

    def __init__(self, date: datetime):
        self.week_number_is_odd = True if date.isocalendar()[1] % 2 else False
        self.day_of_the_week = self.DAY_OF_WEEK[date.weekday()]

    def hours_worked_during_bh(self, rota: str):
        filtered_rota = self.rota_schedule[self.rota_schedule["rota_name"] == rota]
        filtered_rota_day = filtered_rota[filtered_rota["day"] == self.day_of_the_week]
        filtered_rota_day_week = filtered_rota_day[filtered_rota_day["week_number_is_odd"] == self.week_number_is_odd]
        return int(filtered_rota_day_week["hours worked"])
