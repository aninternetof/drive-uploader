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
$> python3 watcher.py -l /path/to/local/dir/to/watch -r DirectoryOnGoogleDrive

```

## Limitations

* Only supports saving to a directory at the root of your Google drive (name supplied by the 
`-r` option). If that directory doesn't exist it will be created.
* No true syncing of the directory contents. If watcher.py is not running when the file is created,
the file will never be uploaded.