import 'dart:io';
import 'package:dart/dart.dart';

void main(List<String> arguments) {
  final lines = File('input.txt').readAsStringSync().split('\n');
  final List depths = lines.map((it) => int.parse(it.trim())).toList();
  final sums = groupListByTree(depths);

  print('part 1: ' + numberOfGreaterThan(depths).toString());
  print('part 1: ' + numberOfGreaterThan(sums).toString());
}
