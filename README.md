# OSS Lab(HGU, 2021-1)
**Project name: Instrumental remover**


**Video Link: [Project presentation video](https://www.youtube.com/watch?v=pu6jcWHH_ho)**


## What does this project do?

**Instrumental remover** is an automatic tool that can listen to the singer's voice and the accompaniment separately.
When you want to listen voice, just open vocals.wav. If you want listen to the instrumental, open accompaniment.wav.


## Why is this project useful?
Since only the singer's voice is distinguished from the music source, it can be seen how much the singer's singing ability is.
And even if you need an accompaniment to sing, it's useful.

these days, there are many tools and programs about dealing with music. but They are too difficult for beginners to handle.

I like to sing, but it was hard to go to karaoke because of the coronavirus, and even with the accompaniment of other karaoke versions on YouTube, it was different from the instrumental used by real singers.

# Tools

I developed this project using python and opensource ffmpeg, spleeter and youtube_dl.

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
# youtube_dl install
pip install youtube_dl
```
```
# spleeter install
pip install spleeter
```
If you use Raspberry Pi, you can't use some latest version. install these modules with requirements.txt
```
pip install -r requirements.txt
```
Beacuase of computing resources, I only use 1 minute wav file. I use 1/4 file of origin wav file. So I split that.
```
# soundfile install
pip install soundfile
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

~~spleeter separate -p spleeter:2stems -i audio_example.wav -o ./~~
spleeter separate -p spleeter:2stems audio_example.wav -o ./

```

# Get some help here

you can send an email on lzmgl5874@gmail.com or give some comments on issues.


# References

https://github.com/deezer/spleeter

https://github.com/ytdl-org/youtube-dl