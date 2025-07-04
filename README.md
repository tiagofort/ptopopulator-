# 🗓️ PTO Populator

**PTO Populator** was built to automate a tedious and error-prone task in our company's workflow. Whenever employees request vacation days, **Team Leaders** need a clear and accessible overview of everyone's scheduled time off.

Unfortunately, the internal PTO management system does **not** provide a friendly or readable calendar view. As a workaround, each Team Leader maintains their own tracker spreadsheet to visualize absences more clearly.

## 💡 The Problem

Transferring PTO data from the internal system to these trackers is:
- Manual
- Time-consuming
- Error-prone

Each day off must be manually marked with a type:
- `H` → Holiday  
- `BH` → Bank Holiday  
- `SL` → Sick Leave  

This repetitive copy-pasting process wastes time and increases the chance of mistakes.

---

## ✅ The Solution: PTO Populator

This app allows you to paste raw PTO data directly from the internal system into a Streamlit interface. It then:
1. Parses the employee name and dates.
2. Detects the correct type of leave.
3. Fills in the Google Sheets tracker automatically, cell by cell.

The result? A clear, friendly visual representation of who is off and when — all with **one click**.

---

## ⚙️ Technologies Used

### 🐍 Why Python?

Python was chosen for its:
- Simplicity and readability
- Rich ecosystem of libraries
- Fast prototyping capabilities
- Native compatibility with Streamlit and Google APIs

### 🔧 Libraries

| Library            | Purpose                                             |
|--------------------|-----------------------------------------------------|
| `streamlit`        | Web interface to paste and process PTO data         |
| `gspread`          | Integration with Google Sheets                      |
| `oauth2client`     | Service account authentication                      |
| `datetime`         | Date manipulation and range generation              |
| `re`               | Data cleaning with regular expressions              |

---

## 🛠️ How to Run Locally

1. Clone the repository:
```bash
git https://github.com/tiagofort/ptopopulator-.git
cd ptopopulator
