import textwrap
import time

# Converting response into markdown text
def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, '> ', predicate=lambda _: True)

# Custom Css
def get_css():
  css =  """
  <style> 
  h1,h2{
    text-align: center; 
  }
  </style>
  
  """
  return css

# Intro
def get_intro():
  return """
  
"""

def stream_data(txt ,sleep_time=0.05):
    for word in txt.split(" "):
        yield word + " "
        time.sleep(sleep_time)

