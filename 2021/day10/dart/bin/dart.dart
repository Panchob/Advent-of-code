import 'package:dart/dart.dart';

void main(List<String> arguments) {
  final lines = parseFile('input.txt');
  print('Part 1: ${checkForError(lines)}');
  print('Part 2: ${autoComplete(lines)}');
}
