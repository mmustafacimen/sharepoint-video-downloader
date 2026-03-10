# SharePoint Video Downloader

This Flask project allows you to download videos from SharePoint shared links.

## Features

- Extracts download URLs from SharePoint pages
- Uses Microsoft OAuth token for authentication
- Simple web interface to enter links and download videos

## Requirements

- Python 3.8+
- Flask
- Requests
- BeautifulSoup4

Installation:

```bash
pip install -r requirements.txt
Configuration

Before running the project, you must provide your own SharePoint and Azure credentials. Otherwise, the application will not work.

Required credentials:

CLIENT_ID – Azure application client ID

CLIENT_SECRET – Azure application client secret

TENANT_ID – Azure tenant ID

SP_USERNAME – SharePoint username

SP_PASSWORD – SharePoint password

Important: Do not write these directly into the code. Use environment variables instead.

Example (Windows):

set CLIENT_ID=your_client_id
set CLIENT_SECRET=your_client_secret
set TENANT_ID=your_tenant_id
set SP_USERNAME=your_username
set SP_PASSWORD=your_password

Example (Linux/macOS):

export CLIENT_ID=your_client_id
export CLIENT_SECRET=your_client_secret
export TENANT_ID=your_tenant_id
export SP_USERNAME=your_username
export SP_PASSWORD=your_password
Running the Application
python sharepointlinkileindirme(calısıyor).py

Open your browser:

http://127.0.0.1:5000

Enter the SharePoint link and press the Download button. The file will be automatically redirected and downloaded.

Notes

The project will not work without valid SharePoint and Azure credentials.

Downloaded files are not stored on the server; only redirection is performed.
