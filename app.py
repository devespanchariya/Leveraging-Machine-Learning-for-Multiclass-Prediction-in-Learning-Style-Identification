from flask import Flask
import os
import time

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Define data for /htop
    name = "Deves panchariya"  # Replace with your full name
    username = os.environ.get('USER', 'unknown')  # Use environment variable to get username
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 5 * 3600))  # Convert to IST
    
    # Get top command output (simplified for compatibility)
    try:
        top_output = os.popen("top -bn1 | head -n 10").read()
    except Exception as e:
        top_output = f"Error fetching 'top' output: {e}"

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
