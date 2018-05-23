import pickle

file = open("d:\\save.p","rb")

obj = pickle.load(file)
print(obj)
