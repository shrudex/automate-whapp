from flask import Flask, request, jsonify
from flask_cors import CORS  
import openpyxl
#import pywhatkit as pw
#from datetime import datetime, timedelta
import pyautogui as pt
import time
import pyperclip
app = Flask(__name__)
CORS(app)  
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'excelFile' not in request.files:
            return jsonify({"error": "No file uploaded."}), 400

        excel_file = request.files['excelFile']
        if excel_file.filename == '':
            return jsonify({"error": "No file selected."}), 400

        workbook = openpyxl.load_workbook(excel_file)
        worksheet = workbook.active

        data = []
        user_message = request.form['wamessage']

        for row in worksheet.iter_rows(min_row=2, values_only=True):
            name, number, date, time = map(str, row)
            if name and number and date and time and name.lower() != "name":
                formatted_number = "+91" + str(number)
                data.append([name, formatted_number, date, time])
        screenWidth, screenHeight = pt.size()
        print(screenWidth, screenHeight)
        pt.hotkey("ctrl", "t")
        pt.sleep(1)
        for name, number, date, time in data:
            if name and date and time:
                message = user_message \
                    .replace("NAME", name) \
                    .replace("DATE", date) \
                    .replace("TIME", time)
                #current_time = datetime.now() + timedelta(minutes=1)

                #pw.sendwhatmsg(number, message, int(current_time.hour), int(current_time.minute), 13, True, 2)
                #time.sleep(30)
                waLink = "https://web.whatsapp.com/send?phone="+str(number)
                print(waLink)
                pyperclip.copy(message)
                #pt.hotkey("ctrl", "t")
                #pt.sleep(1)
                pt.hotkey("ctrl","l")
                pt.typewrite(waLink)
                pt.press("enter")
                pt.sleep(15)
                pt.click(x=(screenWidth*3)//4, y=(screenHeight*9)//10)
                
                #pt.typewrite(message)
                pt.hotkey('ctrl', 'v')
                pt.sleep(1)
                pt.press("enter")
                pt.sleep(3)
        pt.hotkey("ctrl", "w")

        return "File uploaded and data extracted successfully!", 200

    except Exception as e:
        print("Error processing Excel file:", str(e))
        return jsonify({"error": "Error processing the uploaded file."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
