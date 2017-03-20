#coding=utf-8
#from __future__ import print_function
'''
./clintontrump-data-for-ui/clintontrump.vocabulary
./clintontrump-data-for-ui/clintontrump.bagofwords.train
./clintontrump-data-for-ui/clintontrump.labels.train
'''
from Tkinter import *
import ttk


import time

import LoadData   as ld
import NaiveBayes as n_b



def read_v():

    w_to_i = {}
    with open('./clintontrump-data-for-ui/clintontrump.vocabulary','rb') as source:
        for line in source:
            [idx, word] = line.rstrip("\n").split("\t")
            w_to_i[word[:-1]] = idx

    return w_to_i


def calculate(*args):
    try:
        testVar = tweet.get()
        #print (testVar)
        l = testVar.split(" ")
        print(l)
        doc = []
        for word in l:
            if word in w_to_i.keys():
                doc.append(int(w_to_i[word]))
        print(doc)
        # test on based on Py & Pwy
        t1 = float(time.clock())
        #y_hat = naiveBayesModel.predictY_bernoulli_withtag(doc)
        y_hat = naiveBayesModel.predictY_bernoulli(doc)
        if y_hat == 0:
            ans = str0
        else:
            ans = str1
        print ('===========>'+ans)
        t2 = float(time.clock())
        print ('Bernoulli Model predict, using time %.4f s, \n' % (t2-t1))
        predict.set(ans)

    except ValueError:
        pass





print ('************Welcome to the World of Bayes!***********\n')
time.clock()
t0 = float(time.clock())
# # load data, and save as the format under NaiveBayes.
#DIR_RESULT            = "./Result/"
DIR                   = "./clintontrump-data-for-ui/"
FILENAME_BASIC        = "clintontrump."
[vocList, wordNum]    = ld.LoadData_vocabulary(DIR+FILENAME_BASIC+"vocabulary")
[trainX, trainDocNum] = ld.LoadData_bagOfWords(DIR+FILENAME_BASIC+"bagofwords.train")
#[devX,  devDocNum]    = ld.LoadData_bagOfWords(DIR+FILENAME_BASIC+"bagofwords.dev")
#[testX,  testDocNum]  = ld.LoadData_bagOfWords(DIR+FILENAME_BASIC+"bagofwords.test")
str0    = "realDonaldTrump"
str1    = "HillaryClinton"
trainY  = ld.LoadData_labels(DIR+FILENAME_BASIC+"labels.train", str0)
devY   = ld.LoadData_labels(DIR+FILENAME_BASIC+"labels.dev", str0)
t1 = float(time.clock())
print ('Loading data File. using time %.4f s, \n' % (t1-t0))
t2 = float(time.clock())
# # define NaiveBayes instance, and calc prior P(y)
naiveBayesModel = n_b.NAIVE_BAYES_MODEL(wordNum, trainDocNum, trainX, trainY)
naiveBayesModel.estimatePy_MLE()
print ('Mode initializaion, using time %.4f s, \n' % (t2-t1))
#Predict the input
###### Bernoulli model
#LearnAndPredict(nbModel, str0, str1)

# learn Pwy based on Bernoulli model
t1 = float(time.clock())
lapAlpha = 1
naiveBayesModel.estimatePwy_bernoulli()
naiveBayesModel.laplSmoothPwy_bernouli(lapAlpha)
w_to_i = read_v()
t2 = float(time.clock())
print ('Mode estimation, using time %.4f s, \n' % (t2-t1))


############ ui operation #########
root = Tk()
print('start GUI root')
root.title("Twitter classification")

sty = ttk.Style()
sty.configure('my.TButton', font=('Helvetica', 30))
sty1 = ttk.Style()
sty1.configure('my.Label', font=('Helvetica', 30))

mainframe = ttk.Frame(root, padding="40 40 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
tweet = StringVar()
predict = StringVar()
tweet_entry = ttk.Entry(mainframe, width=30, textvariable=tweet,font=('Arial', 30))
tweet_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=predict,font=('Arial', 30,'italic'),foreground='#1478e2').grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Predict", style='my.TButton', command=calculate).grid(column=2, row=5, sticky=W)
ttk.Label(mainframe, text="Input your twitter", style='my.Label').grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Your twitter is more like", style='my.Label').grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="style", style='my.Label').grid(column=3, row=3, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

tweet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()

t2 = float(time.clock())
print ('Overall time %.4f s, \n' % (t2-t1))
