import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

import pandas as pd
import anvil.media

@anvil.server.callable
def get_data():
  summary = get_summary()
  age_gender = get_age_gender()
  by_country = get_country()
  time_of_day = get_time_of_day()
  
  return summary, age_gender, by_country, time_of_day
  
  
  
def get_summary():
  df = get_df('summary')
  return df.to_dict('records')[0]


def get_age_gender():
  df = get_df('age_gender')
  df = df.sort_values('age')
  
  age = pd.DataFrame({'age':df['age'].unique()})
  
  def get_gender(gender):
    x = df.loc[df['gender'] == gender]
    x = x.filter(items=['age', 'clicks'])
    x = age.merge(x, 'left').fillna(0)
    x['clicks'] = x['clicks'].astype(int)
    return x.to_dict('list')

  return get_gender('male'), get_gender('female')

  
def get_country():
  df = get_df('by_country')
  df = df.sort_values('region')
  return df.to_dict('list')


def get_time_of_day():
  df = get_df('time_of_day')
  df = df.rename(columns={'time of day (ad account time zone)': 'time of day'})
  
  def func(time):
    time_start = time.split()[0]
    time_start = time_start.split(':')[:-1]
    time_end = f'{(int(time_start[0]) + 1) % 24}:00'.zfill(5)
    return ':'.join(time_start) + ' - ' + time_end
    
  df['time of day'] = df['time of day'].apply(func) 
  df = df.sort_values('time of day')
  
  return df.to_dict('list')


def get_df(file_name):
  csv = app_tables.csv.get(file_name=file_name)['file']
  with anvil.media.TempFile(csv) as file:
    df = pd.read_csv(file)
  
  # lower case column headers
  df = df.rename(lambda col: col.lower(), axis=1)
  df = df.rename(columns={"clicks (all)": 'clicks'})
  
  return df
  