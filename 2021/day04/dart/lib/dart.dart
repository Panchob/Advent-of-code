num findBingoWinner(List sequence, List bingoCards) {
  final currentSeq = [];
  int winner = 0;
  bool found = false;

  for (int j = 0; !found; j++) {
    currentSeq.add(sequence[j]);
    for (int i = 0; i < bingoCards.length; i++) {
      found = checkForSeq(bingoCards[i], currentSeq);

      if (found) {
        winner = i;
        break;
      }
    }
  }

  return computeScore(bingoCards[winner], currentSeq);
}

num findLastBingoWinner(List sequence, List bingoCards) {
  final currentSeq = [];

  bool last = false;
  bool found = false;
  int seqPosition = 0;

  while (!last) {
    if (!found) {
      currentSeq.add(sequence[seqPosition]);
      seqPosition += 1;
    }

    for (int i = 0; i < bingoCards.length; i++) {
      found = checkForSeq(bingoCards[i], currentSeq);

      if (found) {
        if (bingoCards.length == 1) {
          last = true;
        } else {
          bingoCards.removeAt(i);
        }

        break;
      }
    }
  }

  return computeScore(bingoCards[0], currentSeq);
}

num computeScore(List<List> card, List seq) {
  num score = 0;

  card.forEach((row) {
    row.forEach((number) {
      score += seq.contains(number) ? 0 : number;
    });
  });

  return score * seq.last;
}

bool checkForSeq(card, seq) {
  if (seq.length < card.length) {
    return false;
  }

  return checkRows(card, seq) || checkColumns(card, seq);
}

bool checkRows(List<List> card, List sequence) {
  bool found = false;

  for (int i = 0; i < card.length; i++) {
    found = card[i].every((element) => sequence.contains(element));

    if (found) {
      break;
    }
  }
  return found;
}

bool checkColumns(List<List> card, List sequence) {
  bool found = false;

  for (int i = 0; i < card.length; i++) {
    List col = [];
    card.forEach((row) {
      col.add(row[i]);
    });

    found = col.every((element) => sequence.contains(element));

    if (found) {
      break;
    }
  }
  return found;
}
