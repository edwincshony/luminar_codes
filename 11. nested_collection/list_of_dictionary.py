# ================================
# SONG DATA
# ================================
songs = [
    {"id": 1, "title": "Mayajalam", "spotify_listen_count": 12000, "yt_music": 15000, "downloads": 5000},
    {"id": 2, "title": "Neon Nights", "spotify_listen_count": 850000, "yt_music": 1200000, "downloads": 45000},
    {"id": 3, "title": "Midnight Coffee", "spotify_listen_count": 45000, "yt_music": 32000, "downloads": 1200},
    {"id": 4, "title": "Velvet Sky", "spotify_listen_count": 1200400, "yt_music": 980000, "downloads": 150000},
    {"id": 5, "title": "Echoes of You", "spotify_listen_count": 3100, "yt_music": 4500, "downloads": 200},
    {"id": 6, "title": "Rush Hour", "spotify_listen_count": 560000, "yt_music": 610000, "downloads": 88000},
    {"id": 7, "title": "Quiet Storm", "spotify_listen_count": 150000, "yt_music": 145000, "downloads": 12000}
]

# ================================
# BASIC EXTRACTIONS
# ================================
all_title = [di.get("title") for di in songs]
all_downloads = [di.get("downloads") for di in songs]

print(all_title)
print(all_downloads)


# ================================
# TOP DOWNLOAD SONG
# ================================

# ---- Approach 1 → max() + filter
top_downloads = max(all_downloads)
top_download_song = [di.get("title") for di in songs if di.get("downloads") == top_downloads]
print(top_download_song)

# ---- Approach 2 → dict → swap → sort
all_song_download_count = {di.get("title"): di.get("downloads") for di in songs}
max_download = [[v, k] for k, v in all_song_download_count.items()]
print(sorted(max_download, reverse=True)[0])


# ================================
# MOST PLAYED ON YOUTUBE MUSIC
# ================================

# Pre-extract YT listens once (removes redundancy)
all_yt_listens = [di.get("yt_music") for di in songs]

# ---- Approach 1 → max() + filter
top_yt_listens = max(all_yt_listens)
top_yt_song = [di.get("title") for di in songs if di.get("yt_music") == top_yt_listens]
print(top_yt_song)

# ---- Approach 2 → dict → swap → sort
listened_yt_song = {di.get("title"): di.get("yt_music") for di in songs}
max_listened_yt_song = [[v, k] for k, v in listened_yt_song.items()]
print(sorted(max_listened_yt_song, reverse=True)[0])