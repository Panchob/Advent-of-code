import 'dart:ffi';
import 'dart:io';

Map parseFile(String fileName) {
  Map paths = {};
  final lines = File(fileName).readAsStringSync().split('\n');

  lines.forEach((element) {
    final temp = element.trim().split('-');
    if (paths.keys.contains(temp[0]) && !paths[temp[0]].contains(temp[1])) {
      paths[temp[0]].add(temp[1]);
    } else {
      paths[temp[0]] = [temp[1]];
    }
    if (paths.keys.contains(temp[1]) && !paths[temp[1]].contains(temp[0])) {
      paths[temp[1]].add(temp[0]);
    } else {
      paths[temp[1]] = [temp[0]];
    }
  });

  return paths;
}

List visited = [];
Map memo = {};
Map CAVES = {};

int findAllPaths(caves, visitTwice) {
  CAVES = caves;
  return visitTwice ? findPathsPart2("start", []) : findPaths("start", []);
}

int findPaths(String current, path) {
  int total = 0;
  if (current == "end") {
    total = 1;
    //print([...path, "end"]);
  } else if ((current == current.toLowerCase() && !path.contains(current)) ||
      current == current.toUpperCase()) {
    CAVES[current].forEach((next) => {
          total += findPaths(next, [...path, current])
        });
  }
  if (path.length > 0) {
    path.removeLast();
  }

  return total;
}

int findPathsPart2(String current, path) {
  int total = 0;
  if (current == "end") {
    total = 1;
    //print([...path, "end"]);
  } else if (current != "start" || !path.contains("start")) {
    if ((current == current.toLowerCase() &&
            !checkForDuplicate(path, current)) ||
        current == current.toUpperCase()) {
      CAVES[current].forEach((next) => {
            total += findPathsPart2(next, [...path, current])
          });
    }
  }

  if (path.length > 0) {
    path.removeLast();
  }

  return total;
}

bool checkForDuplicate(List path, current) {
  path.toSet();
  if (!path.contains(current)) {
    return false;
  }

  for (int i = 0; i < path.length; i++) {
    String element = path[i];
    int total = 0;
    if (element == element.toLowerCase()) {
      path.forEach((e) {
        if (e == element) {
          total += 1;
        }
      });
    }

    if (total > 1) {
      return true;
    }

    total = 0;
  }

  return false;
}
