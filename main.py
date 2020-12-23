from govuk_bank_holidays.bank_holidays import BankHolidays
from datetime import datetime, date
from bh import BH
from fastapi import FastAPI
import pandas as pd

rota_schedule = pd.read_csv("rota_schedule.csv")

app = FastAPI()


@app.get("/")
def root():
    rota_list = rota_schedule['rota_name'].unique()
    return list(rota_list)


@app.get("/calc")
def calc_allowance(rota_name: str, start_date: date = date(datetime.today().year, 1, 1),
                   end_date: date = date(datetime.today().year, 12, 31)):
    bank_holidays = BankHolidays()
    current_year_bh = bank_holidays.get_holidays(division='england-and-wales', year=start_date.year)
    hours_owed = 0
    for bh in current_year_bh:
        print(type(start_date))
        if bh['date'] >= start_date and bh['date'] <= end_date:
            bank_h = BH(bh['date'])
            hours_owed += 8 - bank_h.hours_worked_during_bh(rota_name)
    return hours_owed
