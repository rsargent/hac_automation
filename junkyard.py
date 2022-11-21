session_file = "secrets/session.pickle"

def load_session():
    try:
        session = pickle.load(open(session_file, "rb"))
        print(f"Loaded session from {session_file}")
    except:
        session = requests.Session()
        print(f"Created new session")
    session.headers.update(
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
    return session

def save_session(session):
    tmp_file = f"{session_file}.{os.getpid()}.tmp"
    pickle.dump(session, open(tmp_file, "wb"))
    os.rename(tmp_file, session_file)
    print(f"Wrote session to {session_file}")

session = load_session()

def get_main_page():
    #login_url = "https://hac40.pps.k12.pa.us/HomeAccess4_1/Account/LogOn?ReturnUrl=%2fHomeAccess4_1%2fHome%2fWeekView"
    main_page_url = "https://hac40.pps.k12.pa.us/HomeAccess4_1/Home/WeekView"
    resp = session.get(main_page_url)
    bs = BeautifulSoup(resp.text, "html.parser")
    forms = bs.find_all("form")
    if len(forms) > 0:
        resp = log_in_and_get_page()

    return resp
