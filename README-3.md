# Toxicology On-Call Scheduler (Fully Flexible Inputs)

This Streamlit application generates a monthly on-call schedule for toxicology fellows, with fully flexible in-app entry for EM shifts and off-day requests.

## ✅ Features

- Input first-year and second-year fellow names
- Choose month and year for scheduling
- Assigns one fellow per day
- First-year fellows receive 1 more weekday call shift than second-years
- Weekend shifts distributed evenly
- 📅 **Emergency Medicine shift conflicts**:
  - Enter individual EM shift dates OR ranges
  - Any shift starting before 11PM blocks that fellow from tox call that day
- ❌ **Off-day requests**:
  - Enter individual off-days OR date ranges
- 📆 Automatically assigns days of the week to each date
- 🧑‍⚕️ Displays who is on call for a user-selected clinic day
- 📊 Summary table: total shifts and weekend shifts per fellow
- 📥 Download the final schedule as a CSV

## 🚀 How to Deploy

1. Push the files to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Select your repository and point to:
   ```
   toxicology_scheduler_flexible_all_inputs.py
   ```
4. Click **Deploy**.

## Files

- `toxicology_scheduler_flexible_all_inputs.py`: Main Streamlit application
- `requirements.txt`: Dependencies for Streamlit deployment

---

Built for scheduling toxicology fellows efficiently, with real-world flexibility.
