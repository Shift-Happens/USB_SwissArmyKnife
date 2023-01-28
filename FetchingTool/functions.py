import tkinter as tk
import requests
import webbrowser

#1. Create a function that creates a window 
#2. Create a function that creates widgets
#3. Create a function that creates a checklist for opening urls
#4. Create a function that opens urls in browser


class Gui:        
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("USB Swiss army knife")
        self.window.geometry("400x350")
        self.window.resizable(False, False)
        #variables
        self.ubuntu = tk.IntVar()
        self.kali_linux = tk.IntVar()
        self.tails_os = tk.IntVar()
        self.ubuntu = tk.IntVar()
        self.gparted = tk.IntVar()


    def mainloop(self):
        self.window.mainloop()

    def read_checklist_state(self):
        # Read the state of the checklist
        ubuntu = self.ubuntu.get()
        kali_linux = self.kali_linux.get()
        tails_os = self.tails_os.get()
        gparted = self.gparted.get()


    def hashmap(self):
        # Create a hashmap
        hashmap = {
            "ubuntu": "https://ubuntu.com/download/desktop",
            "kali_linux": "https://www.kali.org/get-kali",
            "tails_os": "https://tails.boum.org/install/index.en.html",
            "gparted": "https://gparted.org/download.php"
        }
        return hashmap


    def open_urls(self):
        # Open urls in browser
        if self.ubuntu.get() == 1:
            url = self.hashmap()['ubuntu']
        elif self.kali_linux.get() == 1:
            url = self.hashmap()['kali_linux']
        elif self.tails_os.get() == 1:
            url = self.hashmap()['tails_os']
        elif self.gparted.get() == 1:
            url = self.hashmap()['gparted']

        #te które są 1 do listy i potem w pętli otwieraj
    
        webbrowser.open_new_tab(url)
        # requests.get(url)
        # for i in [self.ubuntu, self.kali_linux, self.tails_os, self.gparted]:
        #     if i.get() == 1:
        #         url = self.hashmap()[i]
        #         requests.get(url)


    def create_widgets(self):
        # Create widgets
        open_urls_bt = tk.Button(self.window, text="Open URL's", command=self.open_urls)
        #checklist 
        checklist_ubuntu = tk.Checkbutton(self.window, text="ubuntu", variable=self.ubuntu, onvalue=1, offvalue=0)
        checklist_kali_linux = tk.Checkbutton(self.window, text="kali linux", variable=self.kali_linux, onvalue=1, offvalue=0)
        checklist_tails_os = tk.Checkbutton(self.window, text="tails os", variable=self.tails_os, onvalue=1, offvalue=0)
        checklist_gparted = tk.Checkbutton(self.window, text="gparted", variable=self.gparted, onvalue=1, offvalue=0)
        # checklist_ = tk.Checkbutton(self.window, text="name", variable=self.var1, onvalue=1, offvalue=0)
        
        # Add widgets to window
        open_urls_bt.grid(row=0, column=0, padx=10, pady=10)

        checklist_ubuntu.grid(row=1, column=0, padx=10, pady=10)
        checklist_kali_linux.grid(row=2, column=0, padx=10, pady=10)
        checklist_tails_os.grid(row=3, column=0, padx=10, pady=10)
        checklist_gparted.grid(row=4, column=0, padx=10, pady=10)    


