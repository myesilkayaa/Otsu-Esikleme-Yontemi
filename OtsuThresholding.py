# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:20:56 2019

@author: Mehmet YEŞİLKAYA
"""

from PIL import Image
import numpy



image = Image.open("kızKulesi.jpg")
np_im = numpy.array(image,dtype=numpy.int64)
imageWidth,imageHeight = image.size
imageArray = numpy.zeros((imageHeight,imageWidth),dtype=numpy.float64)
histogramArray = numpy.arange(256)

def main():
    griyeCevir()
    histogramFunction()
    otsuMethod()

def griyeCevir():
    
    for i in range(imageHeight):
        for j in range(imageWidth):
            grayValue = int(0.299*np_im[i][j][0] + 0.587*np_im[i][j][1] + 0.114*np_im[i][j][2])
            imageArray[i][j]= grayValue
     


def histogramFunction():
    for i in range(256):
        histogramArray[i]=0
    
    for i in range(imageHeight):
        for j in range(imageWidth):
            temp = int(imageArray[i][j])
            histogramArray[temp]= histogramArray[temp] + 1
    

def otsuMethod():   
    toplamPixelSayısı = 0
    varMax=0
    threshold=0
    for i in range(256):
        toplamPixelSayısı = histogramArray[i]+toplamPixelSayısı
        
    for i in range(256):
        backgroundToplamPixelDegeri = 0
        foregroundToplamPixelDegeri = 0
        backgroundMeanSumVariable = 0
        foregroundMeanSumVariable = 0
        for j in range(256):
            if (i<=j): 
                foregroundToplamPixelDegeri =histogramArray[j]+foregroundToplamPixelDegeri
                foregroundMeanSumVariable = j*histogramArray[j] + foregroundMeanSumVariable        
            else:
                backgroundToplamPixelDegeri = histogramArray[j]+backgroundToplamPixelDegeri
                backgroundMeanSumVariable = j*histogramArray[j] + backgroundMeanSumVariable
        
        # 2 sınıfın ağırlıkları    
        backgroundWeight = backgroundToplamPixelDegeri/toplamPixelSayısı
        foregroundWeight = foregroundToplamPixelDegeri/toplamPixelSayısı
        
        if(backgroundToplamPixelDegeri==0):
            backgroundMean = 0
        else:
#             backgroung ağırlıklı ortalama
             backgroundMean = backgroundMeanSumVariable/backgroundToplamPixelDegeri
            
        if(foregroundToplamPixelDegeri==0):
            foregroundMean = 0
        else:
            #foreground ağırlıklı ortalama
            foregroundMean = foregroundMeanSumVariable/foregroundToplamPixelDegeri

        betweenClassVariance = backgroundWeight*foregroundWeight*((backgroundMean-foregroundMean)*(backgroundMean-foregroundMean))

        if (betweenClassVariance > varMax):
            varMax = betweenClassVariance
            threshold= i;
    
    print("varmax:" , varMax)
    print("threshold :" ,threshold)
    for i in range(imageHeight):
        for j in range(imageWidth):
            if(imageArray[i][j]<threshold ):
                imageArray[i][j]= 0
            else: 
                imageArray[i][j]= 255
           
#    
    rgb = Image.fromarray(imageArray.astype('uint8'))    
    rgb.save("kızKulesiOtsu.jpg")
    rgb.show()   