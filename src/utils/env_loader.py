from dotenv import load_dotenv
import os


# 封裝.env的資料，使用此方法即可取得.env檔案內的資料
def load_env() -> dict:
    """
    Return the env data
    Returns:
        _type_: dict{str, str}
    """
    load_dotenv()
    return {
        "CPBL_RECORDS_HITTER": os.getenv("CPBL_RECORDS_HITTER"),
        "CPBL_RECORDS_PITCHER": os.getenv("CPBL_RECORDS_PITCHER"),
        "CPBL_RECORDS_POST": os.getenv("CPBL_RECORDS_POST"),
        "USER_AGENT": os.getenv("USER_AGENT"),
    }
