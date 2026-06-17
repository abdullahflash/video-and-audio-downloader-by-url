from yt_dlp import YoutubeDL

while True:
    print("\n1. Download Video")
    print("2. Download Audio")
    print("3. Exit")

    choice = input("Enter the choice: ")

    if choice == "3":
        print("Goodbye!")
        break

    url = input("Enter the URL: ")

    if choice == "1":
        ydl_opts = {
            "outtmpl": "%(title)s.%(ext)s"
        }

        print("Starting download...")

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download completed!")

    elif choice == "2":
        audio_opts = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
            }],
            "outtmpl": "%(title)s.%(ext)s"
        }

        print("Starting download...")

        with YoutubeDL(audio_opts) as ydl:
            ydl.download([url])

        print("Download completed!")

    else:
        print("Invalid choice!")

        
    
    
    