import 'dart:io';
import 'dart:math';

List<int> parseFile(String fileName) {
  return File(fileName)
      .readAsStringSync()
      .split(',')
      .map((e) => int.parse(e))
      .toList();
}

int findMedian(List<int> list) {
  int l = list.length;
  list.sort();
  if (l % 2 == 1) {
    return list[l ~/ 2];
  }

  return (list[l ~/ 2.floor()] + list[l ~/ 2 - 1]) ~/ 2;
}

int findAverage(List<int> list) {
  int total = list.fold(0, (p, c) => p + c);
  return total ~/ list.length;
}

num moveCrabs(List<int> crabs) {
  int goal = findMedian(crabs);

  return crabs.map((pos) => (pos - goal).abs()).fold(0, (p, c) => p + c);
}

num moveCrabsButForReal(List<int> crabs) {
  int goal = findAverage(crabs);

  return crabs
      .map((pos) => processFuel((pos - goal).abs()))
      .fold(0, (p, c) => p + c);
}

int processFuel(total) {
  int ans = 0;
  for (int i = 0; i <= total; i++) {
    ans += i;
  }
  return ans;
}
