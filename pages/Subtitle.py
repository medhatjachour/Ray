from functools import partial
from PySide6.QtCore import Qt, QThreadPool
from widgets.worker.Worker import Worker
import os
from moviepy.editor import VideoFileClip

from pydub import AudioSegment
from pydub.silence import split_on_silence
class Subtitle:
    def __init__(self):
        from ui.ui_main import Ui_Form

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mp3File = ''

        # threads
        self.threadpool = QThreadPool()
    def init(self):
        #####################################
        # Subtitle.buttons_actions(self)
        print("init")
    def upload(self, file_name):
        
        print("ewe")
    def handle_media(self, file_name):
        print("ewe")
    def handle_converting(self, file_name):

        
        workers = Worker(
            partial(
                Subtitle.start_convert,self,file_name
            )
        )
        workers.signals.result.connect(partial(Subtitle.result_convert,self))
        self.threadpool.start(workers)

    def start_convert(self, file_name, progress_callback ):
        pass
        print(f" handle_converting = {file_name}")
        video = VideoFileClip(os.path.join(file_name))
        name = os.path.splitext(os.path.basename(file_name))[0]
        folder =  os.path.dirname(file_name)
        print(f"  start writting mp3 {folder}/{name}.mp3")
        # video.audio.write_audiofile(f"wsw.mp3")
        video.audio.write_audiofile(f"{folder}/{name}.mp3")
        # audio_segment = video.subclip("00:00:13", "00:00:15")
        # Load your audio file (e.g., "your_audio.mp3").
        # Load your audio file (replace "your_audio.mp3" with the actual file path)
        self.mp3File = f'{folder}/{name}.mp3'
    def result_convert(self,result):
        print(f"  start writting mp3 { self.mp3File }.")
        song = AudioSegment.from_mp3("C:/Users/Medha/OneDrive/Documents/Ray/Ray/ww.mp3")
        # song = AudioSegment.from_mp3("C:/Users/Medha/Videos/Captures/MainWindow 2024-06-18 21-28-51.mp3")
        print(f"  AudioSegment AudioSegment mp3 {self.mp3File}.mp3")

        # Split the track where the silence is 2 seconds or more
        chunks = split_on_silence(
            song,
            min_silence_len=2000,  # Minimum silence length in milliseconds
            silence_thresh=-16  # Consider a chunk silent if quieter than -16 dBFS
        )

        # Process each chunk and export as separate MP3 files
        for i, chunk in enumerate(chunks):
            # Create a silence chunk that's 0.5 seconds long for padding
            silence_chunk = AudioSegment.silent(duration=500)
            # Add padding to the beginning and end of the chunk
            audio_chunk = silence_chunk + chunk + silence_chunk
            # Normalize the entire chunk
            normalized_chunk = match_target_amplitude(audio_chunk, -20.0)
            # Export the audio chunk with a new bitrate
            print(f"Exporting chunk{i}.mp3")
            normalized_chunk.export(f"./chunk{i}.mp3", bitrate="192k", format="mp3")



    def match_target_amplitude(aChunk, target_dBFS):
        ''' Normalize given audio chunk '''
        change_in_dBFS = target_dBFS - aChunk.dBFS
        return aChunk.apply_gain(change_in_dBFS)

