import textwrap

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
