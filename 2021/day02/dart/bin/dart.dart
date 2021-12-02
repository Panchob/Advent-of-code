import 'package:dart/dart.dart';
import 'dart:io';

void main(List<String> arguments) {
  final lines = File('input.txt').readAsStringSync().split('\n');
  final instructions = lines
      .map((l) => {"dir": l.split(" ")[0], "value": int.parse(l.split(" ")[1])})
      .toList();

  final positionPart1 = moveSub(instructions);
  print("part 1: " + (positionPart1["hor"] * positionPart1["dep"]).toString());

  final positionPart2 = moveSubWithAim(instructions);
  print("part 2: " + (positionPart2["hor"] * positionPart2["dep"]).toString());
}
