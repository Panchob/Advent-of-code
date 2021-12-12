import 'dart:io';
import 'dart:math';

List parseFile(String fileName) {
  return File(fileName)
      .readAsStringSync()
      .split('\n')
      .map((String e) => e.trim().split('').map((n) => int.parse(n)).toList())
      .toList();
}

List OctopusesArray = [];
List visited = [];

int cyclingHighlight(List octopuses, steps) {
  int total = 0;
  OctopusesArray = octopuses;
  for (int s = steps; s > 0; s--) {
    visited = [];
    for (int row = 0; row < OctopusesArray.length; row++) {
      for (int col = 0; col < OctopusesArray[0].length; col++) {
        final current = Point(row, col);
        if (OctopusesArray[row][col] == 0 && visited.contains(current)) {
          continue;
        } else if (OctopusesArray[row][col] < 9) {
          OctopusesArray[row][col] += 1;
        } else {
          visited.add(current);
          OctopusesArray[row][col] = 0;
          total += 1 + highlight(current);
        }
      }
    }
  }

  return total;
}

int highlight(Point position) {
  int row = position.x.toInt();
  int col = position.y.toInt();
  int total = 0;
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      int newRow = row + i;
      int newCol = col + j;
      if (newRow >= 0 &&
          newRow < OctopusesArray.length &&
          newCol >= 0 &&
          newCol < OctopusesArray[0].length) {
        final current = Point(newRow, newCol);
        if (OctopusesArray[newRow][newCol] == 0 && visited.contains(current)) {
          continue;
        }
        if (OctopusesArray[newRow][newCol] < 9) {
          OctopusesArray[newRow][newCol] += 1;
        } else {
          OctopusesArray[newRow][newCol] = 0;
          visited.add(current);
          total += 1 + highlight(current);
        }
      }
    }
  }
  return total;
}

int findAllHighlight(List octopuses) {
  bool all = false;
  int step = 0;
  OctopusesArray = octopuses;
  while (!all) {
    step++;
    visited = [];
    int total = 0;
    for (int row = 0; row < OctopusesArray.length; row++) {
      for (int col = 0; col < OctopusesArray[0].length; col++) {
        final current = Point(row, col);
        if (OctopusesArray[row][col] == 0 && visited.contains(current)) {
          continue;
        } else if (OctopusesArray[row][col] < 9) {
          OctopusesArray[row][col] += 1;
        } else {
          visited.add(current);
          OctopusesArray[row][col] = 0;
          total += 1 + highlight(current);
        }
      }
    }
    if (total == octopuses.length * octopuses[0].length) {
      all = true;
    }
  }

  return step;
}
