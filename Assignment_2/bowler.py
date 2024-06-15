def findavg(runs,wickets):
  if wickets == 0:
    print(0.0)
  return runs/wickets

def economyrate(overs,runs):
  if runs == 0:
    print(0.0)
  return runs/overs