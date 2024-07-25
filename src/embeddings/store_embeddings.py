import faiss
import numpy as np

def store_embeddings(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, "E:/DeepSolv_Assignment/data/vector_index")

if __name__ == "__main__":
    embeddings = np.load("E:/DeepSolv_Assignment/data/embeddings.npy")
    store_embeddings(embeddings)
