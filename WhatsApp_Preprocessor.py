import re
import pandas as pd
import datetime


def preprocess(data):

    #replacement
    data = data.replace('\u202f', ' ')   
    data = data.replace('\u200e', '') 
    #12hrs format
    #pattern = r'^(\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2} [ap]m) - (.*?): (.*)$'
    
    
    pattern = r'^(\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2} [apAP][mM]) - (.*?): (.*)$'



    # Use the re.findall() function to extract all occurrences of the pattern in the text file
    matches = re.findall(pattern, data, flags=re.MULTILINE)

    # Create a Pandas DataFrame to store the extracted data
    df = pd.DataFrame(matches, columns=['date', 'user', 'message'])
    #df['message'] = df['message'].replace(['GIF omitted', 'image omitted', 'sticker omitted', 'video omitted'],'<Media omitted>')


    df['date'] = df['date'].astype(str)
    df['date'] = df['date'].str.strip()
    df['date'] = df['date'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d, %H:%M:%S'))
    df = df[~df['user'].str.startswith('You added')]
    df['date'] = pd.to_datetime(df['date'])

    
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df


def preprocessIOS(data):

    data = data.replace('\u200e', '')
    
    pattern = r'^\[(\d{2}\/\d{2}\/\d{2}, \d{2}:\d{2}:\d{2} [apAP][mM])\] (.+?): (.*)$'


    # Use the re.findall() function to extract all occurrences of the pattern in the text file
    matches = re.findall(pattern, data, flags=re.MULTILINE)
   

    # Create a Pandas DataFrame to store the extracted data
    df = pd.DataFrame(matches, columns=['date', 'user', 'message'])
    
    
    df['message'] = df['message'].astype(str)
    
    df['message'] = df['message'].str.strip()
    

    
    df['date'] = df['date'].astype(str)
    df['date'] = df['date'].str.strip()
    df['date'] = df['date'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d, %H:%M:%S'))
    #df['message'] = df['message'].replace(['GIF omitted', 'image omitted', 'sticker omitted', 'video omitted', 'audio omitted'],'<Media omitted>')
    df.loc[df['message'].str.contains('omitted'), 'message'] = '<Media omitted>'
    df = df[~df['user'].str.startswith('You added')]
    df['date'] = pd.to_datetime(df['date'])

    
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df

