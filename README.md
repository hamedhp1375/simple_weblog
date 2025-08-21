
# 📝 Django Blog

A simple blog built with **Django**.  
This project is designed for learning the basics of Django and provides basic blog functionalities.

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/USERNAME/myblog.git
cd myblog
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**
```bash
venv\Scripts\activate
```

- **Linux / Mac**
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

(If you don't have a `requirements.txt` file, create it with:)
```bash
pip freeze > requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Your blog will be available at:  
👉 http://127.0.0.1:8000

---

## ✨ Features
- 🖊️ Create, edit, and delete blog posts  
- 📋 Display a list of all posts  
- 📄 View post details  
- 🔑 Django admin panel to manage posts  

---

## 📸 Screenshots
(Add screenshots of your blog here)

---

## 📚 Technologies Used
- Python 3.x  
- Django 5.x (or the version you installed)  
- SQLite (default Django database)  

---

## 👨‍💻 Author
Project developed by **Hamed**
