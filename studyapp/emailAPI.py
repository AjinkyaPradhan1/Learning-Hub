def sendEmail(email,password):
    import smtplib 
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
	
    me = "ajinkyappradhan@gmail.com"
    you = email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Verification Mail For Learning Hub"
    msg['From'] = me
    msg['To'] = you

    html = """<html>
  					<head></head>
  					<body>
    					<h1>Welcome to Learning Hub</h1>
                        <h4><i>Knowledge is the way to achieve immortality</i></h4>
                        <br>
    					<p>You have successfully registered ,Click on the link below to verify your account</p>
    					<h3>Username : """+email+"""</h3>
    					<h3>Password : """+str(password)+"""</h3>
    					<br>
    					<a href='http://localhost:8000/verifyuser/?email="""+email+"""' >Click here to verify account</a>		
  					</body>
				</html>
    """
	
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("ajinkyappradhan@gmail.com", "ajinkya_2193027") 
	
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
	
    s.sendmail(me,you,str(msg)) 
    s.quit() 
    print("Mail sent to user successfully....")