# 🌦️ Django Weather Forecast Web Application

A responsive weather forecasting web application built with Python and Django. It uses the Open-Meteo API to retrieve weather information based on the searched city.

## Features

- Search weather by city name
- Current weather information
- Temperature and feels-like temperature
- Humidity and wind speed
- Precipitation information
- Weather condition icons
- Dynamic day and night themes
- Daily weather forecast
- Responsive user interface

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- Open-Meteo API

## Project Structure

```text
django_weather_project/
│
├── weather/
│   ├── migrations/
│   ├── templates/
│   │   └── weather/
│   │       └── home.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd django_weather_project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and configure:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

### 6. Run database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

## API

Weather data is provided by [Open-Meteo](https://open-meteo.com/).

## Author

**Indranil Mandal**

- GitHub: [Your GitHub Profile](https://github.com/)

## License

This project is available under the MIT License.
