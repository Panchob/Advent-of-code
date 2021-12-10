import 'package:dart/dart.dart';

void main(List<String> arguments) {
  List heatMap = parseFile("input.txt");
  print('part 1: ${checkForLower(heatMap)}');
  print('part 2: ${checkForBasin(heatMap)}');
}
