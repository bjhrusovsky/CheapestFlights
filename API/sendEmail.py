import rsa
from Utils.OpenJProperties import openFile
import smtplib
import Resources.passwordEncryption as Encrypt


"""If you wish to send an email to yourself or others you will need to setup your own
    api-config.properties file and set your ADC up within google. 
"""
def emailUser():

    configs = openFile("api-config.properties")
    '''
    Change these to your credentials and name
    '''
    privateKey, publicKey = Encrypt.loadKeys()
    encryptedPassword = open("../Resources/encrypted.password", "rb").read()
    pw = Encrypt.decrypt(encryptedPassword, privateKey)

    your_name = configs.get("name").data
    your_email = configs.get("email").data
    your_password = pw

    # If you are using something other than gmail
    # then change the 'smtp.gmail.com' and 465 in the line below
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, your_password)


    name = configs.get("name").data
    email = configs.get("email").data
    subject = 'Flight Data'
    message = configs.get("linkdata").data
    full_email = ("From: {0} <{1}>\n"
                      "To: {2} <{3}>\n"
                      "Subject: {4}\n\n"
                      "{5}"
                      .format(your_name, your_email, name, email, subject, message))

    try:
        server.sendmail(your_email, [email], full_email)
        print('Email to {} successfully sent!\n\n'.format(email))
    except Exception as e:
        print('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))

    # Close the smtp server
    server.close()

if __name__ == "__main__":
    emailUser()
