import time
import argparse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

REMOTE_DIR = 'uploaded-from-drive-uploader'

# credit: https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory
class Watcher:

    def __init__(self, local_dir):
        self.observer = Observer()
        self.local_dir = local_dir

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.local_dir, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - {}.".format(event.src_path))
            file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
            file_list = [f for f in file_list if f['title'] == REMOTE_DIR]
            if file_list:
                dir_id = file_list[0]['id']
            else:
                folder_metadata = {'title': REMOTE_DIR, 'mimeType': 'application/vnd.google-apps.folder'}
                folder = drive.CreateFile(folder_metadata)
                folder.Upload()
                dir_id = folder['id']

            drive_fh = drive.CreateFile({
                'title': event.src_path.split('/')[-1],
                'parents': [{'kind': 'drive#fileLink', 'id': dir_id}]
            })
            drive_fh.SetContentFile(event.src_path)  # Set content of the file from given string.
            drive_fh.Upload()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--local_dir', help='Path to the local directory to watch')
    parser.add_argument('-r', '--remote_dir', help='Destination directory on the remote (Google Drive)')
    args = parser.parse_args()
    REMOTE_DIR = args.remote_dir
    w = Watcher(args.local_dir)
    w.run()
