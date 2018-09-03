#!/usr/bin/python
# -*- coding: UTF-8 -*-

import KNN

if __name__ == '__main__':

    t = (('A', 1), ('B', 2))
    d = dict(t)


    group,labels = KNN.createDataSet()
    print(group)
    print(labels)
    probLabel = KNN.classify0([0,0],group, labels, 3)
    print(probLabel)

