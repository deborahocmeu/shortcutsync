import os
import shutil
import socket
import json
from pathlib import Path
from typing import List

class ShortcutSync:
    def __init__(self, sync_folder: str, devices: List[str]):
        self.sync_folder = Path(sync_folder)
        self.devices = devices
        self.local_ip = socket.gethostbyname(socket.gethostname())

    def get_shortcuts(self) -> List[Path]:
        desktop_path = Path(os.path.join(os.environ['USERPROFILE'], 'Desktop'))
        return list(desktop_path.glob('*.lnk'))

    def sync_shortcuts(self):
        shortcuts = self.get_shortcuts()
        print(f"Found {len(shortcuts)} shortcuts to sync.")
        
        if not self.sync_folder.exists():
            self.sync_folder.mkdir(parents=True, exist_ok=True)

        for shortcut in shortcuts:
            dest = self.sync_folder / shortcut.name
            shutil.copy2(shortcut, dest)
            print(f"Copied {shortcut} to {dest}")

        self.notify_devices()

    def notify_devices(self):
        for device in self.devices:
            if device != self.local_ip:
                self.send_sync_notification(device)

    def send_sync_notification(self, device_ip: str):
        notification = {
            "message": "sync",
            "ip": self.local_ip
        }
        try:
            # Dummy implementation of sending notification
            print(f"Sending sync notification to {device_ip}: {json.dumps(notification)}")
            # Actual implementation would involve network communication
        except Exception as e:
            print(f"Failed to send notification to {device_ip}: {e}")


if __name__ == "__main__":
    devices_list = ["192.168.1.2", "192.168.1.3"]  # Example IPs of devices in the network
    sync_directory = "C:/ShortcutSync"
    
    shortcut_sync = ShortcutSync(sync_folder=sync_directory, devices=devices_list)
    shortcut_sync.sync_shortcuts()