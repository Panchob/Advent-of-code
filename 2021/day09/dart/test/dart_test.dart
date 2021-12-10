import 'package:dart/dart.dart';
import 'package:test/test.dart';

final example = [
  [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
  [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
  [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
  [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
  [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
];
void main() {
  test('ParseFile', () {
    expect(parseFile("inputTest.txt"), example);
  });

  test('Find lowest', () {
    expect(checkForLower(example), 15);
  });

  test('Find basin', () {
    expect(checkForBasin(example), 1134);
  });
}
