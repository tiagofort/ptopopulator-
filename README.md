# 🗓️ PTO Populator

**PTO Populator** was built to automate a tedious and error-prone task in our company's workflow. Whenever employees request vacation days, **Team Leaders** need a clear and accessible overview of everyone's scheduled time off.

Unfortunately, the internal PTO management system does **not** provide a friendly or readable calendar view. As a workaround, each Team Leader maintains their own tracker spreadsheet to visualize absences more clearly.

## 📁 Project Structure
```
.
├── app.py
├── .gitignore
├── Procfile
├── README.md
├── requirements.txt
├── config
│   └── constants.py
├── utils
│   ├── auth.py
│   ├── parser.py
│   └── sheets.py
```


## 📱 Fully Responsive Design

The UI adapts beautifully across all screen sizes — from mobile to tablet and desktop — ensuring a seamless shopping experience for users on any device.

![Responsive Test](https://imagens-tiago.s3.eu-north-1.amazonaws.com/resposive-pto.png)

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

## 🧪 How to Use PTO Populator (Step-by-Step)

### 1. Copy the data from the internal system

The raw PTO data should look like this:

```
H~Holiday_4008478 01/01/2025 2:00 AM 01/05/2025 2:00 AM 1 day(s) 7.50
B~Bank Holiday_4008478 	01/10/2025 2:00 AM 	01/11/2025 2:00 AM 1 day(s) 7.50
```

---

### 2. Make sure the dates are in `dd/mm/yyyy` format

If the copied data is in `mm/dd/yyyy` format, use the **bottom text field in the app** to convert it.  
After conversion, paste the updated data into the **top text field**.

---

### 3. Add the employee's name at the top

The employee's name must appear as the **first line** of the data, like this:

```
Batman
H~Holiday_4008478  01/01/2025 2:00 AM  05/01/2025 2:00 AM 1 day(s) 7.50
B~Bank Holiday_4008478 	10/01/2025 2:00 AM 	11/01/2025 2:00 AM 1 day(s) 7.50
```

---

### 4. Click "Submit" and verify the result

After submitting, a message will confirm how many cells were added to the tracker.  
You can verify the updated entries directly using the link provided in the [Live App](#-live-app) section.

---


## 🌐 Live App

👉 **Try it here:** [https://ptopopulator.onrender.com/](https://ptopopulator.onrender.com/)

📄 **View the tracker sheet:** [Google Sheets PTO Tracker](https://docs.google.com/spreadsheets/d/1-UzTANaw0_997fuIi2BBjw7vS5vMCJ17iSB1fZJXaFs/edit?gid=0#gid=0)

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
git clone https://github.com/your-username/ptopopulator.git
cd ptopopulator
