import 'package:dart/dart.dart';
import 'package:test/test.dart';

final example = [3, 4, 3, 1, 2];
void main() {
  test('Parse file', () {
    expect(parseFile('inputTest.txt'), example);
  });

  test('Spawn fishes', () {
    expect(findTotalFishes(example, 18), 26);
    expect(findTotalFishes(example, 80), 5934);
  });
}
