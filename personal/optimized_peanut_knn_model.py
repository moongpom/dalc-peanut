import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import joblib

r = []
g = []
b = []
color_target = []
cnt = 0

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'color_hex.txt')
with open(filename, 'r') as input:
  lines = input.read().splitlines()
  for line in lines:
    line = line.replace(' ', '')
    if line == "":
        continue
    elif line[-1] != '1' and line[-1] != '2' and line[-1] != '3' and line[-1] != '4':
        continue
    else:
        cnt+=1
        color_info = line.split(',')
        r.append(int(color_info[0][1:3], 16))
        g.append(int(color_info[0][3:5], 16))
        b.append(int(color_info[0][5:7], 16))
        color_target.append(int(color_info[1]))
color_data = [[r, g, b] for r, g, b in zip(r, g, b)]

input = np.array(color_data)
target = np.array(color_target)
np.random.seed(42)
index = np.arange(cnt)
np.random.shuffle(index)

train_input = input[index[:900]]
train_target = target[index[:900]]

test_input = input[index[900:]]
test_target = target[index[900:]]

from sklearn.model_selection import cross_val_score
k_range = input.shape[0]//2
k_list = []

for i in range(3, k_range, 2):
  k_list.append(i)

# print(k_list)

# 최적의 k값
k_scores_k = []
for k in k_list:
  knn = KNeighborsClassifier(n_neighbors=k)
  scores = cross_val_score(knn, input, target, cv = 10 , scoring = 'accuracy')
  k_scores_k.append([k, scores.mean()])

# print(k_scores_k) // k =3
# 최적의 cv값 // k =3 (고정)

k_scores_cv = []
for i in range(2,50):
  knn = KNeighborsClassifier(n_neighbors=3)
  scores = cross_val_score(knn, input, target, cv = i , scoring = 'accuracy')
  k_scores_cv.append([i, scores.mean()])
# print(k_scores_cv)  // optimization = cv 10

# 최종 모델

knn = KNeighborsClassifier(n_neighbors=3)
final_scores = cross_val_score(knn, input, target, cv =10 , scoring = 'accuracy')
k_scores = final_scores.mean()

# print(round(k_scores,3)) // 0.608

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_input, train_target)
filename = os.path.join(scriptpath, 'optimized_peanut_knn_model.pkl')
joblib.dump(knn, filename)
#knn.score(test_input, test_target)
