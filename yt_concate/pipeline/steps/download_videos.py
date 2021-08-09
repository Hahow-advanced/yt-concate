from pytube import YouTube

from .step import Step
from .step import StepException

from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        # 避免下載到重複的影片
        yt_set = set([found.yt for found in data])
        print("videos to download=", len(yt_set))

        for yt in yt_set:
            if utils.video_file_exists(yt):
                print(f"Found existing video file for {yt.url}, skipping")
                continue

            print("downloading ", yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + ".mp4")
        return data
