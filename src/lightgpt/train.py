import argparse
import math
import time
import torch
from torch.utils.data import DataLoader
from datasets import load_dataset
from tqdm import tqdm

from .model import LightGPT


def collate_fn(batch, tokenizer_fn, max_length=64):
    ids = []
    for ex in batch:
        toks = tokenizer_fn(ex['text'])
        if len(toks) == 0:
            continue
        toks = toks[:max_length]
        ids.append(torch.tensor(toks, dtype=torch.long))
    if len(ids) == 0:
        return None
    ids = torch.nn.utils.rnn.pad_sequence(ids, batch_first=True, padding_value=0)
    return ids


def simple_tokenizer(text):
    # reuse model's small tokenizer: whitespace hash
    from .model import LightGPT
    return LightGPT.small_vocab_tokenize(text)


def train(args):
    device = torch.device('cuda' if torch.cuda.is_available() and not args.cpu else 'cpu')
    print('Using device', device)

    ds = load_dataset('wikitext', 'wikitext-2-raw-v1', split='train')
    # filter short lines
    ds = ds.filter(lambda x: len(x['text'].strip())>0)

    model = LightGPT(mode=args.mode, max_seq_len=args.max_seq_len)
    model.to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr)

    batch_size = args.batch_size
    for epoch in range(args.epochs):
        loader = DataLoader(ds, batch_size=batch_size, shuffle=True, collate_fn=lambda b: collate_fn(b, simple_tokenizer, args.max_seq_len))
        pbar = tqdm(loader, desc=f'Epoch {epoch}')
        total_loss = 0.0
        steps = 0
        for batch in pbar:
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
