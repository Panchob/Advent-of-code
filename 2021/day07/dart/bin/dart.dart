import 'package:dart/dart.dart' as dart;

void main(List<String> arguments) {
  List<int> crabs = dart.parseFile("input.txt");

  print('Part 1: ${dart.moveCrabs(crabs)}');
  print('Part 3: ${dart.moveCrabsButForReal(crabs)}');
}
