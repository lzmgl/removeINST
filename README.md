# OSS Lab(HGU, 2021-1)
**Project name: Remove Instrumental**


**Video Link: [Project presentation video](https://youtu.be/GYCX6G9wAZw)**
# Install Dependencies

(1) First, install python=3.7, 64-bit. chech this.
```
# ffmpeg install
sudo apt-get install ffmpeg
# tensorflow install
sudo apt-get install tensorflow
# youtube_dl install
sudo apt-get install youtube_dl
# spleeter install
sudo apt-get install spleeter
```
If you use Raspberry Pi, you can't use some version. install modules with pip
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



# Usage