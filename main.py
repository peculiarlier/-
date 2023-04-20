import csv
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

with open("ads_data_121288_-_ads_data_121288.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        platform = row[3]
        event = row[2]
        if platform == 'web' and event == 'view':
            count1 += 1
        elif platform == 'web' and event == 'click':
          count2+=1
        elif platform == 'ios' and event == 'view':
          count3+=1
        elif platform == 'ios' and event == 'click':
          count4+=1
        elif platform == 'android' and event == 'view':
          count5+=1
        elif platform == 'android' and event == 'click':
          count6+=1
        else:
          count1, count2, count3, count4, count5, count6 = 0

data={"web":[count1, count2],
    "ios": [count3, count4],
    "android": [count5, count6]}
        
with open("new_data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["устройство", "просмотр", "клик"])
    for device, values in data.items():
        writer.writerow([device] + values)

def send_email(text=None):
    sender = "p10821356@gmail.com"
    password = "okbxbnjmflufnpyk"
    filename = "new_data.csv"
    polychai = "lera.tsydenova2003@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEMultipart()
        msg["Subject"] = "Результат проекта!"
        if text:
            msg.attach(MIMEText(text))

        attachment = open(filename, "rb") 
        part = MIMEBase("application", "octet-stream") 
        part.set_payload(attachment.read()) 
        encoders.encode_base64(part) 
        part.add_header("Content-Disposition", f"attachment; filename= {filename}") 
        msg.attach(part) 
        attachment.close() 

        server.sendmail(sender, polychai, msg.as_string())

        return "Письмо отправлено!"
    except Exception as _ex:
        return f"{_ex}\nНеправильный логин или пароль почты!"


def main():
    text = input("Напишите послание: ")
    print(send_email(text=text))


if __name__ == "__main__":
    main()
