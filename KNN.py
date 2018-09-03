#!/usr/bin/python
# -*- coding: UTF-8 -*-

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group,labels

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis = 1)
    distance = sqDistance**0.5
    sortedDistIndesticy = distance.argsort()

    classCount = {}

    for i in range(k):
        voteLabels = labels[sortedDistIndesticy[i]]
        classCount[voteLabels] = classCount.get(voteLabels, 0) + 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
