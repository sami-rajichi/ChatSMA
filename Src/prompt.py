prompt_template = """
Please refer to the provided information to respond accurately to the user's inquiry.
If you lack the necessary information to address the question, kindly state that you don't have the answer instead of providing inaccurate information.

Context: {context}
Question: {question}

Please only present the relevant response below and refrain from including additional content.
Relevant response:
"""