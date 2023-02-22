import streamlit as st
import LinearReg
import SMS_Spam_Prediction_proj
import WhatsApp_app
import IPL_Youtube
import requests
from io import BytesIO
# st.set_option('browser.serverAddress', '127.0.0.1')

# Define function for main page
#def show_main_page():
def show_main_page():
    
    
    import streamlit as st
    from PIL import Image

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://media.istockphoto.com/id/1005466206/photo/orange-creased-tissue-paper-background-texture.jpg?s=612x612&w=0&k=20&c=RMIK3NBPuC0X0Y6DkU-rt4uEELjJvQ0eFku3uOViChg=");
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

    col1, col2 = st.columns(2,gap= 'small')

    with col1:

#         image = Image.open(r"C:\Users\Lakshmeesh s reddy\Desktop\Dinku\JOB\Pages\Pages\profile-picCLR.png")  
#         st.image(image, width=230)
#          https://raw.githubusercontent.com/LakshmeeshSR/DigitalCV/main/profile-picCLR.png       
        url = "https://raw.githubusercontent.com/LakshmeeshSR/DigitalCV/main/profile-picCLR.png?token=GHSAT0AAAAAAB7DTZYO4SY3JZ3CZYAR3KXUY7V2M4A"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, width=230)

    with col2:

        st.write("<h1 style='text-align: left; color: #763E3E; font-size: 30px; font-family:Century Gothic;'>Lakshmeesh S Reddy</h1>", unsafe_allow_html=True)

        text = "An enthusiast in Data Science, full of zeal in applying it in real time situations and contributing in the growth of society. Successful in taking up challenging projects in Engineering, internship and as a Trainee Engineer."
        st.write("<p style='text-align: left; color: white; font-size: 20px; font-family: Calibri;'>{}</p>".format(text), unsafe_allow_html=True)

        contacts = "📳 +91 9739836908&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📧 <a href='mailto:lakshmeeshsr@gmail.com'>lakshmeeshsr@gmail.com</a>"

        st.write("<p style='text-align: left; color: black; font-size: 15px; font-family: Calibri;'>{}</p>".format(contacts), unsafe_allow_html=True)


    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Education 🎓</h1>", unsafe_allow_html=True)

    text = [
        "• 🧑‍🎓 Mechanical Engineering (2021), <span style='font-size: 18px;'>7.87 CGPA</span>, <span style='font-size: 18px;'>Vemana IT, Bengaluru</span>",
        "• 🙋‍♂️ PUC (2017), <span style='font-size: 18px;'>76%</span>, <span style='font-size: 18px;'>Jain College, Bengaluru</span>",
        "• 🚴 S.S.L.C (2015), <span style='font-size: 18px;'>84.96%</span>, <span style='font-size: 18px;'>Sudarshan Vidya Mandir, Bengaluru</span>"
    ]

    for line in text:
        st.write(f'<p style="color: white; font-size: 20px; font-family: Arial;">{line}</p>', unsafe_allow_html=True)

    st.write("#")
    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Skills 🛠️</h1>", unsafe_allow_html=True)

    st.write(
        """
        <div style='color: white; font-size: 20px; font-family: Arial; display: flex;'>
            <div style='margin-right: 10px;'>• 👩‍💻 Programming:</div>
            <div style='color: white; font-family: Arial;'>Python (Scikit-learn, Pandas, Matplotlib), Streamlit</div>
        </div>
        
        <div style='color: white; font-size: 20px; font-family: Arial; display: flex;'>
            <div style='margin-right: 10px;'>• 📊 Data Visualization:</div>
            <div style='color: white; font-family: Arial;'>PowerBi, MS Excel</div>
        </div>

        <div style='color: white; font-size: 20px; font-family: Arial; display: flex;'>
            <div style='margin-right: 10px;'>• 📈 Modeling:</div>
            <div style='color: white; font-family: Arial;'>Logistic regression, linear regression, NLP*</div>
        </div>

        <div style='color: white; font-size: 20px; font-family: Arial; display: flex;'>
            <div style='margin-right: 10px;'>• 🗄️ Databases:</div>
            <div style='color: white; font-family: Arial;'>MS SQL</div>
        </div>

        """, unsafe_allow_html=True
    )
    st.write("#")
    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Experience 🏢</h1>", unsafe_allow_html=True)

    # Set the font family, size, and color for the app
    st.markdown(
        """
        <style>
        .title {
            font-family: Arial;
            font-size: 24px;
            font-weight: bold;
            color: white;
        }
        .subtitle {
            font-family: Arial;
            font-size: 20px;
            font-style: italic;
            color: white;
        }
        .text {
            font-family: Arial;
            font-size: 20px;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the information in the app with formatting
    st.markdown("<p class='title'>Axcend Automation and software solution, Bengaluru</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Trainee Engineer, Sept 2021 – Aug 2022</p>", unsafe_allow_html=True)

    st.markdown("<p class='text'>1. Was a part of Wire Harness project, responsible for</p>", unsafe_allow_html=True)
    st.markdown("<ul class='text'><li>Data cleaning</li><li>Maintaining Data in SQL database</li><li>CAD design alterations based on drawing</li><li>Dashboard preparation for the operator</li></ul>", unsafe_allow_html=True)

    st.markdown("<p class='text'>2. Was a part of Digitization project of a manufacturing hub</p>", unsafe_allow_html=True)
    st.markdown("<ul class='text'><li>Data collection and cleaning using Excel</li></ul>", unsafe_allow_html=True)
    #######################################################
    st.write("#")
    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Engineering Project 🏫</h1>", unsafe_allow_html=True)

    # st.markdown("<p class='text'> \"Customizing cassette ceiling AC and incorporating lights, speakers and projector along with voice enabled feature.Performing analysis to determine the characteristics of flow\"</p>", unsafe_allow_html=True)
    
    col1,col2 = st.columns(2,gap="small")
    # col1, col2, col3 = st.columns([0.2, 0.5, 0.2])
    with col1:
        st.write("#")
        st.markdown("<p class='text'>Designed cassette ceiling AC with integrated lights, speakers and projector along with voice enabled features. Also performed flow analysis.</p>", unsafe_allow_html=True)
    
    with col2:
# C:\Users\Lakshmeesh s reddy\Desktop\Dinku\JOB\Pages\Pages\SmartAC-removebg.png
#         image_2 = Image.open(r"")
#         st.image(image_2,width=250)
        
        response = requests.get("https://raw.githubusercontent.com/LakshmeeshSR/DigitalCV/main/SmartAC-removebg.png?token=GHSAT0AAAAAAB7DTZYOJRTUG2LG7MEK6EKCY7V2QOA")
        img = Image.open(BytesIO(response.content))
        st.image(img, width=230)
    
    ##############################################################

    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Internships 👷‍♂️</h1>", unsafe_allow_html=True)

    st.markdown("<p class='title'>Aditi Precision Technology</p>", unsafe_allow_html=True)
    st.markdown("<p class='text'>●	Designing components using Solid works software.</p>", unsafe_allow_html=True)
    st.markdown("<p class='title'>Prinston Smart Engineers</p>", unsafe_allow_html=True)
    st.markdown("<p class='text'>●	Determining Heat load in different conditions using E20 sheet.</p>", unsafe_allow_html=True)
    ##############################################################
    st.write("#")

    st.write("<h1 style='text-align: left; color: #763E3E; font-size: 26px; font-family:Century Gothic;'>Certificate Courses 📄</h1>", unsafe_allow_html=True)

    st.markdown("<p class='text'>●	Google Data Analytics Professional Certificate, Coursera</p>", unsafe_allow_html=True)
    st.markdown("<p class='text'>●	Python 101 for Data Science, Cognitiveclass.ai, Powered by IBM</p>", unsafe_allow_html=True)
    st.markdown("<p class='text'>●	Data Science Methodology, Cognitiveclass.ai, Powered by IBM</p>", unsafe_allow_html=True)
    st.markdown("<p class='text'>●	PowerBI workshop, Growth School</p>", unsafe_allow_html=True)


    txt = "👈👈👈PROJECTS" 
    st.write("#")
    st.write("#")
    st.write("<p style='text-align: left; black: white; font-size: 20px; font-family: Calibri;'>{}</p>".format(txt), unsafe_allow_html=True)


def select_project():
    st.sidebar.title("Select a project")    
    # project01 = st.sidebar.radio("Home", ["Home"])
    project = st.sidebar.selectbox('Projects', ["Home","Linear Regression", "IPL Analysis using Youtube API" , "Logistic Regression","WhatsApp Chat analyzer"])
    return project



# Handle project selection
project = select_project()

if project == "Linear Regression":
    LinearReg.run()

 
elif project == "IPL Analysis using Youtube API":
    IPL_Youtube.run()

    
elif project == "Logistic Regression":
    SMS_Spam_Prediction_proj.run()

elif project == "WhatsApp Chat analyzer":
    WhatsApp_app.run()



else:
    show_main_page()


