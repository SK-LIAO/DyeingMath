# -*- coding: utf-8 -*-
"""
Created on Thu May 26 08:20:27 2022

@author: A90127
"""

import numpy as np
from itertools import combinations as cb
import matplotlib.pyplot as plt

from cieData import observer, SPD_D65
from cieMath import numInt, Spec2LAB
from DyeMerge import IsFluo, SpecEst, Merge, DyeMatch

#給定空間四面體四點座標矩陣T4(4X3),與另一點p
#回傳 該點是否在 四面體內部。
def isInnerTetrahedron(T4,p):
    for T3,w in zip(list(cb(T4,3)),list(cb(T4,1))[::-1]):
        v = w[0]
        N = np.cross(T3[2]-T3[0],T3[1]-T3[0])
        sign1 = np.sign(np.dot(N,v-T3[0]))
        sign2 = np.sign(np.dot(N,p-T3[0]))
        if sign1*sign2<0:
            return False
    else:
        return True
#圖像化看看四面體內點測試是否正確
def graph(T4,p):
    ax = plt.figure().add_subplot(projection='3d')
    curve = np.array([T4[0],T4[1],T4[2],T4[0],T4[3],T4[1],T4[3],T4[2]])
    ax.plot(curve[:,0],curve[:,1],curve[:,2])
    ax.scatter([p[0]],[p[1]],[p[2]],s=120,c='#F00',marker='*')
    plt.show()

#光譜差異評分,分數越低差異性越低(即符合性越高)。    
def score(spec1,spec2):
    diff = np.abs(spec1-spec2)
    x, y, z = observer   
    S = SPD_D65
    Sx, Sy, Sz = S*x, S*y, S*z 
    X_ref = numInt(Sx*diff,10)
    Y_ref = numInt(Sy*diff,10)
    Z_ref = numInt(Sz*diff,10)
    return np.linalg.norm([X_ref,Y_ref,Z_ref])

#給定配方組1、配方組2、染劑字典
#回傳同色異譜指數
def app_evaluation(dyes1,dyes2,Dyes):
    fiber = Dyes[dyes1[0]].spec[0]
    T4_1 = np.array([Spec2LAB(fiber)] + [Spec2LAB(Dyes[d].spec[-1]) for d in dyes1])
    T4_2 = np.array([Spec2LAB(fiber)] + [Spec2LAB(Dyes[d].spec[-1]) for d in dyes2])
    
    LABmax = np.min(np.vstack((np.max(T4_1,axis=0),np.max(T4_2,axis=0))),axis=0)
    LABmin = np.max(np.vstack((np.min(T4_1,axis=0),np.min(T4_2,axis=0))),axis=0)
    
    flls1 = [IsFluo([d]) for d in dyes1]
    conclsls1 = [Dyes[d].conc for d in dyes1]
    speclsls1 = [Dyes[d].spec for d in dyes1]
    flls2 = [IsFluo([d]) for d in dyes2]
    conclsls2 = [Dyes[d].conc for d in dyes2]
    speclsls2 = [Dyes[d].spec for d in dyes2]
    
    scores = np.zeros(5)
    specsls1 = []
    specsls2 = []
    for i in range(5):
        rdLAB = [np.random.uniform(m,M) for M,m in zip(LABmax,LABmin)]
        while not isInnerTetrahedron(T4_1, rdLAB) or not isInnerTetrahedron(T4_2, rdLAB):
            rdLAB = [np.random.uniform(m,M) for M,m in zip(LABmax,LABmin)]
        concs1, err1, _ = DyeMatch(rdLAB,conclsls1,speclsls1,flls1)
        concs2, err2, _ = DyeMatch(rdLAB,conclsls2,speclsls2,flls2)
        while err1>0.25 or err2>0.25:
            rdLAB = [np.random.uniform(m,M) for M,m in zip(LABmax,LABmin)]
            while not isInnerTetrahedron(T4_1, rdLAB) or not isInnerTetrahedron(T4_2, rdLAB):
                rdLAB = [np.random.uniform(m,M) for M,m in zip(LABmax,LABmin)]
            concs1, err1, _ = DyeMatch(rdLAB,conclsls1,speclsls1,flls1)
            concs2, err2, _ = DyeMatch(rdLAB,conclsls2,speclsls2,flls2)
        print('got {}'.format(i+1))
        specs1 = [SpecEst(Dyes[d].conc,Dyes[d].spec,c,IsFluo([d])) for c,d in zip(concs1,dyes1)]
        spec1 = Merge(concs1, specs1, fiber, 'KSadd', any(flls1))
        specs2 = [SpecEst(Dyes[d].conc,Dyes[d].spec,c,IsFluo([d])) for c,d in zip(concs2,dyes2)]
        spec2 = Merge(concs2,specs2,fiber,'KSadd',any(flls2))
        scores[i] = score(spec1, spec2)
        specsls1 += [spec1]
        specsls2 += [spec2]
        
    return scores, np.array(specsls1), np.array(specsls2)
        
