from src.utils.env_loader import load_env

env = load_env()

HEADERS = {
    "User-Agent": env["USER_AGENT"],
    "Content-Type": "application/x-www-form-urlencoded",
}

URL_HITTER = env["CPBL_RECORDS_HITTER"]
URL_PITCHER = env["CPBL_RECORDS_PITCHER"]
URL_POST = env["CPBL_RECORDS_POST"]
