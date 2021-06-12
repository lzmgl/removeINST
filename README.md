# OSS Lab(HGU, 2021-1)
**Project name: Remove Instrumental**


**Video Link: [Project presentation video]()**


## What does this project do?

**Instrumental remover** is an automatic tool that can listen to the singer's voice and the accompaniment separately.
When you want to listen voice, just open vocals.wav. If you want listen to the instrumental, open accompaniment.wav.


## Why is this project useful?
Since only the singer's voice is distinguished from the music source, it can be seen how much the singer's singing ability is.
And even if you need an accompaniment to sing, it's useful.


# Install Dependencies

(1) First, install python=3.7, 64-bit. check this.
```
# ffmpeg install
sudo apt-get install ffmpeg
```
```
# tensorflow install
pip install tensorflow
```
```
# soundfile install
pip install soundfile
```
```
# youtube_dl install
pip install youtube_dl
```
```
# spleeter install
pip install spleeter
```
If you use Raspberry Pi, you can't use some version. install modules with requirements.txt
```
pip install -r requirements.txt
```
**[WARNING] Check your tensorflow and spleeter version.**


# Preset

* Modify the variable ``input_video_data_path`` in ``config.py`` to specify the path where the wavfile is located.

# Usage
```
bash run.sh [youtube link]
```
**[WARNING] This is drivin by Raspberry Pi. So you can use this for 4 minute or less file. This program cuts your video to 1/4 length**

If you want to try for example file, just
```
spleeter separate -p spleeter:2stems -i audio_example.wav -o ./
```

# Get some help here

you can send an email on lzmgl5874@gmail.com or give some comments on issues.


# References

https://github.com/deezer/spleeter

https://github.com/ytdl-org/youtube-dl