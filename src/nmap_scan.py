import subprocess

def nmap_scan(target):
    try:
        result = subprocess.check_output(['nmap', '-sV', '-Pn', '-T4', target], stderr=subprocess.DEVNULL, text=True)
        return result
    except FileNotFoundError:
        return "[!] Nmap is not installed or not found in PATH."
    except Exception as e:
        return f"[!] Error: {e}"
