import 'package:dart/dart.dart';

void main(List<String> arguments) {
  final fishes = parseFile('input.txt');

  print('Part 1: ${findTotalFishes(fishes, 80)}');
  // Expect a little time for most entries to be memoized
  print('Part 2: ${findTotalFishes(fishes, 256)}');
}
