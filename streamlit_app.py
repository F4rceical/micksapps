import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read( worksheet="Sheet1",
)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")



st.header('Timesheet')

with st.form('Enter Your Name and Choose Week'):
		st.text_input("Name")
		option = st.selectbox(
    		"Choose Week",
    		("29/07/2024", "5/08/24", "12/08/24", "19/08/24"),
)
		st.form_submit_button('Submit week')
	
# here we should get data that already exists for the person

with st.form('time sheet entry'):
   		Mon = st.number_input('Mon',0,7)
   		Tues = st.number_input('Tue',0,7)
   		Wed = st.number_input('Wed',0,7)
   		Thu = st.number_input('Thu',0,7)
   		Fri = st.number_input('Fri',0,7)
   		st.write("You selected:", option)
   		st.write("You selected:", "Mon -", Mon, "Tues - ",Tues, Wed, Thu, Fri)
   		st.form_submit_button('Submit Timesheet')

