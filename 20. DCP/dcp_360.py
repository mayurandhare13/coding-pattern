from heapq import heappush, heappop
from collections import defaultdict

def interleavePlaylists(playlists):
    scores = defaultdict(int)

    for playlist in playlists:
        size = len(playlist)
        playlistScore = ((size + 1) * size) // 2

        for idx, song in enumerate(playlist):
            scores[song] += playlistScore / (idx + 1)
    
    rankSongsHeap = []
    for song, score in scores.items():
        heappush(rankSongsHeap, (score, song))
    
    rankSongs = []
    while rankSongsHeap:
        _, song = heappop(rankSongsHeap)
        rankSongs.append(song)
    
    # its a min heap, so return reverse list (max element first)
    return rankSongs[::-1]


if __name__ == '__main__':
    playlists = [
        [1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]
    ]
    rankSongs = interleavePlaylists(playlists)
    print(rankSongs)
