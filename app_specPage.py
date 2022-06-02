# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:03:49 2022

@author: A90127
"""
import tkinter as tk
import numpy as np
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from app_GUI import GUI
from readme import frame_styles
from RecipeCompare import app_evaluation

class specPage(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        self.name ='specPage'
        frame1 = tk.LabelFrame(self, frame_styles, text="濃度光譜變化率")
        frame1.place(relx=0.1, rely=0.02, height=550, width=172)
        frame1_1 = tk.LabelFrame(frame1, frame_styles,text='配方組差異評分')
        frame1_1.place(relx=0.01, rely=0.27, height=383, width=162)
        frame2 = tk.LabelFrame(self, frame_styles, text="光譜圖形")
        frame2.place(relx=0.27, rely=0.02, height=550, width=630)
        
        Label1 = tk.Label(frame1,text='胚布材質',width=10)
        self.var1 = tk.StringVar()
        self.Combobox1_1 = ttk.Combobox(frame1,textvariable=self.var1,
                                   values = ['T','N','D'],width=8,state="readonly")
        self.Combobox1_1.current(0)
        self.Combobox1_1.bind('<<ComboboxSelected>>', self.dyes_changed)
        Label2 = tk.Label(frame1,text='染劑1')
        self.var2 = tk.StringVar()
        self.Combobox1_2 = ttk.Combobox(frame1,textvariable=self.var2,
                                   values = [''],width=8,state="readonly")
        self.Combobox1_2.current(0)
        self.Combobox1_2.bind('<<ComboboxSelected>>', self.plot)
        Label3 = tk.Label(frame1,text='染劑2')
        self.var3 = tk.StringVar()
        self.Combobox1_3 = ttk.Combobox(frame1,textvariable=self.var3,
                                   values = [''],width=8,state="readonly")
        self.Combobox1_3.current(0)
        self.Combobox1_3.bind('<<ComboboxSelected>>', self.plot)
        Label1.grid(row=0,column=0,sticky='nsew')
        Label2.grid(row=1,column=0,sticky='nsew')
        Label3.grid(row=2,column=0,sticky='nsew')
        self.Combobox1_1.grid(row=0,column=1,sticky='nsew')
        self.Combobox1_2.grid(row=1,column=1,sticky='nsew')
        self.Combobox1_3.grid(row=2,column=1,sticky='nsew')
        
        Label4 = tk.Label(frame1_1,text='配方組1',width=10)
        Label5 = tk.Label(frame1_1,text='染劑1',width=10)
        self.var4 = tk.StringVar()
        self.Combobox1_1_1 = ttk.Combobox(frame1_1,textvariable=self.var4,
                                   values = [''],width=8,state="readonly")
        self.Combobox1_1_1.current(0)
        Label6 = tk.Label(frame1_1,text='染劑2')
        self.var5 = tk.StringVar()
        self.Combobox1_1_2 = ttk.Combobox(frame1_1,textvariable=self.var5,
                                   values = [''],width=8,state="readonly")
        self.Combobox1_1_2.current(0)
        Label7 = tk.Label(frame1_1,text='染劑3')
        self.var6 = tk.StringVar()
        self.Combobox1_1_3 = ttk.Combobox(frame1_1,textvariable=self.var6,
                                   values = [''],width=8,state="readonly")
        self.Combobox1_1_3.current(0)
        Label8 = tk.Label(frame1_1,text='配方組2',width=10)
        Label9 = tk.Label(frame1_1,text='染劑1')
        self.var7 = tk.StringVar()
        self.Combobox1_1_4 = ttk.Combobox(frame1_1,textvariable=self.var7,
                                   values = [''],width=8,state="readonly")
        self.Combobox1_1_4.current(0)
        Label10 = tk.Label(frame1_1,text='染劑2')
        self.var8 = tk.StringVar()
        self.Combobox1_1_5 = ttk.Combobox(frame1_1,textvariable=self.var8,
                                   values = [''],width=8,state="readonly")
        self.Combobox1_1_5.current(0)
        Label11 = tk.Label(frame1_1,text='染劑3')
        self.var9 = tk.StringVar()
        self.Combobox1_1_6 = ttk.Combobox(frame1_1,textvariable=self.var9,
                                   values = [''],width=8,state="readonly")
        self.Combobox1_1_6.current(0)
        Label4.grid(row=0,column=0,sticky='nsew',columnspan=2)
        Label5.grid(row=1,column=0,sticky='nsew')
        Label6.grid(row=2,column=0,sticky='nsew')
        Label7.grid(row=3,column=0,sticky='nsew')
        self.Combobox1_1_1.grid(row=1,column=1,sticky='nsew')
        self.Combobox1_1_2.grid(row=2,column=1,sticky='nsew')
        self.Combobox1_1_3.grid(row=3,column=1,sticky='nsew')
        Label8.grid(row=4,column=0,sticky='nsew',columnspan=2)
        Label9.grid(row=5,column=0,sticky='nsew')
        Label10.grid(row=6,column=0,sticky='nsew')
        Label11.grid(row=7,column=0,sticky='nsew')
        self.Combobox1_1_4.grid(row=5,column=1,sticky='nsew')
        self.Combobox1_1_5.grid(row=6,column=1,sticky='nsew')
        self.Combobox1_1_6.grid(row=7,column=1,sticky='nsew')
        Button1 = tk.Button(frame1_1,text='計算差異指數',command=self.evaluation,fg='#00F')
        Label12 = tk.Label(frame1_1,text='平均')
        self.Label13 = tk.Label(frame1_1,fg='#080',relief='ridge')
        Label14 = tk.Label(frame1_1,text='最大值')
        self.Label15 = tk.Label(frame1_1,fg='#080',relief='ridge')
        Label16 = tk.Label(frame1_1,text='最小值')
        self.Label17 = tk.Label(frame1_1,fg='#080',relief='ridge')
        Button1.grid(row=8,column=0,sticky='nsew',columnspan=2)
        Label12.grid(row=9,column=0,sticky='nsew') 
        self.Label13.grid(row=9,column=1,sticky='nsew')
        Label14.grid(row=10,column=0,sticky='nsew') 
        self.Label15.grid(row=10,column=1,sticky='nsew')
        Label16.grid(row=11,column=0,sticky='nsew') 
        self.Label17.grid(row=11,column=1,sticky='nsew')
        
        
        
        self.f = Figure(figsize=(5, 4), dpi=100)
        self.f_plot = self.f.add_subplot(111)
        self.canvs = FigureCanvasTkAgg(self.f, frame2)
        self.canvs.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def dyes_changed(self,*arg):
        m = self.var1.get()
        ls = ['']+sorted([d for d in self.Dyes.keys() 
                           if self.Dyes[d].material==m], key=lambda x:x[2:])
        self.Combobox1_2['values'] = ls
        self.Combobox1_3['values'] = ls
        self.Combobox1_1_1['values'] = ls
        self.Combobox1_1_2['values'] = ls
        self.Combobox1_1_3['values'] = ls
        self.Combobox1_1_4['values'] = ls
        self.Combobox1_1_5['values'] = ls
        self.Combobox1_1_6['values'] = ls
        
    def plot(self,*arg):
        self.f_plot.clear()
        x = list(range(360,710,10))
        dyes = [self.var2.get(),self.var3.get()]
        dyes = [d for d in dyes if d]
        specs = [ls for d in dyes for ls in self.Dyes[d].spec]
        for spec in specs:
            self.f_plot.plot(x,spec)
        self.f_plot.set_ylabel('reflection')
        self.f_plot.set_title('spectrum data')
        self.f_plot.set_xlabel('wave length(nm)')
        self.canvs.draw()
        
    def evaluation(self,*arg):
        dyes1 = [self.var4.get(),self.var5.get(),self.var6.get()]
        dyes2 = [self.var7.get(),self.var8.get(),self.var9.get()]
        score, specsls1, specsls2 = app_evaluation(dyes1,dyes2,self.Dyes)
        self.Label13.config(text=round(score.mean(),4))
        self.Label15.config(text=round(score.max(),4))
        self.Label17.config(text=round(score.min(),4))
        self.f_plot.clear()
        
        colors = [i for i in '0123456789ABCDE']
        x = list(range(360,710,10))
        for spec1,spec2 in zip(specsls1,specsls2):
            color = '#'+''.join(np.random.choice([i  for i in colors],3))
            self.f_plot.plot(x,spec1,c=color)
            self.f_plot.plot(x,spec2,c=color)    
        self.f_plot.set_ylabel('reflection')
        self.f_plot.set_title('spectrum data')
        self.f_plot.set_xlabel('wave length(nm)')
        self.canvs.draw()

        
        