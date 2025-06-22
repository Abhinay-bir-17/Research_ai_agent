import requests 
def get_embedding(prompt, model="nomic-embed-text"):
    emb_url = "http://localhost:11434/api/embeddings"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "model": model,
        "prompt": prompt
    }
    response = requests.post(emb_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("embedding", [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
if __name__ == "__main__":
    # Example usage
    prompt = "Hello, how are you?"
    embedding = get_embedding(prompt)
    if embedding is not None:
        print(f"embedding dimensions: {len(embedding)}")
        print(f"Embedding for '{prompt}': {embedding}")
    else:
        print("Failed to retrieve embedding.")
        