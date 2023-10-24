import streamlit as st
import openpyxl
import pyautogui as pt
import pyperclip

st.title('AutomateWhapp')
st.markdown('Transform your WhatsApp messaging experience with streamlined automation and personalization.')

st.header('Upload an Excel file that contains:')
st.markdown('Name, Number, Time & Date')
uploaded_file = st.file_uploader('Upload your Excel file', type=['xlsx', 'xls'])

st.header('Enter the WhatsApp message to be sent!')
message = st.text_area('Write a message with variables capitalized...', key="input", height=200)

if st.button('Send BULK messages!'):
    if not uploaded_file:
        st.warning('Please upload an Excel file.')
    elif not message:
        st.warning('Please enter a message.')
    else:
        # Process the uploaded file and send messages
        workbook = openpyxl.load_workbook(uploaded_file)
        worksheet = workbook.active

        data = []

        for row in worksheet.iter_rows(min_row=2, values_only=True):
            name, number, date, time = map(str, row)
            if name and number and date and time and name.lower() != "name":
                formatted_number = "+91" + str(number)
                data.append([name, formatted_number, date, time])

        screenWidth, screenHeight = pt.size()
        pt.hotkey("ctrl", "t")
        pt.sleep(1)
        for name, number, date, time in data:
            if name and date and time:
                formatted_message = message \
                    .replace("NAME", name) \
                    .replace("DATE", date) \
                    .replace("TIME", time)
                
                waLink = "https://web.whatsapp.com/send?phone=" + str(number)
                pyperclip.copy(formatted_message)
                
                pt.hotkey("ctrl", "l")
                pt.typewrite(waLink)
                pt.press("enter")
                pt.sleep(15)
                pt.click(x=(screenWidth * 3) // 4, y=(screenHeight * 9) // 10)
                
                pt.hotkey('ctrl', 'v')
                pt.sleep(1)
                pt.press("enter")
                pt.sleep(3)
        pt.hotkey("ctrl", "w")
        st.success('Messages sent successfully.')
