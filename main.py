from function import ArtiEval, GetArti
import tkinter as tk
# article = GetArti.fetch_article()
# comment, score = ArtiEval.article_evaluation(article)
# print("文章内容：", article)
# print("评语：", comment)
# print("评分：", score)
def display_article():
    article = GetArti.fetch_article()
    article_text.delete(1.0, tk.END)
    article_text.insert(tk.END, article)

# Create the main window
root = tk.Tk()
root.title("作文评估")

# Create a button to fetch a random article
fetch_button = tk.Button(root, text="随机作文", command=display_article)
fetch_button.pack(pady=10)

# Create a text widget to display the article
article_text = tk.Text(root, wrap=tk.WORD, height=15, width=50)
article_text.pack(pady=10)
def evaluate_article():
    article = article_text.get(1.0, tk.END).strip()
    if article:
        comment, score = ArtiEval.article_evaluation(article)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"评语：{comment}\n评分：{score}")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "请先获取或输入文章！")

# Create a button to evaluate the article
evaluate_button = tk.Button(root, text="AI打分", command=evaluate_article)
evaluate_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a text widget to display the evaluation result
result_text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
result_text.pack(side=tk.RIGHT, pady=10)

# Adjust the layout of the article text widget
article_text.pack(side=tk.RIGHT, pady=10)
# Run the GUI event loop
root.mainloop()