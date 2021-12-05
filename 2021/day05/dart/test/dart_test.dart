import 'package:dart/dart.dart';
import 'package:test/test.dart';
import 'dart:math';

final example = [
  [Point(0, 9), Point(5, 9)],
  [Point(8, 0), Point(0, 8)],
  [Point(9, 4), Point(3, 4)],
  [Point(2, 2), Point(2, 1)],
  [Point(7, 0), Point(7, 4)],
  [Point(6, 4), Point(2, 0)],
  [Point(0, 9), Point(2, 9)],
  [Point(3, 4), Point(1, 4)],
  [Point(0, 0), Point(8, 8)],
  [Point(5, 5), Point(8, 2)]
];

void main() {
  test('Parse file', () {
    expect(parseFile('inputTest.txt'), example);
  });

  test('Find at least one intersection', () {
    expect(countIntersections(example, false), 5);
    expect(countIntersections(example, true), 12);
  });
}
