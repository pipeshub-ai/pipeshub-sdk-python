# ModelType

Type of AI model

## Example Usage

```python
from pipeshub_sdk.models import ModelType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ModelType = "llm"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"llm"`
- `"embedding"`
- `"ocr"`
- `"slm"`
- `"reasoning"`
- `"multiModal"`
- `"imageGeneration"`
- `"tts"`
- `"stt"`
