import 'dart:io';

List parseFile(fileName) {
  return File(fileName)
      .readAsStringSync()
      .split('\n')
      .map((e) => e.trim().split('').toList())
      .toList();
}

const CLOSING = {"{": "}", "(": ")", "<": ">", "[": "]"};
Map<String, num> POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137};
Map<String, num> AUTO_POINTS = {")": 1, "]": 2, "}": 3, ">": 4};

num checkForError(List text) {
  List error = [];
  List current = [];
  text.forEach((line) {
    current.add(line[0]);
    for (int i = 1; i < line.length; i++) {
      if (CLOSING.keys.contains(line[i])) {
        current.add(line[i]);
      } else if (CLOSING[current.last] == line[i]) {
        current.removeLast();
      } else {
        error.add(line[i]);
        print(
            "ERROR: Expected ${CLOSING[current.last]} but found ${line[i]} instead");
        break;
      }
    }
    current = [];
  });

  return error.fold(0, (p, c) => p + POINTS[c]!);
}

num autoComplete(List text) {
  bool hasError = false;
  List autoComplete = [];
  List<String> current = [];
  text.forEach((line) {
    current.add(line[0]);
    for (int i = 1; i < line.length; i++) {
      if (CLOSING.keys.contains(line[i])) {
        current.add(line[i]);
      } else if (CLOSING[current.last] == line[i]) {
        current.removeLast();
      } else {
        hasError = true;
        //print("ERROR: Expected ${CLOSING[current.last]} but found ${line[i]} instead");
        break;
      }
    }

    if (!hasError) {
      num total = 0;
      while (current.isNotEmpty) {
        total = (5 * total) + AUTO_POINTS[CLOSING[current.last]]!;
        current.removeLast();
      }
      autoComplete.add(total);
    }

    current = [];
    hasError = false;
  });
  autoComplete.sort();
  return autoComplete[autoComplete.length ~/ 2];
}
