
def run():

    from googleapiclient.discovery import build
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    import plotly.express as px

    api_key = 'AIzaSyBlLqI8kv5vx9cq3ansA8DAtpDf3yjJXLE'


    channel_ids =  ['UCCq1xDJMBRF61kiOgU90_kw', ## RCB
                'UCl23mvQ3321L7zO6JyzhVmg', ## MI
                'UC2J_VKrAzOEJuQvFFtj3KUw', ## CSK
                'UCScgEv0U9Wcnk24KfAzGTXg', ##SRH
                'UCp10aBPqcOeBbEg7d_K9SBw', ##KKR
                'UCEzB47eM-HZu04f4mB2nycg', ##DC
                'UCkpgyRmcNy-aZFLUkKkWK4w', ##RR
                'UCvRa1LWA_-aARq1AQMC4AyA', ##PK
                'UCCBe9iIoN9Ar-Elluxca-Xw', ##GT
                'UC-mi8xUqL43BMlhvJbAf-Ew', ##LSG
                ]
                
    developerKey = api_key
    youtube = build('youtube', 'v3', developerKey=api_key)

    def get_channel_stats(youtube, channel_ids):
        
        all_data = []
        
        request = youtube.channels().list(
                    part='snippet,contentDetails,statistics',
                    id= ','.join(channel_ids))
            
        response = request.execute()
        
        for i in range(len(response['items'])):
            
            data = dict(Channel_Name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_Videos = response['items'][i]['statistics']['videoCount'],
                    playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
            
            all_data.append(data)
        
        
        return all_data


        
    channel_statistics = get_channel_stats(youtube, channel_ids)


    ChannelData = pd.DataFrame(channel_statistics)

    ChannelData['Subscribers'] = pd.to_numeric(ChannelData['Subscribers'])
    ChannelData['Views'] = pd.to_numeric(ChannelData['Views'])
    ChannelData['Total_Videos'] = pd.to_numeric(ChannelData['Total_Videos'])


    ChannelData.sort_values(by = 'Subscribers', ascending = False)


    # st.title('Who is IPL KIng on Youtube ?')
    st.markdown(
        '<h1 style="color: skyblue;">Who is IPL King on Youtube ?</h1>',
        unsafe_allow_html=True
    )

    st.write('<p style="color: White; font-family: Helvetica; font-size: 24px;">The data was extracted using Youtube API in this project. The performance of all IPL teams is analysed below by capturing live data.</p>', unsafe_allow_html=True)



    page_bg_img = f"""
    <style>

    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz7nkIarNRB4dcJKwBuCp-PYeNRwDIf1vCr2HNcjhaq8bRPblIAgHHh2CDsUC5rpmgw9E&usqp=CAU");
    background-size: cover;

    background-position: top left;
    background-repeat: no-repeat;
    opacity: 1;
    background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhUTEhIVFRUXFxUXFRUVFRUVFRUVFRUXFxUVFRUYHSggGBolHRUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFRAQFy0dFR0tLS0tLS0tLS0tLS0tLSstLS0tLS0tNy0tLS0tLS0tLTctLS0tKy0tLS0tNy03LTctN//AABEIALcBEwMBIgACEQEDEQH/xAAYAAEBAQEBAAAAAAAAAAAAAAABAAIDB//EACEQAQEBAQADAAEFAQAAAAAAAAABEQISITHwA2FxgZFR/8QAGAEBAQEBAQAAAAAAAAAAAAAAAAECBQT/xAAXEQEBAQEAAAAAAAAAAAAAAAAAEQEx/9oADAMBAAIRAxEAPwD0zlqDla9rmnoSijCFb0xiVqUXDagQFFuNM9QNEjcZqgmN1iX6QKGlAIrWY1OTgQYYRoqxKoFahIqChQtEVBoXBU6BoFm1aMVk1nD2uQZsTdiCNc1dVnjpqRFNc+a6s3gxdHMbPMNSrmMVrmpmwCo1IJEGLG5BYlDYLDpkBmhqxkFatVVAxYcQKHQIghjTChqkFawRkrDgrFFaqxWWWdbxm8qg7v5/Sn09RmA3iGVA3OTG9c/Jlrg6ufG+a59Q89KjcUv/AFjqiSkWurOkXpFa5p5Z5p1BdM7WupUoOY1rEpgYdHJwcgji6o0CKloEQxAKz1W7HPvkxNa4pHMVFaZFqtEoOlnFRqK0aO4RR1RqxRWW4hhFavTOLkxlQJG5FFpFYpDqqKsYx0ipSMyNQZqoK1kVvmB1nDzGpFIgqzW6MBz+tSGcmLSC8rlKINVnRaLVhut+Tn1z8Sq4mlGUdxBnVTIlSERoYis2NWJVSMYy3KzYrKvaWkHSKxQ2stq0Vfn+ehegVMg6p0Gp0uumEFbitEOIrOHkWnmYqGoYcRUJ01YpAArQwGImsZsVENZOKi5rdjOHyNMMFFUQMixQgoNW+1gqtWiKKjPUMqqEBHtKOtSLDTPSxq/EEYhOM1QmiVmg6ShnWpAWBq0AYrTIEUabQKIadEGqLyEaxcwBYJG6pAZqwi0EFhzAWLDrIEYVQGCnRaILRSGkMQkQjroZ6q5ZjVaitFIolbxjnl000xhSGEBip1YijFKbVzBBpMVgrNNhkHVARSI0FaMVMEUNAFLBtYXGdblHVFFqlNrOqKwRa1rGHxBrWSOtBUGVVUEqZQVqxriNRcyJVzGsLCRo2jyY6q51YlbalYsUqQroIxrcoqsa5GpFOoWGQEy1IrAERowGaY1YzQWDGoAZqw4IqKwY1hwSOcbnKPRVjPUQtMogwdU2iriaFYpDFHPP3Td5IkbkEU6ZjLVbtF6ZrHd9LE3Xbn2sjH6Pxu1FzjNKioIqcoU2mRmLQbQFRWxglOgYr6AtBWqsxoRayKVGqzeStBcms2s6DUFFo56VKquRVFRLWhiCFrPXXttUY8k14oF5KUs9X2DYsU6FqK1zR5MynArXNWlYKdFo1uIvQsaFoJVk24DQs9qDEGtZViihkSakRXPGjaFQWrWOqosStYxXRnqGGs2ictcmiCKtc1n9Sb8BeSo8DgBGRUAklRWufVaGho8mZa3hqopTNZ1RFdeaZWIZUXGpGtYOIpqghop0YsNBSNMyrqopokEqtVDFoICgoGbPYrV+rpakXDPVNZ6gmnmGqDqAOOm9c+Y1QxdVSqKgNVrNvsxUVqN/lCslIQDpIRcfu0kDVi5SRoW1uBGmNYkkaNZ6oQmt6x1UjDVxGkjRDroINNqlCA6rQgSSUStSADySVkSrUgZpxIDUkD//2Q==");
    background-size: cover;

    background-position: top left;
    background-repeat: no-repeat;
    opacity: 1;
    background-attachment: local;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)


    # st.sidebar.title('hi')


    # Define a function to apply CSS styles to the table
    def apply_table_styles():
        return """
            <style>
                table.dataframe td {
                    font-size: 14px;
                    font-weight: bold;
                    padding: 8px;
                    background-color: #d8e8f3;
                    border: 2px solid #fff;
                }
                table.dataframe th {
                    font-size: 16px;
                    font-weight: bold;
                    padding: 8px;
                    background-color: #0077b6;
                    color: #fff;
                    border: 2px solid #fff;
                }
            </style>
        """

    # Apply the styles to the table
    st.write(apply_table_styles(), unsafe_allow_html=True)
    st.dataframe(ChannelData.style.set_properties(**{'background-color': '#caf0f8', 
                                            'color': 'black',
                                            'border-color': '#0077b6'}))



    st.markdown(
        '<h1 style="color: #ff9900;">King of Subscribers</h1>',
        unsafe_allow_html=True
    )


    fig = px.bar(ChannelData, x='Subscribers', y='Channel_Name', orientation='h', color='Channel_Name', color_continuous_scale=px.colors.sequential.Greys)

    # Set the x and y axis labels
    fig.update_xaxes(title_text='Subscribers')
    fig.update_yaxes(title_text='Channels')

    # Rotate the x axis labels
    # fig.update_xaxes(tickangle=90)

    # Show the chart in Streamlit
    st.plotly_chart(fig)


    st.write('<p style="color: White; font-family: Helvetica; font-size: 24px;">RCB has the highest subscribers (32 lakhs + ) and has a thumping lead of around 6 lakhs from the second highest subscriber.</p>', unsafe_allow_html=True)

    st.write('<p style="color: skyblue; font-family: Helvetica; font-size: 28px;">Is the number of subscribers directly proportional to the number of views ?</p>', unsafe_allow_html=True)


    ##############################################################################################################################################


    # st.header("King of Views")

    st.markdown(
        '<h1 style="color: #ff9900;">King of Views</h1>',
        unsafe_allow_html=True
    )


    fig = px.bar(ChannelData, x='Views', y='Channel_Name', orientation='h', color='Channel_Name', color_continuous_scale=px.colors.sequential.Greys)

    # Set the x and y axis labels
    fig.update_xaxes(title_text='Views')
    fig.update_yaxes(title_text='Channels')

    # Rotate the x axis labels
    # fig.update_xaxes(tickangle=90)

    # Show the chart in Streamlit
    st.plotly_chart(fig)


    st.write('<p style="color: White; font-family: Helvetica; font-size: 24px;">So here, we can see that Mumbai Indians have the highest number of views, eventhough it ranks third in number of subscribers. RCB stays third in views . Hence we infer subcriber count is not directly propotional to the view count.</p>', unsafe_allow_html=True)
    ##############################################################################################################################################

    # st.header("King of Uploads")

    st.markdown(
        '<h1 style="color: #ff9900;">King of Uploads</h1>',
        unsafe_allow_html=True
    )


    fig = px.bar(ChannelData, x='Total_Videos', y='Channel_Name', orientation='h', color='Channel_Name', color_continuous_scale=px.colors.sequential.Greys)

    # Set the x and y axis labels
    fig.update_xaxes(title_text='Total_Videos')
    fig.update_yaxes(title_text='Channels')

    # Rotate the x axis labels
    # fig.update_xaxes(tickangle=90)

    # Show the chart in Streamlit
    st.plotly_chart(fig)


    st.write('<p style="color: White; font-family: Helvetica; font-size: 24px;">Mumbai Indians have the highest video count. But again, it is not fair to infer that the total number of videos and views are directly propotional as CSK and RCB ranks second and third in terms of views respectively, while they stand at 8th and 4th in term of videos uploaded respectively.</p>', unsafe_allow_html=True)


    ##############################################################################################################################################

    playlist_id = ChannelData.loc[ChannelData['Channel_Name'] == 'Royal Challengers Bangalore', 'playlist_id'].iloc[0]



    def get_video_ids(youtube, playlist_id):
        
        request = youtube.playlistItems().list(
                    part="contentDetails",
                    playlistId=playlist_id,
                    maxResults=50)  
        response = request.execute()
        
        video_ids = []
        
        for i in range (len(response['items'])):
            video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
        next_page_token = response.get('nextPageToken')
        more_pgs = True
        
        while more_pgs:
            if next_page_token is None:
                more_pgs = False
            
            else:
                
                request = youtube.playlistItems().list(
                            part="contentDetails",
                            playlistId=playlist_id,
                            maxResults=50,
                            pageToken=next_page_token)  
                response = request.execute()
                
                for i in range (len(response['items'])):
                    video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
                next_page_token = response.get('nextPageToken')
        
        return video_ids




    video_ids = get_video_ids(youtube, playlist_id)



    def get_video_details(youtube, video_ids):
        
        all_vid_stats = [] 
        
        for i in range(0,len(video_ids),50):
        
            request = youtube.videos().list(
                        part="snippet,statistics",
                        id=','.join(video_ids[i:i+50]))
        
            response = request.execute()
        
            for video in response['items']:
                video_sts = dict(Title = video['snippet']['title'],
                                Published = video['snippet']['publishedAt'],
                                Views = video['statistics']['viewCount'],
                                Likes = video['statistics']['likeCount']
                                )                         
                                

                all_vid_stats.append(video_sts)
        return all_vid_stats


    Video_data = get_video_details(youtube, video_ids)


    VideoData = pd.DataFrame(Video_data)


    VideoData['Published'] = pd.to_datetime(VideoData['Published']).dt.date 
    VideoData['Views'] = pd.to_numeric(VideoData['Views'])
    VideoData['Likes'] = pd.to_numeric(VideoData['Likes'])

    top10videos = VideoData.sort_values(by = 'Views', ascending = False).head(10)
    # top10videos = VideoData.sort_values(by = 'Views', ascending = False).head(10)

    st.write('<p style="color: skyblue; font-family: Helvetica; font-size: 28px;">Lets Analyse the activities of RCB.</p>', unsafe_allow_html=True)


    # st.header("Top 10 Videos of RCB")
    st.markdown(
        '<h1 style="color: #ff9900;">Top 10 Videos of RCB</h1>',
        unsafe_allow_html=True
    )



    fig = px.bar(top10videos, x='Views', y='Title', orientation='h',  color_continuous_scale=px.colors.sequential.Greys)

    # Set the x and y axis labels
    fig.update_xaxes(title_text='Views')
    fig.update_yaxes(title_text='Title')

    # Rotate the x axis labels
    # fig.update_xaxes(tickangle=90)

    # Show the chart in Streamlit
    st.plotly_chart(fig)

    ## color='Channel_Name',




    st.write('<p style="color: White; font-family: Helvetica; font-size: 24px;">Videos with Virat Kohli content has high number of views.</p>', unsafe_allow_html=True)


    #################################################################################################################################################

    VideoData['Month'] = pd.to_datetime(VideoData['Published']).dt.strftime('%b')
    Videos_per_month = VideoData.groupby('Month', as_index = False).size()

    sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


    Videos_per_month.index = pd.CategoricalIndex(Videos_per_month['Month'], categories=sort_order, ordered=True)

    Videos_per_month = Videos_per_month.sort_index()


    # st.header("Videos per month,RCB")
    st.markdown(
        '<h1 style="color: #ff9900;">Videos per month</h1>',
        unsafe_allow_html=True
    )


    # fig = px.bar(Videos_per_month, x='Month', y='size', orientation='h',  color_continuous_scale=px.colors.sequential.Greys)

    fig = px.line(Videos_per_month, x='Month', y='size', color_discrete_sequence=px.colors.qualitative.Dark2)

    # Set the x and y axis labels
    fig.update_xaxes(title_text='Month')
    fig.update_yaxes(title_text='Uploads')

    # Rotate the x axis labels
    # fig.update_xaxes(tickangle=90)

    # Show the chart in Streamlit
    st.plotly_chart(fig)


    st.write('<p style="color: White; font-family: Helvetica; font-size: 24px;">Maximum number of videos are uploaded in the month of April and May as IPL matches are held in these months.</p>', unsafe_allow_html=True)
