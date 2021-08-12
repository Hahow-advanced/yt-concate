from pytube import YouTube

from .step import Step
from .step import StepException

from yt_concate.settings import VIDEOS_DIR


# to use multi-threading: part away "download process" to another function
class DownloadVideos(Step):
    def process(self, data, inputs, utils, log):
        log.info("Downloading videos...")
        yt_set = set([found.yt for found in data])
        if inputs["fast"]:
            for yt in yt_set:
                if utils.video_file_exists(yt):
                    log.info(f"Found existing video file for {yt.url}, skipping")
                    continue
                try:
                    self.download_videos(log, yt)
                except (KeyError, AttributeError):
                    log.error(f"Error when downloading videos: {yt.url}")
                    continue
        else:
            for yt in yt_set:
                try:
                    self.download_videos(log, yt)
                except (KeyError, AttributeError):
                    log.error(f"Error when downloading videos: {yt.url}")
                    continue
        return data

    @staticmethod
    def download_videos(log, yt):
        log.info(f"Downloading video: {yt.url}")
        YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + ".mp4")
