import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import plotly.express as px

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("MoodQueue").sheet1

st.title("Vibe Meter")
st.subheader("What's your mood today?")

mood = st.selectbox("Select a mood", [ "😊 Happy","😠 Frustrated","😕 Confused","🎉 Excited","😢 Sad","😐 Neutral","😤 Overwhelmed","😅 Stressed but OK","🤔 Curious","🙄 Annoyed","😴 Tired","🥳 Celebrating","😇 Grateful"])
note = st.text_input("Optional note")

if st.button("Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, mood, note])
    st.success("Mood logged!")
    st.query_params["updated"] = str(datetime.now())

data = sheet.get_all_records()
df = pd.DataFrame(data)

if not df.empty:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Date'] = df['Timestamp'].dt.date
    today = datetime.today().date()
    df_today = df[df['Date'] == today]

    if not df_today.empty:
        chart_data = df_today['Mood'].value_counts().reset_index()
        chart_data.columns = ['Mood', 'Count']
        fig = px.bar(chart_data, x='Mood', y='Count', title="Today's Mood Distribution")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No moods logged today yet.")
else:
    st.info("No mood data available.")
