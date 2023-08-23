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
        self.trans_listbox.bind('<ButtonRelease-1>', self.select_translation)
        self.trans_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # 编辑和删除按钮
        ttk.Button(self.root, text="编辑", command=self.edit_translation).pack(side=tk.LEFT, padx=5, pady=10)
        ttk.Button(self.root, text="删除", command=self.delete_translation).pack(side=tk.LEFT, padx=5, pady=10)
        
        # 导出按钮
        ttk.Button(self.root, text="Export Excel", command=self.export_excel).pack(side=tk.RIGHT, padx=20, pady=10)

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

        # 检查新数据是否已经存在于Excel文件中
        merge_df = pd.merge(df_existing, df_new, how='inner', on=['English', 'Chinese'])

        duplicated_data = []
        if not merge_df.empty:
            for index, row in merge_df.iterrows():
                duplicated_data.append(f"{row['English']} - {row['Chinese']}")
            duplicated_msg = "\n".join(duplicated_data)
            messagebox.showwarning("警告", f"以下内容已经存在，不会重复导出:\n\n{duplicated_msg}")
            df_new = df_new.drop(merge_df.index)

        # 只有当存在新数据时，才追加到Excel文件
        if not df_new.empty:
            df_final = pd.concat([df_existing, df_new], ignore_index=True)
            df_final.to_excel('translations.xlsx', index=False, engine='openpyxl')
            print("New data appended to translations.xlsx")
        else:
            print("No new data to append.")



    def on_closing(self):
        answer = messagebox.askyesno("Confirm Exit", "请确保已导出到excel")
        if answer:
            self.root.destroy()
        else:
            return

    def select_translation(self, event):
        self.selected_item = self.trans_listbox.selection()
        self.selected_index = self.trans_listbox.index(self.selected_item)

    def delete_translation(self):
        if hasattr(self, 'selected_item'):
            self.trans_listbox.delete(self.selected_item)
            if self.selected_index < len(self.translations):
                del self.translations[self.selected_index]

    def edit_translation(self):
        if hasattr(self, 'selected_item'):
            original, translation = self.trans_listbox.item(self.selected_item, 'values')

            edit_win = tk.Toplevel(self.root)
            edit_win.title("编辑翻译")

            ttk.Label(edit_win, text="原文:").grid(row=0, column=0, padx=5, pady=5)
            original_entry = ttk.Entry(edit_win)
            original_entry.grid(row=0, column=1, padx=5, pady=5)
            original_entry.insert(0, original)

            ttk.Label(edit_win, text="译文:").grid(row=1, column=0, padx=5, pady=5)
            translation_entry = ttk.Entry(edit_win)
            translation_entry.grid(row=1, column=1, padx=5, pady=5)
            translation_entry.insert(0, translation)

            ttk.Button(edit_win, text="保存", command=lambda: self.save_edits(original_entry.get(), translation_entry.get(), edit_win)).grid(row=2, column=0, columnspan=2, pady=10)

    def save_edits(self, new_original, new_translation, edit_win):
        self.trans_listbox.item(self.selected_item, values=(new_original, new_translation))
        if self.selected_index < len(self.translations):
            self.translations[self.selected_index] = (new_original, new_translation)
        edit_win.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
