# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:03:49 2022

@author: A90127
"""
import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from app_GUI import GUI
from readme import frame_styles

class specPage(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        self.name ='specPage'
        frame1 = tk.LabelFrame(self, frame_styles, text="染劑選擇")
        frame1.place(relx=0.1, rely=0.02, height=50, width=800)
        frame2 = tk.LabelFrame(self, frame_styles, text="光譜圖形")
        frame2.place(relx=0.1, rely=0.12, height=500, width=800)
        
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
        Label2.grid(row=0,column=2,sticky='nsew')
        Label3.grid(row=0,column=4,sticky='nsew')
        self.Combobox1_1.grid(row=0,column=1,sticky='nsew')
        self.Combobox1_2.grid(row=0,column=3,sticky='nsew')
        self.Combobox1_3.grid(row=0,column=5,sticky='nsew')
        
        self.f = Figure(figsize=(5, 4), dpi=100)
        self.f_plot = self.f.add_subplot(111)
        self.canvs = FigureCanvasTkAgg(self.f, frame2)
        self.canvs.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def dyes_changed(self,*arg):
        m = self.var1.get()
        ls = sorted(['']+[d for d in self.Dyes.keys() 
                           if self.Dyes[d].material==m])
        self.Combobox1_2['values'] = ls
        self.Combobox1_3['values'] = ls
        
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

        
        