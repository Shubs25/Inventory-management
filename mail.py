import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key='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')
from_email = Email("d20z601@psgitech.ac.in")  # Change to your verified sender
to_email = To("19cs146@psgitech.ac.in")  # Change to your recipient
subject = 'Test email from sendgrid API'
content = Content("text/plain", "Hello, this is a test")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)
print('done')