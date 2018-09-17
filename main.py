#!/usr/bin/python
# -*- coding: utf-8 -*-

import KNN

if __name__ == '__main__':
    group,labels = KNN.createDataSet()
    try:
        x,y,k = input('input x, y, k\n').split()
        #x,y,k=1,1,2
		print(x, y, k)
        probLabel = KNN.classify([int(x),int(y)],group, labels, int(k))
        print(probLabel)
    except Exception as e:
        print(e)

