# PySide6 Media Player
## Overview
This is a desktop application built with PySide6 that functions as a media player. It supports playing video and MP3 files, detects and displays subtitles, and includes an option to convert voice to text.
![alt text](https://github.com/medhatjachour/Ray/blob/main/sample/im1.png?raw=true)
![alt text](https://github.com/medhatjachour/Ray/blob/main/sample/im2.png?raw=true)
![alt text](https://github.com/medhatjachour/Ray/blob/main/sample/im2.png?raw=true)
## Features
- **Play Video and MP3**: Supports various video and audio formats.
- **Subtitle Detection and Display**: Automatically detects and displays subtitles for video files.
- **Voice to Text**: Converts audio from video or MP3 files into text.

## Installation

### Prerequisites
- Python 3.8+
- PySide6
- Other dependencies listed in `requirements.txt`

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/medhatjachour/ray.git
    cd ray
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

## Usage
1. **Open Media**: Use the file menu to open a video or MP3 file.
2. **Play/Pause**: Use the play/pause button to control playback.
3. **Subtitles**: Subtitles will be automatically detected and displayed if available.
4. **Voice to Text**: Use the voice-to-text option in the menu to convert audio to text.

## Dependencies
- PySide6
- PyQt5 (for additional widgets)
- ffmpeg (for media processing)
- SpeechRecognition (for voice to text)
- Other dependencies listed in `requirements.txt`

## Contributing
Contributions are welcome! If you’d like to contribute to this project, just contact me

## License
This project is licensed under the MIT License - see the LICENSE file for details.
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements
- PySide6 Documentation
- ffmpeg Documentation
- SpeechRecognition Documentation