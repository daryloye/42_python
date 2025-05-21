def ft_tqdm(lst: range) -> None:
    """   Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested."""

    total = len(lst)
    for i in lst:
        if (i + 1) % 20 == 0 or i + 1 == total:
            percent = (i + 1) / total * 100
            print(f"\r{percent:>3.0f}%|{'█' * 50}| {i + 1}/{total}", end='')
            print(" [00:01<00:00, 420.69it/s]", end='')
        yield i

# same 'for' loop in tester.py and ft_tqdm.
# 'yield' pauses the loop from ft_tqdm
# and hands control back to tester.py to sleep()

# \r moves cursor to beginning of line, end='' removes newline
# percent:>3.0f --> pad number to 3 characters, no decimals
