from pytube import YouTube

def download_youtube_video(url):
    try:
        # Create a YouTube object with the video URL
        video = YouTube(url)

        # Get the highest resolution available
        stream = video.streams.get_audio_only()

        # Download the video
        print("Downloading:", video.title)
        stream.download()
        print("Download complete!")

    except Exception as e:
        print("Error:", str(e))

# Example usage 
video_url = "https://www.youtube.com/watch?v=xdGO-qmEJio&pp=ygUFcGFnYWw%3D"
download_youtube_video(video_url)