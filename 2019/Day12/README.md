# Day 12

[Instructions](https://adventofcode.com/2019/day/12)

Part one was (relatively) no big deal here. Part 2 on the other part...ouch. I hit a big wall here. I really ha no clue on how to compute that many values and had to check on Reddit to find some clues how. Luckily from me I was not the only one in this situation. I finally understood that each coordinate are not related to one another and can cycle independently. To find when x, y and z repeat themselves I had to use a least common multiple algorithm. Thanks to stack overflow I found an [example](https://stackoverflow.com/a/42472824/13506641) that I could apply here.
