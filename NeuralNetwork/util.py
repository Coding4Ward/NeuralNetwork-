#-*-coding:utf8;-*-
import os, shutil

def deleteModel(folderOfSave):
	os.chdir(os.path.dirname(os.path.abspath(__file__)))
	path = os.getcwd()+"/data/"+folderOfSave
	try:
		shutil.rmtree(path)
		return True
	except Exception as e:
		   return False

def savedData(folderOfSave, modelName):
	try:
		os.chdir(os.path.dirname(os.path.abspath(__file__)))
		path = os.getcwd()+"/data/"+folderOfSave+"/"+modelName
		arq = open(path, 'r')
		info = arq.read()
		arq.close()
		return info
	except Exception as e:
		   return "<there's no saved data for this model!>"

def actual(dataset):
	result = []
	for i in range(len(dataset)):
		result.append(dataset[i][1])
	return result

def verifyModel(folderOfSave, modelName):
	try:
		os.chdir(os.path.dirname(os.path.abspath(__file__)))
		path = os.getcwd()+"/data/"+folderOfSave+"/"+modelName
		arq = open(path, 'r')
		arq.close()
		return True
	except Exception as e:
		   return False