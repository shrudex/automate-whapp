# AutomateWHAPP🗣️

**AutomateWhapp** is a handy tool for sending customized messages to multiple recipients on WhatsApp. Whether you need to send messages for different societies, clubs in colleges to schedule interviews, or any other group of people, _AutomateWhapp_ streamlines the process, saving you time and effort. It allows you to send _bulk messages_ with personalized _names, dates, and times_ to random phone numbers, all in just one click.

## Overview
- **AutomateWhapp** is a tool for sending customized WhatsApp messages to multiple recipients.
- It simplifies the process of sending bulk messages with personalized names, dates, and times.

## Technologies Used
**AutomateWhapp** utilizes several technologies to automate the messaging process, including:

- **React.js**: For the frontend of Version 1.
- **Tailwind CSS**: For styling the frontend of Version 1.
- **Python Flask**: As the backend of Version 1.
- **Streamlit**: For the frontend and backend of Version 2.
- **PyQt**: For creating the standalone application in Version 3.
- **PyAutoGUI**: For automation of tasks.
- **openpyxl**: For Excel file operations.
- **pyperclip**: To save custom messages to the clipboard.

## Features

- Send _customized messages_ to multiple WhatsApp contacts.
- Upload an Excel file with the following columns: **NAME**, **PHONE**, **DATE**, **TIME**, and a custom message.
- Automate the sending of messages with custom NAME, DATE, and TIME according to the Excel file.
- Works seamlessly with _WhatsApp Web_.

## Installation

AutomateWhapp offers three different versions for your convenience:

### Version 1 - React.js + Tailwind CSS + Python Flask

1. Clone the repository.
2. Run the following commands in your terminal:
   
   ```bash
   npm install
   pip install -r requirements.txt
   npm run dev
   python app.py
   ```
3. Once the server is running, navigate to the provided URL in your web browser.

### Version 2 - Streamlit

1. Install the required Python packages by running:
```bash
pip install -r requirements.txt
```
2. Start the Streamlit application by running:
```bash
streamlit run streamlit.py
```

### Version 3 - Standalone Application
Download the standalone executable application (**automateWHAPP.exe**) and the reference Excel file (**excelSheet.xlsx**). \
Follow these steps:
1. Run the *automateWHAPP.exe* file.
2. Specify the location of the Excel file.
3. Enter your custom message.
4. Ensure that WhatsApp Web is logged in.
5. Click the button to start sending customized messages.

## Excel File Format
The Excel file should have four columns: **NAME**, **PHONE**, **DATE**, and **TIME**. The _custom message_ can be included in one of the columns with variables like NAME, DATE, and TIME **capitalized** for customization.

## Screenshot
![image](https://github.com/shrudex/automate-whapp/assets/91502997/599d470d-2036-41a8-9675-9c0bd539f563)


Feel free to download the **automateWHAPP.exe** and the sample **excelSheet.xlsx** to get started. \ 
Add your recipient details to the Excel file, customize your message, ensure that WhatsApp Web is _logged in_, and you're ready to automate your WhatsApp messages!


#### Happy automating with **AutomateWhapp**!💪🏻👨🏻‍💻




