int numberOfGreaterThan(list) {
  return list.asMap().entries.map((entry) {
    return entry.key < list.length - 1 && list[entry.key + 1] > entry.value
        ? 1
        : 0;
  }).reduce((a, b) => a + b);
}

List groupListByTree(list) {
  final sums = [];
  for (var i = 0; i < list.length - 2; i++) {
    sums.add(list[i] + list[i + 1] + list[i + 2]);
  }
  return sums;
}
