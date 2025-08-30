# Computational Prescriptivism: Algorithmic Reinforcement of Linguistic Bias in Legal NLP

**Master's Thesis in Computational Linguistics**  
Goldsmiths, University of London | 2024/2025

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Thesis](https://img.shields.io/badge/Thesis-MA%20Computational%20Linguistics-purple)](thesis/thesis.pdf)

---

##  About This Project

This repository contains the complete implementation, data, and analysis for my **Master of Arts thesis in Computational Linguistics** at Goldsmiths, University of London (2024/2025). The thesis investigates how large language models systematically erase linguistic features associated with marginalized speakers when summarizing legal testimony.

**Author:** Malorie Grace Iovino  
**Degree:** MA Computational Linguistics  
**Institution:** Department of Computing, Goldsmiths, University of London  
**Supervisors:** Dr. Geri Popova, Dr. Tony Russell-Rose, Dr. Gregory Mills  
**Field Project Advisor:** Dr. Dave Lewis (Nextpoint)

##  Abstract

This Master's thesis investigates computational prescriptivism as an algorithmic enforcement of linguistic standardization in NLP-based summarization systems, with particular focus on legal deposition transcripts. Through empirical analysis of real legal deposition excerpts and curated synthetic examples across six summarization models (BART, Pegasus, T5/Flan-T5, Lead-2, TextRank, and GPT-3.5), this study demonstrates that large language models routinely erase pragmatic features that are disproportionately associated with speakers of non-standard English dialects and women.

**Key Findings:**
- 🔴 **70-85%** of disfluency markers are systematically erased
- 🟡 **30-45%** of hedges and modal expressions are removed  
- 🟢 Temporal and conditional markers show higher retention
- ⚠️ **30-40%** of uncertain statements are transformed into categorical claims

##  Research Question

> How do large language models handle linguistic markers of uncertainty, conditional language, temporal expressions, and disfluency when summarizing legal deposition transcripts, and what does this reveal about their reliability and interpretability in general NLP applications?

## 📖 Thesis Structure

The complete thesis document ([PDF](thesis/thesis.pdf)) includes:

1. **Introduction** - Motivation and research questions
2. **Literature Review** - Sociolinguistic variation, computational processing, summarization, legal NLP
3. **Methodology** - Data collection, model selection, evaluation framework
4. **Empirical Analysis** - Systematic evaluation across 6 models
5. **PDCI Framework** - Novel metric for pragmatic distortion
6. **Discussion & Implications** - Theoretical and practical contributions
7. **Conclusion** - Synthesis and future directions

## Quick Start

### Prerequisites
- Python 3.8 or higher
- CUDA-capable GPU (recommended for model inference)
- At least 16GB RAM

### Installation

```bash
# Clone the repository
git clone https://github.com/malorieiovino/Computational-Prescriptivism.git
cd Computational-Prescriptivism

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
### Running the Analysis 

```
# Run feature extraction on datasets
python code/preprocessing/feature_extraction.py --data_path data/

# Evaluate models
python scripts/run_experiments.py --models all --dataset curated

# Generate PDCI scores
python code/evaluation/pdci_analyzer.py --input results/ --output results/pdci_scores/

# Create visualizations
python scripts/generate_figures.py

```
## Repository Structure 

```
Computational-Prescriptivism/
│   └── thesis.pdf            # Complete MA thesis
├── data/                      # Datasets
│   ├── original_datasets/     # Raw deposition data
│   ├── *_curated_data.csv    # Curated synthetic examples
│   └── *_pilot_data.csv      # Pilot study data
├── notebooks/                 # Jupyter notebooks for analysis
├── figures/                   # Visualizations from thesis
│   ├── BART/                 # Model-specific figures
│   ├── Pegasus/
│   ├── GPT-3.5/
│   ├── T5-FlanT5/
│   └── Comparisons/          # Cross-model comparisons
├── code/                     # Source code implementation
└── thesis/                   # Master's Thesis Document
```
## 🔬 Methodology

### Datasets
- **Real Deposition Dataset**: 351 excerpts from 10 anonymized legal depositions
- **Curated Synthetic Dataset**: 126 unique excerpts with gold-standard summaries

### Models Evaluated

| Model Type | Models | Key Characteristics |
|------------|--------|---------------------|
| **Abstractive** | BART, Pegasus, T5, Flan-T5 | Generate new text, prone to feature erasure |
| **Extractive** | Lead-2, TextRank | Select existing sentences, high feature retention |
| **API-based** | GPT-3.5 | Tested with 4 prompting conditions |

### Linguistic Features Analyzed
1. **Hedges & Modal Expressions** (e.g., "I think", "maybe", "could")
2. **Conditional Constructions** (factual and counterfactual)
3. **Temporal Expressions** (e.g., "before", "after", "at the time")
4. **Disfluency Markers** (e.g., "um", "uh", repetitions, self-corrections)

## 📊 Key Results

### Feature Retention Rates by Model

| Model | Overall Retention | Disfluency Retention | Certainty Inflation |
|-------|------------------|---------------------|-------------------|
| BART | 91.4% | 93.3% | Low |
| Pegasus | 58.7% | 74.5% | High |
| T5 | 82.1% | 84.4% | Moderate |
| Flan-T5 | 73.6% | 84.3% | Moderate |
| Lead-2 | 93.9% | 97.2% | None |
| TextRank | 92.7% | 96.7% | None |
| GPT-3.5 (Default) | 66.2% | 74.0% | High |
| GPT-3.5 (Feature-Preserving) | 80.0% | 84.5% | Low |

### PDCI Framework Scores (Lower is Better)

| Model | PDCI Score | Interpretation |
|-------|------------|----------------|
| BART | 0.055 | Lowest distortion |
| T5 | 0.105 | Moderate distortion |
| Flan-T5 | 0.105 | Moderate distortion |
| Pegasus | 0.225 | Highest distortion |
| GPT-3.5 (Default) | 0.193 | High distortion |
| GPT-3.5 (Feature-Preserving) | 0.146 | Moderate distortion |
