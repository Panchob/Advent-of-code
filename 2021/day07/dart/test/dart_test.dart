import 'package:dart/dart.dart';
import 'package:test/test.dart';

final example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14];

void main() {
  test('Parse file', () {
    expect(parseFile('inputTest.txt'), example);
  });

  test('Find median', () {
    expect(findMedian(example), 2);
  });

  test('Find fuel cost', () {
    expect(moveCrabs(example), 37);
  });

  test('Find fuel cost again', () {
    expect(moveCrabsButForReal(example), 168);
  });

  test('Sum fuel cost ', () {
    expect(processFuel(3), 6);
    expect(processFuel(0), 0);
    expect(processFuel(1), 1);
    expect(processFuel(11), 66);
    expect(processFuel(9), 45);
  });
}
