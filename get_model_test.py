import joblib
import numpy as np
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'optimized_peanut_knn_model.pkl')
model = joblib.load(filename)
test = np.array([[190, 30, 74]])
res = model.predict(test)
print(res)