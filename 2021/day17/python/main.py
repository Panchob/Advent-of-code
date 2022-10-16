
X_RANGE=(137, 171)
Y_RANGE=(-98, -73)



if __name__ == '__main__':
  x = 0
  y = 0
  maxY=0
  total=set()

  while(x <= X_RANGE[1]):
    x += 1
    y = Y_RANGE[0] - 1
    while(y <= abs(Y_RANGE[0])):
      y += 1
      currentX = 0
      currentY = 0
      xVelocity = x
      yVelocity = y
      currentMaxY = 0
      while True:
        currentX += xVelocity
        currentY += yVelocity
        xVelocity -= int(xVelocity > 0)
        yVelocity -= 1

        if currentY > currentMaxY:
          currentMaxY = currentY
        
        if ((currentX >= X_RANGE[0] and currentX <= X_RANGE[1])
          and (currentY >= Y_RANGE[0] and currentY <= Y_RANGE[1])):
            total.add((x,y))
            if currentMaxY > maxY:
              maxY = currentMaxY
        
        if currentX > X_RANGE[1]: break
        if currentY < Y_RANGE[0]: break
        
  print(maxY, len(total))


