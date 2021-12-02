import 'package:dart/dart.dart';
import 'package:test/test.dart';

final example = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
final exampleGrouped = [607, 618, 618, 617, 647, 716, 769, 792];
void main() {
  test('part1', () {
    expect(numberOfGreaterThan(example), 7);
  });

  test('part2', () {
    expect(groupListByTree(example), exampleGrouped);
    expect(numberOfGreaterThan(exampleGrouped), 5);
  });
}
