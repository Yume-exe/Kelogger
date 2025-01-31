import psutil
import os
import time

def detect_and_kill_keylogger():
    keywords = ["pynput", "cryptography", "keylogs"]

    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if process.info['cmdline'] and any(keyword in ' '.join(process.info['cmdline']).lower() for keyword in keywords):
                print(f"[!] Keylogger detected! Shutting it down {process.info['pid']} ({process.info['name']})")
                os.kill(process.info['pid'], 9)
                time.sleep(1)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

detect_and_kill_keylogger()
