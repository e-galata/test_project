# Test Project

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing%20Framework-orange)
![POM](https://img.shields.io/badge/Pattern-Page%20Object%20Model-yellow)

This is the final course project updated in **2025** to work with **Python 3.13**. The project includes updates to requirements, fixes for various errors, and improvements to ensure compatibility with modern tools and libraries. It uses **pytest** for testing, **Selenium** for front-end automation, and follows the **Page Object Model (POM)** design pattern.

---

## 🚀 Features

- **Front-end Testing**: Automated browser testing using Selenium and WebDriver.
- **Backend API Testing**: Comprehensive API testing using pytest.
- **Page Object Model (POM)**: Clean and maintainable code structure for UI tests.
- **Python 3.13 Support**: Fully compatible with the latest Python version.
- **Error Fixes**: Resolved known issues and improved stability.

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/test_project.git
   cd test_project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
     On Windows:
     ```bash
     venv\Scripts\activate
     ```
     On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install the requirements**:
   ```bash
   pip install -r requirements.txt
   ```

🚀 **How to run tests**  

Front-end Tests (Selenium)  
`You need installed chrome browser, webdriver will be installed automatically`  
To run the Selenium front-end tests, execute the following command from the home directory of the project:
```bash
pytest -v --tb=line --language=en
```
  * `-v`: verbose output.
  * `--tb=line`: short traceback format.
  * `--language=en`: set the browser language to English.

Backend API Tests  
To run the API tests, execute the following command from the home directory of the project:
```bash
pytest -v api
```

🛠️ Tools and Technologies  
* Python3.13: The tested version of Python with project.  
* Selenium: For browser automation.  
* Pytest: A powerful testing framework.  
* WebDriver: To interact with web browsers.  
* Page Object Model (POM): A design pattern for better test maintenance.  

📂 Project Structure
```
test_project/
├── api/                  # Backend API tests
├── frontend/             # Front-end tests using Selenium
├── pages/                # Page Object Model (POM) classes
├── requirements.txt      # Project dependencies
├── conftest.py           # Pytest configuration and fixtures
└── README.md             # Project documentation
```

📧 Contact
For any questions or feedback, feel free to reach out: dushirak@gmail.com
