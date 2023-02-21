def run():
    import streamlit as st
    import pickle
    import string
    from nltk.corpus import stopwords
    import nltk
    from nltk.stem.porter import PorterStemmer
    from PIL import Image



    ps = PorterStemmer()

# ec8100
    text = "SMS Spam Detector"

    st.write(
        """
        <div style="position: relative; height: 50px; width: 100%;">
            <h1 style="position: relative; top: -65px; left: 0%; color:#A2EDF4; font-size:60px; font-family: Arial Rounded MT Bold; font-style: BOLD">{}</h1>
        </div>
        """.format(text),
        unsafe_allow_html=True
    )
# https://www.shutterstock.com/image-photo/sea-andes-mountains-over-clouds-260nw-1905247738.jpg

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://pbs.twimg.com/media/E5IlF6SWQAEQ09k.jpg");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat;
    opacity: 1;
    background-attachment: scroll;
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



    def transform_text(text):
        text = text.lower()
        text = nltk.word_tokenize(text)
        
        y = []
        for i in text:
            if i.isalnum():
                y.append(i)
        
        text = y[:]
        y.clear()
        
        stop_words = set(stopwords.words('english'))
        for i in text:
            if i not in stop_words and i not in string.punctuation:
                y.append(i)
                
        text = y[:]
        y.clear()
        
        ps = PorterStemmer()
        for i in text:
            y.append(ps.stem(i))
        
        return " ".join(y)


    tfidf = pickle.load(open(r'C:\Users\Lakshmeesh s reddy\Desktop\Dinku\JOB\SMS_Spam_Project\SMS_Spam_vectorizer.pkl','rb'))
    model = pickle.load(open(r'C:\Users\Lakshmeesh s reddy\Desktop\Dinku\JOB\SMS_Spam_Project\SMS_Spam_model.pkl','rb'))


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

    #if input_sms != None:
    st.markdown('<p style="color: skyblue; font-style: Bold; font-size:30px">Enter message</p>', unsafe_allow_html=True)
    input_sms = st.text_area("")
    

    if st.button('Detect'):

     
        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. predict
        result = model.predict(vector_input)[0]
        # 4. Display

        if len(input_sms.strip()) == 0:
            # st.error("Please enter a message", style='color: red')
            st.markdown('<p style="color: Darkorange; font-style: Bold; font-size:30px">Please enter a message</p>', unsafe_allow_html=True)

        else:
                
            if result == 0:
                text_01 = "Hey! It is not a Spam"

                st.write(
                """
                <div style="position: relative; height: -0px; width: 100%;">
                    <h1 style="position: relative; top: -35px; left: 0%; color:#FFFFFF; font-size:30px; font-style: Bold">{}</h1>
                </div>
                """.format(text_01),
                unsafe_allow_html=True
            )

        
                
            else:
                text_02 = "Ooops! It is a Spam"
            

                st.write(
                """
                <div style="position: relative; height: -0px; width: 100%;">
                    <h1 style="position: relative; top: -35px; left: 0%; color:#FFFFFF; font-size:30px; font-style: Bold">{}</h1>
                </div>
                """.format(text_02),
                unsafe_allow_html=True
            )

   
    
    st.write(
        "<div style='position:fixed; bottom: 35px; left:25%; z-index: 1;'>",
        "<p style='font-size: 20px; color: red; font-style: italic'> * The data isn't real time </p>",
        "<p style='font-size: 20px; color: red; font-style: italic;'> * Raw data courtesy - <a style='text-decoration: none; color: red;' href='https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset'>https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset -</p>",
        "</div>",
        unsafe_allow_html=True,
    )
