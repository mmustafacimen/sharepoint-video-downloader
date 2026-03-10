import os
from flask import Flask, request, redirect, render_template
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

client_id = "client_id"
client_secret = "client_secret"
tenant_id = "tenant_id"


def get_access_token(username, password):
    token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    token_data = {
        'grant_type': 'password',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'offline_access Files.Read.All Files.Read Sites.Read.All',
        'username': username,
        'password': password
    }
    token_r = requests.post(token_url, data=token_data)
    token_r.raise_for_status()
    token_response = token_r.json()
    return token_response['access_token']


def get_download_url(sharepoint_url, access_token):
    try:
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(sharepoint_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        script_tags = soup.find_all('script')

        download_url = None
        for script in script_tags:
            script_content = script.string
            if script_content:
                match = re.search(r'downloadUrl":"(.*?)"', script_content)
                if match:
                    download_url = match.group(1).replace('\\u0026', '&')
                    break

        if not download_url:
            raise Exception("Download URL not found.")

        clean_url = re.sub(r'&.*', '', download_url)
        return clean_url

    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while retrieving data from SharePoint: {str(e)}")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download_file():
    try:
        sharepoint_link = request.form.get('sharepoint_link')

        if not sharepoint_link:
            return "Sharepoint link is missing:", 400


        username = "_username_"
        password = "_password_"

        access_token = get_access_token(username, password)
        download_url = get_download_url(sharepoint_link, access_token)

        return redirect(download_url)

    except Exception as e:
        return f"Download Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
