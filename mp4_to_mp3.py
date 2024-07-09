from moviepy.editor import VideoFileClip

# Function to convert MP4 to MP3
def mp4_to_mp3(mp4_file_path, mp3_file_path):
    # Load the MP4 file
    video = VideoFileClip(mp4_file_path)
    
    # audio extraction
    audio = video.audio
    
    # audio to a MP3 file
    audio.write_audiofile(mp3_file_path)

# Example usage
mp4_file_path = r'C:\Users\adity\OneDrive\Desktop\Learning\Media\phonk.mp4'  # Path to the MP4 file
mp3_file_path = r'C:\Users\adity\OneDrive\Desktop\Learning\Media\phonk_mp3.mp3'   # Path to save the MP3 file

# Converting MP4 file to MP3
mp4_to_mp3(mp4_file_path, mp3_file_path)
print(f"MP4 file '{mp4_file_path}' has been converted to MP3 file '{mp3_file_path}'")
