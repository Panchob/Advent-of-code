import 'package:dart/dart.dart';

void main(List<String> arguments) {
  List signals = parseFile('input.txt');

  print('Part 1: ${countUniqueSeq(signals)}');
  print('Part 2: ${processInput(signals)}');
}
