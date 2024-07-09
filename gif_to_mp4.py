from moviepy.editor import VideoFileClip

# Function that convert GIF to MP4
def gif_to_mp4(gif_file_path, mp4_file_path):
    # Load the GIF file
    clip = VideoFileClip(gif_file_path)
    
    # video file.
    clip.write_videofile(mp4_file_path, codec='libx264')

# Example usage
gif_file_path = r'C:\Users\adity\OneDrive\Desktop\Learning\Media\210431.gif'  # Path to the GIF file
mp4_file_path = r'C:\Users\adity\OneDrive\Desktop\Learning\Media\210431.mp4'  # Path to save the MP4 file

# Converting the GIF file to MP4
gif_to_mp4(gif_file_path, mp4_file_path)
print(f"GIF file '{gif_file_path}' has been converted to MP4 file '{mp4_file_path}'")
