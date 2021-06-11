HI

This program removes instrumental

# Install Dependencies

(1) First, install python=3.7, [ffmpeg](https://ffmpeg.org/)
```
# ffmpeg install
sudo apt-get install ffmpeg
```
(2) Second, install modules with pip
```
pip install -r requirements.txt
```
**[WARNING] Check your tensorflow and spleeter version.**


# Preset

* Modify the variable ``input_video_data_path`` in ``config.py`` to specify the path where the wavfile is located.