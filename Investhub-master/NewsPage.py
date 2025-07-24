from tkinter import *
from datetime import datetime
from newsapi import NewsApiClient

root = Tk()
root.title("News")
root.geometry("800x600")

# News API
newsapi = NewsApiClient(api_key='6c72b2026acb44ada2fff51f379bb042')

# Create a scrollable frame
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# Function to fetch and display news headlines
def display_news():
    # Fetch top headlines
    top_headlines = newsapi.get_top_headlines(language="en", country="in", category="business")

    # Display headlines in the text widget
    for article in top_headlines['articles']:
        f1 = Frame(scrollable_frame, background="white", relief=SOLID, borderwidth=1)
        f1.pack(fill="x", padx=10, pady=10)

        # Display article title
        title_label = Label(f1, text=article['title'], font=("Trebuchet MS", 14, "bold"), wraplength=700, background="white")
        title_label.pack(anchor="w", padx=10, pady=5)

        # Display article description
        description_label = Label(f1, text=article['description'], wraplength=700, background="white", font=("Trebuchet MS", 12))
        description_label.pack(anchor="w", padx=10, pady=5)

        # Display article source
        source_label = Label(f1, text=f"Source: {article['source']['name']}", background="white", font=("Trebuchet MS", 10, "italic"))
        source_label.pack(anchor="w", padx=10, pady=5)

        # Display article published date
        # Format the published date to display only the date
        published_at = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
        date_label = Label(f1, text=f"Published: {published_at}", background="white", font=("Trebuchet MS", 10))
        date_label.pack(anchor="w", padx=10, pady=5)


display_news()
root.mainloop()
