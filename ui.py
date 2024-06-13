import os
import tkinter as tk
from tkinter import ttk
import subprocess

class ServerInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Server Management Interface")
        self.geometry("400x300")
        
        self.tabControl = ttk.Notebook(self)
        self.tabControl.pack(expand=1, fill="both")
        
        self.users_tab = ttk.Frame(self.tabControl)
        self.groups_tab = ttk.Frame(self.tabControl)
        self.features_tab = ttk.Frame(self.tabControl)
        self.logs_tab = ttk.Frame(self.tabControl)
        self.GPO_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.users_tab, text='Users')
        self.tabControl.add(self.groups_tab, text='Groups')
        self.tabControl.add(self.features_tab, text='Features')
        self.tabControl.add(self.logs_tab, text='Logs')
        self.tabControl.add(self.GPO_tab, text='GPO')
        
        self.setup_users_tab()
        self.setup_groups_tab()
        self.setup_features_tab()
        self.setup_logs_tab()
        self.setup_GPO_tab()

    def setup_users_tab(self):
        user_label = ttk.Label(self.users_tab, text="User Index:")
        user_label.pack(pady=10)
        user_listbox = tk.Listbox(self.users_tab)
        user_listbox.pack(expand=True, fill="both")
        # Fetching system users
        users = subprocess.check_output('net user', shell=True).decode().split('\n')[4:-2]
        for user in users:
            user_listbox.insert(tk.END, user.strip())

    def setup_groups_tab(self):
        group_label = ttk.Label(self.groups_tab, text="Group Index:")
        group_label.pack(pady=10)
        group_listbox = tk.Listbox(self.groups_tab)
        group_listbox.pack(expand=True, fill="both")
        # Fetching system groups
        groups = subprocess.check_output('net localgroup', shell=True).decode().split('\n')[4:-2]
        for group in groups:
            group_listbox.insert(tk.END, group.strip())

    def setup_features_tab(self):
        feature_label = ttk.Label(self.features_tab, text="Server Features:")
        feature_label.pack(pady=10)
        feature_listbox = tk.Listbox(self.features_tab)
        feature_listbox.pack(expand=True, fill="both")
        # Fetching system features
        features = subprocess.check_output('systeminfo', shell=True).decode().split('\n')
        features = [f.strip() for f in features if "feature" in f.lower()]
        for feature in features:
            feature_listbox.insert(tk.END, feature)

    def setup_logs_tab(self):
        log_label = ttk.Label(self.logs_tab, text="System Logs:")
        log_label.pack(pady=10)
        log_text = tk.Text(self.logs_tab, wrap='word', height=10)
        log_text.pack(expand=True, fill="both")
        # Fetching system logs
        logs = subprocess.check_output('wevtutil qe System "/q:*[System [(Level=1 or Level=2)]]" /c:10 /f:text', shell=True).decode().split('\n')
        for log in logs:
            log_text.insert(tk.END, log + '\n')

    def setup_GPO_tab(self):
        gpo_label = ttk.Label(self.GPO_tab, text="Group Policy Objects:")
        gpo_label.pack(pady=10)
        gpo_listbox = tk.Listbox(self.GPO_tab)
        gpo_listbox.pack(expand=True, fill="both")
        # Fetching GPOs
        gpos = subprocess.check_output('gpresult /R', shell=True).decode().split('\n')
        gpos = [g.strip() for g in gpos if "GPO" in g]
        for gpo in gpos:
            gpo_listbox.insert(tk.END, gpo)

if __name__ == "__main__":
    app = ServerInterface()
    app.mainloop()

