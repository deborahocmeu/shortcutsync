# ShortcutSync

ShortcutSync is a Python-based utility designed to synchronize desktop shortcuts across multiple Windows devices. This tool ensures a consistent user interface by sharing shortcuts between devices on the same network.

## Features

- Automatically detects and synchronizes `.lnk` shortcut files from the user's desktop.
- Copies shortcuts to a centralized sync folder.
- Notifies other devices on the network to synchronize their shortcuts.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ShortcutSync.git
   ```
2. Navigate into the directory:
   ```bash
   cd ShortcutSync
   ```

## Usage

1. Modify the `devices_list` variable in `ShortcutSync.py` to include the IP addresses of the devices you want to sync with.
2. Specify a `sync_directory` where the shortcuts will be stored temporarily.
3. Run the program:
   ```bash
   python ShortcutSync.py
   ```

## Limitations

- This script assumes that all devices are on the same local network and can communicate with each other via IP addresses.
- The notification system for syncing is a placeholder and should be replaced with a real network communication implementation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.