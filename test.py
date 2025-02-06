import os
import sys
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import sqlite3

class BudgetManager:
    def __init__(self, master):
        self.master = master
        self.master.title("家庭收支管理")
        self.center_window()
        self.create_widgets()
        self.create_database()
        self.update_financial_summary()
        self.update_transaction_list()

    def center_window(self):
        width = 400
        height = 400  # Adjusted height to accommodate the listbox
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.master.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        self.label = tk.Label(self.master, text="欢迎使用家庭收支管理系统")
        self.label.pack(pady=20)

        self.income_button = tk.Button(self.master, text="记录收入", command=self.record_income)
        self.income_button.pack(pady=10)

        self.expense_button = tk.Button(self.master, text="记录支出", command=self.record_expense)
        self.expense_button.pack(pady=10)

        self.summary_button = tk.Button(self.master, text="查看财务情况", command=self.update_financial_summary)
        self.summary_button.pack(pady=10)

        self.transaction_list = ttk.Treeview(self.master, columns=('type', 'amount'), show='headings')
        self.transaction_list.column('type', anchor=tk.W, width=100)
        self.transaction_list.column('amount', anchor=tk.W, width=100)
        self.transaction_list.heading('type', text='类型', anchor=tk.W)
        self.transaction_list.heading('amount', text='金额', anchor=tk.W)
        self.transaction_list.pack(pady=10)

    def create_database(self):
        self.conn = sqlite3.connect('budget_manager.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                amount REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def record_income(self):
        income = simpledialog.askfloat("记录收入", "请输入收入金额:")
        if income is not None:
            self.cursor.execute("INSERT INTO transactions (type, amount) VALUES (?, ?)", ('income', income))
            self.conn.commit()
            print(f"记录收入: {income}元")
            self.update_financial_summary()
            self.update_transaction_list()

    def record_expense(self):
        expense = simpledialog.askfloat("记录支出", "请输入支出金额:")
        if expense is not None:
            self.cursor.execute("INSERT INTO transactions (type, amount) VALUES (?, ?)", ('expense', expense))
            self.conn.commit()
            print(f"记录支出: {expense}元")
            self.update_financial_summary()
            self.update_transaction_list()

    def update_financial_summary(self):
        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
        total_income = self.cursor.fetchone()[0] or 0

        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
        total_expense = self.cursor.fetchone()[0] or 0

        current_assets = total_income - total_expense

        summary_message = f"总收入: {total_income}元\n总支出: {total_expense}元\n当前资产: {current_assets}元"
        messagebox.showinfo("家庭财务情况", summary_message)

    def update_transaction_list(self):
        self.transaction_list.delete(*self.transaction_list.get_children())
        self.cursor.execute("SELECT type, amount FROM transactions")
        for row in self.cursor.fetchall():
            self.transaction_list.insert('', 'end', values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetManager(root)
    root.mainloop()
