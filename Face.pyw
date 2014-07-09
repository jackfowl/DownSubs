import sys
import Tkinter as tk
import OpenSubtitles
import urllib

class CheckboxSubTitle(tk.Checkbutton):
    
    def __init__(self, master=None):
        tk.Checkbutton.__init__(self, master)
        self.var = tk.IntVar()
        self.config(variable=self.var)

    def fill(self, texto='', url=''):
        self.config(text=texto)
        self.name=texto
        self.url=url
        
    def value(self):
        return self.var.get()
        
class Application(tk.Frame):              
   
    checkBoxes = []
    def baixar(self):
        for box in self.checkBoxes:
            if box.value() == 1:
                urllib.urlretrieve(box.url, box.name+".zip")
        
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()
        self.getLegendas()

    def createWidgets(self):
        top=self.winfo_toplevel()                
        self.down = tk.Button(self, text='Download', command=self.baixar)
        self.down.grid(row=2, column=0, stick=tk.W)
        self.quit = tk.Button(self, text='Fechar', command=top.destroy)
        self.quit.grid(row=2, column=1, stick=tk.E)
        
    def getLegendas(self):
        if len(sys.argv) > 1:
            for arquivo in sys.argv[1:]:
                self.createBoxes(OpenSubtitles.Legendas(arquivo))
        
    def createBoxes(self, lista):
        for item in lista:
            self.checkBoxes.append(CheckboxSubTitle(self))
            self.checkBoxes[-1].fill(item['name'],item['url'])
            self.checkBoxes[-1].grid(sticky=tk.W)

app = Application()                       
app.master.title('SubDownloader')    
app.mainloop()                            
