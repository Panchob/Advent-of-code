import 'package:dart/dart.dart';
import 'dart:io';

void main(List<String> arguments) {
  final lines = File('input.txt').readAsStringSync().split('\n').toList();
  final gamma = findGamma(lines);
  final co2Gen = findCo2(lines, 0, false);
  final co2Srcub = findCo2(lines, 0, true);

  print('part 1:' +
      (convertBinaryToInt(gamma, false) * convertBinaryToInt(gamma, true))
          .toString());

  print('part 2:' +
      (convertBinaryToInt(co2Gen, false) * convertBinaryToInt(co2Srcub, false))
          .toString());
}
