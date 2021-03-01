# benfords-law-covid-vaccinations-data
The concept of grouping numbers based on which integer they start with and 
noticing a pattern, regardless of where the numbers come from, has amazed me. May it retail
prices or football stats.As long as the numbers have not been tampered with, 
the distribution of numbers remains relatively similar. 
This is why Benford's law has been used for purposes such as fraud detection. 
I've decided to try and apply Benford's law on world's Covid-19 vaccinations data 
(full set of data can be found [here](https://www.kaggle.com/gpreda/covid-world-vaccination-progress)) 

Works by passing in the column name, which contains quantitative data only.
Once the law has been applied, the data is visualised using matplotlib's bar chart.

## Run script:
```
# Install dependencies
python3 -m pip install -r requirements.txt
# or
python3 -m pip install click matplotlib 

# Get a list of all available columns (space separated)
python3 /Users/markem04/code/benfords-law-covid-vaccinations-data/benfords_law.py --help        
Usage: benfords_law.py [OPTIONS]

Options:
  --col_name TEXT  total_vaccinations people_vaccinated
                   people_fully_vaccinated daily_vaccinations_raw
                   daily_vaccinations total_vaccinations_per_hundred
                   people_vaccinated_per_hundred
                   people_fully_vaccinated_per_hundred
                   daily_vaccinations_per_million

  --help           Show this message and exit.

python3 benfords_law.py --col_name people_vaccinated
```