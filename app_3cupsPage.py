# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:28:28 2022

@author: A90127
"""

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from app_GUI import GUI
from readme import frame_styles
from numpy import array,zeros,vstack, transpose, linalg
from DyeMerge import SpecEst, Merge, IsFluo, DyeMatch,tetrahedron
from cieMath import Spec2LAB

class hit3cupsPage(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        self.name ='hit3cupsPage'
        frame1 = tk.LabelFrame(self, frame_styles, text="參數設定")
        frame1.place(relx=0.1, rely=0.02, height=550, width=232)
        frame2 = tk.LabelFrame(self, frame_styles, text="模擬結果色差")
        frame2.place(relx=0.33, rely=0.02, height=550, width=570)
        
        lb1_1 = tk.Label(frame1,text='材質')
        lb1_2 = tk.Label(frame1,text='染劑1')
        lb1_3 = tk.Label(frame1,text='染劑2')
        lb1_4 = tk.Label(frame1,text='染劑3')
        lb1_5 = tk.Label(frame1,text='濃度',width=8)
        lb1_6 = tk.Label(frame1,text='濃度')
        lb1_7 = tk.Label(frame1,text='濃度')
        self.var1 = tk.StringVar()
        self.cb1_1 = ttk.Combobox(frame1,textvariable=self.var1,
                                   values = ['T','N','D'],
                                   width=6,state="readonly")
        self.cb1_1.current(0)
        self.cb1_1.bind('<<ComboboxSelected>>', self.dyes_changed1)
        self.var2 = tk.StringVar()
        self.cb1_2 = ttk.Combobox(frame1,textvariable=self.var2,
                                   values = [''],
                                   width=6,state="readonly")
        self.cb1_2.current(0)
        self.var3 = tk.StringVar()
        self.cb1_3 = ttk.Combobox(frame1,textvariable=self.var3,
                                   values = [''],
                                   width=6,state="readonly")
        self.cb1_3.current(0)
        self.var4 = tk.StringVar()
        self.cb1_4 = ttk.Combobox(frame1,textvariable=self.var4,
                                   values = [''],
                                   width=6,state="readonly")
        self.cb1_4.current(0)
        self.et1_1 = tk.Entry(frame1,width=8,
                                validate='key',validatecommand=(parent.register(controller.Is_float), '%P'))
        self.et1_2 = tk.Entry(frame1,width=8,
                                validate='key',validatecommand=(parent.register(controller.Is_float), '%P'))
        self.et1_3 = tk.Entry(frame1,width=8,
                                validate='key',validatecommand=(parent.register(controller.Is_float), '%P'))
        lb1_1.grid(row=0,column=0,sticky='nsew')
        lb1_2.grid(row=1,column=0,sticky='nsew')
        lb1_3.grid(row=2,column=0,sticky='nsew')
        lb1_4.grid(row=3,column=0,sticky='nsew')
        lb1_5.grid(row=1,column=2,sticky='nsew')
        lb1_6.grid(row=2,column=2,sticky='nsew')
        lb1_7.grid(row=3,column=2,sticky='nsew')
        self.cb1_1.grid(row=0,column=1,sticky='nsew')        
        self.cb1_2.grid(row=1,column=1,sticky='nsew')        
        self.cb1_3.grid(row=2,column=1,sticky='nsew')
        self.cb1_4.grid(row=3,column=1,sticky='nsew')
        self.et1_1.grid(row=1,column=3)
        self.et1_2.grid(row=2,column=3)
        self.et1_3.grid(row=3,column=3)
        
        lb1_8 = tk.Label(frame1,text='色差',fg='#F00')
        lb1_9 = tk.Label(frame1,text='DL',fg='#F00')
        lb1_10 = tk.Label(frame1,text='Da*',fg='#F00')
        lb1_11 = tk.Label(frame1,text='Db*',fg='#F00')
        lb1_12 = tk.Label(frame1,text='配方1',fg='#00F')
        self.et1_4 = tk.Entry(frame1,width=7,
                              validate='key',validatecommand=(parent.register(controller.Is_float), '%P'))
        self.et1_5 = tk.Entry(frame1,width=7,
                              validate='key',validatecommand=(parent.register(controller.Is_float), '%P'))
        self.et1_6 = tk.Entry(frame1,width=7,
                              validate='key',validatecommand=(parent.register(controller.Is_float), '%P'))
        lb1_8.grid(row=4,column=0,sticky='nsew')
        lb1_9.grid(row=4,column=1,sticky='nsew')
        lb1_10.grid(row=4,column=2,sticky='nsew')
        lb1_11.grid(row=4,column=3,sticky='nsew')
        lb1_12.grid(row=5,column=0,sticky='nsew')
        self.et1_4.grid(row=5,column=1,sticky='nsew')
        self.et1_5.grid(row=5,column=2,sticky='nsew')
        self.et1_6.grid(row=5,column=3,sticky='nsew')
        bt1_1 = tk.Button(frame1,text='模擬線性調修1',command=self.analysis1,fg='#00F')
        #bt1_4 = tk.Button(frame1,text='模擬線性調修2',command=self.analysis4,fg='#00F')
        bt1_2 = tk.Button(frame1,text='建議三杯打色1',command=self.analysis2,fg='#00F')
        #bt1_3 = tk.Button(frame1,text='建議三杯打色2',command=self.analysis3,fg='#00F')
        lb1_16 = tk.Label(frame1,text="修正1",fg="#00F")
        lb1_13 = tk.Label(frame1,text='配方2',fg='#00F')
        lb1_14 = tk.Label(frame1,text='配方3',fg='#00F')
        lb1_15 = tk.Label(frame1,text='配方4',fg='#00F')
        bt1_1.grid(row=6,column=0,sticky='nsew',columnspan=4)
        #bt1_4.grid(row=7,column=0,sticky='nsew',columnspan=4)
        bt1_2.grid(row=9,column=0,sticky='nsew',columnspan=4)
        #bt1_3.grid(row=10,column=0,sticky='nsew',columnspan=4)
        lb1_16.grid(row=8,column=0,sticky='nsew')
        lb1_13.grid(row=11,column=0,sticky='nsew')
        lb1_14.grid(row=12,column=0,sticky='nsew')
        lb1_15.grid(row=13,column=0,sticky='nsew')
        
        self.lb = {}
        for i in [8,11,12,13]:
            for j in range(1,4):
                self.lb[(i,j)] = tk.Label(frame1,fg='#080',relief='ridge') 
                self.lb[(i,j)].grid(row=i,column=j,sticky='nsew')
        
        
        fig = Figure()         
        self.canvas = FigureCanvasTkAgg(fig,frame2)
        self.canvas.draw()
        self.ax = fig.add_subplot(111, projection="3d")
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def dyes_changed1(self,*arg):
        m = self.var1.get()
        ls = ['']+sorted([d for d in self.Dyes.keys() 
                           if self.Dyes[d].material==m], key=lambda x:x[2:])
        self.cb1_2['values'] = ls
        self.cb1_3['values'] = ls
        self.cb1_4['values'] = ls
    
    #模擬線性調修1
    def analysis1(self):
        dyes_ = [self.var2.get(),self.var3.get(),self.var4.get()]
        dyes = [d for d in dyes_ if d]
        concs_ = [self.et1_1.get(), self.et1_2.get(),self.et1_3.get()]
        concs = [float(i) for i in concs_ if i]
        fiber = self.Dyes[dyes[0]].spec[0]
        fl = IsFluo(dyes)
        if fl:
            C = sum(concs)
            specs = [SpecEst(self.Dyes[d].conc,self.Dyes[d].spec,C,IsFluo([d])) for d in dyes]
            self.stdspec = Merge(concs,specs,fiber,'nonequi',fl)
        else:
            specs = [SpecEst(self.Dyes[d].conc,self.Dyes[d].spec,c,IsFluo([d])) for c,d in zip(concs,dyes)]
            self.stdspec = Merge(concs,specs,fiber,'KSadd',fl)
        self.stdlab = Spec2LAB(self.stdspec)
        DLab = array([float(self.et1_4.get()),float(self.et1_5.get()),float(self.et1_6.get())])
        lab_ = self.stdlab + DLab
        concls = [self.Dyes[d].conc for d in dyes]
        specls = [self.Dyes[d].spec for d in dyes]
        flls = [IsFluo([d]) for d in dyes if d]
        cAprox, _, labAprox = DyeMatch(lab_,concls,specls,flls)
        j0 = 0
        for j in range(1,4):
            self.lb[(8,j)].config(text='')
            if dyes_[j-1]:
                self.lb[(8,j)].config(text=round(2*concs[j0]-cAprox[j0],4))
                j0 += 1
        
    #建議三杯打色1    
    def analysis2(self):
        dyes_ = [self.var2.get(),self.var3.get(),self.var4.get()]
        dyes = [d for d in dyes_ if d]
        concs_ = [self.et1_1.get(), self.et1_2.get(),self.et1_3.get()]
        concs = [float(i) for i in concs_ if i]
        fiber = self.Dyes[dyes[0]].spec[0]
        fl = IsFluo(dyes)
        if fl:
            C = sum(concs)
            specs = [SpecEst(self.Dyes[d].conc,self.Dyes[d].spec,C,IsFluo([d])) for d in dyes]
            self.stdspec = Merge(concs,specs,fiber,'nonequi',fl)
        else:
            specs = [SpecEst(self.Dyes[d].conc,self.Dyes[d].spec,c,IsFluo([d])) for c,d in zip(concs,dyes)]
            self.stdspec = Merge(concs,specs,fiber,'KSadd',fl)
        self.stdlab = Spec2LAB(self.stdspec)
        DLab = array([float(self.et1_4.get()),float(self.et1_5.get()),float(self.et1_6.get())])
        DLab1, DLab2, DLab3 = tetrahedron(DLab)
        concls = [self.Dyes[d].conc for d in dyes]
        specls = [self.Dyes[d].spec for d in dyes]
        flls = [IsFluo([d]) for d in dyes if d]
        for i,d in zip([11,12,13],[DLab1,DLab2,DLab3]):
            lab = self.stdlab + d - DLab
            cAprox, deltaE, labAprox = DyeMatch(lab,concls,specls,flls)
            if deltaE>0.2:
                tk.messagebox.showinfo(title='注意', message='配方{}誤差大於0.2'.format(i-10))
            j0 = 0
            for j in range(1,4):
                self.lb[(i,j)].config(text='')
                if dyes_[j-1]:
                    self.lb[(i,j)].config(text=round(cAprox[j0],4))
                    j0+=1
                
        mat = array([DLab,DLab1,DLab2,DLab3])
        center = array([0,0,0])
        
        self.ax.clear()
        curve1 = array([mat[0],center,mat[1],center,mat[2],center,mat[3]])
        curve2 = array([mat[0],mat[1],mat[2],mat[0],mat[3],mat[1],mat[3],mat[2]])
        self.ax.plot(curve1[:,1],curve1[:,2],curve1[:,0])
        self.ax.plot(curve2[:,1],curve2[:,2],curve2[:,0])
        self.ax.scatter([0],[0],[0],s=120,c='#F00',marker='*')
        for x,y,z,label in zip(mat[:,1],mat[:,2],mat[:,0],['Recipe 1','Recipe 2','Recipe 3','Recipe 4']):
            self.ax.text(x,y,z,label)
        self.ax.set_xlabel("Da* ",c='#F00',fontsize=20)
        self.ax.set_ylabel("Db*",c='#F00',fontsize=20)
        self.ax.set_zlabel("DL",c='#F00',fontsize=20)
        self.ax.set_title("Delta La*b* Space of Dying")
        self.canvas.draw()
    
    '''算是個失敗的估計方式
    #建議三杯打色2
    #根據L值判斷染劑濃度過高或過低、對配方3取2做總濃度10%調整計算    
    def analysis3(self):
        #抓面板數據資訊
        dyes_ = [self.var2.get(),self.var3.get(),self.var4.get()]
        dyes = [d for d in dyes_ if d]
        concs_ = [self.et1_1.get(), self.et1_2.get(),self.et1_3.get()]
        concs = array([float(i) for i in concs_ if i])
        if len(dyes)!=3 or len(concs)!=3:
            tk.messagebox.showerror(title='錯誤', message='數據不足、無法計算')
            return
        DLab = array([float(self.et1_4.get()),float(self.et1_5.get()),float(self.et1_6.get())])
        fiber = self.Dyes[dyes[0]].spec[0]
        #找三染劑形成的的Lab空間基底向量
        basis = array([Spec2LAB(self.Dyes[n].spec[-1])-Spec2LAB(self.Dyes[n].spec[0]) for n in dyes])
        basis = transpose(basis)
        proj = linalg.solve(basis, DLab)
        proj = -proj/linalg.norm(proj)
        conc123 = zeros((3,3))
        for i,loc in zip([11,12,13],[(0,1),(1,2),(0,2)]):
            c = 0.08*sum(concs)
            n = linalg.norm(DLab)
            for j,p in enumerate(proj):
                self.lb[(i,j+1)].config(text='')
                if j in loc:
                    self.lb[(i,j+1)].config(text=max(round(concs[j]+p*c*n,4),0))
                    conc123[i-11,j] = max(round(concs[j]+p*c*n,4),0)
                else:
                    self.lb[(i,j+1)].config(text=round(concs[j],4))
                    conc123[i-11,j] = round(concs[j],4)
        
        fl = IsFluo(dyes)
        conc1234 = vstack((concs,conc123))
        mat = zeros((4,3))
        for i,conc in enumerate(conc1234):
            if fl:
                C = sum(conc)
                specs = [SpecEst(self.Dyes[d].conc,self.Dyes[d].spec,C,IsFluo([d])) for d in dyes]
                stdspec = Merge(concs,specs,fiber,'nonequi',fl)
            else:
                specs = [SpecEst(self.Dyes[d].conc,self.Dyes[d].spec,c,IsFluo([d])) for c,d in zip(conc,dyes)]
                stdspec = Merge(conc,specs,fiber,'KSadd',fl)
            mat[i] = Spec2LAB(stdspec)
        self.ax.clear()
        curve = array([mat[0],mat[1],mat[2],mat[0],mat[3],mat[1],mat[3],mat[2]])
        self.ax.plot(curve[:,1],curve[:,2],curve[:,0])
        for x,y,z,label in zip(mat[:,1],mat[:,2],mat[:,0],['Recipe 1','Recipe 2','Recipe 3','Recipe 4']):
            self.ax.text(x,y,z,label)
        self.ax.set_xlabel("a* ",c='#F00',fontsize=20)
        self.ax.set_ylabel("b*",c='#F00',fontsize=20)
        self.ax.set_zlabel("L",c='#F00',fontsize=20)
        self.ax.set_title("La*b* Space of Dying")
        self.canvas.draw()    
     
     
    #模擬線性調修2    
    def analysis4(self):
        dyes_ = [self.var2.get(),self.var3.get(),self.var4.get()]
        dyes = [d for d in dyes_ if d]
        concs_ = [self.et1_1.get(), self.et1_2.get(),self.et1_3.get()]
        concs = [float(i) for i in concs_ if i]
        fiber = self.Dyes[dyes[0]].spec[0]
        fl = IsFluo(dyes)
        if fl:
            C = sum(concs)
            specs = [SpecEst(self.Dyes[d].conc,self.Dyes[d].spec,C,IsFluo([d])) for d in dyes]
            self.stdspec = Merge(concs,specs,fiber,'nonequi',fl)
        else:
            specs = [SpecEst(self.Dyes[d].conc,self.Dyes[d].spec,c,IsFluo([d])) for c,d in zip(concs,dyes)]
            self.stdspec = Merge(concs,specs,fiber,'KSadd',fl)
        self.stdlab = Spec2LAB(self.stdspec)
        DLab = array([float(self.et1_4.get()),float(self.et1_5.get()),float(self.et1_6.get())])
        lab_ = self.stdlab - DLab
        concls = [self.Dyes[d].conc for d in dyes]
        specls = [self.Dyes[d].spec for d in dyes]
        flls = [IsFluo([d]) for d in dyes if d]
        cAprox, _, labAprox = DyeMatch(lab_,concls,specls,flls)
        j0 = 0
        for j in range(1,4):
            self.lb[(8,j)].config(text='')
            if dyes_[j-1]:
                self.lb[(8,j)].config(text=round(cAprox[j0],4))
                j0 += 1
     '''     
            
            
    