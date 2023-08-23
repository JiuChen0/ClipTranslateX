
# ClipTranslateX 剪贴板翻译器

中文 | [English](README.EN.md)

这是一个简单的Python工具，当你复制英文文本时，它可以自动将文本翻译成中文，并允许用户将这些翻译导出到Excel文件中。
目前只支持英文翻译成中文。

## 功能

- 实时监听剪贴板，自动翻译复制的英文文本。
- 可以选择使用Google翻译API或DeepL翻译API。
- 实时在GUI界面中显示原文和翻译。
- 允许用户将所有翻译导出到Excel文件中。

## 安装和运行

1. 首先确保您已经安装了Python 3.x。

2. 克隆此仓库或下载ZIP包。

3. 进入项目文件夹，并安装所需的依赖项：
   ```
   pip install -r requirements.txt
   ```

4. 运行程序：
   ```
   python GUI.py
   ```

## 使用说明

1. 打开GUI应用程序后，它将自动开始监听您的剪贴板。
2. 复制任何英文文本，您将在界面中看到其翻译。
3. 在程序的生命周期中，您可以任意多次点击“导出Excel”按钮，将所有翻译导出到一个Excel文件中。
4. 关闭程序时，会出现一个提示，确保您已经导出所有翻译到Excel文件中。

## 依赖库

- tkinter
- pyperclip
- requests
- googletrans
- pandas
- openpyxl

