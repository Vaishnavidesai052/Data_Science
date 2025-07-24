## 📌 Problem Statement
A college wants to **automate the process of filtering students based on their grades** and analyze performance metrics efficiently using Python.

---

## ✅ **Features**
✔ Filter students scoring above 60  
✔ Assign **Pass/Fail** status  
✔ Calculate **square of grades** for performance indexing  
✔ Identify **top performers** scoring above 85  
✔ List students who require **remedial classes** (score < 50)

---

## 💻 **Technologies Used**
- **Language:** Python 3
- **Concepts:** List Comprehensions, Conditional Expressions, Tuple Unpacking

---

## 📂 **Code**
```python
students = [("Aarav",82),("Bhavna",56),("Sita",91),("Raju",36),
            ("Harshita",48),("Aditi",63),("Tina",43)]

pass_mark = 40
remedial_threshold = 50
top_performance = 85

above_60 = [name for name, grade in students if grade > 60]
pass_fail_status = [(name, "Pass" if grade >= pass_mark else "Fail") for name, grade in students]
square_grades = [(name, grade**2) for name, grade in students]
top_performers = [name for name, grade in students if grade >= top_performance]
remedial_students = [name for name, grade in students if grade < remedial_threshold]