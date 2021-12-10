import 'dart:io';

final INPUT = 0;
final OUPUT = 1;
final UNIQUES = [2, 3, 4, 7];
final FIVES = ['3', '2', '5'];
final SIXES = ['6', '0', '9'];
Map UNIQUE_VALUES = {2: '1', 3: '7', 4: '4', 7: '8'};

List parseFile(String fileName) {
  return File(fileName)
      .readAsStringSync()
      .split('\n')
      .map((e) => e
          .split(' | ')
          .map((e) => e.split(" ").map((s) => s.trim()).toList())
          .toList())
      .toList();
}

num countUniqueSeq(List signals) {
  num total = 0;

  signals.forEach((element) {
    total += element[OUPUT]
        .fold(0, (p, c) => p + (UNIQUES.contains(c.length) ? 1 : 0));
  });

  return total;
}

String sumOutput(signal, comparator) {
  String ans = '';

  signal[OUPUT].forEach((String s) => {
        if (UNIQUES.contains(s.length))
          {ans += UNIQUE_VALUES[s.length]}
        else if (s.length == 5)
          {
            FIVES.forEach((n) {
              if (s.split('').every((item) => comparator[n].contains(item))) {
                ans += n;
              }
            })
          }
        else
          {
            SIXES.forEach((n) {
              if (s.split('').every((item) => comparator[n].contains(item))) {
                ans += n;
              }
            })
          }
      });
  return ans;
}

num processInput(List signals) {
  Map input = {};
  num total = 0;

  signals.forEach((signal) {
    // 1. get unique
    signal[INPUT].forEach((element) {
      if (element.length == 2) {
        input['1'] = element;
      } else if (element.length == 3) {
        input['7'] = element;
      } else if (element.length == 4) {
        input['4'] = element;
      } else if (element.length == 7) {
        input['8'] = element;
      }
    });

    String middleAndLeft = input["4"]
        .replaceAll(RegExp("(${input["1"][0]}|${input["1"][1]})"), '');
    RegExp match1 = RegExp('(?=.*${input["1"][0]})(?=.*${input["1"][1]})');
    RegExp matchMiddleLeft =
        RegExp('(?=.*${middleAndLeft[0]})(?=.*${middleAndLeft[1]})');

    // 2. finds len 5 based on unique
    signal[INPUT].forEach((element) {
      if (element.length == 5) {
        if (match1.hasMatch(element)) {
          input["3"] = element.split('');
        } else if (matchMiddleLeft.hasMatch(element)) {
          input["5"] = element.split('');
        } else {
          input["2"] = element.split('');
        }
      }
    });

    RegExp match4 = RegExp(
        '(?=.*${input["4"][0]})(?=.*${input["4"][1]})(?=.*${input["4"][2]})(?=.*${input["4"][3]})');

    // 3. find remainings
    signal[INPUT].forEach((element) {
      if (element.length == 6) {
        if (match4.hasMatch(element)) {
          input["9"] = element.split('');
        } else if (matchMiddleLeft.hasMatch(element)) {
          input["6"] = element.split('');
        } else {
          input["0"] = element.split('');
        }
      }
    });

    total += num.parse(sumOutput(signal, input));
  });

  return total;
}
