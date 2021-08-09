import os

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR


class Utils:
    def __init__(self):
        pass

    # in Preflight
    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    # in GetVideoList
    @staticmethod
    def get_video_list_filepath(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + ".txt")

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    # in DownloadCaptions
    @staticmethod
    def caption_file_exists(yt):
        file_path = yt.caption_filepath
        return os.path.exists(file_path) and os.path.getsize(file_path) > 0

    # in DownloadVideos
    @staticmethod
    def video_file_exists(yt):
        file_path = yt.video_filepath
        return os.path.exists(file_path) and os.path.getsize(file_path) > 0
