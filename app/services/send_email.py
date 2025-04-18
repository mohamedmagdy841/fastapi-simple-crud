import smtplib
from jinja2 import Environment, FileSystemLoader, select_autoescape
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

templates = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html", "xml"])
)

def send_email(to_email: str, subject: str, template_name: str, context: dict):
    template = templates.get_template(template_name)
    html_content = template.render(**context)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.getenv("MAIL_FROM")
    msg["To"] = to_email

    msg.set_content(f"Hi, welcome!")
    msg.add_alternative(html_content, subtype="html")

    with smtplib.SMTP(os.getenv("MAIL_SERVER"), int(os.getenv("MAIL_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("MAIL_USERNAME"), os.getenv("MAIL_PASSWORD"))
        server.send_message(msg)