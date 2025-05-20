# embed_terraform.py

from app.services.embedding import load_and_embed_terraform

if __name__ == "__main__":
    print("📦 Embedding Terraform files from ./infra ...")
    load_and_embed_terraform("infra")
    print("✅ Embedding complete.")
