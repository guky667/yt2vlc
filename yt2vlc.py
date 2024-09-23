"""
YouTube to VLC Streaming Script
Original Script Author: ChatGPT (via OpenAI)
Collaborator: Guky

Description:
This script uses yt-dlp to extract a direct YouTube video/audio URL and plays it in VLC Media Player.

Date: 2024-09-23

Notes:
Feel free to modify, share, and improve the script. 
Attribution to the original authors (ChatGPT and Guky) is appreciated.
"""

import subprocess
import sys

# Function to install packages
def install_package(package_name):
    try:
        # Try importing the package
        __import__(package_name)
    except ImportError:
        print(f"'{package_name}' not found. Installing...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])

# Ensure yt-dlp is installed
install_package('yt_dlp')

# Now import yt_dlp after ensuring it's installed
import yt_dlp

# Start the original script functionality
# Ask for the URL
url = input("Enter the YouTube URL: ")

# Define yt-dlp options
ydl_opts = {
    'format': 'bestaudio/best',  # Target best audio available
    'quiet': False,
    'nocheckcertificate': True,  # Avoid SSL certificate errors
}

# Extract the video URL
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    # Get the list of formats available
    formats = info_dict.get('formats', [])
    
    # Iterate to find the first valid playable URL
    video_url = None
    for fmt in formats:
        if fmt.get('ext') in ['mp4', 'webm', 'm4a']:  # Common streamable formats
            video_url = fmt['url']
            break

if not video_url:
    print("Failed to extract a direct playable video URL.")
    exit(1)

print(f"Direct streaming URL: {video_url}")  # Debug output

# Full path to VLC executable
vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"

# Attempt to launch VLC with the direct video URL
try:
    print(f"Running command: {vlc_path} {video_url}")  # Display the command being executed
    subprocess.run([vlc_path, video_url], shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error launching VLC: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
