import csv
import re
from pathlib import Path

import matplotlib.pyplot as plt
import click


"""
Data retrieved for this project is only up to date 
until around March 2021. Up-to-date CSV can be found here:
https://www.kaggle.com/gpreda/covid-world-vaccination-progress
"""

class BenfordsLawCovidVaccinations:

    def __init__(self, col_name):
        self.all_cols = [
            "total_vaccinations",
            "people_vaccinated",
            "people_fully_vaccinated",
            "daily_vaccinations_raw",
            "daily_vaccinations",
            "total_vaccinations_per_hundred",
            "people_vaccinated_per_hundred",
            "people_fully_vaccinated_per_hundred",
            "daily_vaccinations_per_million"
        ]
        self.column_name = col_name
        self.data = csv.DictReader(
            open(f"{Path(__file__).parent}/country_vaccinations.csv")
        )
        self.apply()


    def get_column_data(self, column):
        return [
            row[column] for row in self.data 
                if re.match(r"^[1-9]", row[column])
        ]

    def apply(self):
        if self.column_name not in self.all_cols:
            print(f"{self.column_name} does not exist")
            return
            
        column_data = self.get_column_data(self.column_name)
        grouped = {}

        for col in column_data:
            first_number = col[0]
            
            if first_number not in grouped:
                grouped[first_number] = 1
            else:
                grouped[first_number] += 1

        get_precentage = lambda n: (n / sum(grouped.values())) * 100
        grouped = dict(sorted(
            {int(k): get_precentage(v) for k, v in grouped.items()}.items()
        ))
        self.plot_data(
            grouped, 
            title=self.column_name.replace("_", " ").capitalize()
        )

    def plot_data(self, data, title):
        plt.style.use('ggplot')
        plt.title(f"Benford's Law - {title}")
        x_pos = range(len(data.keys()))
        plt.bar(x_pos, data.values(), color='green')
        plt.xlabel("Number")
        plt.ylabel("Frequency (%)")
        plt.xticks(x_pos, data.keys())
        plt.show()
    

@click.command()
@click.option("--col_name", help="""
all
total_vaccinations
people_vaccinated
people_fully_vaccinated
daily_vaccinations_raw
daily_vaccinations
total_vaccinations_per_hundred
people_vaccinated_per_hundred
people_fully_vaccinated_per_hundred
daily_vaccinations_per_million
""")
def init(col_name):
    BenfordsLawCovidVaccinations(col_name)



if __name__ == '__main__':
    init()


