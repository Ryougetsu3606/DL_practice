import tkinter as tk
from tkinter import messagebox
from function import ArtiEval, GetArti
import json
import random

class DLApp:
    def __init__(self, root):
        self.root = root
        try:
            with open("option.json", "r", encoding="utf-8") as f:
                options = json.load(f)
        except:
            options = {"API": " ", "AI评分标准": "easing"}
        self.api, self.standard = options["API"], options["AI评分标准"]
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        # 获取屏幕宽度和高度
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # 设置窗口宽度和高度为屏幕的黄金比例
        golden_ratio = 0.618
        window_width = int(screen_width * golden_ratio)
        window_height = int(screen_height * golden_ratio)

        # 计算窗口居中位置
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.root.title("超绝最强究极作文生成打分一体化系统")
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.root.configure(bg="lightgray")

        # 设置最小尺寸
        self.root.minsize(window_width, window_height)

    def create_widgets(self):
        # 顶部标题
        title_label = tk.Label(self.root, bg="lightgray", font=("SimSun", 20))
        title_text = "超绝最强究极作文生成打分一体化系统"
        colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        bias = random.randint(0, len(colors))
        for i, char in enumerate(title_text):
            color = colors[(i+bias) % len(colors)]
            title_label_text = tk.Label(title_label, text=char, fg=color, bg="lightgray", font=("SimSun", 20))
            title_label_text.pack(side=tk.LEFT)
        title_label.pack(pady=15)

        # 左侧按钮栏
        button_frame = tk.Frame(self.root, width=100, bg="lightgray", padx=10, pady=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        appreciate_button = tk.Button(button_frame, text="佳作共赏", command=self.fetch_article, width=15)
        appreciate_button.pack(pady=14)

        evaluate_button = tk.Button(button_frame, text="AI打分", command=self.evaluate_article, width=15)
        evaluate_button.pack(pady=14)

        manual_button = tk.Button(button_frame, text="使用说明", command=self.show_manual, width=15)
        manual_button.pack(pady=14)

        option_button = tk.Button(button_frame, text="设置", command=self.open_settings_window, width=15)
        option_button.pack(pady=14)

        # 右侧内容区域
        content_frame = tk.Frame(self.root, bg="lightgray")
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # 上方文章展示框
        text_frame = tk.Frame(content_frame, bg="white")
        text_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.article_text = tk.Text(text_frame, wrap=tk.WORD, height=12, font=("SimSun", 12))
        self.article_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 添加垂直滚动条
        text_scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.article_text.yview)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.article_text.configure(yscrollcommand=text_scrollbar.set)

        # 下方评语和评分区域
        result_frame = tk.Frame(content_frame, bg="lightgray")
        result_frame.pack(fill=tk.BOTH, expand=True)

        # 评语
        comment_label = tk.Label(result_frame, text="评语：", font=("SimSun", 14), bg="lightgray", anchor="w")
        comment_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.comment_text = tk.Text(result_frame, wrap=tk.WORD, height=5, font=("SimSun", 12), state=tk.DISABLED)
        self.comment_text.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        # 评分
        score_label = tk.Label(result_frame, text="评分：", font=("SimSun", 14), bg="lightgray", anchor="w")
        score_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.score_text = tk.Text(result_frame, wrap=tk.WORD, height=1.2, width=5, font=("SimSun", 12), state=tk.DISABLED, relief=tk.GROOVE, bd=2)
        self.score_text.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        # 调整布局
        result_frame.columnconfigure(1, weight=1)

    def fetch_article(self):
        article = GetArti.fetch_article()
        self.article_text.delete(1.0, tk.END)
        self.article_text.insert(tk.END, article)

    def evaluate_article(self):
        article = self.article_text.get(1.0, tk.END).strip()
        if article:
            comment, score = ArtiEval.article_evaluation(article, self.api, self.standard)
            self.comment_text.configure(state=tk.NORMAL)
            self.comment_text.delete(1.0, tk.END)
            self.comment_text.insert(tk.END, comment)
            self.comment_text.configure(state=tk.DISABLED)
            self.score_text.configure(state=tk.NORMAL)
            self.score_text.delete(1.0, tk.END)
            self.score_text.insert(tk.END, score)
            self.score_text.configure(state=tk.DISABLED)
        else:
            self.comment_text.configure(state=tk.NORMAL)
            self.comment_text.delete(1.0, tk.END)
            self.comment_text.insert(tk.END, "请先获取或输入文章！")
            self.comment_text.configure(state=tk.DISABLED)
            self.score_text.configure(state=tk.NORMAL)
            self.score_text.delete(1.0, tk.END)
            self.score_text.insert(tk.END, "N/A")
            self.score_text.configure(state=tk.DISABLED)

    def show_manual(self):
        if hasattr(self, 'manual_window') and self.manual_window.winfo_exists():
            self.manual_window.lift()
            return

        manual_text = (
            "\n使用说明：\n\n"
            "1.第一次使用前，请先登录智谱官网https://www.bigmodel.cn/console/overview，随后点击右上角进入“个人中心”->“API_Keys”->“添加新的API_Key”，并把所得的Key复制并填入本程序“设置”的“API”中。执行该步骤后，你的API只会保存在本地，不存在泄露风险，可以放心使用。\n\n"
            "2.界面主体部分为输入框，你可以在上面尽情挥洒你的才华，或点击“佳作共赏”，获取一篇精选文章。\n\n"
            "3.点击“AI打分”，可以调用GLM-4大模型对当前文章进行评分。注意：使用代理连接会使此功能失效。\n\n"
            "4.点击“设置”按钮，可以修改当前使用的API，或变更AI打分标准。"
        )
        self.manual_window = tk.Toplevel(self.root)
        self.manual_window.title("使用说明")
        self.manual_window.geometry("600x450")
        self.manual_window.configure(bg="white")

        # 使用 Text 小部件以便更好地控制布局和滚动
        text_frame = tk.Frame(self.manual_window, bg="white")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        manual_text_widget = tk.Text(
            text_frame, wrap=tk.WORD, font=("SimSun", 12), bg="white", relief=tk.FLAT
        )
        manual_text_widget.insert(tk.END, manual_text)
        manual_text_widget.configure(state=tk.DISABLED)
        manual_text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 禁止窗口拉伸
        self.manual_window.resizable(False, False)

    def open_settings_window(self):
        try:
            with open("option.json", "r", encoding="utf-8") as f:
                options = json.load(f)
        except:
            options = {"API": " ", "AI评分标准": "easing"}

        if hasattr(self, 'settings_window') and self.settings_window.winfo_exists():
            self.settings_window.lift()
            return

        self.settings_window = tk.Toplevel(self.root)
        self.settings_window.title("设置")
        self.settings_window.geometry("400x250")
        self.settings_window.configure(bg="lightgray")
        self.settings_window.resizable(False, False)

        # API设置
        api_label = tk.Label(self.settings_window, text="API：", font=("SimSun", 12), bg="lightgray", anchor="w")
        api_label.pack(pady=10, padx=10, anchor="w")

        api_entry = tk.Entry(self.settings_window, font=("SimSun", 10), width=50)
        api_entry.insert(0, options.get("API", ""))
        api_entry.pack(pady=5, padx=10, anchor="w")

        # AI评分标准设置
        standard_var = tk.StringVar(value=options.get("AI评分标准", "easing"))
        standard_label_frame = tk.LabelFrame(self.settings_window, text="选择评分标准", font=("SimSun", 12), bg="lightgray", padx=10, pady=10)
        standard_label_frame.pack(pady=10, padx=10, fill="both", expand=True)

        easing_radio = tk.Radiobutton(standard_label_frame, text="宽松(建议)", variable=standard_var, value="easing", font=("SimSun", 10), bg="lightgray", anchor="w")
        easing_radio.pack(anchor="w", pady=5)

        strict_radio = tk.Radiobutton(standard_label_frame, text="严格", variable=standard_var, value="strict", font=("SimSun", 10), bg="lightgray", anchor="w")
        strict_radio.pack(anchor="w", pady=5)

        # 确认修改按钮
        def save_settings():
            new_api = api_entry.get().strip()
            new_standard = standard_var.get()
            self.api = new_api
            self.standard = new_standard
            options["API"] = new_api
            options["AI评分标准"] = new_standard
            with open("option.json", "w", encoding="utf-8") as f:
                json.dump(options, f, ensure_ascii=False, indent=4)
            self.api = new_api
            tk.messagebox.showinfo("提示", "设置已保存！")
            self.settings_window.destroy()

        save_button = tk.Button(self.settings_window, text="确认修改", font=("SimSun", 10), command=save_settings)
        save_button.pack(padx=20, pady=10, anchor="w")


if __name__ == "__main__":
    root = tk.Tk()
    app = DLApp(root)
    root.mainloop()