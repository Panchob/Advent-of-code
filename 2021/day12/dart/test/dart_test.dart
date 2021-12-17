import 'package:dart/dart.dart';
import 'package:test/test.dart';

final example = {
  'dc': ['end', 'start', 'HN', 'LN', 'kj'],
  'end': ['dc', 'HN'],
  'HN': ['start', 'dc', 'end', 'kj'],
  'start': ['HN', 'kj', 'dc'],
  'kj': ['start', 'sa', 'HN', 'dc'],
  'LN': ['dc'],
  'sa': ['kj']
};

void main() {
  test('ParseFile', () {
    expect(parseFile('inputTest.txt'), example);
  });

  test('Find all paths', () {
    expect(findAllPaths(example, false), 19);
  });

  test('Find all paths 2', () {
    expect(findAllPaths(example, true), 103);
  });
}
