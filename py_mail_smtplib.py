import smtplib

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart


sender_email = "example@gmail.com"                                            # sender email id
receiver_email = "example@example.com"                                        # receiver email id
sender_email_password = "example@password"                                    # password of sender email id
email_subject = "Type your email subject here"                                # email subject
msg_body = "Type your email content here. You can also add an attachment to this email"             # message body text
file_path = "C:\\Users\\admin\\Desktop\\"                                     # file path (directory)
file_name = "example_file.txt"                                                # attachment/file name with extension 



# don't mess up with the code below this comment unless you want to experiment 

msg = MIMEMultipart()
msg['Subject'] = email_subject                                              # mail subject
msg['From'] = sender_email                                                  # source/sender email
msg['To'] = receiver_email                                                  # receiver email
msg.attach(MIMEText(msg_body, 'plain'))                                     # attaching msg_body to msg


attachment = open(file_path+file_name+"","rb")                              # setting attachment directory & fileMode
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(part)                                                            # attaching file to msg


print("email content ready........")
server = smtplib.SMTP('smtp.gmail.com', 587)                                # gmail smtp tls port = 587
server.starttls()
print("server connceted......")
server.login(sender_email, sender_email_password)                           # login to gmail
print ("sending.........")
server.sendmail(sender_email, [receiver_email], msg.as_string())            # send email
print("email sent............")
server.quit()

