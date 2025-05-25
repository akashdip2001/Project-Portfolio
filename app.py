from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)  # 👈 Enables requests from your frontend

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    full_name = data.get('fullName')
    github = data.get('githubLink')
    repos = data.get('repos')

    body = f"Full Name: {full_name}\nGitHub: {github}\nRepositories:\n"
    for i, repo in enumerate(repos, 1):
        body += f"• Repo {i}: {repo}\n"

    msg = MIMEText(body)
    msg["Subject"] = "🎓 Project Submission from GitHub Challenge"
    msg["From"] = "mail.me.akashdip2001@gmail.com"
    msg["To"] = "mail.me.akashdip2001@gmail.com"

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("mail.me.akashdip2001@gmail.com", "svdcklfdwphyrdvr")
        server.send_message(msg)
        server.quit()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
