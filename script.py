import schedule
import time

def job(t):
    print('process started')
#     import yfinance as yf
#     import pandas as pd
#     import warnings
#     warnings.filterwarnings("ignore")
#     import dataframe_image as dfi
#     from email.utils import formataddr

#     ds = pd.read_csv('db.csv')
#     df = pd.read_csv('crash.csv')

#     list1= ['RELIANCE.NS','HDFCBANK.NS','INFY.NS','ICICIBANK.NS','HDFC.NS','TCS.NS','KOTAKBANK.NS','ITC.NS','HINDUNILVR.NS','LT.NS','SBIN.NS','AXISBANK.NS','BHARTIARTL.NS','BAJFINANCE.NS','ASIANPAINT.NS','MARUTI.NS','M&M.NS','HCLTECH.NS','SUNPHARMA.NS','TITAN.NS','TATAMOTORS.NS','POWERGRID.NS','TATASTEEL.NS', 'NTPC.NS', 'BAJAJFINSV.NS', 'ULTRACEMCO.NS','TECHM.NS','NESTLEIND.NS','WIPRO.NS','ONGC.NS','JSWSTEEL.NS','DRREDDY.NS','INDUSINDBK.NS','HDFCLIFE.NS','GRASIM.NS','CIPLA.NS','HINDALCO.NS','ADANIPORTS.NS','SBILIFE.NS','BAJAJ-AUTO.NS','DIVISLAB.NS','TATACONSUM.NS','BRITANNIA.NS','COALINDIA.NS','EICHERMOT.NS','APOLLOHOSP.NS','HEROMOTOCO.NS','UPL.NS','BPCL.NS','SHREECEM.NS']

#     count=0

#     for values in list1:
#         msft = yf.Ticker(f"{values}")
#         hist = msft.history(period="1d", interval="1d")
#         ser = pd.Series(hist['Close'])
#         df['Close'][count]=round(ser[0], 2)


#         df['Percentage Change'][count] =  ((round(ser[0],2)-round(ds['26-Aug-22'][count],2))/round(ds['26-Aug-22'][count],2))*100

#         count = count+1

#     del df['Unnamed: 0']

#     def Highlight_Majors(val):

#         color = 'black' if type(val) == str else 'dark'
#         if color=='dark' and val<50:
#             color = 'red' if val < 0 else 'black'
#             color = 'green' if val > 0 else color
#         return 'color: %s' % color

#     df = df.style.applymap(Highlight_Majors)

#     dfi.export(df, 'df_styled.jpg')
#     print('image created')
#     import smtplib
#     from email.mime.multipart import MIMEMultipart
#     from email.mime.text import MIMEText
#     from email.mime.base import MIMEBase
#     from email import encoders
#     import datetime
#     # import pdfkit

#     x = datetime.datetime.now()

#     body = f'''
#     Hello,

#     Kindly Find Below Today's({x}) Stock Report [[After Crash - August Crash]]

#     Yours sincerely

#     Booyah!
#     '''

#     sender = 'stocksdetails12345@gmail.com'

#     password = 'wkucubjnjkvouaea'

#     receiver = "tannahiren42@gmail.com, tannaom69@gmail.com"

#     #Setup the MIME
#     message = MIMEMultipart()
#     message['From'] = formataddr(('Stockpile Update', 'stocksdetails12345@gmail.com'))
#     message['To'] = "tannahiren42@gmail.com, tannaom69@gmail.com"
#     message['Subject'] = 'This email has an attacment, a pdf file'

#     message.attach(MIMEText(body, 'plain'))
#     #

#     import img2pdf
#     from PIL import Image

#     # storing image path
#     img_path = "df_styled.jpg"

#     # storing pdf path
#     pdf_path = "final.pdf"

#     # opening image
#     image = Image.open(img_path)

#     # converting into chunks using img2pdf
#     pdf_bytes = img2pdf.convert(image.filename)

#     # opening or creating pdf file
#     file = open(pdf_path, "wb")

#     # writing pdf files with chunks
#     file.write(pdf_bytes)

#     # closing image file
#     image.close()

#     # closing pdf file
#     file.close()

#     #
#     print('pdf attached')
#     pdfname = 'final.pdf'

#     # open the file in bynary
#     binary_pdf = open(pdfname, 'rb')

#     payload = MIMEBase('application', 'octate-stream', Name=pdfname)
#     # payload = MIMEBase('application', 'pdf', Name=pdfname)
#     payload.set_payload((binary_pdf).read())

#     # enconding the binary into base64
#     encoders.encode_base64(payload)

#     # add header with pdf name
#     payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
#     message.attach(payload)

#     #use gmail with port
#     session = smtplib.SMTP('smtp.gmail.com', 587)

#     #enable security
#     session.starttls()

#     #login with mail_id and password
#     session.login(sender, password)

#     text = message.as_string()
#     session.sendmail(sender, receiver.split(","), text)
#     session.quit()
    print('Mail Sent')
    print(t)

schedule.every(1).minutes.at(":00").do(job,'It is 19:45')
while True:
    schedule.run_pending()
    time.sleep(6) # wait one minute
