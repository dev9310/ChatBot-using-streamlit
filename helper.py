import textwrap

def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, '> ', predicate=lambda _: True)

def get_css():
  css =  """
  <style> 
  h1,h2{
    text-align: center; 
  }
  </style>
  
  """
  return css

def get_intro():
  return """

This tool provides a **comprehensive analysis** of various stocks. Here are some of the features you can explore:



- **📊 Stock Price Analysis**: View **historical stock prices** with interactive line charts.

- **📅 Current Stock Data**: Get the latest stock data including **Open, Close, High, Low**, and **Volume**.

- **📈 Volume Analysis**: Visualize the trading volume with colorful bar charts.

- **🔄 Moving Averages**: Analyze the stock's performance with **10, 30, and 100-day moving averages**.

- **⏳ Customizable Intervals**: Choose different time intervals to tailor the analysis to your needs.

- 🌿 Also check my [GitHub](https://github.com/bannu82)

Select a stock from the sidebar to get started! 🚀
"""
