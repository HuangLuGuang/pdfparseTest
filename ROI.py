s = "299.000 1.000 -1.000 298.842 -0.158 0.000"
res = s.split(" ")
keys = ["AX", "NOMINAL", "+TOL", "-TOL", "MEAS", "DEV", "OUTTOL"]
res = zip(keys, res)
res = dict(res)
print(res)


