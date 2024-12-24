# Pytest UI Automation Demo - Sports Goods Website

This project is a simple demonstration of UI automation for a sports goods website using `pytest`. It contains tests for user login, account editing, and product search functionalities.

## Project Structure

```
.
├── pages/
│   ├── constants.py         # Contains test data. Gitignored for security purposes
│   ├── page_account.py      # AccountPage class, defines methods to interact with user account page
│   ├── page_login.py        # LoginPage class, defines methods to interact with login screen
│   └── page_search.py       # SearchPage class, defines methods to interact with search screen
│
├── tests/
│   ├── conftest.py          # Browser configuration for pytest
│   ├── test_account.py      # TestAccount class, contains test to edit account, inherits from TestLogin
│   ├── test_login.py        # TestLogin class, contains tests to validate valid/invalid login
│   └── test_search.py       # TestSearch class, contains tests to validate valid/invalid search
│
├── utils/
│   └── common_helpers.py    # Contains helper functions to interact with web elements
│   └── reader.py            # Contains helper to read/record data to .txt files
│
├── pytest.ini               # Pytest configuration file
├── requirements.txt         # Python dependencies for the project
└── README.md                # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.x
- `pip` (Python package installer)
- A web browser (e.g., Chrome or Firefox)
- WebDriver for the chosen browser (e.g., `chromedriver` for Chrome or `geckodriver` for Firefox)

### Installation

1. Clone the repository.

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Browser WebDriver Setup

The project uses WebDriverManager, which automatically handles downloading and setting up the WebDriver for your browser, so no manual installation of browser drivers is required.

WebDriverManager will automatically download the correct version of the WebDriver for the browser you are testing (e.g., Chrome or Firefox) and configure it during the test execution.

No additional steps are needed for WebDriver setup.

### Configuration. Gitignored

- **`constants.py`**:
  - **`constant_base_url`**: The base URL of the sports goods website.
  - **`constant_months`**: A list with months available on website.
  - **`constant_valid_user`**: A dictionary containing a valid username and password.
  - **`constant_invalid_user`**: A dictionary with invalid login details.
  - **`constant_valid_id`**: A product ID to search for in the website.
  - **`constant_invalid_id`**: An invalid product ID to search for in the website.

### Running Tests

1. To run all tests:

   ```bash
   pytest
   ```

2. To run specific tests (e.g., tests for the login page):

   ```bash
   pytest tests/test_login.py
   ```

3. To run tests with browser-specific configurations:

   Change current **params=["chrome"]** to **params=["firefox"]** in conftest.py.

4. To run tests by marks:

   ```bash
   pytest -s -m login   #'login' as example of registered mark.
   ```  

### Test Descriptions

- **`test_login.py`**:
  - Validates successful login with valid credentials.
  - Tests login failure with invalid credentials.

- **`test_account.py`**:
  - Inherits from `TestLogin`. Tests account editing functionality after login.

- **`test_search.py`**:
  - Tests searching for a valid product ID.
  - Tests searching for an invalid product ID.

### Utilities

- **`conftest.py`**: Contains browser setup and teardown configuration for running tests in different browsers.
- **`common_helpers.py`**: Provides common helper functions to interact with web elements like clicking buttons, entering text, etc.
- **`reader.py`**: The ReaderClass is a utility class designed to help with reading and recording data from/to a .txt file. This class can be especially useful when you need to manage key-value pairs or specific information in a text file where each line follows a recognizable pattern. **Not used in current project.**

### Pytest Configuration

- **`pytest.ini`**: Configures pytest options, including browser-specific settings, markers, and test directories.

### How to Add New Tests

1. Create a new test file in the `tests/` directory.
2. Use page object classes from the `pages/` directory to interact with web elements.
3. Add the necessary helper functions from `utils/common_helpers.py` as needed.

### Example Test

Here’s an example test for login functionality in `test_login.py`:

```python
class TestLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(valid_credentials['username'], valid_credentials['password'])
        assert login_page.is_logged_in()

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(invalid_credentials['username'], invalid_credentials['password'])
        assert login_page.is_login_failed()
```
