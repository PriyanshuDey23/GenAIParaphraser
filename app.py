from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from prompt import *
from utils import *
import fitz


# Load environment variables from the .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")



# Paraphrasing Function
def paraphraser(input_text, paraphrase_mode, fluency_penalty, diversity_penalty, length_of_words, tone):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=1, api_key=GOOGLE_API_KEY)
    PROMPT_TEMPLATE =PROMPT
    prompt = PromptTemplate(
        input_variables=["input_text", "paraphrase_mode", "fluency_penalty", "diversity_penalty", "length_of_words", "tone"],
        template=PROMPT_TEMPLATE,
    )
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    response = llm_chain.run({
        "input_text": input_text,
        "paraphrase_mode": paraphrase_mode,
        "fluency_penalty": fluency_penalty,
        "diversity_penalty": diversity_penalty,
        "length_of_words": length_of_words,
        "tone": tone,
    })
    return response

# Streamlit App Configuration
st.set_page_config(page_title="Paraphraser", layout="wide")
st.header("Paraphraser")

# File upload or text input
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    try:
        # Read and extract text using PyMuPDF (fitz)
        pdf_text = ""
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page in pdf_document:
            pdf_text += page.get_text()
        pdf_document.close()

        user_input = pdf_text
        st.text_area("Extracted Text from PDF", user_input, height=200)
    except Exception as e:
        st.error(f"Failed to process the uploaded PDF: {e}")
else:
    user_input = st.text_area("Enter your text", height=200)

# Sidebar Parameters
with st.sidebar:
    st.title("Parameters")
    paraphrase_mode = st.selectbox("Select paraphrase mode", ["light", "medium", "heavy"])
    fluency_penalty = st.selectbox("Select fluency penalty", ["low", "medium", "high"])
    diversity_penalty = st.selectbox("Select diversity penalty", ["low", "medium", "high"])
    length_of_words = st.text_input("Select the word limit")
    tone = st.selectbox("Select tone", ["Formal", "Informal", "Friendly", "Sarcastic", "Professional"])

# Generate paraphrased text
if st.button("Generate Paraphrased Text"):
    if not user_input.strip():
        st.error("Please provide input text or upload a valid PDF.")
    else:
        response = paraphraser(user_input, paraphrase_mode, fluency_penalty, diversity_penalty, length_of_words, tone)
        st.subheader("Paraphrased Text:")
        st.write(response)

        # Download options
        st.download_button(
            label="Download as TXT",
            data=convert_to_txt(response),
            file_name="paraphrased_text.txt",
            mime="text/plain",
        )
        st.download_button(
            label="Download as DOCX",
            data=convert_to_docx(response),
            file_name="paraphrased_text.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
