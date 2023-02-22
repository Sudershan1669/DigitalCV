def run():

    import streamlit as st, pandas as pd, numpy as np
    import json
    import pickle
    import requests
    import io
    from sklearn.linear_model import LinearRegression



    text = "Select your dream home"

    st.write(
        """
        <div style="position: relative; height: 50px; width: 100%;">
            <h1 style="position: relative; top: -65px; left: 0%; color:#FF4B4B; font-size:60px; font-family: IMAGO BOLD">{}</h1>
        </div>
        """.format(text),
        unsafe_allow_html=True
    )


    text002 = "-- Your dream is not a dream any more"

    st.write(
        """
        <div style="position: relative; height: -65px; width: 100%;">
            <h1 style="position: relative; top: -55px; left: 60%; color:black; font-size:20px; font-style: italic">{}</h1>
        </div>
        """.format(text002),
        unsafe_allow_html=True
    )



    newfile = json.load(open("columns.json","r"))
    X = pd.DataFrame(newfile)
    options = list(newfile['data_columns'][3:])


    location = st.sidebar.selectbox('Location', options)

    sqft = st.sidebar.number_input("Enter square feet area", min_value=600, max_value=40000, step=50)



    bath = st.sidebar.slider('Bath', 0,10, 1)
    bhk = st.sidebar.slider('Bhk', 0,10, 1)

    data = {'Location' : location,
                'Total Square Feeet' :sqft,
                'Bathrooms' : bath,
                'BHK': bhk}

    features = pd.DataFrame(data, index=[0])


    df = pd.DataFrame(features)

    st.subheader('Features')


    st.dataframe(df)

    # Reads in saved classification model
#     load_clf = pickle.load(open(r'C:\Users\Lakshmeesh s reddy\Desktop\Dinku\JOB\Pages\model002.pickle','rb'))
    
    response = requests.get('https://raw.githubusercontent.com/LakshmeeshSR/DigitalCV/main/model002.pickle')
    file = io.BytesIO(response.content)
    load_clf = pickle.load(file)

    loc_index = X[X['data_columns'] == location].index[0]

    x = np.zeros(X.shape[0])
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1


    prediction = round(load_clf.predict([x])[0], 2)

    button = st.button("Click here")

    st.subheader('Estimation')


    if sqft > 0:

        #button = st.button("Click Me!")
        text = "Rs.{}/- per sqft".format(prediction)

        if button:
            st.write(
            """
            <div style="position: relative; height: 5px; width: 100%;">
                <h1 style="position: relative; top: -35px; left: 0%; color:#FF4B4B; font-size:30px; font-style: Bold">{}</h1>
            </div>
            """.format(text),
            unsafe_allow_html=True
            )

    else :
        st.write('please select sqft')


    st.subheader('Total Price')

    text003 = "Rs.{}/-".format(round(prediction*sqft, 2))

    if button:
        st.write(
            """
            <div style="position: relative; height: -0px; width: 100%;">
                <h1 style="position: relative; top: -35px; left: 0%; color:#FF4B4B; font-size:30px; font-style: Bold">{}</h1>
            </div>
            """.format(text003),
            unsafe_allow_html=True
        )

    st.write(
        "<div style='position:fixed; bottom: 35px; left:25%; z-index: 1;'>",
        "<p style='font-size: 14px; color: black; font-style: italic'> *The data isn't real time </p>",
        "<p style='font-size: 14px; color: black; font-style: italic;'> *Raw data courtesy - <a style='text-decoration: none; color: black;' href='https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data'>https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data</a> -</p>",
        "</div>",
        unsafe_allow_html=True,
    )


    page_bg_img = f"""
    <style>
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


    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://images.unsplash.com/photo-1619006179863-f65e2b0c8fba?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxjb2xsZWN0aW9uLXBhZ2V8MXw5Mjc1ODk1NXx8ZW58MHx8fHw%3D&w=1000&q=80");
    background-size: cover;

    background-position: top left;
    background-repeat: no-repeat;
    opacity: 1;
    background-attachment: local;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)







