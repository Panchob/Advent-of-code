import 'package:dart/dart.dart';
import 'package:test/test.dart';
import 'dart:math';

final example = {
  'points': {
    Point(6, 10),
    Point(0, 14),
    Point(9, 10),
    Point(0, 3),
    Point(10, 4),
    Point(4, 11),
    Point(6, 0),
    Point(6, 12),
    Point(4, 1),
    Point(0, 13),
    Point(10, 12),
    Point(3, 4),
    Point(3, 0),
    Point(8, 4),
    Point(1, 10),
    Point(2, 14),
    Point(8, 10),
    Point(9, 0)
  },
  'instructions': ['fold along y=7', 'fold along x=5']
};
void main() {
  test('Parse file', () {
    expect(parseFile("inputTest.txt"), example);
  });

  test('Fold paper', () {
    expect(
        numberAfterFold(example['points'], example['instructions'], true), 17);
  });

  test('Fold paper', () {
    expect(
        numberAfterFold(example['points'], example['instructions'], false), 16);
  });
}
