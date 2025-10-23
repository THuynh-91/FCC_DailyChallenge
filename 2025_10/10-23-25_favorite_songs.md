

#  Favorite Songs
## Prompt


Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

-   Each object will have a  `"title"`  property (string), and a  `"plays"`  property (integer).

## My Thoughts
Really simple, just sort it in descending order, then grab the first 2 songs.

## Solution (Python)
```python
def favorite_songs(songs):
	songs_sorted = sorted(songs, key=lambda s: s["plays"], reverse=True)
	return  [songs_sorted[0]["title"], songs_sorted[1]["title"]]

```

