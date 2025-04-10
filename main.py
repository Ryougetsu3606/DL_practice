import tkinter as tk
from function import ArtiEval, GetArti

class DLApp:
    def __init__(self, root):
        self.root = root
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
        title_label = tk.Label(self.root, text="超绝最强究极作文生成打分一体化系统 v1.0", font=("SimSun", 20), bg="lightgray")
        title_label.pack(pady=15)

        # 左侧按钮栏
        button_frame = tk.Frame(self.root, width=100, bg="lightgray", padx=10, pady=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        generate_button = tk.Button(button_frame, text="小作文生成", width=15)
        generate_button.pack(pady=14)

        appreciate_button = tk.Button(button_frame, text="佳作共赏", command=self.fetch_article, width=15)
        appreciate_button.pack(pady=14)

        evaluate_button = tk.Button(button_frame, text="AI打分", command=self.evaluate_article, width=15)
        evaluate_button.pack(pady=14)

        manual_button = tk.Button(button_frame, text="使用说明", width=15)
        manual_button.pack(pady=14)

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
            comment, score = ArtiEval.article_evaluation(article)
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


if __name__ == "__main__":
    root = tk.Tk()
    app = DLApp(root)
    root.mainloop()