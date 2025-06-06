# Vibe Meter

This simple internal tool helps support agents log the emotional "mood" of the ticket queue throughout the day and visualize mood trends for the current date.

---

## Features

- Select and log a mood using a list of emojis
- Add an optional note helps in knowing the situation better
- Data is automatically saved to a Google Sheet
- Visualizes daily mood counts using a bar chart

---

## Built With

- [Streamlit](https://streamlit.io/)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [gspread](https://github.com/burnash/gspread)
- [Plotly](https://plotly.com/python/)

---

##  How to Run Locally

1. Go to this repo:
    https://github.com/alka57/Moodqueue.git
 
2. Set up Virtual environment
    
    python -m venv venv
    venv/Scripts/activate

3. Install dependencies:
    pip install -r requirements.txt

4. Adding the google sheets credentials.json file to this folder

5. Running the app
    streamlit run app.py


# For the google sheet setup the header row must be exactly Timestamp | Mood | Note and then share the sheet with the service account email as Editor


## Screenshots
### 1. Mood Logging Interface
    ![Vibe meter showing the dropdown of emojis and optional note] (./VibeMeter.png)

### 2. Mood chart for Today
    ![The chart describes the moods selected by individuals] (./ChartDistribution.png)

### 3. Google Sheet
    ![The Google sheet showing the timestamp, mood selected and alternative note] (./GoogleSheet.png)


# Google sheets link:
https://docs.google.com/spreadsheets/d/1B5qP5sDtB6Ry_2cWKVkQRZIMk_SSg8QidlpBuigk-08/edit?usp=sharing

Created by
FNU Alka
