import 'dart:io';
import 'dart:math';

Map parseFile(String fileName) {
  List text = File(fileName).readAsStringSync().split("\r\n\r\n").toList();
  List rawPoints =
      text[0].split('\n').map((p) => p.trim().split(',').toList()).toList();
  List instructions = text[1].split('\n').map((i) => i.trim()).toList();

  Set<Point> points =
      rawPoints.map((e) => Point(int.parse(e[0]), int.parse(e[1]))).toSet();
  return {"points": points, "instructions": instructions};
}

int numberAfterFold(points, instructions, onlyFirst) {
  Set foldedPaper = points;

  for (int i = 0; i < instructions.length; i++) {
    foldedPaper = foldPaper({...foldedPaper}, instructions[i]);
    if (onlyFirst) {
      break;
    }
  }

  if (!onlyFirst) {
    writeToFile(foldedPaper);
  }
  return foldedPaper.length;
}

Set foldPaper(Set<Point> points, instruction) {
  final temp = instruction.split('=');
  int position = int.parse(temp[1].trim());
  String direction = instruction[temp[0].length - 1];
  Set foldedPaper = {};

  points.forEach((point) {
    if (direction == 'x' && point.x > position) {
      foldedPaper.add(Point(position - (point.x - position), point.y));
    } else if (direction == 'y' && point.y > position) {
      foldedPaper.add(Point(point.x, position - (point.y - position)));
    } else {
      foldedPaper.add(point);
    }
  });

  return foldedPaper;
}

void writeToFile(Set points) {
  num maxY = points.reduce((cur, next) => cur.y > next.y ? cur : next).y;
  num maxX = points.reduce((cur, next) => cur.x > next.x ? cur : next).x;

  String line = '';

  for (int i = 0; i <= maxY; i++) {
    for (int j = 0; j <= maxX; j++) {
      if (points.contains(Point(j, i))) {
        line += ' # ';
      } else {
        line += ' . ';
      }
    }
    print(line);
    line = '';
  }
}
