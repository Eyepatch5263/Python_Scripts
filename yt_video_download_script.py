from yt_dlp import YoutubeDL

def download_and_convert(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'  # Convert to MP4
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download_and_convert("https://youtu.be/32si5cfrCNc")