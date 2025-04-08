# 🚗 HexaRide - CarPool Web Application

**HexaRide** is a Django-based web application that facilitates seamless carpooling within a company or organization. Save fuel, reduce traffic, and build connections with your colleagues while commuting!

---

## 📌 Features

- 🧑‍💼 User Registration & Authentication
- 📧 Company email validation
- 🚘 Post a ride (driver)
- 🧍‍♀️ Request a ride (rider)
- 🔍 Search available rides
- ✅ Admin panel to manage users and commutes
- 🔒 Secure and minimal personal data usage (email only)

---

## 🚀 Getting Started


# 📦 Install Dependencies
python -m pip install -r requirements.txt

# ⚙️ Set Up the Database
python manage.py makemigrations ui
python manage.py migrate

# 👤 Create a Superuser (Optional)
python manage.py createsuperuser

# ▶️ Run the Development Server
python manage.py runserver

