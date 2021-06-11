import youtube_dl
import os
import sys
import config as cfg

def downfile(link):
    output_dir = os.path.join(cfg.input_video_data_path, 'audio.%(ext)s')
    ydl_opt = {
    'outtmpl': output_dir,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }, {'key': 'FFmpegMetadata'},], # 메타데이터도 함께 저장
    }
    download_list = []
    download_list.append(link)

    with youtube_dl.YoutubeDL(ydl_opt) as ydl:
        ydl.download(download_list)

    print('다운로드 완료했습니다.')

if __name__ == "__main__":

    assert len(sys.argv) == 2, "[ERROR] option must be provided!"


    link = sys.argv[1]
    downfile(link)
