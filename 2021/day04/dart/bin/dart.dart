import 'package:dart/dart.dart';
import 'dart:io';

void main(List<String> arguments) {
  final bingoCards = [];
  final text = File('input.txt').readAsStringSync().split("\r\n\r\n").toList();
  final seq = text[0].split(",").map((e) => int.parse(e)).toList();
  text.removeAt(0);

  text.forEach((element) {
    List<List> card = [];
    List<String> rows = element.split("\n").toList();
    rows.forEach((String line) {
      List row = line
          .trim()
          .split(RegExp('\\s+'))
          .toList()
          .map((e) => int.parse(e.trim()))
          .toList();
      card.add(row);
    });
    bingoCards.add(card);
  });

  print("part 1: " + findBingoWinner(seq, bingoCards).toString());
  print("part 2: " + findLastBingoWinner(seq, bingoCards).toString());
}
