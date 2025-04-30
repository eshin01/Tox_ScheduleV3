
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import calendar
import random
from collections import defaultdict

st.set_page_config(page_title="Toxicology On-Call Scheduler", layout="centered")
st.title("📅 Toxicology On-Call Scheduler")

first_year_fellows = st.text_input("Enter First-Year Fellows (comma-separated)", "Shin, Mahony")
second_year_fellows = st.text_input("Enter Second-Year Fellows (comma-separated)", "Burke, Johnson")
first_year_fellows = [f.strip() for f in first_year_fellows.split(",") if f.strip()]
second_year_fellows = [f.strip() for f in second_year_fellows.split(",") if f.strip()]
all_fellows = first_year_fellows + second_year_fellows

col1, col2 = st.columns(2)
with col1:
    selected_month = st.selectbox("Select Month", list(calendar.month_name)[1:], index=datetime.today().month - 1)
with col2:
    selected_year = st.number_input("Select Year", min_value=2000, max_value=2100, value=datetime.today().year)

month_number = list(calendar.month_name).index(selected_month)
start_date = datetime(selected_year, month_number, 1).date()
_, last_day = calendar.monthrange(selected_year, month_number)
end_date = datetime(selected_year, month_number, last_day).date()

clinic_date = st.date_input("Toxicology Clinic Date (usually Thursday)")

# === EM SHIFT INPUT SECTION ===
st.markdown("### 🚑 Emergency Medicine Shift Conflicts")
em_blocked_dict = defaultdict(set)

for fellow in all_fellows:
    with st.expander(f"Enter EM Shifts for {fellow}"):
        num_em_ranges = st.number_input(f"How many EM shifts or date ranges for {fellow}?", min_value=0, max_value=30, value=0, key=f"{fellow}_em_range")
        for i in range(num_em_ranges):
            em_entry = st.date_input(f"EM Shift #{i+1} Date or Range", key=f"{fellow}_em_entry_{i}")
            shift_start = st.time_input(f"Start time (24h)", value=datetime.strptime("07:00", "%H:%M").time(), key=f"{fellow}_em_time_{i}")
            if isinstance(em_entry, tuple):
                shift_start_date = em_entry[0]
                shift_end_date = em_entry[1] if len(em_entry) > 1 else em_entry[0]
            else:
                shift_start_date = shift_end_date = em_entry
            if shift_start < datetime.strptime("23:00", "%H:%M").time():
                for day in pd.date_range(start=shift_start_date, end=shift_end_date).date:
                    em_blocked_dict[fellow].add(day)

# === OFF-DAY INPUT SECTION ===
st.markdown("### ❌ Off-Day Requests")
off_day_dict = defaultdict(set)

for fellow in all_fellows:
    with st.expander(f"Enter Off-Days for {fellow}"):
        num_off = st.number_input(f"How many off-day entries for {fellow}?", min_value=0, max_value=30, value=0, key=f"{fellow}_offentry")
        for i in range(num_off):
            off_entry = st.date_input(f"Off-Day #{i+1} (date or range)", key=f"{fellow}_off_{i}")
            if isinstance(off_entry, tuple):
                off_start = off_entry[0]
                off_end = off_entry[1] if len(off_entry) > 1 else off_entry[0]
            else:
                off_start = off_end = off_entry
            for day in pd.date_range(start=off_start, end=off_end).date:
                off_day_dict[fellow].add(day)
