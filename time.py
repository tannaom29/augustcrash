def run():
    import yfinance as yf
    import pandas as pd
    from email.utils import formataddr
    import warnings
    warnings.filterwarnings("ignore")

    ds = pd.read_csv('db.csv')
    df = pd.read_csv('crash.csv')

    list1= ['RELIANCE.NS','HDFCBANK.NS','INFY.NS','ICICIBANK.NS','HDFC.NS','TCS.NS','KOTAKBANK.NS','ITC.NS','HINDUNILVR.NS','LT.NS','SBIN.NS','AXISBANK.NS','BHARTIARTL.NS','BAJFINANCE.NS','ASIANPAINT.NS','MARUTI.NS','M&M.NS','HCLTECH.NS','SUNPHARMA.NS','TITAN.NS','TATAMOTORS.NS','POWERGRID.NS','TATASTEEL.NS', 'NTPC.NS', 'BAJAJFINSV.NS', 'ULTRACEMCO.NS','TECHM.NS','NESTLEIND.NS','WIPRO.NS','ONGC.NS','JSWSTEEL.NS','DRREDDY.NS','INDUSINDBK.NS','HDFCLIFE.NS','GRASIM.NS','CIPLA.NS','HINDALCO.NS','ADANIPORTS.NS','SBILIFE.NS','BAJAJ-AUTO.NS','DIVISLAB.NS','TATACONSUM.NS','BRITANNIA.NS','COALINDIA.NS','EICHERMOT.NS','APOLLOHOSP.NS','HEROMOTOCO.NS','UPL.NS','BPCL.NS','SHREECEM.NS']

    count=0

    for values in list1:
        msft = yf.Ticker(f"{values}")
        hist = msft.history(period="1d", interval="1d")
        ser = pd.Series(hist['Close'])
        df['Close'][count]=round(ser[0], 2)


        df['Percentage Change'][count] =  ((round(ser[0],2)-round(ds['26-Aug-22'][count],2))/round(ds['26-Aug-22'][count],2))*100
        df['Month Change'][count] = ((round(ser[0],2)-round(ds['Month Change'][count],2))/round(ds['Month Change'][count],2))*100
        count = count+1

    del df['Unnamed: 0']
    df = df.rename(columns = {"Percentage Change":"August_Crash"})
    def Highlight_Majors(val):

        color = 'black' if type(val) == str else 'dark'
        if color=='dark' and val<50:
            color = 'red' if val < 0 else 'black'
            color = 'green' if val > 0 else color
        return 'color: %s' % color

    df = df.style.applymap(Highlight_Majors)
    df.to_excel("output.xlsx")

    import openpyxl
    worksheet = openpyxl.load_workbook("output.xlsx")
    sheet = worksheet.active
    sheet.column_dimensions['A'].width = 5
    sheet.column_dimensions['B'].width = 35
    sheet.column_dimensions['C'].width = 10
    sheet.column_dimensions['D'].width = 15
    sheet.column_dimensions['E'].width = 14
    worksheet.save("output.xlsx")

    import jpype
    jpype.startJVM()
    from asposecells.api import Workbook, SaveFormat

    # Load Excel file
    workbook = Workbook("output.xlsx")
    # Convert Excel to PDF
    workbook.save("final.pdf", SaveFormat.PDF)

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime

    x = datetime.datetime.now()

    body = f'''
    Hello,

    Kindly Find Below Today's({x}) Stock Report [[After Crash - August Crash]]

    Yours sincerely

    Booyah!
    '''

    sender = 'stocksdetails12345@gmail.com'

    password = 'wkucubjnjkvouaea'

    receiver = "tannahiren42@gmail.com, tannaom69@gmail.com"

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = formataddr(('Stockpile Update', 'stocksdetails12345@gmail.com'))
    message['To'] = "tannahiren42@gmail.com, tannaom69@gmail.com"
    message['Subject'] = 'This email has an attacment, a pdf file'

    message.attach(MIMEText(body, 'plain'))

    pdfname = 'final.pdf'

    # open the file in bynary
    binary_pdf = open(pdfname, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    # payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())

    # enconding the binary into base64
    encoders.encode_base64(payload)

    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)

    #use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)

    #enable security
    session.starttls()

    #login with mail_id and password
    session.login(sender, password)

    text = message.as_string()
    session.sendmail(sender, receiver.split(","), text)
    session.quit()
    print('Mail Sent')

import pandas_market_calendars as mcal
import pandas as pd
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import yfinance as yf
nyse = mcal.get_calendar('XBOM')
abcd = nyse.valid_days(start_date=date.today(), end_date=date.today())

if(abcd.size==1):
    db = pd.read_csv('db.csv')
    
    input = db['Date'][0]
    format = '%d-%m-%Y'
    datetime = datetime.datetime.strptime(input, format)
    datetime = datetime.month
    datetime

    
    today = date.today()
    datem = today.month
    datem
    
    if(datetime-datem!=0):
        tickers_list = ['RELIANCE.NS','HDFCBANK.NS','INFY.NS','ICICIBANK.NS','HDFC.NS','TCS.NS','KOTAKBANK.NS','ITC.NS','HINDUNILVR.NS','LT.NS','SBIN.NS','AXISBANK.NS','BHARTIARTL.NS','BAJFINANCE.NS','ASIANPAINT.NS','MARUTI.NS','M&M.NS','HCLTECH.NS','SUNPHARMA.NS','TITAN.NS','TATAMOTORS.NS','POWERGRID.NS','TATASTEEL.NS', 'NTPC.NS', 'BAJAJFINSV.NS', 'ULTRACEMCO.NS','TECHM.NS','NESTLEIND.NS','WIPRO.NS','ONGC.NS','JSWSTEEL.NS','DRREDDY.NS','INDUSINDBK.NS','HDFCLIFE.NS','GRASIM.NS','CIPLA.NS','HINDALCO.NS','ADANIPORTS.NS','SBILIFE.NS','BAJAJ-AUTO.NS','DIVISLAB.NS','TATACONSUM.NS','BRITANNIA.NS','COALINDIA.NS','EICHERMOT.NS','APOLLOHOSP.NS','HEROMOTOCO.NS','UPL.NS','BPCL.NS','SHREECEM.NS']

        db = pd.read_csv('db.csv')
        count=0

        for items in tickers_list:
            data = yf.download(items,date.today())
            data=data.head(1)
            data['Close'].iloc[0]
            db['Month Change'][count]=data['Close'].iloc[0]
            count=count+1
        db['Date'] = date.today()
    run()