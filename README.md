# OSS Lab(HGU, 2021-1)
**Project name: Remove Instrumental**


**Video Link: [Project presentation video]()**
# Install Dependencies

(1) First, install python=3.7, 64-bit. check this.
```
# ffmpeg install
sudo apt-get install ffmpeg
```
```
# tensorflow install
sudo apt-get install tensorflow
```
```
# youtube_dl install
sudo apt-get install youtube_dl
```
```
# spleeter install
sudo apt-get install spleeter
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
**[WARNING] This is drivin by Raspberry Pi. So you can use this for 1 minute or less file.**

If you want to try for example file, just
```
spleeter separate -p spleeter:2stems -i audio_example.wav -o ./
```




# References

https://github.com/deezer/spleeter

https://github.com/ytdl-org/youtube-dl