import 'dart:io';
import 'dart:math';

List<List<Point>> parseFile(fileName) {
  final lines = File(fileName)
      .readAsStringSync()
      .split('\n')
      .map((e) => e.trim().split('->').toList());

  final positions =
      lines.map((l) => l.map((p) => parsePoint(p)).toList()).toList();

  return positions;
}

Point parsePoint(p) {
  final point = p.trim().split(',');
  return Point(int.parse(point[0]), int.parse(point[1]));
}

// Not all intersections, only the first time a point intersects.
int countIntersections(positions, diagonals) {
  Map vents = {};
  for (int i = 0; i < positions.length; i++) {
    final current = positions[i];
    final p1 = current[0];
    final p2 = current[1];

    if (diagonals || isHorOrVer(p1, p2)) {
      int x1 = p1.x;
      int x2 = p2.x;
      int y1 = p1.y;
      int y2 = p2.y;

      int diffX = (x2 - x1);
      int diffY = (y2 - y1);

      final lineLenght = max(diffX.abs(), diffY.abs());

      int stepX = (diffX / lineLenght).floor();
      int stepY = (diffY / lineLenght).floor();

      for (int i = 0; i <= lineLenght; i++) {
        final key = Point(x1 + (stepX * i), y1 + (stepY * i));

        if (vents.containsKey(key)) {
          vents[key] += 1;
        } else {
          vents[key] = 1;
        }
      }
    }
  }

  return vents.values.where((p) => p > 1).length;
}

bool isHorOrVer(Point p1, Point p2) {
  return p1.x == p2.x || p1.y == p2.y;
}
