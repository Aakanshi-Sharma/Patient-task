#  Patient Management Dashboard (EcoFinds Health)

A simple and intuitive web application built using **Flask** for managing patient data in clinics or hospitals. 
It provides login/signup functionality, a secure user dashboard, patient CRUD operations, and a responsive UI inspired by the EcoFinds theme.


##  Features

- 👤 User Authentication (Sign Up / Login / Logout)
- 📋 Patient Records Management (Add, Edit, Delete, View)
- 📂 Profile Page for Logged-in User
- 📅 Date handling for Admit and Discharge
- ✅ Responsive UI (Mobile & Desktop)
- 🔒 Session-based secure routes
- 📦 SQLite database



##  Tech Stack

| Tech          | Description                          |
|---------------|--------------------------------------|
| Python (3.x)  | Core backend language                |
| Flask         | Lightweight web framework            |
| SQLite        | Simple file-based database           |
| HTML5/CSS3    | Front-end structure and styling      |
| Tailwind-inspired styling | Custom CSS with modern UI components |
| Jinja2        | Templating engine for rendering HTML |
| Werkzeug      | Secure sessions and request handling |

---

## Functionality

### 1. 🔐 Authentication
- **Sign Up**: Register using email, username, and password.
- **Login**: Secure login using bcrypt password hashing.
- **Logout**: Session cleared on logout.

  <img width="954" alt="image" src="https://github.com/user-attachments/assets/1672cc63-4e09-4510-911d-604aa8b21c81" />
  <img width="959" alt="image" src="https://github.com/user-attachments/assets/d8c00678-5ea2-4e07-95a5-ccd649749aed" />


### 2. 🧾 Patient Dashboard
- View all patients in a table
- Each record includes:
  - Name, Age, Address, Phone, Email
  - Disease, Current Condition
  - Doctor Assigned, Admit Date, Discharge Date
- Buttons to **Edit** or **Delete** each entry
- Delete prompts a modal confirmation

  <img width="958" alt="image" src="https://github.com/user-attachments/assets/a29e225e-7709-459a-b4e1-acd76cde587b" />

### 3. ➕ Add / ✏️ Edit Patient
- Reuses the same form
- For edit: fields are pre-filled
- Uses HTML5 date inputs and validation

  <img width="944" alt="image" src="https://github.com/user-attachments/assets/945d3a9b-e566-4a73-a591-cc5da8b84154" />


### 4. 👤 Profile Page
- View logged-in user info (username + email)
- Back navigation to dashboard

  <img width="959" alt="image" src="https://github.com/user-attachments/assets/523bea2d-6076-4fcf-99de-ce0d56381d56" />


##  Future Enhancements
Search & filter patients

Profile editing and password update

Export patient reports

Role-based access (admin/doctor)

