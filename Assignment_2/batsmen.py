def findavarage(runs,matches):
  if matches == 0:
    print(0.0)
  return runs/matches

def findstrikerate(runs,balls):
  if balls == 0:
    print(0.0)
  return (runs/balls)*100

findstrikerate(11,7)
