# cd /
# cd Users/"Lakshmeesh S Reddy"/Desktop/Dinku/JOB/Whatsapp_Chat_Analyser
def run():
              
    import streamlit as st
    import WhatsApp_Preprocessor, helper
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os
    import zipfile
    # from ipywidgets import interactive


    def create_zip_archive(folder_path, output_path):
        try:
            with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), arcname=os.path.join(os.path.relpath(root, folder_path), file))
        except Exception as e:
            st.write(f"Error creating zip archive: {e}")

    # if st.sidebar.button("Dont have the chat file? Download a sample here"):
    #     app_dir = os.path.abspath(os.path.dirname(__file__))
    #     folder_path = os.path.join(app_dir, r"C:\Users\Lakshmeesh s reddy\Desktop\Dinku\JOB\Pages\Pages\assets")
    #     output_path = "folder.zip"
    #     create_zip_archive(folder_path, output_path)
    #     with open(output_path, "rb") as f:
    #         bytes = f.read()
    #     st.sidebar.download_button(label="Download", data=bytes, file_name="folder.zip", mime="application/zip")


    button_label = "Dont have the chat file? Download a sample here"
    app_dir = os.path.abspath(os.path.dirname(__file__))
    folder_path = os.path.join(app_dir, r"C:\Users\Lakshmeesh s reddy\Desktop\Dinku\JOB\Pages\Pages\assets")
    output_path = "folder.zip"
    create_zip_archive(folder_path, output_path)
    with open(output_path, "rb") as f:
            bytes = f.read()
    st.sidebar.download_button(label= button_label, data=bytes, file_name="folder.zip", mime="application/zip")

    page_bg_img = f"""
    <style>
     [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://cdn.wallpapersafari.com/54/0/HluF7g.jpg");
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


    st.markdown("<h1 style='color: green;'>Whatsapp Chat Analyzer</h1>", unsafe_allow_html=True)

    uploaded_file_Android = st.sidebar.file_uploader("Upload Android WhatsApp chat txt file")
    
    uploaded_file_IOS = st.sidebar.file_uploader("Upload IOS WhatsApp chat txt file")

    if uploaded_file_Android is not None:
        bytes_data = uploaded_file_Android.getvalue()
        data = bytes_data.decode("utf-8")
        
        df = WhatsApp_Preprocessor.preprocess(data)

        
        # fetch unique users
        user_list = df['user'].unique().tolist()
        #user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0,"Overall")

        selected_user = st.sidebar.selectbox("Analysis according to users",user_list)

        

        if st.button("Show Analysis"):

            num_messages,words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
            # st.title("Top Statistics")


            col1, col2, col3, col4 = st.columns(4)

            with col1:            
                st.header('Total messages')
                st.title(num_messages)

            with col2:            
                st.header('Total words')
                st.title(words)

            with col3:
                st.header("Media Shared")
                st.title(num_media_messages)

            with col4:
                st.header("Total links")
                st.title(num_links)

            # monthly timeline
            # st.title("Monthly Timeline")
            st.markdown("<h1 style='color: green;'>Monthly Timeline</h1>", unsafe_allow_html=True)
            timeline = helper.monthly_timeline(selected_user,df)
            fig,ax = plt.subplots(figsize=(5, 3))
            ax.plot(timeline['time'],timeline['message'], color='green')

            ax.set_xlim(timeline['time'].min(), timeline['time'].max())
            ax.xaxis.set_major_locator(plt.MaxNLocator(20))
            ax.set_xlabel('Months')
            ax.set_ylabel('Messages')
            plt.xticks(rotation='vertical')
            fig.set_size_inches(8, 4)
            st.pyplot(fig)

            # daily timeline
            # st.title("Daily Timeline")
            st.markdown("<h1 style='color: green;'>Daily Timeline</h1>", unsafe_allow_html=True)
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='skyblue')
            fig.set_size_inches(8, 4)
            plt.xticks(rotation='vertical')
            # Set x-axis limits to include full range of dates
            ax.set_xlim(daily_timeline['only_date'].min(), daily_timeline['only_date'].max())
            ax.set_xlabel('Dates')
            ax.set_ylabel('Messages')
            st.pyplot(fig)

            # activity map
            # st.title('Activity Map')
            st.markdown("<h1 style='color: green;'>Activity Map</h1>", unsafe_allow_html=True)
            col1,col2 = st.columns(2)

            with col1:
                st.header("Most busy day")
                busy_day = helper.week_activity_map(selected_user,df)
                fig,ax = plt.subplots()
                ax.bar(busy_day.index,busy_day.values,color='purple')
                #ax.set_xlabel('Dates')
                ax.set_ylabel('Messages')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.header("Most busy month")
                busy_month = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_month.index, busy_month.values,color='orange')
                ax.set_ylabel('Messages')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            # st.title("Weekly Activity Map")
            st.markdown("<h1 style='color: green;'>Weekly Activity Map</h1>", unsafe_allow_html=True)
            user_heatmap = helper.activity_heatmap(selected_user,df)
            fig,ax = plt.subplots()
            ax = sns.heatmap(user_heatmap, cmap="coolwarm")
            ax.set_xlabel("Hours of Day")
            ax.set_ylabel("WeekDay")
            st.pyplot(fig)
            
            
            col1, col2 = st.columns(2)

            # finding the busiest users in the group(Group level)
            if selected_user == 'Overall':
                # st.title('Most Busy Users')
                st.markdown("<h1 style='color: green;'>Most Busy Users</h1>", unsafe_allow_html=True)
                x,new_df = helper.most_busy_users(df)
                fig, ax = plt.subplots()

                col1, col2 = st.columns(2)

                with col1:
                    ax.bar(x.index, x.values,color='red')
                    ax.set_ylabel("Messages")
                    plt.xticks(rotation='vertical')
                    st.pyplot(fig)

                with col2:
                    st.dataframe(new_df)


            # Most common words
            most_common_df = helper.most_common_words(selected_user,df)

            fig, ax = plt.subplots()

            ax.barh(most_common_df[0],most_common_df[1], color='Grey')
            ax.set_ylabel("Words")
            ax.set_xlabel("Frequency of usage")
            plt.xticks(rotation='vertical')

            # st.title('Most common words')
            st.markdown("<h1 style='color: green;'>Most common words</h1>", unsafe_allow_html=True)
            st.pyplot(fig)



    ##############################################################################################################################################

    if uploaded_file_IOS is not None:
        bytes_data = uploaded_file_IOS.getvalue()
        data = bytes_data.decode("utf-8")
        
        df = WhatsApp_Preprocessor.preprocessIOS(data)
        
        
        # fetch unique users
        user_list = df['user'].unique().tolist()
        #user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0,"Overall")

        selected_user = st.sidebar.selectbox("Analysis according to users",user_list)

        #st.dataframe(df)

        # st.set_page_config(page_title="My Streamlit App")

        # if st.button("Show Analysis", key="analysis_button"):
        #     st.write("Performing analysis...")

        # # Set the background color of the button to red
        # st.markdown(
        #     """
        #     <style>
        #     .stButton button {
        #         background-color: red;
        #     }
        #     </style>
        #     """,
        #     unsafe_allow_html=True
        # )




        if st.button("Show Analysis"):

            num_messages,words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
            # st.title("Top Statistics")


            col1, col2, col3, col4 = st.columns(4)

            with col1:            
                st.header('Total messages')
                st.title(num_messages)

            with col2:            
                st.header('Total words')
                st.title(words)

            with col3:
                st.header("Media Shared")
                st.title(num_media_messages)

            with col4:
                st.header("Total links")
                st.title(num_links)

            # monthly timeline
            # st.title("Monthly Timeline")
            st.markdown("<h1 style='color: green;'>Monthly Timeline</h1>", unsafe_allow_html=True)
            timeline = helper.monthly_timeline(selected_user,df)
            fig,ax = plt.subplots(figsize=(5, 3))
            ax.plot(timeline['time'],timeline['message'], color='green')

            ax.set_xlim(timeline['time'].min(), timeline['time'].max())
            ax.xaxis.set_major_locator(plt.MaxNLocator(20))
            ax.set_xlabel('Months')
            ax.set_ylabel('Messages')
            plt.xticks(rotation='vertical')
            fig.set_size_inches(8, 4)
            st.pyplot(fig)

            # daily timeline
            # st.title("Daily Timeline")
            st.markdown("<h1 style='color: green;'>Daily Timeline</h1>", unsafe_allow_html=True)
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='skyblue')
            fig.set_size_inches(8, 4)
            plt.xticks(rotation='vertical')
            # Set x-axis limits to include full range of dates
            ax.set_xlim(daily_timeline['only_date'].min(), daily_timeline['only_date'].max())
            ax.set_xlabel('Dates')
            ax.set_ylabel('Messages')
            st.pyplot(fig)

            # activity map
            # st.title('Activity Map')
            st.markdown("<h1 style='color: green;'>Activity Map</h1>", unsafe_allow_html=True)
            col1,col2 = st.columns(2)

            with col1:
                st.header("Most busy day")
                busy_day = helper.week_activity_map(selected_user,df)
                fig,ax = plt.subplots()
                ax.bar(busy_day.index,busy_day.values,color='purple')
                #ax.set_xlabel('Dates')
                ax.set_ylabel('Messages')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.header("Most busy month")
                busy_month = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_month.index, busy_month.values,color='orange')
                ax.set_ylabel('Messages')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            # st.title("Weekly Activity Map")
            st.markdown("<h1 style='color: green;'>Weekly Activity Map</h1>", unsafe_allow_html=True)
            user_heatmap = helper.activity_heatmap(selected_user,df)
            fig,ax = plt.subplots()
            ax = sns.heatmap(user_heatmap, cmap="coolwarm")
            ax.set_xlabel("Hours of Day")
            ax.set_ylabel("WeekDay")
            st.pyplot(fig)
            
            
            col1, col2 = st.columns(2)

            # finding the busiest users in the group(Group level)
            if selected_user == 'Overall':
                # st.title('Most Busy Users')
                st.markdown("<h1 style='color: green;'>Most Busy Users</h1>", unsafe_allow_html=True)
                x,new_df = helper.most_busy_users(df)
                fig, ax = plt.subplots()

                col1, col2 = st.columns(2)

                with col1:
                    ax.bar(x.index, x.values,color='red')
                    ax.set_ylabel("Messages")
                    plt.xticks(rotation='vertical')
                    st.pyplot(fig)

                with col2:
                    st.dataframe(new_df)


            most_common_df = helper.most_common_words(selected_user,df)

            fig, ax = plt.subplots()

            ax.barh(most_common_df[0],most_common_df[1], color='Grey')
            ax.set_ylabel("Words")
            ax.set_xlabel("Frequency of usage")
            plt.xticks(rotation='vertical')

            # st.title('Most common words')
            st.markdown("<h1 style='color: green;'>Most common words</h1>", unsafe_allow_html=True)
            st.pyplot(fig)

            



