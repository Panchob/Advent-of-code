import 'package:dart/dart.dart';
import 'package:test/test.dart';

final example = [
  {"dir": "forward", "value": 5},
  {"dir": "down", "value": 5},
  {"dir": "forward", "value": 8},
  {"dir": "up", "value": 3},
  {"dir": "down", "value": 8},
  {"dir": "forward", "value": 2}
];

void main() {
  test('move submarine', () {
    expect(moveSub(example), {"hor": 15, "dep": 10});
  });

  test('move submarine with aim', () {
    expect(moveSubWithAim(example), {"hor": 15, "dep": 60, "aim": 10});
  });
}
