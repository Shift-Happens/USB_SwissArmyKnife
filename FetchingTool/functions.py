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
        self.window.geometry("500x600")
        self.window.resizable(False, False)
        self.window.configure(bg="white")
        self.window.iconbitmap("usb.ico")
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(15, weight=1)

        #variables_left_column
        self.ubuntu = tk.IntVar()
        self.kali_linux = tk.IntVar()
        self.tails_os = tk.IntVar()
        self.ubuntu = tk.IntVar()
        self.gparted = tk.IntVar()
        self.qubes_os = tk.IntVar()
        self.windows = tk.IntVar()
        #variables_right_column
        self.internet_browser = tk.IntVar()
        self.text_editor = tk.IntVar()
        self.seven_zip = tk.IntVar()
        self.gimp = tk.IntVar()
        self.tor = tk.IntVar()
        self.gpg = tk.IntVar()
        self.vlc = tk.IntVar()
        self.ventoy_portable = tk.IntVar()
        self.VirtualBox = tk.IntVar()
        self.teamviewer_portable = tk.IntVar()


    def mainloop(self):
        self.window.mainloop()


    def hashmap(self):
        # Create a hashmap
        hashmap = {
            "ubuntu": "https://ubuntu.com/download/desktop",
            "kali_linux": "https://www.kali.org/get-kali",
            "tails_os": "https://tails.boum.org/install/index.en.html",
            "gparted": "https://gparted.org/download.php",
            "qubes_os": "https://www.qubes-os.org/downloads/",
            "windows": "https://www.microsoft.com/en-us/software-download/windows10",
            "internet_browser": "https://www.google.com/chrome/",
            "text_editor": "https://notepad-plus-plus.org/downloads/",
            "seven_zip": "https://www.7-zip.org/download.html",
            "gimp": "https://www.gimp.org/downloads/",
            "tor": "https://www.torproject.org/download/",
            "gpg": "https://www.gnupg.org/download/",
            "vlc": "https://www.videolan.org/vlc/download-windows.html",
            "ventoy_portable": "https://www.ventoy.net/en/download.html",
            "VirtualBox": "https://www.virtualbox.org/wiki/Downloads",
            "teamviewer_portable": "https://www.teamviewer.com/en/download/windows/"

        }
        return hashmap


    def open_urls(self):
        # Open urls in browser
        # This is a bad way to do it, but it works
        if self.ubuntu.get() == 1:
            url_ubuntu = self.hashmap()['ubuntu']
            webbrowser.open_new_tab(url_ubuntu)
        
        if self.kali_linux.get() == 1:
            url_kali_linux = self.hashmap()['kali_linux']
            webbrowser.open_new_tab(url_kali_linux)
        
        if self.tails_os.get() == 1:
            url_tails_os = self.hashmap()['tails_os']
            webbrowser.open_new_tab(url_tails_os)

        if self.gparted.get() == 1:
            url_gparted = self.hashmap()['gparted']
            webbrowser.open_new_tab(url_gparted)

        if self.qubes_os.get() == 1:
            url_qubes_os = self.hashmap()['qubes_os']
            webbrowser.open_new_tab(url_qubes_os)

        if self.windows.get() == 1:
            url_windows = self.hashmap()['windows']
            webbrowser.open_new_tab(url_windows)

        if self.internet_browser.get() == 1:
            url_internet_browser = self.hashmap()['internet_browser']
            webbrowser.open_new_tab(url_internet_browser)

        if self.text_editor.get() == 1:
            url_text_editor = self.hashmap()['text_editor']
            webbrowser.open_new_tab(url_text_editor)

        if self.seven_zip.get() == 1:
            url_seven_zip = self.hashmap()['seven_zip']
            webbrowser.open_new_tab(url_seven_zip)

        if self.gimp.get() == 1:
            url_gimp = self.hashmap()['gimp']
            webbrowser.open_new_tab(url_gimp)
        
        if self.tor.get() == 1:
            url_tor = self.hashmap()['tor']
            webbrowser.open_new_tab(url_tor)

        if self.gpg.get() == 1:
            url_gpg = self.hashmap()['gpg']
            webbrowser.open_new_tab(url_gpg)

        if self.vlc.get() == 1:
            url_vlc = self.hashmap()['vlc']
            webbrowser.open_new_tab(url_vlc)

        if self.ventoy_portable.get() == 1:
            url_ventoy_portable = self.hashmap()['ventoy_portable']
            webbrowser.open_new_tab(url_ventoy_portable)

        if self.VirtualBox.get() == 1:
            url_virtualbox = self.hashmap()['VirtualBox']
            webbrowser.open_new_tab(url_virtualbox)

        if self.teamviewer_portable.get() == 1:
            url_teamviwer_portable = self.hashmap()['teamviewer_portable']
            webbrowser.open_new_tab(url_teamviwer_portable)

        # requests.get(url)
        # for i in [self.ubuntu, self.kali_linux, self.tails_os, self.gparted]:
        #     if i.get() == 1:
        #         url = self.hashmap()[i]
        #         requests.get(url)


    def create_widgets(self):
        # Create widgets
        open_urls_bt = tk.Button(self.window, text="Open URL's", command=self.open_urls, width=25, height=2, bg="blue", fg="white")
        #text
        left_column_text = tk.Label(self.window, text="Operating Systems:          ", bg="white")
        right_column_text = tk.Label(self.window, text="Tools:", bg="white")

        #text_parameters
        left_column_text.configure(font=("Arial", 12, "bold"))
        right_column_text.configure(font=("Arial", 12, "bold"))

        #checklist_left_column:
        checklist_ubuntu = tk.Checkbutton(self.window, text="ubuntu", variable=self.ubuntu, onvalue=1, offvalue=0)
        checklist_kali_linux = tk.Checkbutton(self.window, text="kali linux", variable=self.kali_linux, onvalue=1, offvalue=0)
        checklist_tails_os = tk.Checkbutton(self.window, text="tails os", variable=self.tails_os, onvalue=1, offvalue=0)
        checklist_gparted = tk.Checkbutton(self.window, text="gparted", variable=self.gparted, onvalue=1, offvalue=0)
        checklist_qubes_os = tk.Checkbutton(self.window, text="qubes os", variable=self.qubes_os, onvalue=1, offvalue=0)
        checklist_windows10 = tk.Checkbutton(self.window, text="windows 10", variable=self.windows, onvalue=1, offvalue=0)

        #checklist_right_column: https://portableapps.com/apps/utilities
        checklist_internet_browser = tk.Checkbutton(self.window, text="Brave browser", variable=self.internet_browser, onvalue=1, offvalue=0)
        checklist_text_editor = tk.Checkbutton(self.window, text="Notepad++", variable=self.text_editor, onvalue=1, offvalue=0)
        checklist_seven_zip = tk.Checkbutton(self.window, text="7zip", variable=self.seven_zip, onvalue=1, offvalue=0)
        checklist_gimp = tk.Checkbutton(self.window, text="GIMP", variable=self.gimp, onvalue=1, offvalue=0)
        checklist_tor = tk.Checkbutton(self.window, text="TOR project", variable=self.tor, onvalue=1, offvalue=0)
        checklist_gpg = tk.Checkbutton(self.window, text="GPG", variable=self.gpg, onvalue=1, offvalue=0)
        checklist_vlc = tk.Checkbutton(self.window, text="VLC Player", variable=self.vlc, onvalue=1, offvalue=0)
        checklist_ventoy_portable = tk.Checkbutton(self.window, text="Ventoy Portable", variable=self.ventoy_portable, onvalue=1, offvalue=0)
        checklist_VirtualBox = tk.Checkbutton(self.window, text="VirtualBox", variable=self.VirtualBox, onvalue=1, offvalue=0)
        checklist_teamviewer_portable = tk.Checkbutton(self.window, text="Teamviewer Portable", variable=self.teamviewer_portable, onvalue=1, offvalue=0)


        # checklist_ = tk.Checkbutton(self.window, text="name", variable=self.var1, onvalue=1, offvalue=0)
        
        # Add widgets to window
        open_urls_bt.grid(row=0, column=0, columnspan=2, padx=15, pady=15)
        #left column
        #text
        left_column_text.grid(row=1, column=0, padx=15, pady=10)
        #buttons
        checklist_ubuntu.grid(row=2, column=0, sticky=tk.W ,padx=15, pady=10)
        checklist_kali_linux.grid(row=3, column=0, sticky=tk.W ,padx=15, pady=10)
        checklist_tails_os.grid(row=4, column=0, sticky=tk.W ,padx=15, pady=10)
        checklist_gparted.grid(row=5, column=0, sticky=tk.W ,padx=15, pady=10)    
        checklist_qubes_os.grid(row=6, column=0, sticky=tk.W ,padx=15, pady=10)
        checklist_windows10.grid(row=7, column=0, sticky=tk.W, padx=15, pady=10)

        #right column
        #text
        right_column_text.grid(row=1, column=1, padx=15, pady=10)
        #buttons
        checklist_internet_browser.grid(row=2, column=1, sticky=tk.W ,padx=15, pady=10)
        checklist_text_editor.grid(row=3, column=1, sticky=tk.W , padx=15, pady=10)
        checklist_seven_zip.grid(row=4, column=1, sticky=tk.W, padx=15, pady=10)
        checklist_gimp.grid(row=5, column=1, sticky=tk.W, padx=15, pady=10)
        checklist_tor.grid(row=6, column=1, sticky=tk.W, padx=15, pady=10)
        checklist_gpg.grid(row=7, column=1, sticky=tk.W, padx=15, pady=10)
        checklist_vlc.grid(row=8, column=1, sticky=tk.W, padx=15, pady=10)
        checklist_ventoy_portable.grid(row=9, column=1, sticky=tk.W , padx=15, pady=10)
        checklist_VirtualBox.grid(row=10, column=1, sticky=tk.W, padx=15, pady=10)
        checklist_teamviewer_portable.grid(row=11, column=1, sticky=tk.W , padx=15, pady=10)

    # for test purposes:
    # def read_checklist_state(self):
    #     # Read the state of the checklist
    #     ubuntu = self.ubuntu.get()
    #     kali_linux = self.kali_linux.get()
    #     tails_os = self.tails_os.get()
    #     gparted = self.gparted.get()
    #     qubes_os = self.qubes_os.get()
    #print(..)