# A demo file on how to use Llama3 model to summarize a text and pick out the important parts.
import ollama

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': '''Can you write a project introduction for a personal project that summarizes the debates happening in the canadian parliament using LLMs. These debates are sourced from the official Hansard document of Canada. Do not generate more information and write it in paragraphs.''',
  },
])

print(response['message']['content'])