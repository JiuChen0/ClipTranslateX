import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import pyperclip
import time
import pandas as pd
import os
import trans

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard Translator")
        self.translations = []

        # API选择
        self.api_var = tk.StringVar(value="google")
        ttk.Label(self.root, text="Select API:").pack(pady=10)
        ttk.Radiobutton(self.root, text="Google", variable=self.api_var, value="google").pack(anchor=tk.W, padx=20)
        ttk.Radiobutton(self.root, text="DeepL", variable=self.api_var, value="deepl").pack(anchor=tk.W, padx=20)

        # 翻译记录列表
        self.trans_listbox = ttk.Treeview(self.root, columns=('Original', 'Translated'), show='headings')
        self.trans_listbox.heading('Original', text='Original')
        self.trans_listbox.heading('Translated', text='Translated')
        self.trans_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # 导出按钮
        ttk.Button(self.root, text="Export Excel", command=self.export_excel).pack(padx=20, pady=10)

        # 当尝试关闭窗口时
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # 启动剪贴板监听
        self.start_translation()

    def start_translation(self):
        self.translations.clear()

        def monitor_clipboard():
            old_clipboard_data = pyperclip.paste()
            while True:
                clipboard_data = pyperclip.paste()
                if clipboard_data != old_clipboard_data:
                    translated_text = trans.translate_text(clipboard_data, self.api_var.get())
                    self.trans_listbox.insert('', 'end', values=(clipboard_data, translated_text))
                    self.translations.append((clipboard_data, translated_text))
                    old_clipboard_data = clipboard_data
                time.sleep(1)

        self.monitor_thread = threading.Thread(target=monitor_clipboard, daemon=True)
        self.monitor_thread.start()

    def export_excel(self):
        # 如果存在Excel文件，读取内容
        if os.path.exists('translations.xlsx'):
            df_existing = pd.read_excel('translations.xlsx', engine='openpyxl')
        else:
            df_existing = pd.DataFrame(columns=['English', 'Chinese'])

        # 将新数据追加到现有数据的末尾
        df_new = pd.DataFrame(self.translations, columns=['English', 'Chinese'])
        df_final = pd.concat([df_existing, df_new], ignore_index=True)

        # 保存回Excel文件
        df_final.to_excel('translations.xlsx', index=False, engine='openpyxl')
        print("Data appended to translations.xlsx")

    def on_closing(self):
        answer = messagebox.askyesno("Confirm Exit", "请确保已导出到excel")
        if answer:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
