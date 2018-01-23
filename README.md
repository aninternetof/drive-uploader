# Drive Uploader

A simple Python script to monitor a directory and upload any new files to your Google Drive.

## Usage

Follow the steps 1 through 5 in the [PyCharm Quickstart](https://pythonhosted.org/PyDrive/quickstart.html) to create 
Google Drive secrets. Save them as `client_secrets.json` in the same directory as this README.md.

Then, install the requirements for this app:
```bash
$> pip3 install -r requirements.txt
```

Then, run the app:
```bash
$> python3 watcher.py /path/to/the/local/dir/to/watch /dest/path/on/google/drive
```