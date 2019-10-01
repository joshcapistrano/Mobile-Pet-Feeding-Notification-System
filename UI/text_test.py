import smtplib


def text(email):
    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )

    server.starttls()

    receivers = ['9082090019@mms.att.net']
    receivers.append(email)

    server.login( 'capstoneece2019@gmail.com', 'Ratpatrol$$' )

    # Send text message through SMS gateway of destination number
    server.sendmail( '9082090020', receivers , 'Your pet needs to be fed!' )

#Sprint:@pm.sprint.com
#Verizon:@vtext.com
#AT&T:@mms.att.net
#Tmobile:@tmomail.net


