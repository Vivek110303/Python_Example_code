
***

# 📂 Project Structure 

Here’s the **recommended folder structure** with explanations:  

```
FullStack_Projects/
│
├── Django_UserAuth/                     # Integrated User Registration + Login Project
│   ├── manage.py
│   ├── db.sqlite3
│   ├── requirements.txt
│   ├── project_root/                             # Django core project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── users/                                    # Custom app for auth
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py                              # Custom RegistrationForm
│   │   ├── models.py                             # Django default User (extended with forms.py)
│   │   ├── tests.py
│   │   ├── urls.py                               # App-level routing (register, login, logout, dashboard)
│   │   ├── views.py                              # Auth and registration logic
│   │   └── templates/users/
│   │       ├── register.html
│   │       ├── login.html
│   │       ├── logout.html
│   │       └── dashboard.html
│   ├── templates/                                # Global templates
│   │   ├── base.html
│   │   └── home.html
│   └── static/                                   # Static assets
│       ├── css/style.css
│       └── js/script.js
│
├── Django_FormProject/                  # Standalone Form Handling Project
│   ├── manage.py
│   ├── form_project/                              # Django main app
│   ├── formsapp/                                 # Custom form handling app
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/formsapp/
│   │       ├── form.html                         # Form rendering & validation
│   │       └── result.html                       # Display submitted data
│   └── static/
│
├── Flask_Registration/                  # Flask Registration Form Project
│   ├── app.py                                    # Main Flask app
│   ├── templates/
│   │   ├── base.html
│   │   └── register.html
│   ├── static/css/style.css
│   ├── forms.py                                  # (if using Flask-WTF)
│   └── requirements.txt
│
├── Module18_OpenCV/                              # OpenCV Practical Implementations
│   ├── image_read_display.py                     # Loading & displaying
│   ├── image_resize_crop.py
│   ├── image_color_spaces.py
│   ├── drawing_shapes_text.py
│   ├── image_blur_edge.py
│   ├── video_capture.py                          # Webcam processing
│   └── screenshots/                              # Required for submission
│       ├── image_output_1.png
│       ├── image_output_2.png
│       └── ...
│
├── Selenium_GetData/                    # Selenium Web Scraping Project
│   ├── scrape_data.py                            # Script for automation
│   ├── requirements.txt
│   ├── outputs/
│   │   ├── scraped_data.json
│   │   └── scraped_data.csv
│   └── logs/
│       └── execution_log.txt
│
├── Selenium_FBPoster/                   # Selenium Auto Blog Poster
│   ├── fb_autopost.py                            # Automation script
│   ├── credentials.json                          # (Optional: for storing test credentials securely)
│   ├── screen_recording.mp4                      # Required submission file
│   ├── logs/
│   │   └── fb_post_log.txt
│   └── requirements.txt
│
├── requirements.txt                              # Master requirements for all projects
└── README.md                                     # Detailed documentation (portfolio showcase)
```

***

# 📖 Detailed Description of Each Module  

***

## Django – User Registration & Login (28 Files)**  
- Main integrated project combining **Registration + Login/Logout**.  
- Used Django’s `UserCreationForm` and `AuthenticationForm`.  
- **Key files modified:**  
  - `settings.py` → added `users` app, templates/static dirs  
  - `urls.py` → added routes for register/login/logout/dashboard  
  - `forms.py` → custom `RegistrationForm`  
  - `views.py` → functions for auth system  
  - Templates (`register.html`, `login.html`, `logout.html`, `dashboard.html`)  

 **Flow:**  
```
Register Form → Save to DB → Login → Redirect to Dashboard → Logout
```

***

## Django – Form Project**  
- Standalone **custom form handling project**.  
- Shows how to **create forms independently**, validate input, and render processed output.  
- Templates (`form.html`, `result.html`) demonstrate form input & processed output.  

***

## **Module 15: Flask – Registration Form Project**  
- Lightweight project using **Flask + Jinja2 templates**.  
- Registration form built with optional **Flask-WTF/WTForms**.  
- Showcases understanding of simpler framework vs Django.  

 **Flow:**  
```
User fills form → Validation (Flask backend) → Data rendered/printed on result page
```

***

## OpenCV Implementations**  
- All tasks from the module implemented with **proper screenshots**.  
- Code scripts correspond to lectures:  
  - Image load, save, display  
  - Resize, crop, rotate  
  - Convert to gray/HSV  
  - Drawing (shapes, text)  
  - Blur, threshold, edge detection  
  - Real-time webcam capture  

 **Flow:**  
```
Code → Executes in Python terminal → Generates Image/Video Output → Screenshot Taken w/ Timestamp
```

***

## Selenium – Automation (Get Data)**  
- Built a **web scraping automation** script.  
- Extracts **dynamic website content** with Selenium.  
- Outputs saved in JSON/CSV format.  

 **Flow:**  
```
Open Website → Extract Data → Save Structured Data (CSV/JSON)
```

***

## Selenium – Facebook Auto Blog Poster**  
- Fully functional Selenium script that:  
  - Logs into Facebook  
  - Automates writing a post/blog  
  - Publishes it  
- Submitted along with **screen recording** for proof of execution.  

 **Flow:**  
```
Credentials → Selenium WebDriver → Facebook Login → Post Content Submitted
```

***

# Technologies Used  
- **Backend:** Python, Django, Flask  
- **Frontend:** HTML, CSS, Bootstrap, Jinja2  
- **Database:** SQLite  
- **Automation:** Selenium, WebDriver (ChromeDriver/GeckoDriver)  
- **Computer Vision:** OpenCV  

***

#  How to Run Projects  

- See **individual module folders** for more details.  
- Install dependencies using:  
```bash
pip install -r requirements.txt
```
- Django → `python manage.py runserver`  
- Flask → `python app.py`  
- OpenCV → `python script_name.py`  
- Selenium → `python automation_script.py`  

***
