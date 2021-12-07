import 'dart:io';

List parseFile(String fileName) {
  return File(fileName)
      .readAsStringSync()
      .split(',')
      .map((e) => int.parse(e))
      .toList();
}

num findTotalFishes(List fishes, int cycle) {
  num total = fishes.length;
  Map memo = {};
  int o = 0;

  fishes.forEach((fish) {
    print(o);
    o++;
    if (memo.containsKey(fish)) {
      total += memo[fish];
    } else {
      int temp = 1;
      num currentCycle = cycle - (fish + 1);

      for (num i = currentCycle; i >= 7; i -= 7) {
        temp += 1 + spawnFish(i);
      }
      memo[fish] = temp;
      total += temp;
    }
  });

  return total;
}

int spawnFish(num cycle) {
  if (cycle < 9) {
    return 0;
  }
  num currentCycle = cycle - 9;
  int temp = 1;
  for (num i = currentCycle; i >= 7; i -= 7) {
    temp += 1 + spawnFish(i);
  }

  return temp;
}
