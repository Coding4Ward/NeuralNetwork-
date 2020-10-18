#-*-coding:utf8;-*-
import sys, os, random, json, glob, shutil
from util import *
from mathpy import *
from matrixpy import *


class NeuralNetwork:
      def __init__(self, numberInputNodes=2, numberHiddenNodes=2, numberOutputNodes=1, problem="xorProblem"):
          self.numbInputLayer = numberInputNodes
          self.numbHiddenLayer = numberHiddenNodes
          self.numbOutputLayer = numberOutputNodes
          self.evolutionFileName = problem
          self.modelName = problem+str(self.numbInputLayer)+str(self.numbHiddenLayer)+str(self.numbOutputLayer)+".json"
          self.folderOfSave = problem+str(self.numbInputLayer)+str(self.numbHiddenLayer)+str(self.numbOutputLayer)
          self.hbias = generateBias(self.numbHiddenLayer)
          self.obias = generateBias(self.numbOutputLayer)


          os.chdir(os.path.dirname(os.path.abspath(__file__)))
          if os.path.isdir("data/"+self.folderOfSave):
             pass
          else:
              os.makedirs("data"+"/"+self.folderOfSave)

          if self.loadModel() == False:
             self.initialWeightsIH = generateWeights(self.numbHiddenLayer, self.numbInputLayer)
             self.initialWeightsHO = generateWeights(self.numbOutputLayer, self.numbHiddenLayer)
             self.hiddenBias = generateBiasWeights(self.numbHiddenLayer)
             self.outputBias = generateBiasWeights(self.numbOutputLayer)
             #droid.makeToast("Modelo nao encontrado!")
          else:
              self.loadModel()
              #droid.makeToast("Modelo encontrado.")


      def deleteModel(self):
      	  return deleteModel(self.folderOfSave)

      def takeEpoch(self):
          if verifyModel(self.folderOfSave, self.modelName) == False:
             return 0.0
          else:
               data = self.savedData()
               epoch = json.loads(str(data))
               return epoch["Epoch"]

      def savedData(self):
      	  return savedData(self.folderOfSave, self.modelName)

      def loadModel(self):
          try:
             data = self.savedData()
             weights = json.loads(str(data))
             self.initialWeightsIH = weights["weights"][0]
             self.initialWeightsHO = weights["weights"][1]
             self.hiddenBias = weights["biasWeights"][0]
             self.outputBias = weights["biasWeights"][1]
             return True
          except Exception as e:
                 return False

      def feedForward(self, inputs):
          #Calculating the hidden layer
          hidden = multiply(self.initialWeightsIH, fromArray(inputs))
          hidden = add(hidden, hadamard(self.hbias, self.hiddenBias))
          hidden = sigmoid(hidden)
          #Calculating the output layer
          output = multiply(self.initialWeightsHO, hidden)
          output = add(output, hadamard(self.obias, self.outputBias))
          output = sigmoid(output)
          return fromMatrix(output)
          
      def predict(self, inputs):
      	  #Calculating the hidden layer
          hidden = multiply(self.initialWeightsIH, fromArray(inputs))
          hidden = add(hidden, hadamard(self.hbias, self.hiddenBias))
          hidden = sigmoid(hidden)
          #Calculating the output layer
          output = multiply(self.initialWeightsHO, hidden)
          output = add(output, hadamard(self.obias, self.outputBias))
          output = sigmoid(output)
          return fromMatrix(output)

      def predicted(self, dataset):
      	  result = []
      	  for i in range(len(dataset)):
      	  	  result.append(self.predict(dataset[i][0]))
      	  return result


      
      def BackPropagation(self, inputs, targets, learning_rate):
          # (1) - FEEDFORWARD
          # Calculating the hidden layer
          hidden = multiply(self.initialWeightsIH, fromArray(inputs))
          hidden = add(hidden, hadamard(self.hbias, self.hiddenBias))
          hidden = sigmoid(hidden)

          # Calculating the output layer
          output = multiply(self.initialWeightsHO, hidden)
          output = add(output, hadamard(self.obias, self.outputBias))
          output = sigmoid(output)

          # (2) - BACKPROPAGATION
          # BackPropagation for output layer
          # Calculating output errors
          outputErrors = subtract(fromArray(targets), output)
          # Calculating the output gradients
          outputGradient = hadamard(outputErrors, dsigmoid(output))
          outputGradient = multiply(outputGradient, learning_rate)

          # Calcutating new weights for output layer
          deltaWeightsHO = multiply(outputGradient, transpose(hidden))

          # Adjusting
          self.initialWeightsHO = add(self.initialWeightsHO, deltaWeightsHO)
          self.outputBias = add(self.outputBias, outputGradient)

          # BackPropagation for hidden layer
          # Calculating hidden errors
          hiddenErrors = multiply(transpose(self.initialWeightsHO), outputErrors)
          # Calculating the hidden gradients
          hiddenGradient = hadamard(hiddenErrors, dsigmoid(hidden))
          hiddenGradient = multiply(hiddenGradient, learning_rate)
          # Calcutating new weights for output layer
          deltaWeightsIH = multiply(hiddenGradient, transpose(inputs))
          # Adjusting
          self.initialWeightsIH = add(self.initialWeightsIH, deltaWeightsIH)
          self.hiddenBias = add(self.hiddenBias, hiddenGradient)

          return [[self.initialWeightsIH, self.initialWeightsHO], [self.hiddenBias, self.outputBias], output, outputErrors]


      def train(self, dataset, learning_rate, epoch, randomly=True):
          # VERIFY IF randomly mode IS TRUE OR FALSE
          if randomly == False:
             if typeOf(dataset[0])==0:
                 return "NeuralNetwork could not train because <Dataset must be a matrix!> e.g: dataset = [ [[0,0],[0]], [[1,1], [0]], [[0,1],[1]], [[1,0],[1]] ]"
             cont = 0; cont_data = 0
             
             for ep in range(epoch):
                 for i in range(len(dataset)):
                     result = self.BackPropagation(dataset[i][0], dataset[i][1], learning_rate)
                     print("[","="*50,"]")
                     print("[ PROBLEM-NAME: ",self.evolutionFileName)
                     print("[","="*50,"]")
                     print("[ EPOCH: ",ep,"/",epoch," || FOR-DATASET: ",cont_data)
                     print("[ Expected.: ",dataset[i][1])
                     print("[ Guess....: ",result[2])
                     print("[ Out.Error: ",result[3])
                     print("[","="*50,"]\n\n")

                     if cont_data == (len(dataset)):
                        cont_data = 0
                     cont_data += 1
                 cont += 1

             sumEpoch = epoch+self.takeEpoch()
             # SAVING WEIGHTS FOR EVOLUTION
             os.chdir(os.path.dirname(os.path.abspath(__file__)))
             path = os.getcwd()+"/data/"+self.folderOfSave+"/"+self.modelName
             with open(path, "w") as f:
                  f.write("{"+"\n")
                  f.write('"modelName":'+'"'+self.modelName+'"'+','+'\n\n')
                  f.write('"weights":'+'['+str(result[0][0])+','+str(result[0][1])+'],'+'\n\n')
                  f.write('"biasWeights":'+'['+str(result[1][0])+','+str(result[1][1])+'],'+'\n\n')
                  f.write('"neuralNetworkConfig":'+str(self.numbInputLayer)+str(self.numbHiddenLayer)+str(self.numbOutputLayer)+',\n\n')
                  f.write('"Epoch":'+str(sumEpoch))
                  f.write("\n}")

          elif randomly == True:
               if typeOf(dataset[0])==0:
                  return "NeuralNetwork could not train because <Dataset must be a matrix!> e.g: dataset = [ [[0,0],[0]], [[1,1], [0]], [[0,1],[1]], [[1,0],[1]] ]"
               cont = 0
               for ep in range(epoch):
                   chose_data = random.choice(dataset)
                   result = self.BackPropagation(chose_data[0], chose_data[1], learning_rate)
                   print("[","="*50,"]")
                   print("[ PROBLEM-NAME: ",self.evolutionFileName)
                   print("[","="*50,"]")
                   print("[ EPOCH: ",cont,"/",epoch)
                   print("[ Expected.: ",chose_data[1])
                   print("[ Guess....: ",result[2])
                   print("[ Out.Error: ",result[3])
                   print("[","="*50,"]\n\n")
                   cont += 1

               sumEpoch = epoch+self.takeEpoch()
               # SAVING WEIGHTS FOR EVOLUTION
               os.chdir(os.path.dirname(os.path.abspath(__file__)))
               path = os.getcwd()+"/data/"+self.folderOfSave+"/"+self.modelName
               with open(path, "w") as f:
                    f.write("{"+"\n")
                    f.write('"modelName":'+'"'+self.modelName+'"'+','+'\n\n')
                    f.write('"weights":'+'['+str(result[0][0])+','+str(result[0][1])+'],'+'\n\n')
                    f.write('"biasWeights":'+'['+str(result[1][0])+','+str(result[1][1])+'],'+'\n\n')
                    f.write('"neuralNetworkConfig":'+str(self.numbInputLayer)+str(self.numbHiddenLayer)+str(self.numbOutputLayer)+',\n\n')
                    f.write('"Epoch":'+str(sumEpoch))
                    f.write("\n}")
                    




"""
   NeuralNetwork: Coded by - jmsixpenze
"""



