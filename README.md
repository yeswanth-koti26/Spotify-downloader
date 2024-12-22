
# Spotify Downloader

A Python-based project to fetch songs from Spotify, search them on YouTube, and download MP3 files.


## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)


---

## Features
- Authenticate with Spotify using OAuth.
- Fetch songs from Spotify albums or playlists.
- Search for songs on YouTube.
- Download MP3 files from YouTube using `pytube`.

---

## Technologies
This project was built using:
- Python
- Spotify API (`spotipy`)
- YouTube Search (`youtube-search-python`)
- MP3 Conversion (`pytube`)

---

## Setup Instructions
Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yeswanth-koti26/Spotify-downloader.git
   cd Spotify-downloader
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Spotify API credentials:
   - Open `spotify/auth.py`.
   - Replace placeholders with your **Client ID**, **Client Secret**, and **Redirect URI**.

5. Run the project:
   ```bash
   python main.py
   ```

---

## Usage
1. Authenticate with Spotify when prompted.
2. Fetch songs from the specified album or playlist.
3. Download MP3 files to the `downloads/` folder in the project directory.

---


### **How to Add This to Your Repository**
1. Create a `README.md` file in your project directory.
2. Copy and paste the above content into the file.
3. Stage, commit, and push the file to GitHub:
   ```bash
   git add README.md
   git commit -m "Add README with license"
   git push
   ```

