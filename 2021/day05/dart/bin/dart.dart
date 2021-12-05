import 'package:dart/dart.dart';
import 'dart:io';

void main(List<String> arguments) {
  final positions = parseFile("input.txt");
  print('Part 1: ${countIntersections(positions, false)}');
  print('Part 2: ${countIntersections(positions, true)}');
}
