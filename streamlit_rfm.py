import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
#import matplotlib.pyplot as plt

data_rfm = pd.read_csv("rfm.csv") 
df=data_rfm.copy().set_index("customer_no")
len_df=len(df)


st.header(" CUSTOMER RFM POINT INSPECTION")
st.subheader("(Data: Coworce )")

#st.image("rfm_metrics.png",width=600, caption="It is made of 3 main criterias?")
#st.image("champions.png",width=600,caption="Explore the groups ")
st.image("https://d35fo82fjcw0y8.cloudfront.net/2018/03/01013508/Incontent_image.png",width=600,caption="It is made of 3 main criterias? ")
st.image("https://d35fo82fjcw0y8.cloudfront.net/2018/03/01013239/Header-e1551869702205.png",width=600,caption="Explore the groups ")
st.image("rfm_explnation.png",width=600,caption="Explnation")


st.write("## CUSTOMER RFM POINTS")
st.write()
st.write()


st.subheader(" Please choose the customer_no ")

st.info(" Total Number of Customers  : {}".format(len_df))

label1="first 2 digit"
label2="second 2 digit"
a=st.slider(label1, min_value=1, max_value=28, value=14,step=1, label_visibility="visible");
b=st.slider(label2, min_value=0, max_value=19, value=10,step=1, label_visibility="visible")
c=a*100+b
st.write("CHOSEN CUSTOMER NO :", c)


dff=df.iloc[c-1]
st.table(dff)
st.write(dff)

dff=df[["Recency","Frequency","Monetary"]]
dff.hist()

sns.histplot(data=df[["Recency"]])
sns.histplot(data=df[["Frequency"]])
sns.histplot(data=df[["Monetary"]])


#________________________________
numeric=df.select_dtypes(include=['int64','float64']).columns
def plot_hist(f1,feature):
    fig = plt.figure(figsize=(10, 4))
    plt.hist(f1[feature], bins = 50)
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.title("{} distribution with hist".format(feature))
    plt.show()
    st.write(fig)      # st.pyplot(fig) 
#for n in numeric:
#   plot_hist(df,n)
#______________________________________

def hist_plot(f1, feature):
    fig, ax=plt.subplots(figsize=(10, 4))
    ax.hist([feature],bins=50)
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.title("{} distribution with hist".format(feature))
    plt.xlabel(feature)
    st.write(fig)

# for n in numeric:
#    hist_plot(df,n)

#______________________________________
objects=df.drop(["customer_id"],axis=1).select_dtypes(include=['object']).columns

def countPlot(f1,feature):
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x = feature, data = f1)
    st.pyplot(fig)
# for n in objects:
#    countPlot(df,n)




#------------------------------------------
# Violin plot
#------------------------------------------
#       ['customer_id', 'Recency', 'Frequency', 'Monetary', 'Recency_score',
#       'Frequency_score', 'Monetary_score', 'RFM_SCORE', 'Segment','Is_Loyal']


def violinStrip_plot():
    st.header("Violin & Strip Plot")
    sd = st.selectbox(
        "Select a Plot", #Drop Down Menu Name
        [
            "Violin Plot", #First option in menu
            "Strip Plot"   #Seconf option in menu
        ]
    )

    fig = plt.figure(figsize=(12, 6))

    if sd == "Violin Plot":
        sns.violinplot(x = "Monetary", y = "Frequency", data = df)
    
    elif sd == "Strip Plot":
        sns.stripplot(x = "Monetary", y = "Recency", data = df)

    st.pyplot(fig)

#violinStrip_plot()

  #------------------------------------------
