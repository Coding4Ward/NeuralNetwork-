#-*-coding:utf8;-*-
from NeuralNetWork.NeuralNetwork import NeuralNetwork
import sys, os, json, random

def read():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.getcwd()+"\data.json"
    with open(path, "r") as f:
         return f.read()
def access(key):
    return json.loads(read())[key]



dataset = access("xor_dataset")

nn = NeuralNetwork(numberInputNodes=2, numberHiddenNodes=5, numberOutputNodes=1, problem="xor")
nn.train(dataset=dataset, learning_rate=0.10, epoch=10, randomly=True)

print("\n\n\n\n [ ","="*55," ]")
print("[ Known - data ]")
for i in range(len(dataset)):
    print("[ Expected: ",dataset[i][1], "For <",dataset[i][0],">"," || Guess: ",nn.predict(dataset[i][0]))
print("[ ","="*55," ]")



	  


