


from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Wellcome to Rohit's Profile", page_icon=":tada:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#load Annimation
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_wqypnpu5.json")
img_contact_from = Image.open("aaa.jpg")
img_lottie_animation = Image.open("ccc.jpg")

img_contact_from1 = Image.open("zzz2.jpg")
img_lottie_animation1 = Image.open("yyy2.jpg")

with st.container():
    st.title("I AM 'ROHIT'")
    st.subheader("Hello, Welcome to My Website :wave: :smile:")
    st.write("----")
    st.subheader("I am a 'Python Developer' & 'Data Analyst'")
    st.write("I am from Betul Madhya Pradesh [INDIA]")
    st.write("My Resume - [learn More >](https://drive.google.com/file/d/15aEbCbVkIcx_5S628IG3rPpzlzqw23GP/view?usp=sharing)")

with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("know more about me")
        st.write("##")
        st.write(
            """
        I am an enthusiastic and motivated individual with
        a strong passion for data analytics and a 
        background in Computer Applications. Proficient in
        Python programming, I have experience in statistical
        analysis, data visualization, and machine learning techniques. 
        Through my recent data science internship,
        I honed my skills in monitoring process efficiencies, improving business performance,
        and developing predictive models. With a Master's degree in Computer Application and a 
        Bachelor's degree in Science, I am equipped with a solid educational foundation. 
        I am excited to contribute my expertise and knowledge to a dynamic organization in the
        field of 'Data Analyst' and 'Python Backend Devloper' .
            """
        )
        st.write(" Here Is My linkedin Profile - [Click here >](https://www.linkedin.com/in/rohitrkvarathe111)")
    with right_column:
       st_lottie(lottie_coding, height=500, key="coding")

#-------- Project------
with st.container():
    st.write("----")
    st.header("➡️ My Project 1.")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
       st.image(img_lottie_animation)
    with image_column:
        st.image(img_contact_from)

    with text_column:
        st.subheader("STOCK PRICE PREDICTION 📈")
        st.write("Analyzing the data using visual techniques :--")

        st.write(
            """
            Here I to present to you an exciting project in the field of data science - a machine learning model to predict stock prices.
            With advances in machine learning, we are now able to analyze and process large amounts of data to make predictions about the future
            behavior of stocks. Our team has developed a machine learning model that uses historical stock prices, financial statements, news 
            articles,and other relevant data to predict the future price of a stock. We trained the model on a large dataset and fine-tuned it 
            to improve its accuracy and reliability.By analyzing historical data, our model can identify trends and patterns that may indicate 
            future market movements, allowing investors to make informed decisions. In conclusion, our machine learning model for predicting 
            stock prices represents an exciting development in the field of data science.
            """
        )
        st.markdown("Watch My Project [Click here....](https://github.com/rohitrkvarathe111/Stock-Price-Prediction-)")

        st.write("----")

with st.container():
    st.write("----")
    st.header("➡️ My Project 2.")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
       st.image(img_lottie_animation1)
    with image_column:
        st.image(img_contact_from1)
    with text_column:
        st.subheader("WINE QUALITY ANALYSIS 🍷")
        st.write("Wine quality data prediction analysis using Machine Learning :--")
        st.write(
            """
            Wine Quality Analysis ML Data Science Project. Our team is a machine learning model that can accurately predict wine quality based on
            various chemical characteristics. We started by collecting a large dataset of wine samples, including their respective chemical compositions. 
            We then used this data to train our model, which includes Decision Random Forest and several algorithms.  
            Our model takes into account many important chemical factors such as pH level, alcohol content and volatile acidity and can accurately predict 
            wine quality on a scale of 1 to 10. We believe that our wine quality analysis ML model could have a significant impact on the wine industry,
            enabling winemakers to continually improve the quality of their products by optimizing their production processes
            """
        )
        st.markdown("Watch My Project [Click here....](https://github.com/rohitrkvarathe111/Wine-Quality-Data-Exploration-and-Analysis-Python)")

        st.write("----")



#-------CONTACT ------
with st.container():
    st.write("---")
    st.header("Get In Touch With Me !")
    st.write("##")

    contact_form = """
     <form action="https://formsubmit.co/rohitrkvarathe111@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder= "Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
     </form>
     """
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
with left_column:
    st.write("[Click here  ](https://forms.gle/KVAoak1mW6m9hRCy7) to contact me")
