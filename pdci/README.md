#  PDCI — Pragmatic Distortion and Certainty Index 

The **Pragmatic Distortion and Certainty Index (PDCI)** is a custom metric for evaluating summarization systems on how well they preserve or distort pragmatic/linguistic cues.  

It measures:
- **Loss Rate** → how much pragmatic information is dropped
- **Hallucination Rate** → how much is invented in the summary
- **Certainty Inflation Index (CII)** → how much uncertainty is turned into categorical certainty
- **Pragmatic Distortion Score (PDS)** → weighted combination of the above
- **PDCI** → overall score:  
  \[
  \text{PDCI} = \lambda \cdot \text{CII} + (1 - \lambda) \cdot \text{PDS}
  \]

---

## 📦 Installation

From the repo root:

```bash
pip install -e .
```
---
## Usage 
```bash
from pdci import analyze_pair

source = "I think it might have been Tuesday, I'm not sure, um, around 9 in the evening."
summary = "The witness stated it was Tuesday at 9 PM."

result = analyze_pair(source, summary)
print(result)
```
---
### Example Output
```bash
{
  'loss_rate': 1.0,
  'hallucination_rate': 0.0,
  'CII': 0.5,
  'PDS': 0.6,
  'PDCI': 0.55
}
```
---
## Tests
```bash
pytest -v
```
---

