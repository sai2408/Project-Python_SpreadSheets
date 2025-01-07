# Google Sheets Authentication Project

## 📝 Project Overview
This project is a web application built using **Flask** that includes user **Login** and **Register** functionalities. Unlike traditional projects that store user data in databases like MySQL or PostgreSQL, this project stores the data in **Google Sheets**, leveraging the **gspread** module in Python to interact with the Google Sheets API.

## 🚀 Key Features
- **User Registration**: Allows users to register by entering their details, which are securely stored in a Google Sheet.
- **User Login**: Users can log in using their credentials, and the app verifies the login information from Google Sheets.
- **Google Sheets Integration**: The project uses the **gspread** module to connect to Google Sheets, enabling real-time data storage and retrieval.
- **Secure Authentication**: Data is handled securely, ensuring that user credentials are protected.

## 📚 Tech Stack
- **Python** (with Flask framework)
- **HTML/CSS/Bootstrap** (for frontend)
- **gspread** (Python module for Google Sheets integration)
- **Google Sheets API**
- **GitHub** (for version control)

## ⚙️ Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url
   ```
2. Navigate to the project directory:
   ```bash
   cd your-project-directory
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your **Google Sheets API** credentials and share the Google Sheet with the service account email.
5. Run the Flask app:
   ```bash
   python app.py
   ```
6. Open the application in your browser at `http://localhost:5000`.

## 🛠️ How It Works
1. **User Registration**:
   - The user fills out a registration form with their details.
   - The data is sent to the server and stored in a designated Google Sheet.
2. **User Login**:
   - The user provides their login credentials.
   - The application checks the provided credentials against the data in the Google Sheet.

## 🌐 Google Sheets Integration
To connect to Google Sheets:
- Use the **gspread** module to authenticate and access the sheets.
- Ensure your **service account key file** is correctly set up.
- Share your Google Sheet with the service account email address.

## 📄 Code Snippets
**Connecting to Google Sheets:**
```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Authenticate
credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('Your Google Sheet Name').sheet1
```

## 📈 Advantages of Using Google Sheets
- **Real-Time Data Access**: Updates to Google Sheets are instantly reflected in the application.
- **Easy Data Management**: Google Sheets provides a user-friendly interface to view and manage data.
- **Cloud-Based Storage**: No need to maintain a separate database server.

## 🖼️ Project Screenshots
| Page           | Description                |
|----------------|----------------------------|
| **Login Page** | User can log in using their credentials. |
| **Register Page** | User can register and have their data stored in Google Sheets. |

## 🔐 Security Considerations
- Ensure that your **service account key file** is kept secure and not exposed in public repositories.
- Use **environment variables** to manage sensitive data such as API credentials.

## 💻 Future Enhancements
- Implement **password hashing** for more secure authentication.
- Add **email verification** during registration.
- Create a **dashboard** to view and manage user data from the web application.

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

## 🤝 Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request with your changes.

## 📧 Contact
For any queries or suggestions, please reach out to [saivardhan.thimmisetty@gmail.com].