st.write("---")




import streamlit as st

st.markdown("<h1 style='text-align: center; color: blue; font-size: 80px;'>Thankyou for visiting my Website</h1>", unsafe_allow_html=True)


#toolbar -- Home, About, Contact
import streamlit as st
from PIL import Image

# Load the image
image = Image.open("bbb.jpg")

# Display the image in its original size
st.image(image, use_column_width=True)

import streamlit as st

# Create a sidebar toolbar
toolbar_selection = st.sidebar.radio("Toolbar", ("Home", "About", "Contact"))

# Define the content for each toolbar item
if toolbar_selection == "Home":
    st.write("Welcome to the Home page!,but page is under construction..")
elif toolbar_selection == "About":
    st.write("This is the About page.")
elif toolbar_selection == "Contact":
    # Open a new window when "Contact" is clicked
    st.write("Contact page is under construction...")
    if st.button("Open New Window"):
        # Open a new browser tab with the URL
        new_window_url = "Photo by Guilherme Rossi from Pexels: https://www.pexels.com/photo/concrete-bridge-near-buildings-during-golden-hour-1755683/"
        js_code = f"window.open('{new_window_url}')"
        st.write(f'<script>{js_code}</script>', unsafe_allow_html=True)



##lottie upload
lottie_coding1 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_3rqwsqnj.json")


#with st.container():
 #   st.write("----")
  #  left_column, right_column = st.columns(2)

   # with right_column:
st.write("----")
st_lottie(lottie_coding1, height=700, key="coding1")


lottie_coding2 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_1CKhDgcctU.json")
st_lottie(lottie_coding2, height=1000, key="coding2")






##Chatboot
import streamlit as st

# Define a list of sample questions and corresponding answers
qa_pairs = [
    {
        'question': 'What is your name?',
        'answer': 'My name is ChatBot.'
    },
    {
        'question': 'hii?',
        'answer': 'hello .how can i help you.'
    },
    {
        'question': 'How are you?',
        'answer': 'I am doing well, thank you!'
    },
    {
        'question': 'What can you do?',
        'answer': 'I can assist you with answering questions.'
    }
]

# Function to get the response for a given question
def get_response(question):
    for pair in qa_pairs:
        if question.lower() in pair['question'].lower():
            return pair['answer']
    return 'I am sorry, but I do not have an answer for that question.'

# Streamlit app
st.title('ChatBot')
st.write('Welcome! I am a simple chatbot. How can I assist you?')

# User input
user_input = st.text_input('You:', key='user_input')

# Chatbot response
if st.button('Send'):
    if user_input.strip() != '':
        response = get_response(user_input)
        st.text_area('ChatBot:', value=response, height=100, key='chatbot_response')
    else:
        st.warning('Please enter a question.')

# Instructions
st.markdown('---')
st.markdown('**Instructions:**')
st.write('- Type a question in the input box.')
st.write('- Click the "Send" button to get the chatbot\'s response.')


##WHATSAPP
import streamlit as st
import requests

# WhatsApp API endpoint
API_URL = "https://api.whatsapp.com/send"

# Your WhatsApp business phone number
phone_number = "<.........>"

def send_whatsapp_message(message):
    # Prepare the URL for the WhatsApp chat
    url = f"{API_URL}?phone={phone_number}&text={message}"
    
    # Open the WhatsApp chat URL
    st.write(f"Click [here]({url}) to start a WhatsApp chat.")

# Streamlit app
def main():
    st.title("WhatsApp Chat Integration")
    
    # Input field for user message
    user_message = st.text_input("Enter your message")
    
    # Send message button
    if st.button("Send Message"):
        send_whatsapp_message(user_message)

if __name__ == "__main__":
    main()










##Live watch
import streamlit as st
import datetime
import time

# Create an empty space to display the time
time_placeholder = st.empty()

# Update the time continuously
while True:
    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Update the placeholder with the current time
    time_placeholder.markdown(f"<h1 style='text-align: center;'>{current_time}</h1>", unsafe_allow_html=True)

    # Delay for 1 second before updating again
    time.sleep(1)




