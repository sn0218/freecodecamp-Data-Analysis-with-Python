import numpy as np

def calculate(list):
  # validate function parameters
  if (len(list) < 9):
    raise ValueError("List must contain nine numbers.")
    
  calculations = {}

  # copy the list to numpy array and convert it to 3x3 matrix
  npMatrix = np.array(list).reshape((3, 3))

  # calculate vertical means
  yMean = np.mean(npMatrix, axis=0).tolist()
  # calculate horizontal means
  xMean = np.mean(npMatrix, axis=1).tolist()
  # caluclate flatten mean
  fMean = np.mean(npMatrix).tolist()

  # calculate vertical variance
  yVar = np.var(npMatrix, axis=0, dtype=np.float64).tolist()
  # calculate horizontal variance
  xVar = np.var(npMatrix, axis=1, dtype=np.float64).tolist()
  # calculate flatten variance
  fVar = np.var(npMatrix).tolist()

   # calculate vertical std dev
  ySd = np.std(npMatrix, axis=0, dtype=np.float64).tolist()
  # calculate horizontal std dev
  xSd = np.std(npMatrix, axis=1, dtype=np.float64).tolist()
  # calculate flatten std dev
  fSd = np.std(npMatrix).tolist()

   # calculate vertical max
  yMax = np.max(npMatrix, axis=0).tolist()
  # calculate horizontal max
  xMax = np.max(npMatrix, axis=1).tolist()
  # calculate flatten max
  fMax = np.max(npMatrix).tolist()

   # calculate vertical min
  yMin = np.min(npMatrix, axis=0).tolist()
  # calculate horizontal min
  xMin = np.min(npMatrix, axis=1).tolist()
  # calculate flatten min
  fMin = np.min(npMatrix).tolist()

   # calculate vertical sum
  ySum = np.sum(npMatrix, axis=0).tolist()
  # calculate horizontal sum
  xSum = np.sum(npMatrix, axis=1).tolist()
  # calculate flatten sum
  fSum = np.sum(npMatrix).tolist()

  
  calculations['mean'] = [yMean, xMean, fMean]
  calculations['variance'] = [yVar, xVar, fVar]
  calculations['standard deviation'] = [ySd, xSd, fSd]
  calculations['max'] = [yMax, xMax, fMax]
  calculations['min'] = [yMin, xMin, fMin]
  calculations['sum'] = [ySum, xSum, fSum]

  
  return calculations