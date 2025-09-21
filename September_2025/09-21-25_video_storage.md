

# Video Storage
## Prompt



Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

-   The unit for the video size can be bytes (`"B"`), kilobytes (`"KB"`), megabytes (`"MB"`), or gigabytes (`"GB"`).
-   If not given one of the video units above, return  `"Invalid video unit"`.
-   The unit of the hard drive capacity can be gigabytes (`"GB"`) or terabytes (`"TB"`).
-   If not given one of the hard drive units above, return  `"Invalid drive unit"`.
-   Return the number of whole videos the drive can fit.



## My Thoughts
Same type of questions as the previous days. I took the drive unit, got the size and divided


## Solution (Python)
```python
def number_of_videos(video_size, video_unit, drive_size, drive_unit):
	th = 1000
	v_size = {"B":  1,  "KB": th,  "MB": th*th,  "GB":th*th*th}
	d_size = {"GB": th*th*th,  "TB": th*th*th*th}

	if video_unit not  in v_size:
		return  "Invalid video unit"
	elif drive_unit not  in d_size:
		return  "Invalid drive unit"

	v_space = video_size * v_size[video_unit]
	d_space = drive_size * d_size[drive_unit]
	return d_space // v_space
```
