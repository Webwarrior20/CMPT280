#!/usr/bin/env python3
"""
Web Initial-Access Simulation Portal

⚠ EDUCATIONAL USE ONLY ⚠
- This is NOT a real login page.
- Do NOT enter any real credentials.
- Use only fake usernames/tokens inside your isolated VM.
"""

from flask import Flask, request, render_template_string, redirect
import os
from datetime import datetime

app = Flask(__name__)

# Same base directory as the rest of the project
LOG_DIR = "/home/seed/Documents/CMPT280/Final_Project/collected"
LOG_FILE = os.path.join(LOG_DIR, "simulated_web_tokens.txt")
os.makedirs(LOG_DIR, exist_ok=True)


LOGIN_PAGE = """
<!doctype html>
<html>
  <head>
    <title>Simulation Course Portal</title>
    <style>
      body { font-family: Arial, sans-serif; background:#f5f5f5; }
      .container { width: 320px; margin: 80px auto; padding: 20px;
                   background:white; border-radius: 5px;
                   box-shadow: 0 0 10px rgba(0,0,0,0.1); }
      h2 { text-align:center; }
      p.notice { font-size: 0.9em; color:#aa0000; }
      input[type=text], input[type=password] {
        width:100%; padding:8px; margin:6px 0; box-sizing:border-box;
      }
      button {
        width:100%; padding:8px; margin-top:10px;
        border:none; cursor:pointer;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h2>Initial Access Simulation</h2>
      <p class="notice">
        This is a LAB SIMULATION ONLY.<br>
        Do <b>NOT</b> enter any real credentials.
      </p>
      <form method="POST" action="/login">
        <label>Fake Username</label>
        <input type="text" name="username" required>
        <label>Fake Token / Password-like String</label>
        <input type="password" name="token" required>
        <button type="submit">Submit (Simulation)</button>
      </form>
    </div>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(LOGIN_PAGE)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    token = request.form.get("token", "")

    # Log simulated access data, NOT real credentials
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] USER={username} TOKEN={token}\n")

    # Redirect to a neutral site or info page (here: Google as placeholder)
    return redirect("https://www.google.com")

if __name__ == "__main__":
    # Listen on all interfaces so other VMs/containers in the lab can access
    app.run(host="0.0.0.0", port=5000)
