from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            print("Downloading caption for ", url)
            if utils.caption_file_exists(url):
                print("Found existing file:", utils.get_video_id_from_url(url))
                continue

            try:
                source = YouTube(url)
                en_caption = source.captions['en']
                en_caption_convert_to_srt = en_caption.generate_srt_captions()
            except (KeyError, AttributeError):
                print("Error when downloading caption for ", url)
                continue

            text_file = open(utils.get_caption_filepath(url), "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
