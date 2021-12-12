import 'package:dart/dart.dart';

void main(List<String> arguments) {
  print('Part 1: ${cyclingHighlight(parseFile('input.txt'), 100)}');
  print('Part 2: ${findAllHighlight(parseFile('input.txt'))}');
}
