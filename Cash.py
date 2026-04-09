import tkinter as tk
from tkinter import ttk, messagebox

products = [
    {"name": "Burger", "price": 50},
    {"name": "Pizza", "price": 120},
    {"name": "Coke", "price": 30},
    {"name": "Fries", "price": 40},
    {"name": "Sandwich", "price": 60},
    {"name": "Pasta", "price": 100},
]

class CashCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cash Counter System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#1e1e2f")
        self.cart = {}

        self.left_frame = tk.Frame(root, bg="#2e2e42", padx=10, pady=10)
        self.left_frame.pack(side="left", fill="both", expand=True)

        tk.Label(self.left_frame, text="MENU", font=("Helvetica", 20, "bold"),
                 bg="#2e2e42", fg="#f1c40f").pack(pady=15)

        for product in products:
            btn = tk.Button(
                self.left_frame,
                text=f"{product['name']} - ₹{product['price']}",
                font=("Helvetica", 14, "bold"),
                bg="#3498db", fg="white",
                activebackground="#2980b9",
                relief="ridge",
                bd=3,
                command=lambda p=product: self.add_to_cart(p)
            )
            btn.pack(pady=8, fill="x", ipady=8)

        self.right_frame = tk.Frame(root, bg="#ecf0f1", padx=10, pady=10)
        self.right_frame.pack(side="right", fill="both", expand=True)

        tk.Label(self.right_frame, text="Cart", font=("Helvetica", 20, "bold"),
                 bg="#ecf0f1").pack(pady=15)

        self.tree = ttk.Treeview(self.right_frame, columns=("Name", "Price", "Qty", "Total"), show="headings")
        for col in ("Name", "Price", "Qty", "Total"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)
        self.tree.pack(fill="both", expand=True, pady=10)

        self.total_label = tk.Label(self.right_frame, text="Total: ₹0",
                                    font=("Helvetica", 16, "bold"), bg="#ecf0f1")
        self.total_label.pack(pady=10)

        btn_frame = tk.Frame(self.right_frame, bg="#ecf0f1")
        btn_frame.pack(pady=10)

        self.generate_btn = tk.Button(btn_frame, text="Generate Bill", font=("Helvetica", 12, "bold"),
                                      bg="#27ae60", fg="white", activebackground="#1e8449",
                                      padx=20, pady=10, command=self.generate_bill)
        self.generate_btn.grid(row=0, column=0, padx=10)

        self.clear_btn = tk.Button(btn_frame, text="Clear Cart", font=("Helvetica", 12, "bold"),
                                   bg="#e74c3c", fg="white", activebackground="#c0392b",
                                   padx=20, pady=10, command=self.clear_cart)
        self.clear_btn.grid(row=0, column=1, padx=10)


    def add_to_cart(self, product):
        name = product["name"]
        price = product["price"]
        if name in self.cart:
            self.cart[name]["qty"] += 1
        else:
            self.cart[name] = {"price": price, "qty": 1}
        self.update_cart()

    def update_cart(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        total = 0
        for name, item in self.cart.items():
            line_total = item["price"] * item["qty"]
            total += line_total
            self.tree.insert("", "end", values=(name, item["price"], item["qty"], line_total))

        self.total_label.config(text=f"Total: ₹{total}")

    def generate_bill_text(self):
        bill = "------ Invoice ------\n\n"
        total = 0
        for name, item in self.cart.items():
            line_total = item["price"] * item["qty"]
            bill += f"{name} x {item['qty']} = ₹{line_total}\n"
            total += line_total
        bill += f"\nTotal: ₹{total}"
        return bill

    def generate_bill(self):
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Cart is empty!")
            return
        bill = self.generate_bill_text()
        messagebox.showinfo("Bill", bill)


    def clear_cart(self):
        self.cart.clear()
        self.update_cart()

if __name__ == "__main__":
    root = tk.Tk()
    app = CashCounterApp(root)
    root.mainloop()
