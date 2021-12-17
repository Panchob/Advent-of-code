import 'package:dart/dart.dart';

void main(List<String> arguments) {
  Map parsedData = parseFile('input.txt');

  print(
      'Part 1: ${numberAfterFold(parsedData['points'], parsedData['instructions'], true)}');

  print(
      'Part 2: ${numberAfterFold(parsedData['points'], parsedData['instructions'], false)}');
}
