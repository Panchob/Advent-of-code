import os
import sys

if __name__ == '__main__':
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    calories = f.read().split("\n\n")
    ans = []
    for cal in calories:
      current = cal.split("\n")

      ans.append(sum(list(map(lambda x: int(x) if x != '' else 0, current))))
    print('PART 1:', max(ans))
    ans.sort()
    print('PART 2:', sum(ans[-3::]))
