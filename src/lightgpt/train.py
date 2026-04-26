# LightGPT Training Script (Finetuning)
# ------------------------------------------------------------
# This script demonstrates a very simple finetuning loop using the Hugging
# Face ``transformers`` library. It is intentionally lightweight: it loads a
# pretrained causal model, adds a language‑modeling head (already present in the
# model), and runs a few training epochs on a small text dataset.
# ------------------------------------------------------------

import argparse
import os
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForCausalLM, AdamW

class TextDataset(Dataset):
    """A tiny dataset used for demonstration purposes.

    It reads a plain‑text file where each line is considered an independent
    training example.
    """

    def __init__(self, file_path: str, tokenizer, max_length: int = 128):
        self.samples = []
        self.tokenizer = tokenizer
        self.max_length = max_length
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.samples.append(line)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        text = self.samples[idx]
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding="max_length",
            max_length=self.max_length,
            return_tensors="pt",
        )
        # ``input_ids`` and ``attention_mask`` are tensors of shape (1, seq_len)
        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
        }


def finetune(
    model_name: str,
    train_file: str,
    output_dir: str,
    epochs: int = 3,
    batch_size: int = 4,
    learning_rate: float = 5e-5,
    max_length: int = 128,
):
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.train()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Dataset and dataloader
    dataset = TextDataset(train_file, tokenizer, max_length=max_length)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Optimizer
    optimizer = AdamW(model.parameters(), lr=learning_rate)

    print(f"Starting finetuning on {len(dataset)} examples, {epochs} epochs")
    for epoch in range(epochs):
        total_loss = 0.0
        for batch in dataloader:
            optimizer.zero_grad()
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            # The model returns ``loss`` when ``labels`` are provided
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=input_ids,
            )
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        avg_loss = total_loss / len(dataloader)
        print(f"Epoch {epoch + 1}/{epochs} – Avg loss: {avg_loss:.4f}")

    # Save model and tokenizer
    os.makedirs(output_dir, exist_ok=True)
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"Finetuned model saved to {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finetune a pretrained HuggingFace model for LightGPT")
    parser.add_argument("--model", default="gpt2", help="Base model name or path on the HF hub")
    parser.add_argument("--train_file", required=True, help="Path to a plain‑text training file")
    parser.add_argument("--output_dir", required=True, help="Directory where the finetuned model will be stored")
    parser.add_argument("--epochs", type=int, default=3, help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=4, help="Training batch size")
    parser.add_argument("--lr", type=float, default=5e-5, help="Learning rate")
    parser.add_argument("--max_length", type=int, default=128, help="Maximum token length per example")
    args = parser.parse_args()
    finetune(
        model_name=args.model,
        train_file=args.train_file,
        output_dir=args.output_dir,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.lr,
        max_length=args.max_length,
    )
