English | [中文](README.md)

# ClipTranslateX

**ClipTranslateX**: Dive into a hassle-free translation experience with real-time clipboard monitoring and streamlined Excel exports. Currently, our tool bridges the language barrier from English to Chinese.

## 🌟 Features

- 🚀 **Real-time Translation**: Clip an English phrase or paragraph and watch it get translated in real-time.
- 🌐 **Flexible API Choices**: Swing between Google and DeepL translation services. Remember to set up your own API key if you lean towards DeepL.
- 🖥 **Interactive GUI Display**: Keep track of your source content and its translated counterpart in a user-friendly interface.
- 📈 **Excel Export**: Compile and export your translations to an Excel sheet, ensuring they're always ready for future reference.

## 🔧 Installation & Usage

1. Get Python 3.x up and running on your machine.

2. Secure a copy of this repository either by cloning or downloading the ZIP package:
   ```bash
   git clone git@github.com:JiuChen0/ClipTranslateX.git
   ```

3. Inside the project directory, install the needed dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ignite the program with:
   ```bash
   python GUI.py
   ```

## 📘 How to Use

1. With the GUI application up, it instantly sets its sights on your clipboard.
2. As you copy English content, its translation seamlessly surfaces in the application.
3. During your journey, hit the "Export to Excel" button to encapsulate your translations into an Excel file whenever needed.
4. And as you edge towards exiting the program, a nudge ensures that you've stockpiled all your translations into Excel.

## 📦 Dependencies

- tkinter
- pyperclip
- requests
- googletrans
- pandas
- openpyxl

**Note**: If you're aligned with the DeepL translation service, don't forget to embed your API key within `trans.py`.

