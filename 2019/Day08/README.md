# Day 8

[Instructions](https://adventofcode.com/2019/day/8)

This problem was pretty fun and not too difficult. For part 1 I just had to go through each layers and find the one with the fewest 0. For part two all I had to do is to start with top layer and overwrite each other with what came next to have the final message. The real challenge (for me) was to find a way to display it since the terminal have limited space. I did it by using numpy and saving it directly to a file.

I also discovered [webbrowser](https://www.geeksforgeeks.org/python-launch-a-web-browser-using-webbrowser-module/). It can totally open a local file on a computer which is what I did here so I don't have to do the excruciating task to click on it when its generated (what am I gonna do with all this free time now).

## Dependencies

### numpy

```bash
pip install numpy
```
