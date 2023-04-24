from download import download_audio, download_video

def main():
  while True:
    try:
      # Prompt the user to enter a YouTube video link
      url = input('Enter link: ')
  
      # Prompt the user to choose the file format
      print("Choose format: ")
      print("1. Video")
      print("2. Audio-only")
      choice = int(input("Enter your choice: "))
  
      if choice == 1:
        download_video(url)
      elif choice == 2:
        download_audio(url)
      else:
        print('Try again')
  
    except:
      print('There seems to be some error')
  
    finally:
      option = int(input('\n1.download again \n2.Exit\n\nOption here :'))
      if option!=1:
          break


if __name__ == '__main__':
    main()
