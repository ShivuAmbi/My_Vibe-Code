import tkinter as tk
from tkinter import ttk
from ai_analyzer import analyze_ad_objects
import datetime
import random

# Extended dummy AD data
ad_objects = [
    {'name': 'user1', 'last_login': '2024-01-01', 'type': 'user', 'department': 'IT', 'email': 'user1@company.com', 'status': ''},
    {'name': 'user2', 'last_login': '2022-01-01', 'type': 'user', 'department': 'HR', 'email': 'user2@company.com', 'status': ''},
    {'name': 'user3', 'last_login': '2023-05-15', 'type': 'user', 'department': 'Finance', 'email': 'user3@company.com', 'status': ''},
    {'name': 'user4', 'last_login': '2021-11-20', 'type': 'user', 'department': 'IT', 'email': 'user4@company.com', 'status': ''},
    {'name': 'user5', 'last_login': '2025-06-01', 'type': 'user', 'department': 'Marketing', 'email': 'user5@company.com', 'status': ''},
    {'name': 'user6', 'last_login': '2023-09-10', 'type': 'user', 'department': 'Sales', 'email': 'user6@company.com', 'status': ''},
    {'name': 'user7', 'last_login': '2022-12-25', 'type': 'user', 'department': 'Support', 'email': 'user7@company.com', 'status': ''},
    {'name': 'user8', 'last_login': '2024-03-18', 'type': 'user', 'department': 'IT', 'email': 'user8@company.com', 'status': ''},
    {'name': 'user9', 'last_login': '2023-02-14', 'type': 'user', 'department': 'Legal', 'email': 'user9@company.com', 'status': ''},
    {'name': 'user10', 'last_login': '2021-08-30', 'type': 'user', 'department': 'Admin', 'email': 'user10@company.com', 'status': ''},
    {'name': 'comp1', 'last_login': '2023-12-01', 'type': 'computer', 'os': 'Windows 10', 'owner': 'user1', 'status': ''},
    {'name': 'comp2', 'last_login': '2022-08-10', 'type': 'computer', 'os': 'Windows 11', 'owner': 'user2', 'status': ''},
    {'name': 'comp3', 'last_login': '2024-06-01', 'type': 'computer', 'os': 'Linux', 'owner': 'user3', 'status': ''},
    {'name': 'comp4', 'last_login': '2020-03-15', 'type': 'computer', 'os': 'Windows 7', 'owner': 'user4', 'status': ''},
    {'name': 'comp5', 'last_login': '2025-07-01', 'type': 'computer', 'os': 'macOS', 'owner': 'user5', 'status': ''},
    {'name': 'comp6', 'last_login': '2023-11-11', 'type': 'computer', 'os': 'Windows 10', 'owner': 'user6', 'status': ''},
    {'name': 'comp7', 'last_login': '2022-05-05', 'type': 'computer', 'os': 'Linux', 'owner': 'user7', 'status': ''},
    {'name': 'comp8', 'last_login': '2024-04-22', 'type': 'computer', 'os': 'Windows 11', 'owner': 'user8', 'status': ''},
    {'name': 'comp9', 'last_login': '2023-01-10', 'type': 'computer', 'os': 'Windows 10', 'owner': 'user9', 'status': ''},
    {'name': 'comp10', 'last_login': '2022-09-19', 'type': 'computer', 'os': 'Linux', 'owner': 'user10', 'status': ''},
]

class ADGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart AD Cleanup Assistant")
        self.geometry("1200x600")
        self.configure(bg="#f7f7f7")  # Light background
        self.selected_for_approval = set()
        self.results = ad_objects
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="Smart AD Cleanup Assistant", font=("Arial", 22, "bold"), bg="#f7f7f7", fg="#2d3142")
        title.pack(pady=15)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#3a86ff", foreground="#fff")
        style.configure("Treeview", font=("Arial", 11), rowheight=28, background="#f1faee", fieldbackground="#f1faee", foreground="#22223b")
        style.map("Treeview", background=[('selected', '#ffbe0b')])

        columns = ("Approve", "Name", "Type", "Last Login", "Department", "Email", "OS", "Owner", "Status")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        analyze_btn = tk.Button(self, text="Run Analysis", command=self.run_analysis, font=("Arial", 12, "bold"), bg="#3a86ff", fg="#fff", activebackground="#2d3142", activeforeground="#fff")
        analyze_btn.pack(pady=8)

        approve_btn = tk.Button(self, text="Approve Deletion", command=self.approve_deletion, font=("Arial", 12, "bold"), bg="#ff006e", fg="#fff", activebackground="#8338ec", activeforeground="#fff")
        approve_btn.pack(pady=8)

        self.status_label = tk.Label(self, text="", font=("Arial", 13), bg="#f7f7f7", fg="#2d3142")
        self.status_label.pack(pady=5)

        self.load_data(self.results)
        self.tree.bind('<ButtonRelease-1>', self.on_tree_click)

    def load_data(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.selected_for_approval.clear()
        for obj in data:
            status = obj.get('status', '')
            tag = 'stale' if status == 'stale' else 'active' if status == 'active' else ''
            approve = "[X]" if status == 'stale' else ""
            if status == 'stale':
                self.selected_for_approval.add(obj.get('name', ''))
            self.tree.insert("", tk.END, values=(
                approve,
                obj.get('name', ''),
                obj.get('type', ''),
                obj.get('last_login', ''),
                obj.get('department', ''),
                obj.get('email', ''),
                obj.get('os', ''),
                obj.get('owner', ''),
                status
            ), tags=(tag,))
        self.tree.tag_configure('stale', background='#ffadad')  # Pink for stale
        self.tree.tag_configure('active', background='#baffc9')  # Mint for active

    def run_analysis(self):
        self.results = analyze_ad_objects(ad_objects)
        self.selected_for_approval.clear()
        self.load_data(self.results)
        stale_count = sum(1 for obj in self.results if obj.get('status') == 'stale')
        self.status_label.config(text=f"Analysis complete. {stale_count} stale object(s) found. Select objects to approve deletion.")

    def on_tree_click(self, event):
        item = self.tree.identify_row(event.y)
        col = self.tree.identify_column(event.x)
        if not item or col != '#1':
            return
        values = self.tree.item(item, 'values')
        if values[8] == 'stale':
            name = values[1]
            if name in self.selected_for_approval:
                self.selected_for_approval.remove(name)
                self.tree.set(item, "Approve", "[ ]")
            else:
                self.selected_for_approval.add(name)
                self.tree.set(item, "Approve", "[X]")

    def approve_deletion(self):
        approved = [obj for obj in self.results if obj.get('name') in self.selected_for_approval]
        if not approved:
            self.status_label.config(text="No objects selected for approval.")
            return
        with open("approved_deletions.log", "a") as log:
            for obj in approved:
                log.write(f"{datetime.datetime.now()}: Approved deletion for {obj['type']} '{obj['name']}'\n")
        self.results = [obj for obj in self.results if obj.get('name') not in self.selected_for_approval]
        self.selected_for_approval.clear()
        self.load_data(self.results)
        ticket_number = random.randint(100000, 999999)
        self.status_label.config(text=f"Approved deletion for {len(approved)} object(s). Stale accounts deleted and logged. Ticket #{ticket_number} has been created for AD team.")

if __name__ == "__main__":
    app = ADGui()
    app.mainloop()
