from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            print("Downloading caption for ", yt.id)
            if utils.caption_file_exists(yt):
                print("Found existing file")
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions['en']
                en_caption_convert_to_srt = en_caption.generate_srt_captions()
            except (KeyError, AttributeError):
                print("Error when downloading caption for ", yt.url)
                continue

            text_file = open(yt.caption_filepath, "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        return data
