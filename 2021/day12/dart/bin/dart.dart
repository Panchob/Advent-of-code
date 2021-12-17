import 'package:dart/dart.dart';

void main(List<String> arguments) {
  final caves = parseFile("input.txt");

  print("Part 1: ${findAllPaths(caves, false)}");
  print("Part 2: ${findAllPaths(caves, true)}");
}
