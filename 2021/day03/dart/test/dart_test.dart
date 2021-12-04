import 'package:dart/dart.dart';
import 'package:test/test.dart';

final example = [
  "00100",
  "11110",
  "10110",
  "10111",
  "10101",
  "01111",
  "00111",
  "11100",
  "10000",
  "11001",
  "00010",
  "01010"
];

void main() {
  final gamma = findGamma(example);
  test('Find gamma', () {
    expect(gamma, [1, 0, 1, 1, 0]);
  });

  test('Convert gamma to int', () {
    expect(convertBinaryToInt(gamma, false), 22);
  });

  test('Convert epsilon to int', () {
    expect(convertBinaryToInt(gamma, true), 9);
  });

  test('Find co2 generator', () {
    expect(findCo2(example, 0, false), [1, 0, 1, 1, 1]);
  });

  test('Find co2 scrubber', () {
    expect(findCo2(example, 0, true), [0, 1, 0, 1, 0]);
  });
}
