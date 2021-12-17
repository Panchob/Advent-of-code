import 'package:dart/dart.dart';
import 'package:test/test.dart';

final example1 = [
  [1, 1, 1, 1, 1],
  [1, 9, 9, 9, 1],
  [1, 9, 1, 9, 1],
  [1, 9, 9, 9, 1],
  [1, 1, 1, 1, 1]
];

final example2 = [
  [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
  [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
  [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
  [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
  [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
  [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
  [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
  [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
  [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
  [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]
];

void main() {
  test('Parse file', () {
    expect(parseFile('inputTest.txt'), example2);
  });

  test('Cycle octopuses', () {
    expect(cyclingHighlight(example2, 100), 1656);
  });

  test('Find sync', () {
    expect(findAllHighlight(example2), 195);
  });
}
