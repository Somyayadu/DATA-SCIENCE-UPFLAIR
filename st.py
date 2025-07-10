## streamlit

import streamlit as st
import numpy as np
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import altair as alt
import time

st.set_page_config(
    page_title="streamlit function demo",
    page_icon="1",
    layout="centered"
)

st.title("hello world")
st.header("1. text elements")
st.subheader("markdown")
st.markdown("**bold text**,*italic text*,'code'text")
st.code("print('hello evaryone')",language="python")
st.latex(r"a^2+b^2=c^2")
st.divider()

#metrices and messages
st.header("2.metrices and messages")
st.metric(label="Revanue", value=1234, delta="+10%", delta_color="inverse")  #metric
st.error("This is an error message")  #error message
st.warning("This is a warning message")  #warning message   
st.info("This is an info message")  #info message
st.success("This is a success message")  #success message
st.exception("This is an exception message")  #exception message
st.divider()  #horizontal line



# data display 
st.header("3.Data display")
df=pd.DataFrame(np.random.randn(10, 3), columns=["a","b","c"])  #dataframe
st.dataframe(df) 
st.table(df.head(3)) 
st.json(df.to_dict())  
st.divider()


# charts
st.header("4. charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart=alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig ,ax =plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()

#widgets
st.header("5.widgets")
with st.form("Input form: "):
    name=st.text_input("Enter your name:",type="password")
    age=st.number_input("Enter your age:")
    mood=st.radio("Select your mood",("happy","sad","neutral"))
    languages = st.multiselect("Select your language:", ["hindi", "english", "spanish", "french"])

    #languages=st.multiselect("select your language:","hindi","english","spanish","french")
    submit=st.form_submit_button("submit")
    if submit:
        st.success(f"Name:{name},Age:{age},Mood:{mood},Language:{languages}")

col1,col2,col3=st.columns([4,1,1])   #width to be managed
with col1:
    st.text_input("Enter your name:",type="password")
    st.number_input("Enter your age:")


with col2:
    st.radio("Select your mood",("happy","sad","neutral"))
    st.multiselect("Select your language:", ["hindi", "english", "spanish", "french"])


with col3:
    st.title("output")    
# submit=st.form_submit_button("submit")
# if submit:
#         st.success(f"Name:{name},Age:{age},Mood:{mood},Language:{languages}")    


col1,col2=st.columns(2)
with col1:
     number=st.slider("select a number",0,100)        
with col2:
     colour=st.color_picker("select the colour")

st.text_area("Enter your message")
st.date_input("Select a date")
st.time_input("select the time")
st.file_uploader("upload a file")     
st.divider()

#media
st.header("6.media")
st.image("https://unsplash.com/photos/a-person-swimming-in-the-ocean-with-a-camera-NhWxAIs61MM")
#st.audio("")
st.video("https://pin.it/5fEvAdAqu")

# sidebar and layout 
st.sidebar.header("sidebar header")
st.sidebar.write("this is a side bar text")
st.sidebar.button("click me")
option= st.sidebar.selectbox("select an option",("option 1","option 2","option 3"))

with st.container():
    st.write("this is a container")

with st.expander("expand header"):
    st.write("this is an expander")

with st.spinner("loading data.."):
    time.sleep(2)

st.toast("toast message",icon="*")
