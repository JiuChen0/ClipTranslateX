# ClipTranslateX 剪贴板翻译器

中文 | [English](README.EN.md)

ClipTranslateX是一个方便的小工具。只要你复制英文文本，该工具就会自动将其翻译成中文，并允许你保存这些翻译记录。目前，它支持从英文翻译到中文。

## 🌟 功能

- 🚀 **实时监听**：工具会实时监控剪贴板的内容，无需任何额外操作。
- 🌐 **多API支持**：支持Google翻译和DeepL翻译API。请注意，使用DeepL需要自行配置API密钥。
- 📋 **即时显示**：在GUI界面实时显示原文和对应的翻译结果。
- 📂 **导出功能**：一键将所有的翻译结果导出到Excel文件，方便后续查看和使用。

## 🔧 安装和运行

1. 确认你的系统上已安装Python 3.x版本。
2. 克隆此GitHub仓库，或直接下载ZIP包解压。
3. 在终端或命令提示符中导航到项目目录，并安装所有必要的依赖库：
   ```bash
   pip install -r requirements.txt
   ```
4. 启动程序：
   ```bash
   python GUI.py
   ```

## 📘 使用说明

1. 启动GUI应用后，它会自动开始监控剪贴板。
2. 任意复制英文内容，你将在应用界面实时看到其翻译。
3. 在使用过程中，你可以随时点击“导出Excel”按钮，将翻译记录保存到Excel文件。
4. 当你试图关闭程序时，会出现一个提示，确保你已将所有翻译内容保存到Excel。

## 📦 依赖库

- tkinter
- pyperclip
- requests
- googletrans
- pandas
- openpyxl


🌐 **特别提醒**：如果你选择使用DeepL翻译，记得在`trans.py`中配置你的API密钥。