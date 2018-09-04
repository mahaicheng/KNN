#!/usr/bin/python
# -*- coding: utf-8 -*-

import KNN

if __name__ == '__main__':
    group,labels = KNN.createDataSet()
    try:
        x,y,k = input('input x, y, k\n').split()
        probLabel = KNN.classify0([int(x),int(y)],group, labels, int(k))
        print(probLabel)
    except Exception as e:
        print(e)

