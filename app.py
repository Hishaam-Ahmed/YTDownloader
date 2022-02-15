from yt_dlp import YoutubeDL

def main():
    audio_downloader = YoutubeDL({'format':'bestaudio'})
    video_downloader = YoutubeDL({'format':'bestvideo'})

    while True:
        try:
            URL = input('Enter youtube url :  ')
            format = int(input("Select format: \n1. Video\n2. Audio-only\nEnter: "))
            if format == 1:
                video_downloader.extract_info(URL)
            elif format == 2:
                audio_downloader.extract_info(URL)
            else:
                print("Invalid Input. Try Again")

        except Exception:
            print("Couldn\'t download")

        finally:
            option = int(input('\n1.download again \n2.Exit\n\nOption here :'))
            if option!=1:
                break

if __name__ == '__main__':
    main()
