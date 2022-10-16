import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

data_rfm = pd.read_csv("rfm.csv") 
df=data_rfm.copy()
#df=data_rfm.copy().set_index("customer_no")
len_df=len(df)


st.header(" CUSTOMER RFM POINT INSPECTION")
st.subheader("(Data: Coworce )")

#st.image("rfm_metrics.png",width=600, caption="It is made of 3 main criterias?")
#st.image("champions.png",width=600,caption="Explore the groups ")
st.image("https://d35fo82fjcw0y8.cloudfront.net/2018/03/01013508/Incontent_image.png",width=600,caption="It is made of 3 main criterias? ")
st.image("https://d35fo82fjcw0y8.cloudfront.net/2018/03/01013239/Header-e1551869702205.png",width=600,caption="Explore the groups ")
st.image("rfm_explanation.PNG",width=600,caption="Explanation")
st.image("treemap.jpg",width=600,caption="Explanation")

st.write("## CUSTOMER RFM POINTS")
st.write()
st.write()

#======================================================================
#st.set_page_config(page_title ="RFM Analysis",page_icon= ":bar_chart:", layout= "wide")

df["customer_id"]=df["customer_id"].astype(str)
st.header("All Data:")
st.dataframe(df)

    
st.sidebar.subheader("Please type the Customer ID")
customers=df["customer_id"].drop_duplicates()
customer_id= st.sidebar.selectbox("Select the Customer",customers)

st.sidebar.subheader("Please select Segments")
segments=df["Segment"].drop_duplicates()
segments= st.sidebar.selectbox("Select Segments",segments)


df_selection = df.query(
    "customer_id == @customer_id")

st.subheader("Results of Customer Filter:")
st.write(df.loc[(df['customer_id']==customer_id)])
st.subheader("Results of Segment Filter:")
st.write(df.loc[(df['Segment']==segments)])



*________________________________________________

st.subheader(" Please choose the customer_no ")

st.info(" Total Number of Customers  : {}".format(len_df))

label1="first 2 digit"
label2="second 2 digit"
a=st.slider(label1, min_value=0, max_value=28, value=14,step=1, label_visibility="visible");
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




#___________________ Customer Loyalty Analysis____________________________

st.subheader(" Customer Loyalty Analysis ")
st.write("Any customer who has a recency score equal or greater than 4 and also has a Frequency score equal or greater than 2, accepted as LOYAL")

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Not Loyal', 'Loyal'

is_loyal=df[df["Is_Loyal"]=="Loyal"]
loyal_y=len(df[df["Is_Loyal"]=="Loyal"]["Is_Loyal"])
loyal_n=len(df[df["Is_Loyal"]=="Not Loyal"]["Is_Loyal"])

sizes = [loyal_n, loyal_y]
explode = (0,0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

st.write("""
How to Increase Customer Loyalty

1.Make customer service a priority – even on social
According to a Microsoft study, 90% of consumers across the globe consider customer service to be important in their choice of a brand.

2.Reward your customers
One of the best ways to keep customers coming back is to reward them for their loyalty. Set up a loyalty program that gives customers discounts, gifts and exclusive offers

3. Ask for advice and listen to it
When your mom gave you advice as a teenager, you rolled your eyes, got defensive and probably said something like, “She doesn’t know what she’s talking about.”
""")


#___________________ Customer Churn Analysis____________________________

st.subheader(" Customer Churn Analysis ")
# Churn ( passive)  If there are more than 6 months from the last purchase 
st.write("Customer churn is the percentage of customers that stopped using your company's product or service during a certain time frame")

labels = 'Active','Churn ( Passive)'
total_c=2819  #  total_customer
churn_c=921  #   churn_customer
active_c=total_c-churn_c

sizes = [active_c, churn_c]
explode = (0,0.1)  # only "explode" the 2nd slice )

fig2, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')    # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("The Last 6 months passive customer ratio ")
st.pyplot(fig2)

st.write("""How to Reduce Customer Churn
1. Focus your attention on your best customers.
Rather than simply focusing on offering incentives to customers who are considering churning, it could be even more beneficial to pool your resources into your loyal, profitable customers.

2. Analyze churn as it occurs.
Use your churned customers as a means of understanding why customers are leaving. Analyze how and when churn occurs in a customer's lifetime with your company, and use that data to put into place preemptive measures.

3. Show your customers that you care.
Instead of waiting to connect with your customers until they reach out to you, try a more proactive approach. Communicate with them all the perks you offer and show them you care about their experience, and they'll be sure to stick around.
""")
