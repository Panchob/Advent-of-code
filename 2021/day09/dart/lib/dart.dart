import 'dart:io';
import 'dart:math';

final CARDINAL = [
  [1, 0],
  [0, 1],
  [-1, 0],
  [0, -1]
];

List parseFile(String fileName) {
  return File(fileName)
      .readAsStringSync()
      .split('\n')
      .map((String e) => e.trim().split('').map((n) => int.parse(n)).toList())
      .toList();
}

num checkForLower(List heatMap) {
  num total = 0;
  int r = 0;

  heatMap.forEach((row) {
    for (int i = 0; i < row.length; i++) {
      if (isLowest({"row": r, "col": i}, heatMap)) {
        total += heatMap[r][i] + 1;
      }
    }
    r += 1;
  });

  return total;
}

bool isLowest(Map position, heatMap) {
  final row = position["row"];
  final col = position["col"];
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      if (i + j != 0 &&
          row + i >= 0 &&
          row + i < heatMap.length &&
          col + j >= 0 &&
          col + j < heatMap[0].length) {
        if (heatMap[row + i][col + j] <= heatMap[row][col]) {
          return false;
        }
      }
    }
  }
  return true;
}

Set visited = {};
Set totalVisited = {};
num checkForBasin(List heatMap) {
  List<int> basins = [];
  int r = 0;

  heatMap.forEach((row) {
    for (int i = 0; i < row.length; i++) {
      if (isLowest({"row": r, "col": i}, heatMap)) {
        visited.add(Point(r, i));
        basinMapping({"row": r, "col": i}, heatMap);
        basins.add(visited.length);
        totalVisited.addAll(visited);
        visited = {};
      }
    }
    r += 1;
  });
  basins.sort();
  return basins[basins.length - 1] *
      basins[basins.length - 2] *
      basins[basins.length - 3];
}

// oof
void basinMapping(Map position, heatMap) {
  int row = position["row"];
  int col = position["col"];
  CARDINAL.forEach((c) {
    if (row + c[0] >= 0 &&
        row + c[0] < heatMap.length &&
        col + c[1] >= 0 &&
        col + c[1] < heatMap[0].length) {
      if (heatMap[row + c[0]][col + c[1]] > heatMap[row][col] &&
          heatMap[row + c[0]][col + c[1]] != 9) {
        final current = Point(row + c[0], col + c[1]);
        if (!visited.contains(current) && !totalVisited.contains(current)) {
          visited.add(current);
          basinMapping({"row": row + c[0], "col": col + c[1]}, heatMap);
        }
      }
    }
  });
}
