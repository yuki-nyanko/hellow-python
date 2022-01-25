import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("データの個数=",len(digits.images))
print("画像データ=",digits.images[0])
print("何の数か=",digits.target[0])
