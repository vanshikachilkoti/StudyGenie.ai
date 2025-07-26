import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_USER, EMAIL_PASS

def send_email(to, subject, body):
    # Format the roadmap content with line breaks and styling
    personalized_body = body.replace("[Your Name]", "Vanshika Chilkoti")
    formatted_body = personalized_body.replace('\n', '<br>')


    full_message = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <h2 style="color: #4CAF50;">📘 Your AI Learning Guide!</h2>
        <p>Greetings,</p>

        <p>We are excited to present you with a personalized curriculum designed to help guide you through your learning journey.</p>
        <p>This AI-generated curriculum has been created to provide you with tailored topics, resources, and learning goals to help you achieve your objectives efficiently.</p>

        <h3>Here's your customized learning plan:</h3>

        <div style="background-color: #f0f8ff; padding: 15px; border-radius: 8px; border: 1px solid #ddd;">
            {formatted_body}
        </div>

        <p>We hope you enjoy your learning journey!</p>

        <p>Best regards,<br><strong>Team StudyGenie</strong></p>
    </body>
    </html>
    """

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = to

        msg.attach(MIMEText(full_message, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

    except Exception as e:
        raise Exception(f"Failed to send email: {e}")
