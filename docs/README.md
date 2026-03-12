# Vscode Toolkit Documentation

## Getting Started

See the main README for installation instructions.

## API Reference

### Core Classes

- `Toolkit` - Main class for file processing
- `scan_files()` - Scan directory for files
- `export_data()` - Export results to JSON

## Examples

```python
from src import Toolkit

toolkit = Toolkit(verbose=True)
results = toolkit.scan("/path/to/files")
toolkit.export("output.json")
```
