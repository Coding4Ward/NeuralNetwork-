#-*-coding:utf8;-*-
from matrixpy import *
from math import log
import math

# calculate mean squared error
def mean_squared_error(actual, predicted):
    sum_square_error = 0.0
    for i in range(len(actual)):
        sum_square_error += (actual[i] - predicted[i])**2.0
    mean_square_error = 1.0 / len(actual) * sum_square_error
    return mean_square_error

# calculate binary cross entropy
def binary_cross_entropy(actual, predicted):
    sum_score = 0.0
    for i in range(len(actual)):
        sum_score += actual[i] * log(1e-15 + predicted[i]) + (1 - actual[i]) * log(1 + 1e-15 - predicted[i])
        mean_sum_score = 1.0 / len(actual) * sum_score
    return -mean_sum_score

# calculate categorical cross entropy
def categorical_cross_entropy(actual, predicted):
    sum_score = 0.0
    for i in range(len(actual)):
        for j in range(len(actual[i])):
            sum_score += actual[i][j] * log(1e-15 + predicted[i][j])
    mean_sum_score = 1.0 / len(actual) * sum_score
    return -mean_sum_score

def accuracy(actual, predicted):
	total = 0.0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
		   total += 1.0
		else:
			pass
	return total/(len(predicted))



def sigmoid(data_x):
    if typeOf(data_x)==0: #Array
       return list(map(lambda x: 1/(1+math.exp(-x)), data_x))
    elif typeOf(data_x)==1: #Matrix
       result = []
       for rows in data_x:
           result.append(list(map(lambda x: 1/(1+math.exp(-x)), rows)))
       return result
    else: return "<the object> must be an array or matrix"
    
def dsigmoid(data_x):
    if typeOf(data_x)==0: #Array
       return list(map(lambda x: x*(1-x), data_x))
    elif typeOf(data_x)==1: #Matrix
       result = []
       for rows in data_x:
           result.append(list(map(lambda x: x*(1-x), rows)))
       return result
    else: return "<the object> must be an array or matrix"


# EXTRACT THE FIRST 3 CHANCES OF DIGIT RECOGNITION RESULT
def extractChance1(guess):
  try:
     chance = sorted(guess, reverse=True); result = []
     for i in range(len(guess)):
         if chance[0] == guess[i]:
            result.append(str(i)+" - "+str(chance[0]))
     return result
  except Exception as e:
         return e


def extractChance2(guess):
    try:
       chance = sorted(guess, reverse=True); result = []
       for i in range(len(guess)):
           if chance[1] == guess[i]:
              result.append(str(i)+" - "+str(chance[1]))
       return result
    except Exception as e:
           return e

def extractChance3(guess):
    try:
       chance = sorted(guess, reverse=True); result = []
       for i in range(len(guess)):
           if chance[2] == guess[i]:
              result.append(str(i)+" - "+str(chance[2]))
       return result
    except Exception as e:
           return e

def extractChance4(guess):
    try:
       chance = sorted(guess, reverse=True); result = []
       for i in range(len(guess)):
           if chance[3] == guess[i]:
              result.append(str(i)+" - "+str(chance[3]))
       return result
    except Exception as e:
           return e

def extractChance5(guess):
    try:
       chance = sorted(guess, reverse=True); result = []
       for i in range(len(guess)):
           if chance[4] == guess[i]:
              result.append(str(i)+" - "+str(chance[4]))
       return result
    except Exception as e:
           return e


def extractChance6(guess):
    try:
       chance = sorted(guess, reverse=True); result = []
       for i in range(len(guess)):
           if chance[5] == guess[i]:
              result.append(str(i)+" - "+str(chance[5]))
       return result
    except Exception as e:
           return e

def extractChance7(guess):
    try:
       chance = sorted(guess, reverse=True); result = []
       for i in range(len(guess)):
           if chance[6] == guess[i]:
              result.append(str(i)+" - "+str(chance[6]))
       return result
    except Exception as e:
           return e


def extractChance8(guess):
    try:
       chance = sorted(guess, reverse=True); result = []
       for i in range(len(guess)):
           if chance[7] == guess[i]:
              result.append(str(i)+" - "+str(chance[7]))
       return result
    except Exception as e:
           return e          



def extractChance9(guess):
    try:
       chance = sorted(guess, reverse=True); result = []
       for i in range(len(guess)):
           if chance[8] == guess[i]:
              result.append(str(i)+" - "+str(chance[8]))
       return result
    except Exception as e:
           return e


def extractChance(guess):
    try:
       return [extractChance1(guess), extractChance2(guess), extractChance3(guess), extractChance4(guess), extractChance5(guess), extractChance6(guess), extractChance7(guess), extractChance8(guess), extractChance9(guess)]
    except Exception as e:
           return e


def extractNumber(array):
    try:
        result = []
        for i in range(len(array)):
            if array[i] == 1.0:
               result.append(i)
        return result
    except Exception as e:
           return e

def nX(number, array):
    cont = 0.0
    for i in range(len(array)):
        if array[i] == number:
           cont += 1
    return cont

