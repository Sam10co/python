import tkinter as tk
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    sender_email = "samuelsilvescoterin@gmail.com"  
    password = "hjsu ujmm zdol kzek"  

    
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, password)

    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))


    server.sendmail(sender_email, to_email, message.as_string())
    server.quit()


def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    label = tk.Label(popup, text="brigadu")
    label.pack(padx=20, pady=20)

    subject = "Resposta da sua pergunta"
    body = "El* aceitou fazer o chá!"
    to_email = "samuelsilvescoterin@gmail.com" 
    send_email(subject, body, to_email)

def move_button(event):
    max_width = root.winfo_width() - no_button.winfo_width()
    max_height = root.winfo_height() - no_button.winfo_height()
    x = random.randint(0, max_width)
    y = random.randint(0, max_height)
    no_button.place(x=x, y=y)

root = tk.Tk()
root.title("Faz um chazinho pra gente?")
root.geometry("400x400")

question_label = tk.Label(root, text="faz um chazinho pra gente?")
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Ta bom, eu faço", command=show_popup)
yes_button.pack()

no_button = tk.Button(root, text="Não")
no_button.place(x=150, y=200)

no_button.bind("<Enter>", move_button)

root.mainloop()