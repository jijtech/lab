import tkinter as tk
from tkinter import ttk

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
        
        self.tabControl.add(self.users_tab, text='Users')
        self.tabControl.add(self.groups_tab, text='Groups')
        self.tabControl.add(self.features_tab, text='Features')
        
        self.setup_users_tab()
        self.setup_groups_tab()
        self.setup_features_tab()
    
    def setup_users_tab(self):
        user_label = ttk.Label(self.users_tab, text="User Index:")
        user_label.pack(pady=10)
        user_listbox = tk.Listbox(self.users_tab)
        user_listbox.pack(expand=True, fill="both")
        # Dummy data for demonstration
        users = ["User1", "User2", "User3"]
        for user in users:
            user_listbox.insert(tk.END, user)
    
    def setup_groups_tab(self):
        group_label = ttk.Label(self.groups_tab, text="Group Index:")
        group_label.pack(pady=10)
        group_listbox = tk.Listbox(self.groups_tab)
        group_listbox.pack(expand=True, fill="both")
        # Dummy data for demonstration
        groups = ["Group1", "Group2", "Group3"]
        for group in groups:
            group_listbox.insert(tk.END, group)
    
    def setup_features_tab(self):
        feature_label = ttk.Label(self.features_tab, text="Server Features:")
        feature_label.pack(pady=10)
        feature_listbox = tk.Listbox(self.features_tab)
        feature_listbox.pack(expand=True, fill="both")
        # Dummy data for demonstration
        features = ["Feature1", "Feature2", "Feature3"]
        for feature in features:
            feature_listbox.insert(tk.END, feature)

if __name__ == "__main__":
    app = ServerInterface()
    app.mainloop()



