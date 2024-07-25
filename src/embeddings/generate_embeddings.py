from sentence_transformers import SentenceTransformer

def generate_embeddings(texts):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode(texts)
    return embeddings

if __name__ == "__main__":
    with open("E:/DeepSolv_Assignment/data/extracted_pdf_text.txt", "r") as f:
        pdf_text = f.read()
    with open("E:/DeepSolv_Assignment/data/extracted_website_text.txt", "r") as f:
        website_text = f.read()
    with open("E:/DeepSolv_Assignment/data/youtube/video_transcript.txt", "r") as f:
        transcript_text = f.read()

    texts = [pdf_text, website_text, transcript_text]
    embeddings = generate_embeddings(texts)

    import numpy as np
    np.save("E:/DeepSolv_Assignment/data/embeddings.npy", embeddings)
