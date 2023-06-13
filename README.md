## zm_test
# RUN:
1. Clone repo: git clone https://github.com/yuwisasha/zm_test.git
2. Create virtual environment: python -m venv .venv
3. Activate venv: source .venv/bin/activate
4. Install requirements: pip install -r requirements.txt
5. Run: python main.py
# DESCRITION
This sript creating 15 profiles in sqlite db with fields **creation_time**, **cookie**, **lust_run_time** and **run_count**,
makes a 5 processes for profiles sessions(they are opening a news at google.com/news), if profile has a cookie, put them into session,
scrolls page and update cookie.
