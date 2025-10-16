# Amanuensis Setup Log

## Environment Details
- **OS**: ChromeOS Linux (Debian-based)
- **Python**: 3.11.2
- **Pip**: 23.0.1
- **Date Started**: October 16, 2025
- **Project Goal**: Transcription app with PyQt GUI, offline-first, lightweight

## Setup Steps

### 1. Checked Python Environment (2025-10-16)
- Command: `python3 --version``
  - Output: Python 3.11.2
- Command: `pip3 --version`
  - Output: pip 23.0.1 from /usr/lib/python3/dist-packages/pip (python 3.11)
- Command: `pip3 list`
  - Output: [gyp, Mako, Markdown, MarkupSafe, pip, pycairo, Pygments, PyGObject, PyYAML, setuptools, six, wheel]
- Command: `python3 -c "import tkinter; print('Tkinter imported successfully')"
  - Output: ModuleNotFoundError: no module named 'tkinter'

### 2. Install PyQt5 (2025-10-16)
- Command: `pip3 install PyQt5`
  - Output: Error (externally-managed-environment, PEP 668)
- Command: `sudo apt update`
  - Output: Package lists up-to-date
- Command: `sudo apt install python3-pyqt5`
  - Output: Installed python3-pyqt5 (5.15.9+dfsg-1), python3-pyqt5.sip (12.11.1-1), and dependencies (~6MB downloaded, 25.6MB disk space)
- Command: `python3 -c "import PyQt5.QtWidgets; print('PyQt5 imported successfully')"`
  - Output: PyQt imported successfully
- Command: `dpkg -l | grep pyqt5`
  - Output: python3-pyqt5 (5.15.9+dfsg-1), python3-pyqt5.sip (12.11.1-1)
- Notes: Used apt to avoid breaking system Python. Wi-Fi stable for download.

### 3. Test PyQt5 Window (2025-10-16)
- Command: `python3 ~/projects/amanuensis/test_pyqt5.py`
  - Output: Window displayed (400x300, titled "Amanuensis Test Window").
- Notes: Window worked, Wayland warning harmless. Ready for GUI design.

## Notes
- Limited Wi-Fi Access: Plan downloads carefully
- GitHub used for backups and version control.
- Next: Test PyQt5 with a simple window, optimize bash environment.
