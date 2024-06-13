import os
import tkinter as tk
from tkinter import ttk
import subprocess

class ServerInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Server toolbox")
        self.geometry("400x500")
        
        self.tabControl = ttk.Notebook(self)
        self.tabControl.pack(expand=1, fill="both")

        self.welcome_tab = ttk.Frame(self.tabControl)
        self.users_tab = ttk.Frame(self.tabControl)
        self.groups_tab = ttk.Frame(self.tabControl)
        self.features_tab = ttk.Frame(self.tabControl)
        self.logs_tab = ttk.Frame(self.tabControl)
        self.GPO_tab = ttk.Frame(self.tabControl)
        self.Edit_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.welcome_tab, text='Welcome')
        self.tabControl.add(self.users_tab, text='Users')
        self.tabControl.add(self.groups_tab, text='Groups')
        self.tabControl.add(self.features_tab, text='Features')
        self.tabControl.add(self.logs_tab, text='Logs')
        self.tabControl.add(self.GPO_tab, text='GPO')
        self.tabControl.add(self.Edit_tab, text='Edit Domain')

        self.setup_welcome_tab()
        self.setup_users_tab()
        self.setup_groups_tab()
        self.setup_features_tab()
        self.setup_logs_tab()
        self.setup_GPO_tab()
        self.setup_Edit_tab()

    def setup_welcome_tab(self):
        welcome_label = ttk.Label(self.welcome_tab, text="Welcome to TheImperium Domain!")
        welcome_label.pack(pady=20)

        # Execute and display system information
        system_info = subprocess.check_output('powershell "Get-WmiObject Win32_NTDomain"', shell=True).decode()
        info_label = ttk.Label(self.welcome_tab, text=system_info)
        info_label.pack(pady=10)

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

    def setup_Edit_tab(self):
        edit_label = ttk.Label(self.Edit_tab, text="Edit Users:")
        edit_label.pack(pady=10)
        # Lav funktion Knapper
        open_netplwiz_button = ttk.Button(self.Edit_tab, text="Manage User Accounts", command=self.open_netplwiz)
        open_netplwiz_button.pack(pady=10)

        export_users_button = ttk.Button(self.Edit_tab, text="Export to CSV", command=self.export_users_to_csv)
        export_users_button.pack(pady=10)

        network_settings_button = ttk.Button(self.Edit_tab, text="Network Settings", command=self.open_network_settings)
        network_settings_button.pack(pady=10)

        # Ensure the Edit_tab is properly initialized and packed to display content
        # self.Edit_tab.pack(expand=True, fill="both")

    def open_netplwiz(self):
        subprocess.Popen('netplwiz', shell=True)

    def export_users_to_csv(self):
        import csv
        import subprocess
        users_info = subprocess.check_output('net user', shell=True).decode().split('\n')
        users = [user.strip() for user in users_info if user.strip() and "----" not in user and "User accounts for" not in user]
        
        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Username"])
            for user in users:
                writer.writerow([user])

        # export brugere csv fil
        # Placeholder for future implementation
        pass

    def open_network_settings(self):
        subprocess.Popen('ncpa.cpl', shell=True)

if __name__ == "__main__":
    app = ServerInterface()
    app.mainloop()

