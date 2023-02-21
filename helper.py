from urllib.parse import urlsplit
#from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import nltk
from nltk.corpus import stopwords
import re


# from emoji import UNICODE_EMOJI
# import emoji


def fetch_stats(selected_user, df):

    
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]


    # fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(url for url in message.split() if url.startswith("http"))


    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    df = df[df['user'] != 'group_notification']
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index': 'name', 'user': 'percent'})
        
    return x,df



#nltk.download('stopwords')
def most_common_words(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>']
    temp = temp[temp['message'] != 'omitted']
    
    
    cleaned_words = []

    for message in temp['message']:
        for word in message.lower().split():
            clean_word = re.sub('[^a-zA-Z]', '', word)
            stop_words = set(stopwords.words('english'))
            if clean_word and clean_word not in stop_words:
                cleaned_words.append(clean_word)

    most_common_df = pd.DataFrame(Counter(cleaned_words).most_common(10))
    return most_common_df





def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline


def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    daily_timeline['only_date'] = pd.to_datetime(daily_timeline['only_date'])

    return daily_timeline


def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()



def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap



