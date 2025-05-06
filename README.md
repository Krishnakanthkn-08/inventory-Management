# 🏪 Inventory Management Web Application

This is a Flask-based web application for managing inventory across multiple warehouses or locations. It allows users to manage products, locations, and record product movements between locations. The system provides a report to show the current quantity of each product in each location.

## 📦 Features

- Add, edit, and view products
- Add, edit, and view locations
- Record and track product movements between locations
- Generate a report showing current product balances in each warehouse

## 🗃️ Database Schema

- **Product**
  - `product_id` (Primary Key)
  - `name` (String)
  - `description` (Optional)

- **Location**
  - `location_id` (Primary Key)
  - `name` (String)
  - `address` (Optional)

- **ProductMovement**
  - `movement_id` (Primary Key)
  - `timestamp` (Datetime)
  - `from_location` (Nullable, Foreign Key to Location)
  - `to_location` (Nullable, Foreign Key to Location)
  - `product_id` (Foreign Key to Product)
  - `qty` (Integer)

**Note**: If `from_location` is NULL, it indicates items are being added to inventory. If `to_location` is NULL, it indicates items are being removed from inventory.

## 📋 Use Cases

- Create 3–4 Products (e.g., Product A, B, C)
- Create 3–4 Locations (e.g., Location X, Y, Z)
- Record movements like:
  - Move Product A to Location X
  - Move Product B to Location X
  - Move Product A from Location X to Location Y
  - Record at least 20 such movements
- Generate a report: grid with 3 columns — `Product`, `Warehouse`, `Qty`

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- SQLite (default for development)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/inventory-management-flask.git
   cd inventory-management-flask
 2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
  ```bash
 pip install -r requirements.txt
