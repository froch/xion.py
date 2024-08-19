# xion.py

Python SDK for XION - the Generalized Chain Abstraction Layer

## Getting started

- We are using [rye](https://rye.astral.sh/) to manage dependencies

```bash
$ rye sync
```

## Examples

- Check the `./tests/...` directory for examples for each module.

```bash
def test_bank_send():
    m = os.getenv("XION_MNEMONIC", generate_mnemonic())
    wallet = XionWallet.from_mnemonic(m)

    network = NetworkConfig.localhost()
    xion = XionClient(network)
    amount = 1_000_000

    draft_tx = xion.bank.tx_send(
        sender=wallet.address(),
        recipient=wallet.address(),
        amount=amount,
        denom=network.denom_fee,
    )

    tx = xion.txs.submit(
        tx=draft_tx,
        sender=wallet,
    )

    assert tx is not None
    assert isinstance(tx, TxResponse)
    assert tx.hash is not None
    assert tx.code == 0
```

## Regenerating Protocol Buffers

- Component versions are defined in the `Makefile`
- Components are fetched to `./build/...`
- We use [buf.build](https://buf.build/) to generate the protocol buffers

```bash
$ make proto
```

## Linting

- We are using [ruff](https://astral.sh/ruff) and [isort](https://pycqa.github.io/isort/) to lint the code

```bash
$ make lint
```

## Security

- We are using [bandit](https://bandit.readthedocs.io/) to check for security issues

```bash
$ make safe
```

