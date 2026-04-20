import argparse
import math
import time
import torch
from torch.utils.data import DataLoader
from datasets import load_dataset
from tqdm import tqdm
from transformers import GPT2Tokenizer

from .model import LightGPT


def collate_fn(batch, tokenizer, max_length=128):
    """Collate function for GPT-2 tokenizer."""
    texts = [ex['text'] for ex in batch if ex['text'].strip()]

    # Tokenize with GPT-2 tokenizer
    encodings = tokenizer(texts, truncation=True, padding=True,
                         max_length=max_length, return_tensors='pt')

    return encodings


def train(args):
    device = torch.device('cuda' if torch.cuda.is_available() and not args.cpu else 'cpu')
    print('Using device', device)
    print('Fine-tuning pre-trained GPT-2 model on WikiText-2...')

    # Load dataset
    ds = load_dataset('wikitext', 'wikitext-2-raw-v1', split='train')
    # Filter out empty texts
    ds = ds.filter(lambda x: len(x['text'].strip()) > 10)

    # Initialize model and tokenizer
    model = LightGPT(mode=args.mode, max_seq_len=args.max_seq_len)
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token

    model.to(device)
    model.train()

    # Use much lower learning rate for fine-tuning
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr)

    print(f'Model config: {model.get_config()}')
    print(f'Training on {len(ds)} samples')

    batch_size = args.batch_size
    for epoch in range(args.epochs):
        loader = DataLoader(ds, batch_size=batch_size, shuffle=True,
                          collate_fn=lambda b: collate_fn(b, tokenizer, args.max_seq_len))

        pbar = tqdm(loader, desc=f'Epoch {epoch}')
        total_loss = 0.0
        steps = 0

        for batch in pbar:
            if batch is None:
                continue

            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)

            opt.zero_grad()

            # Forward pass
            outputs = model.model(input_ids=input_ids,
                                attention_mask=attention_mask,
                                labels=input_ids)

            loss = outputs.loss
            loss.backward()
            opt.step()

            total_loss += loss.item()
            steps += 1

            pbar.set_postfix({'loss': f'{loss.item():.4f}'})

        avg_loss = total_loss / steps
        print(f'Epoch {epoch} completed. Average loss: {avg_loss:.4f}')

        # Save checkpoint
        checkpoint_path = f'lightgpt_{args.mode}_epoch_{epoch}.pt'
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': opt.state_dict(),
            'loss': avg_loss,
            'config': model.get_config()
        }, checkpoint_path)
        print(f'Checkpoint saved: {checkpoint_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='normal', choices=['underkill', 'normal', 'overkill'])
    parser.add_argument('--max_seq_len', type=int, default=128)
    parser.add_argument('--batch_size', type=int, default=4)
    parser.add_argument('--epochs', type=int, default=1)
    parser.add_argument('--lr', type=float, default=5e-5)  # Much lower LR for fine-tuning
    parser.add_argument('--cpu', action='store_true')
    args = parser.parse_args()

    train(args)
            if batch is None:
                continue
            batch = batch.to(device)
            inputs = batch[:, :-1]
            targets = batch[:, 1:]
            logits = model(inputs)
            loss = torch.nn.functional.cross_entropy(logits.view(-1, logits.size(-1)), targets.reshape(-1), ignore_index=0)
            opt.zero_grad()
            loss.backward()
            opt.step()
            total_loss += loss.item()
            steps += 1
            pbar.set_postfix(loss=total_loss/steps)
        print(f'Epoch {epoch} avg loss {total_loss/steps:.4f}')

    # save a small checkpoint
    torch.save({'model_state_dict': model.state_dict(), 'config': model.__dict__}, args.out)
    print('Saved checkpoint to', args.out)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--mode', choices=['overkill','normal','underkill'], default='normal')
    p.add_argument('--epochs', type=int, default=1)
    p.add_argument('--batch_size', type=int, default=8)
    p.add_argument('--lr', type=float, default=1e-4)
    p.add_argument('--max_seq_len', type=int, default=64)
    p.add_argument('--out', default='lightgpt.chkpt')
    p.add_argument('--cpu', action='store_true')
    args = p.parse_args()
    train(args)
