from pytube import YouTube

print ('''     .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
        _
     /\                        (_)
    /  \   _ __  ___  __ _ _ __ _
   / /\ \ | '_ \/ __|/ _` | '__| |
  / ____ \| | | \__ \ (_| | |  | |
 /_/    \_\_| |_|___/\__,_|_|  |_| 
 
   Author : AnsariHacker07
   github : https://github.com/AnsariHacker07
   Instagram : https://instagram.com/hacker_ansari_07
  
       ''')

# Example usage
url = input ('url : ')
youtube = YouTube(url)

# Print video title
print("Video Title: " + youtube.title)

# Select video format
video = youtube.streams.filter(file_extension='mp4').first()

# Define download path
download_path = "/storage/emulated/0/"

# Download video
video.download(download_path)

# Print success message
print("Video downloaded successfully")
