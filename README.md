# Smart Library System

A modern, extensible library management system built with Python, demonstrating advanced Object-Oriented Programming (OOP) concepts, decorators, and access control mechanisms.

## 🚀 Features

- **Advanced OOP**: Implemented `Book` and `Library` classes with a focus on Pythonic patterns.
- **Dunder Methods**: Utilized special methods like `__str__`, `__repr__`, `__len__`, `__eq__`, and `__getitem__` for intuitive object behavior.
- **Logging Infrastructure**: Custom `@track_access` decorator to automatically log system activities with timestamps.
- **Access Control**: Secure `permission_check` closure/decorator to enforce role-based access (e.g., Admin vs. Guest).
- **Duck Typing**: Demonstrates Python's dynamic nature by supporting different object types seamlessly in core logic.
- **Search System**: Powerful search functionality across titles and authors.

## 📁 Project Structure

```text
.
├── core.py           # Core Book and Library logic
├── utils.py          # Decorators and utility functions
├── __init__.py       # Package initialization
├── __main__.py       # Demo and package entry point
├── run.py            # Main execution script
├── .env              # Environment configuration
└── requirements.txt  # Project dependencies
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/smart-library.git
   cd smart-library
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

To run the interactive demo and see the system in action:

```bash
python run.py
```

This will initialize the "Newbies Public Library", demonstrate book additions, permission checks, borrowing/returning books, and the internal search engine.

## 🧪 Concepts Demonstrated

### Decorators & Closures
- `track_access`: Logs every call to a method, including the arguments and a precise timestamp.
- `permission_check`: A higher-order function returned as a decorator to validate user roles before executing sensitive actions.

### Pythonic Design (Dunder Methods)
- `Library` objects are iterable and indexable thanks to `__getitem__`.
- `len(Library)` returns the current book count.
- `Book` equality (`==`) is based on content rather than memory address.

### Search & Filtering
The system uses list comprehensions and case-insensitive matching to provide a smooth search experience.

---
Built with ❤️ by [Your Name/Username]
