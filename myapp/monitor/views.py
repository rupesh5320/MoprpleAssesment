#from django.shortcuts import render

# monitor/views.py
import os
import subprocess
import datetime
from django.http import HttpResponse
from pytz import timezone

def htop_view(request):
    # Your full name
    name = "Rupesh Kumar" 

    # System username (fallback if os.getlogin() fails in Codespace)
    username = os.getenv('USER', 'unknown')
    
    # Current server time in IST
    ist_time = datetime.datetime.now(timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S %Z")
    
    # Get the top output (limited to the first 10 lines)
    try:
        top_output = subprocess.getoutput("top -bn1 | head -10")
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    # HTML response content
    content = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <h2>Top Processes</h2>
    <pre>{top_output}</pre>
    """
    return HttpResponse(content)

