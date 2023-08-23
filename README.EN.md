

[中文](README.md) | English

# ClipTranslateX

**ClipTranslateX: An intuitive real-time clipboard translator with seamless Excel integration.Currently only English to Chinese translation is supported.**

## Features

- **Real-time Translation:** Automatically translates English text copied to the clipboard.
- **API Choices:** Choose between Google and DeepL translation APIs.
- **Live GUI Display:** View the original and translated text directly within the interface.
- **Excel Export:** Export your translations to Excel with the push of a button.

## Installation & Usage

1. Ensure you have Python 3.x installed.

2. Clone this repository or download the ZIP package:
   ```
   git clone git@github.com:JiuChen0/ClipTranslateX.git
   ```

3. Navigate to the project folder and install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the program:
   ```
   python GUI.py
   ```

## How to Use

1. Upon launching the GUI application, it automatically begins monitoring your clipboard.
2. Copy any English text, and its translation will appear in the interface.
3. Throughout the session, click the "Export to Excel" button whenever you wish to save all translations to an Excel file.
4. Upon attempting to close the program, a prompt will ensure you've exported all translations to Excel.

## Dependencies

- tkinter
- pyperclip
- requests
- googletrans
- pandas
- openpyxl

