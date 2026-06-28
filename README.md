# 🛒 Best Buy Store Inventory System

A lightweight, command-line inventory and ordering system for a simple electronics store — built in pure Python.

## ✨ Features

- **Product Management** — create products with a name, price, and stock quantity
- **Store Operations** — add, remove, and list products
- **Order Processing** — place multi-item orders with automatic stock validation
- **Auto Stock Control** — products deactivate automatically when they sell out
- **Input Validation** — guards against bad names, prices, quantities, and over-ordering

## 📁 Project Structure

```
Best-Buy/
├── main.py       # CLI entry point
├── products.py   # Product class
├── store.py      # Store class
└── README.md     # This file
```

## 🚀 Getting Started

**Requirements:** Python 3.6+

Clone the repo: 

```bash
git clone https://github.com/ahmadalshouly/Best-Buy.git
```
Run the programm
```bash
python main.py
```

## 🖥️ Menu

```
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

## 📦 Example Session

```
Please choose a number: 1
1. MacBook Air M2, Price: 1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: 250, Quantity: 500
3. Google Pixel 7, Price: 500, Quantity: 250

Please choose a number: 3
When you want to finish order, enter empty text.
Which product # do you want? 1
What amount do you want? 2
Added to list!
Which product # do you want?

Order made! Total payment: $2900.0
```

## 🧩 Classes

### `Product`

| Method | Description |
|---|---|
| `__init__(name, price, quantity)` | Creates a new product |
| `get_quantity()` | Returns current stock |
| `set_quantity(quantity)` | Updates stock; deactivates automatically at 0 |
| `is_active()` | Checks if the product is available |
| `activate()` / `deactivate()` | Manually toggle availability |
| `show()` | Returns a display string for the product |
| `buy(quantity)` | Reduces stock and returns the total price |

### `Store`

| Method | Description |
|---|---|
| `__init__(products)` | Initializes the store with a list of products |
| `add_product(product)` | Adds a product to the store |
| `remove_product(product)` | Removes a product from the store |
| `get_total_quantity()` | Returns total items in stock |
| `get_all_products()` | Returns only active products |
| `order(shopping_list)` | Processes a list of `(product, quantity)` pairs and returns the total price |

## ✅ Validation Rules

- Product name must be a non-empty string
- Price must be a positive number
- Quantity must be a non-negative integer
- Orders cannot exceed available stock
- Inactive products cannot be ordered