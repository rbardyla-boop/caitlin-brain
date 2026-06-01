(Existing content...)

## Quick Start — Local CLI (Recommended for your own vault)

```bash
git clone https://github.com/rbardyla-boop/caitlin-brain
cd caitlin-brain

# Using a vault export (recommended)
python cli/council_cli.py --pack ~/Backups/Memory-Export-2026-06-01.tar.gz --seed "continual learning on edge devices"

# Or raw text
python cli/council_cli.py --text "Note 1 content...\n---\nNote 2 content..." --seed "my research gap"
```

The CLI uses the local S2 client (rate-limited) + your personal context as the steering signal and writes a full leap note with provenance.

See `cli/council_cli.py` for details.
