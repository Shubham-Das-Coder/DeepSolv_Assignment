import streamlit as st
from .query_gpt3 import query_gpt3
import faiss
import numpy as np

def main():
    st.title("Apple Vision Pro Q/A Chatbot")
    question = st.text_input("Ask a question about Apple Vision Pro:")
    
    if st.button("Submit"):
        index = faiss.read_index("E:/DeepSolv_Assignment/data/vector_index")
        # Assuming the context is just the first result from the index for simplicity
        context_id = 0
        _, I = index.search(np.array([index.reconstruct(context_id)]), 1)
        context = I[0][0]

        answer = query_gpt3(question, context)
        st.write(f"Answer: {answer}")

if __name__ == "__main__":
    main()
