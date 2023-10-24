# Inventory Management System

![IMS Logo](https://example.com/ims-logo.png)

## Summary

The Inventory Management System is a FastAPI-based application designed to facilitate the management of products for an e-commerce platform. It provides a set of API endpoints to perform basic CRUD operations (Create, Read, Update, Delete) on products in the inventory. The system employs Prisma as a database ORM for seamless data manipulation. Key features include the ability to add new products, retrieve product information by ID, update existing products, and remove products from the inventory. The application is designed to handle high volumes of concurrent read and write operations, ensuring efficient management of product data.

## Features

- Add new products with details such as name, description, price, SKU, image URL, and quantity.
- Retrieve detailed information about a product by its unique ID.
- Modify existing products including name, description, price, SKU, image URL, and quantity.
- Remove products from the inventory.

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/inventory-management.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
uvicorn main:app --reload
```

## Usage

1. Access the API documentation by navigating to `http://localhost:8000/docs` in your web browser.

2. Use the provided API endpoints to interact with the Inventory Management System.

## Technologies Used

- FastAPI
- Prisma
- Python

## Contributing

Contributions are welcome! Please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
