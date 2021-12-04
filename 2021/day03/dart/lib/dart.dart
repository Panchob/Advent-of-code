import 'dart:math';

List findGamma(List report) {
  final gamma = [];
  final binaryLength = report[0].trim().length;
  for (int i = 0; i < binaryLength; i++) {
    gamma.add(totalAtPosition(report, i));
  }
  return gamma.map((e) => e > report.length / 2 ? 1 : 0).toList();
}

List findCo2(List report, idx, least) {
  if (report.length == 1) {
    final binary = [];
    for (int i = 0; i < report[0].trim().length; i++) {
      binary.add(int.parse(report[0][i]));
    }
    return binary;
  }

  var keep = totalAtPosition(report, idx) >= report.length / 2 ? 1 : 0;
  if (least) {
    keep = keep == 1 ? 0 : 1;
  }
  final newList =
      report.where((element) => element[idx] == keep.toString()).toList();
  return findCo2(newList, idx + 1, least);
}

int totalAtPosition(List report, int position) {
  return report.fold(
      0, (int value, element) => value + int.parse(element[position]));
}

num convertBinaryToInt(List number, bool epsilon) {
  num result = 0;

  number.reversed.toList().asMap().forEach((idx, value) {
    int current = value;
    if (epsilon) {
      current = value == 1 ? 0 : 1;
    }
    result += pow(2, idx) * current;
  });

  return result;
}
