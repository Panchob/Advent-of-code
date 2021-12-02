Map moveSub(List instructions) {
  final position = {"dep": 0, "hor": 0};

  instructions.forEach((instruction) {
    mapping[instruction["dir"]]!(instruction["value"], position);
  });

  return position;
}

Map moveSubWithAim(List instructions) {
  final position = {"dep": 0, "hor": 0, "aim": 0};

  instructions.forEach((instruction) {
    mappingWithAim[instruction["dir"]]!(instruction["value"], position);
  });

  return position;
}

final mapping = {
  "up": (n, pos) => pos["dep"] -= n,
  "down": (n, pos) => pos["dep"] += n,
  "forward": (n, pos) => pos["hor"] += n,
};

final mappingWithAim = {
  "up": (n, pos) => pos["aim"] -= n,
  "down": (n, pos) => pos["aim"] += n,
  "forward": (n, pos) => moveForward(n, pos),
};

Object moveForward(value, position) {
  position["hor"] += value;
  position["dep"] += position["aim"] * value;

  return position;
}
