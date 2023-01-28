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
        self.window.geometry("450x350")
        self.window.resizable(False, False)
        self.window.configure(bg="white")
        # self.window.iconbitmap("usb.ico")
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(8, weight=1)

        #variables
        self.ubuntu = tk.IntVar()
        self.kali_linux = tk.IntVar()
        self.tails_os = tk.IntVar()
        self.ubuntu = tk.IntVar()
        self.gparted = tk.IntVar()
        self.qubes_os = tk.IntVar()
        self.windows = tk.IntVar()

    def mainloop(self):
        self.window.mainloop()

    def read_checklist_state(self):
        # Read the state of the checklist
        ubuntu = self.ubuntu.get()
        kali_linux = self.kali_linux.get()
        tails_os = self.tails_os.get()
        gparted = self.gparted.get()
        qubes_os = self.qubes_os.get()

    def hashmap(self):
        # Create a hashmap
        hashmap = {
            "ubuntu": "https://ubuntu.com/download/desktop",
            "kali_linux": "https://www.kali.org/get-kali",
            "tails_os": "https://tails.boum.org/install/index.en.html",
            "gparted": "https://gparted.org/download.php",
            "qubes_os": "https://www.qubes-os.org/downloads/",
            "windows": "https://www.microsoft.com/en-us/software-download/windows10ISO"
        }
        return hashmap


    def open_urls(self):
        # Open urls in browser
        # This is a bad way to do it, but it works
        if self.ubuntu.get() == 1:
            url_ubuntu = self.hashmap()['ubuntu']
            webbrowser.open_new_tab(url_ubuntu)
        else:
            pass
        
        if self.kali_linux.get() == 1:
            url_kali_linux = self.hashmap()['kali_linux']
            webbrowser.open_new_tab(url_kali_linux)
        else:
            pass
        
        if self.tails_os.get() == 1:
            url_tails_os = self.hashmap()['tails_os']
            webbrowser.open_new_tab(url_tails_os)
        else: 
            pass

        if self.gparted.get() == 1:
            url_gparted = self.hashmap()['gparted']
            webbrowser.open_new_tab(url_gparted)
        else:
            pass

        if self.qubes_os.get() == 1:
            url_qubes_os = self.hashmap()['qubes_os']
            webbrowser.open_new_tab(url_qubes_os)
        else:
            pass

        if self.windows.get() == 1:
            url_windows = self.hashmap()['windows']
            webbrowser.open_new_tab(url_windows)
        else:
            pass


        # requests.get(url)
        # for i in [self.ubuntu, self.kali_linux, self.tails_os, self.gparted]:
        #     if i.get() == 1:
        #         url = self.hashmap()[i]
        #         requests.get(url)


    def create_widgets(self):
        # Create widgets
        open_urls_bt = tk.Button(self.window, text="Open URL's", command=self.open_urls, width=25, height=2, bg="blue", fg="white")
        #checklist 
        checklist_ubuntu = tk.Checkbutton(self.window, text="ubuntu", variable=self.ubuntu, onvalue=1, offvalue=0)
        checklist_kali_linux = tk.Checkbutton(self.window, text="kali linux", variable=self.kali_linux, onvalue=1, offvalue=0)
        checklist_tails_os = tk.Checkbutton(self.window, text="tails os", variable=self.tails_os, onvalue=1, offvalue=0)
        checklist_gparted = tk.Checkbutton(self.window, text="gparted", variable=self.gparted, onvalue=1, offvalue=0)
        checklist_qubes_os = tk.Checkbutton(self.window, text="qubes os", variable=self.qubes_os, onvalue=1, offvalue=0)
        checklist_windows10 = tk.Checkbutton(self.window, text="windows 10", variable=self.windows, onvalue=1, offvalue=0)
        # checklist_ = tk.Checkbutton(self.window, text="name", variable=self.var1, onvalue=1, offvalue=0)
        
        # Add widgets to window
        open_urls_bt.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

        #left column
        checklist_ubuntu.grid(row=1, column=0, sticky=tk.N ,padx=15, pady=10)
        checklist_kali_linux.grid(row=2, column=0, sticky=tk.W ,padx=15, pady=10)
        checklist_tails_os.grid(row=3, column=0, sticky=tk.W ,padx=15, pady=10)
        checklist_gparted.grid(row=4, column=0, sticky=tk.W ,padx=15, pady=10)    
        checklist_qubes_os.grid(row=5, column=0, sticky=tk.W ,padx=15, pady=10)

        #right column
        checklist_windows10.grid(row=1, column=1, padx=15, pady=10)


