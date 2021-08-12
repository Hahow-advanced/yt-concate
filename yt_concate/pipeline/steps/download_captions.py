from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils, log):
        log.info("Downloading captions...")
        if inputs["fast"]:
            for yt in data:
                if utils.caption_file_exists(yt):
                    log.info(f"Found existing file {yt.id}, skipping.")
                    continue
                try:
                    self.download_captions(yt)
                except (KeyError, AttributeError):
                    log.error(f"Error when downloading: {yt.url}")
                    continue
        else:
            for yt in data:
                try:
                    self.download_captions(yt)
                except (KeyError, AttributeError):
                    log.error(f"Error when downloading: {yt.url}")
                    continue
        return data

    @staticmethod
    def download_captions(yt):
        print("Downloading caption: ", yt.id)
        source = YouTube(yt.url)
        en_caption = source.captions['en']
        en_caption_convert_to_srt = en_caption.generate_srt_captions()

        text_file = open(yt.caption_filepath, "w", encoding="utf-8")
        text_file.write(en_caption_convert_to_srt)
        text_file.close()


