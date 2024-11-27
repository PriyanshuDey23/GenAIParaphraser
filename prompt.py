PROMPT="""

Paraphrase the provided input text into a unique, plagiarism-free, and coherent piece of writing while adhering to the following specifications:

Input Parameters:
- Input Text: {input_text}
- Paraphrase Mode: {paraphrase_mode} (Choose: light, medium, or heavy paraphrasing)
- Fluency Level: {fluency_penalty} (Specify: low, medium, or high)
- Diversity Level: {diversity_penalty} (Specify: low, medium, or high)
- Word Count: {length_of_words} (Approximate number of words in the output)
- Tone: {tone} (Specify: formal, informal, persuasive, creative, etc.)

Output Requirements:
1. Generate a paraphrased text that meets the input parameters and ensures originality (plagiarism-free).
2. Deliver the output in the following formats:
   - Plain Text: Provide the paraphrased text as a string.
   - Downloadable File: Allow the text to be downloaded as a .txt or .docx file.

Additional Rules:
- Remove all special characters from the output text (e.g., symbols, emojis).
- Ensure the output maintains logical consistency and aligns with the selected tone and parameters.

"""