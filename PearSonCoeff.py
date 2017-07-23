import numpy as np
PhysicsScores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
HistoryScores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

PhysicsScores = np.array(PhysicsScores)
HistoryScores = np.array(HistoryScores)

p2 = PhysicsScores*PhysicsScores
h2 = HistoryScores*HistoryScores

ph = PhysicsScores*HistoryScores

N = len(PhysicsScores)

tempNum = N*np.sum(ph)-(np.sum(PhysicsScores)*np.sum(HistoryScores))
tempDen = pow(N*np.sum(p2)-pow(np.sum(PhysicsScores), 2),0.5)*pow(N*np.sum(h2)-pow(np.sum(HistoryScores), 2),0.5)

PC = tempNum/tempDen

print("%.3f"%PC)