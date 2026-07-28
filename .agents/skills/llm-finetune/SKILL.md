---
name: llm-finetune
description: "Use when the user says 'fine tune', 'finetune LLM', 'latih model', 'train my model', 'fine-tuning lokal', '/finetune', or 'I want to fine-tune an LLM on my data'. Guides the user step-by-step through local LLM fine-tuning on any JSONL dataset. Auto-detects platform: MLX + LoRA for Mac Apple Silicon, Unsloth + LoRA for Windows/Colab/NVIDIA. Auto-searches optimal config, runs training to target loss 0.055, then automatically tests the output and reports whether the model learned correctly. Exports to GGUF and imports to Ollama."
tags: [fine-tuning, LLM, MLX, Unsloth, LoRA, Qwen, training, GGUF, Ollama, local-AI, Apple-Silicon, Mac, Windows]
dependencies: [mlx-lm, unsloth, torch, transformers, trl, datasets, peft]
---

# LLM Fine-Tune Skill — Local Fine-Tuning dengan MLX (Mac) / Unsloth (Windows)

Skill ini membimbing siapa pun untuk melakukan **fine-tuning model LLM secara lokal** menggunakan **LoRA**, dengan dataset JSONL milik mereka sendiri — lalu **menguji hasilnya otomatis** untuk memastikan model berhasil belajar.

**Dual-platform:**
- **Mac Apple Silicon (M1/M2/M3/M4)** → MLX LoRA (native, no NVIDIA GPU needed)
- **Windows / Linux / Colab** → Unsloth + LoRA (requires NVIDIA GPU or Colab T4)

> **Berlaku untuk semua data.** Skill ini tidak terikat pada satu dataset. Setiap orang bisa menggunakan file `train.jsonl` mereka sendiri dengan topik dan bahasa apa pun.

---

## Kapan Skill Ini Digunakan

Trigger ketika pengguna menyebut:
- `"fine tune"` / `"finetune"` / `"fine-tuning"`
- `"latih model"` / `"train model"` / `"train LLM"`
- `"fine-tuning lokal"` / `"local fine-tuning"`
- `"/finetune"` / `"llm-finetune"`
- `"I want to fine-tune an LLM on my data"`
- `"saya mau melatih model dengan data saya"`
- `"how do I train Qwen"` / `"cara fine-tune Qwen"`

---

## Apa yang Dilakukan Skill Ini

1. **Detect platform** — Mac Apple Silicon → MLX path; Windows/Linux/Colab → Unsloth path
2. **Mengumpulkan informasi** — model target, path dataset, tujuan fine-tuning
3. **Mencari konfigurasi optimal secara online** — search internet untuk hyperparameter terbaik
4. **Membimbing persiapan data** — validasi format JSONL, buat file contoh jika belum ada
5. **Menjalankan fine-tuning** — MLX atau Unsloth, target **loss akhir 0.055**
6. **Menguji hasil** — jalankan inference test otomatis dan evaluasi apakah output benar
7. **Export GGUF + import ke Ollama** — fuse, convert, dan deploy

---

## Stage 0 — Detect Platform

### Step 0.1 — Deteksi OS dan hardware

```bash
# Deteksi platform
uname -s  # Darwin = Mac, Linux = Linux/WSL

# Cek Apple Silicon
sysctl -n machdep.cpu.brand_string 2>/dev/null || echo "Not Mac"
# Jika mengandung "Apple M" → MLX path
# Jika tidak → Unsloth path

# Cek NVIDIA GPU (untuk Windows/Linux)
nvidia-smi 2>/dev/null || echo "No NVIDIA GPU"
```

**Routing:**
| Platform | Framework | Path |
|---|---|---|
| Mac Apple Silicon (M1/M2/M3/M4) | MLX LoRA | **Path A (MLX)** |
| Windows + NVIDIA GPU | Unsloth + LoRA | **Path B (Unsloth)** |
| Linux + NVIDIA GPU | Unsloth + LoRA | **Path B (Unsloth)** |
| Google Colab (T4/A100) | Unsloth + LoRA | **Path B (Unsloth)** |
| Mac Intel / no GPU | Google Colab | **Path B (Colab)** |

Simpan sebagai `PLATFORM`: `"MLX"` atau `"UNSLOTH"`.

---

## Stage 1 — Kumpulkan Informasi

### Step 1.1 — Tanya model yang ingin digunakan

> *"Model LLM apa yang ingin kamu fine-tune? (Default: `Qwen2.5-1.5B` — model ringan yang cepat dan hemat memori). Ketik nama model atau tekan Enter untuk default."*

Simpan sebagai `MODEL_NAME`. Default: `Qwen2.5-1.5B`.

| Model | Mac MLX VRAM | Unsloth VRAM | Platform |
|---|---|---|---|
| `Qwen2.5-1.5B` | ~2GB | ~4GB | Mac / Colab / Windows |
| `Qwen2.5-3B` | ~4GB | ~6GB | Mac / Colab / Windows |
| `Qwen2.5-7B` | ~8GB | ~10GB | Mac 16GB+ / Colab A100 |
| `Llama-3.2-1B` | ~2GB | ~4GB | Mac / Colab |
| `Llama-3.2-3B` | ~4GB | ~6GB | Mac / Colab |

### Step 1.2 — Tanya lokasi dataset

> *"Di mana file `train.jsonl` kamu? Paste path lengkapnya, atau ketik 'buat contoh' jika belum punya data."*

Simpan sebagai `DATASET_PATH`.

**Format JSONL yang diterima (gaya Alpaca):**
```json
{"instruction": "Pertanyaan atau instruksi", "input": "", "output": "Jawaban yang benar"}
```

**Juga mendukung format Chat (WAJIB untuk MLX):**
```json
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
```

> ⚠️ **Penting untuk MLX (Mac):** MLX memerlukan format Chat (`messages`), bukan format Alpaca (`instruction`/`output`). Jika dataset masih format Alpaca, konversi ke format Chat sebelum training (lihat Step 3.2).

### Step 1.3 — Tanya tujuan fine-tuning

> *"Apa tujuan fine-tuning ini? (Contoh: agar model hafal data tertentu, agar model menjawab dengan gaya tertentu, agar model jadi expert di domain X)"*

Simpan sebagai `OBJECTIVE`. Ini akan mempengaruhi konfigurasi training.

### Step 1.4 — Tanya nama model di Ollama

> *"Apa nama model yang kamu inginkan di Ollama? (Contoh: `model-saya`, `ai-lokal-saya`)"*

Simpan sebagai `OLLAMA_MODEL_NAME`.

---

## Stage 2 — Cari Konfigurasi Optimal (Online Search)

### Step 2.1 — Search konfigurasi untuk model yang dipilih

**WAJIB: Search internet untuk konfigurasi terbaru sebelum memulai training.**

Gunakan web search dengan query berikut (sesuaikan `MODEL_NAME` dan `FRAMEWORK`):

```
Search queries (jalankan semua, gabungkan hasilnya):
1. "{FRAMEWORK} {MODEL_NAME} fine-tuning optimal hyperparameters LoRA 2024 2025"
2. "Qwen2.5 fine-tuning anti-hallucination config epochs learning rate"
3. "{FRAMEWORK} {MODEL_NAME} LoRA r rank alpha best practices"
4. "{MODEL_NAME} SFTTrainer configuration reduce hallucination"
5. "site:github.com {FRAMEWORK} {MODEL_NAME} notebook example"
```

Ganti `{FRAMEWORK}` dengan `MLX` (Mac) atau `Unsloth` (Windows/Colab).

### Step 2.2 — Konfigurasi baseline berdasarkan platform

#### Path A: MLX (Mac Apple Silicon)

**Referensi:** [Unsloth docs](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide) — "loss 0.5-1.0 umum, 0 = overfit, 1-3 epochs recommended"

```yaml
# lora_config.yaml (MLX)
model: mlx-community/Qwen2.5-1.5B-Instruct-4bit
train: true
data: data
fine_tune_type: lora

# TARGET LOSS: 0.055
# Iterasi disesuaikan dengan ukuran dataset untuk mencapai loss ~0.055
# Gunakan tabel di Step 2.3 untuk menentukan jumlah iterasi

iters: {diisi berdasarkan tabel}
batch_size: 2
grad_accumulation_steps: 4
learning_rate: 1e-4
num_layers: 16
mask_prompt: true

adapter_path: adapters
steps_per_report: 10
steps_per_eval: 50
```

**Aturan iterasi MLX:** MLX menggunakan key `iters` (BUKAN `num_iters`). Key `num_iters` akan diabaikan dan default ke 1000.

#### Path B: Unsloth (Windows/Linux/Colab)

```python
# Konfigurasi Unsloth
model_name = "unsloth/Qwen2.5-1.5B-bnb-4bit"
max_seq_length = 2048
load_in_4bit = True

# LoRA config (anti-hallucination tuned)
r = 16
lora_alpha = 16
lora_dropout = 0
target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                  "gate_proj", "up_proj", "down_proj"]
use_gradient_checkpointing = "unsloth"

# Training config — TARGET LOSS: 0.055
num_train_epochs = {diisi berdasarkan tabel}
learning_rate = 2e-4
per_device_train_batch_size = 2
gradient_accumulation_steps = 4
lr_scheduler_type = "constant"  # Untuk dataset kecil
weight_decay = 0.0
```

### Step 2.3 — Tabel iterasi/epochs berdasarkan ukuran dataset

**Target loss akhir: 0.055** (cukup untuk hafal fakta, tidak overfit, pre-training terjaga)

| Jumlah baris data | MLX `iters` | Unsloth `num_train_epochs` | Estimasi loss akhir |
|---|---|---|---|
| 1-10 baris | 50-100 | 200-500 | ~0.01-0.05 |
| 11-30 baris | 100-150 | 100-200 | ~0.02-0.05 |
| 31-50 baris | 150-200 | 50-100 | ~0.03-0.06 |
| 51-100 baris | 200-300 | 20-50 | ~0.04-0.07 |
| 101-200 baris | 350-450 | 10-20 | ~0.05-0.08 |
| 201-500 baris | 500-800 | 5-10 | ~0.05-0.08 |
| >500 baris | 800-1500 | 1-5 | ~0.05-0.10 |

**Cara mencapai loss 0.055:**
1. Hitung jumlah baris dataset: `wc -l train.jsonl`
2. Pilih iterasi/epochs dari tabel di atas
3. Jalankan training
4. Jika loss akhir > 0.060 → naikkan iterasi/epochs 20%
5. Jika loss akhir < 0.030 → turunkan iterasi/epochs 20% (terlalu overfit)
6. Ulangi hingga loss mendekati 0.055

### Step 2.4 — Aturan kualitas dataset (anti-halusinasi)

**WAJIB untuk mencegah halusinasi dan kontaminasi:**

1. **Rasio data:** 50-60% data utama (topik yang ingin diajarkan) + 40-50% anchor data (pengetahuan umum untuk melindungi pre-training)
2. **Anchor data:** Tambahkan pertanyaan umum (ibukota, matematika, sains, teknologi) dengan jawaban yang TIDAK mengandung kata-kata dari data utama
3. **Disambiguasi:** Jika ada angka yang bisa tertukar (misal "7 tahun" vs "17" dari tanggal lahir), tambahkan Q&A eksplisit: "Apakah X punya 17 tahun?" → "Tidak, X punya 7 tahun, bukan 17"
4. **Negative examples:** "Apakah Bill Gates cybersecurity expert?" → "Tidak, Bill Gates pendiri Microsoft, bukan cybersecurity expert"
5. **Minimal 30 baris** data utama + 20 baris anchor untuk hasil yang baik
6. **Bilingual:** Jika ingin model menjawab dalam ID dan EN, buat kedua versi untuk setiap Q&A

---

## Stage 3 — Persiapan Dataset

### Step 3.1 — Validasi format JSONL

Jalankan validasi ini:

```python
import json

errors = []
with open('train.jsonl', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            # Cek format Alpaca
            if 'instruction' in data:
                required = ['instruction', 'output']
                missing = [k for k in required if k not in data]
                if missing:
                    errors.append(f"Baris {i}: field '{missing}' tidak ada")
                if 'input' not in data:
                    data['input'] = ''  # input opsional, default kosong
            # Cek format Chat
            elif 'messages' in data:
                if not isinstance(data['messages'], list):
                    errors.append(f"Baris {i}: 'messages' harus berupa list")
            else:
                errors.append(f"Baris {i}: tidak ada field 'instruction' atau 'messages'")
        except json.JSONDecodeError as e:
            errors.append(f"Baris {i}: JSON tidak valid — {e}")

if errors:
    print("❌ Ditemukan error:")
    for e in errors:
        print(f"  {e}")
else:
    print(f"✅ Dataset valid! {i} baris siap digunakan.")
```

### Step 3.2 — Konversi Alpaca ke Chat format (untuk MLX)

Jika `PLATFORM == "MLX"` dan dataset masih format Alpaca, konversi:

```python
import json

SYS = "Kamu adalah asisten AI yang membantu."

with open('train.jsonl', 'r', encoding='utf-8') as f:
    alpaca_data = [json.loads(line) for line in f if line.strip()]

with open('train.jsonl', 'w', encoding='utf-8') as f:
    for entry in alpaca_data:
        if 'instruction' in entry:
            chat_entry = {
                "messages": [
                    {"role": "system", "content": SYS},
                    {"role": "user", "content": entry['instruction']},
                    {"role": "assistant", "content": entry['output']}
                ]
            }
            f.write(json.dumps(chat_entry, ensure_ascii=False) + '\n')
        else:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

print(f"Konversi selesai: {len(alpaca_data)} baris -> format Chat")
```

### Step 3.3 — Jika pengguna belum punya data

Jika pengguna meminta contoh, tanya topik dan buat minimal 30 baris data utama + 20 baris anchor.

---

## Stage 4 — Setup Environment & Training

### Path A: MLX (Mac Apple Silicon)

#### Step 4A.1 — Setup virtual environment

```bash
cd <folder dengan train.jsonl>
python3.13 -m venv mlx_env
source mlx_env/bin/activate
pip install --upgrade pip
pip install "mlx-lm[train]"
```

#### Step 4A.2 — Buat folder data dan config

```bash
mkdir -p data
# Pastikan train.jsonl ada di folder data/
```

Buat file `lora_config.yaml`:

```yaml
model: mlx-community/Qwen2.5-1.5B-Instruct-4bit
train: true
data: data
fine_tune_type: lora
iters: {dari tabel Step 2.3}
batch_size: 2
grad_accumulation_steps: 4
learning_rate: 1e-4
num_layers: 16
mask_prompt: true
adapter_path: adapters
steps_per_report: 10
steps_per_eval: 50
```

#### Step 4A.3 — Jalankan training

```bash
mlx_env/bin/python -m mlx_lm.lora --config lora_config.yaml
```

**Monitor loss:** Lihat output training. Loss harus turun dari ~1.0 ke ~0.055.

**Jika loss > 0.060 setelah training selesai:**
1. Naikkan `iters` di lora_config.yaml sebanyak 20%
2. Hapus folder `adapters/`
3. Jalankan ulang training

**Jika loss < 0.030 (overfit):**
1. Turunkan `iters` sebanyak 20%
2. Hapus folder `adapters/`
3. Jalankan ulang training

#### Step 4A.4 — Fuse adapter ke model BF16

```bash
# WAJIB: gunakan model BF16, BUKAN 4bit (4bit tidak bisa convert ke GGUF)
mlx_env/bin/python -m mlx_lm.fuse \
    --model mlx-community/Qwen2.5-1.5B-Instruct-bf16 \
    --adapter-path adapters \
    --save-path fused_model
```

#### Step 4A.5 — Convert ke GGUF

```bash
# Clone llama.cpp (sekali saja)
if [ ! -d /tmp/llama.cpp ]; then
    git clone --depth 1 https://github.com/ggml-org/llama.cpp.git /tmp/llama.cpp
fi
mlx_env/bin/pip install -e /tmp/llama.cpp

# Convert fused model ke GGUF
mlx_env/bin/python /tmp/llama.cpp/convert_hf_to_gguf.py fused_model --outtype f16 --outfile fused_model/ggml-model-f16.gguf
```

#### Step 4A.6 — Buat Modelfile dan import ke Ollama

```bash
cat > Modelfile << 'EOF'
FROM ./fused_model/ggml-model-f16.gguf

TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
{{ .Response }}<|im_end|>
"""

PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
PARAMETER temperature 0.7
PARAMETER top_p 0.85
PARAMETER top_k 30
PARAMETER repeat_penalty 1.1
EOF

ollama create "{OLLAMA_MODEL_NAME}" -f Modelfile
```

### Path B: Unsloth (Windows/Linux/Colab)

#### Step 4B.1 — Generate notebook Colab atau script lokal

Berdasarkan `ENV`:
- **Colab** → generate file `finetune_notebook.ipynb` (Jupyter Notebook)
- **Lokal** → generate file `finetune_local.py` (Python script)

#### Step 4B.2 — Install dependencies

```bash
# Colab
!pip install -U "torch==2.10.0" --index-url https://download.pytorch.org/whl/cu128
!pip install "numpy<2.1" "datasets>=3.4.1,<4.4.0" "trl>=0.18.2,<=0.24.0"
!pip install --no-deps unsloth_zoo bitsandbytes accelerate "xformers==0.0.34" peft unsloth triton
!pip install --upgrade --force-reinstall transformers==4.56.2
```

#### Step 4B.3 — Load model dan jalankan training

```python
from unsloth import FastLanguageModel
import torch

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen2.5-1.5B-bnb-4bit",
    max_seq_length = 2048,
    load_in_4bit = True,
)

model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    lora_alpha = 16,
    lora_dropout = 0,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    use_gradient_checkpointing = "unsloth",
)

from trl import SFTTrainer
from transformers import TrainingArguments

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = 2048,
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        num_train_epochs = {dari tabel Step 2.3},
        learning_rate = 2e-4,
        lr_scheduler_type = "constant",
        weight_decay = 0.0,
        logging_steps = 10,
        fp16 = not torch.cuda.is_bf16_supported(),
        bf16 = torch.cuda.is_bf16_supported(),
        output_dir = "outputs",
    ),
)

trainer_stats = trainer.train()
```

**Monitor loss:** Loss harus turun dari ~1.0 ke ~0.055. Jika loss > 0.060, tambah epochs. Jika < 0.030, kurangi epochs.

#### Step 4B.4 — Export ke GGUF

```python
model.save_pretrained_gguf("model", tokenizer=tokenizer, quantization_method="q4_k_m")
```

#### Step 4B.5 — Import ke Ollama

```bash
cat > Modelfile << 'EOF'
FROM ./model-unsloth.Q4_K_M.gguf
TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
{{ .Response }}<|im_end|>
"""
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
EOF

ollama create "{OLLAMA_MODEL_NAME}" -f Modelfile
```

---

## Stage 5 — Jalankan Training & Monitor

### Step 5.1 — Instruksi menjalankan

**Untuk MLX (Mac):**
> *"Jalankan: `mlx_env/bin/python -m mlx_lm.lora --config lora_config.yaml`*
>
> *Training akan selesai dalam estimasi X menit."*

**Untuk Unsloth (Colab):**
> *"Buka Google Colab → Upload notebook dan `train.jsonl` → Runtime → Change runtime type → T4 GPU → Runtime → Run all"*

**Estimasi waktu training:**
| Platform | Data x Iterasi | Estimasi Waktu |
|---|---|---|
| Mac M4 (MLX) | 100 x 300 | ~2 menit |
| Mac M4 (MLX) | 200 x 410 | ~4 menit |
| Colab T4 (Unsloth) | 100 x 50 epochs | ~15 menit |
| Colab T4 (Unsloth) | 500 x 5 epochs | ~20 menit |

### Step 5.2 — Tanda training sukses

Training berhasil jika:
- Loss turun dari awal hingga akhir
- **Loss akhir mendekati 0.055** (range acceptable: 0.030-0.060)
- Tidak ada error/exception di tengah training
- File model/adapters tersimpan

**Target loss: 0.055**

| Loss akhir | Status | Tindakan |
|---|---|---|
| 0.030-0.060 | BERHASIL | Lanjut ke test |
| > 0.060 | Kurang hafal | Naikkan iterasi/epochs 20%, retrain |
| < 0.030 | Overfit | Turunkan iterasi/epochs 20%, retrain |
| 0.000 | Parah overfit | Setengah iterasi, retrain |

**Tanda WARNING:**
- Loss tidak turun sama sekali → coba naikkan `learning_rate`
- Loss turun lalu naik lagi (diverge) → turunkan `learning_rate`, tambah `weight_decay`
- CUDA out of memory → kurangi `per_device_train_batch_size` ke 1

---

## Stage 6 — Test Otomatis Hasil Fine-Tuning

### Step 6.1 — Buat test cases dari dataset

**WAJIB dijalankan setelah training selesai dan model diimport ke Ollama.** Test ini memeriksa apakah model berhasil belajar.

```python
import json
import subprocess
import re
import random

# Baca dataset untuk ambil test cases
with open('train.jsonl', 'r', encoding='utf-8') as f:
    all_data = [json.loads(line) for line in f if line.strip()]

# Ambil sample: 20% dari data atau minimum 5, maksimum 15
n_test = min(15, max(5, len(all_data) // 5))
test_samples = random.sample(all_data, n_test)

print(f"Menjalankan {n_test} test case dari {len(all_data)} total data...\n")
```

### Step 6.2 — Jalankan inference via Ollama (dua platform)

```python
OLLAMA_MODEL = "{OLLAMA_MODEL_NAME}"  # Ganti dengan nama model Ollama

results = []

for i, sample in enumerate(test_samples, 1):
    # Extract question and expected answer
    if 'messages' in sample:
        # Chat format
        question = ""
        expected = ""
        for msg in sample['messages']:
            if msg['role'] == 'user':
                question = msg['content']
            elif msg['role'] == 'assistant':
                expected = msg['content']
    else:
        # Alpaca format
        question = sample.get('instruction', '')
        expected = sample.get('output', '')

    # Run via Ollama
    result = subprocess.run(
        ["ollama", "run", OLLAMA_MODEL, question],
        capture_output=True, text=True, timeout=60
    )
    # Clean ANSI codes from output
    model_answer = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', result.stdout).replace('\r', '').strip()

    results.append({
        'question': question,
        'expected': expected,
        'got': model_answer,
    })
```

### Step 6.3 — Evaluasi dan scoring

```python
def evaluate_answer(expected, got):
    """
    Evaluasi jawaban model dengan 3 kriteria:
    1. Exact match (persis sama)
    2. Key terms match (kata-kata penting ada di jawaban)
    3. Partial match (minimal 50% konten sama)
    """
    expected_lower = expected.lower().strip()
    got_lower = got.lower().strip()

    # 1. Exact match
    if expected_lower == got_lower:
        return 'EXACT', 1.0

    # 2. Key terms: ambil kata-kata penting dari expected (>4 karakter)
    expected_words = set(w for w in expected_lower.split() if len(w) > 4)
    got_words = set(w for w in got_lower.split() if len(w) > 4)

    if not expected_words:
        return 'PARTIAL', 0.5

    overlap = len(expected_words & got_words) / len(expected_words)

    if overlap >= 0.8:
        return 'GOOD', overlap
    elif overlap >= 0.5:
        return 'PARTIAL', overlap
    elif overlap > 0:
        return 'POOR', overlap
    else:
        return 'WRONG', 0.0

# Jalankan evaluasi
print("=" * 60)
print("HASIL TEST FINE-TUNING")
print("=" * 60)

total_score = 0
for i, r in enumerate(results, 1):
    grade, score = evaluate_answer(r['expected'], r['got'])
    total_score += score

    emoji = {'EXACT': 'PASS', 'GOOD': 'PASS', 'PARTIAL': 'PARTIAL', 'POOR': 'FAIL', 'WRONG': 'FAIL'}[grade]

    print(f"\nTest {i}/{len(results)} - [{emoji}] {grade} ({score:.0%})")
    print(f"  Q: {r['question'][:80]}")
    print(f"  Expected: {r['expected'][:100]}")
    print(f"  Got: {r['got'][:100]}")

# Hitung skor keseluruhan
avg_score = total_score / len(results)
print("\n" + "=" * 60)
print(f"SKOR KESELURUHAN: {avg_score:.0%} ({total_score:.1f}/{len(results)})")

if avg_score >= 0.8:
    print("BERHASIL - Model berhasil belajar dari data!")
    print("  Lanjut ke export GGUF untuk Ollama (jika belum)")
elif avg_score >= 0.5:
    print("CUKUP - Model sebagian belajar, tapi belum sempurna.")
    print("  Coba: tambah epochs, naikkan learning_rate, atau tambah data training")
else:
    print("GAGAL - Model belum belajar dengan baik.")
    print("  1. Tambah num_train_epochs (2x lipat)")
    print("  2. Ganti lr_scheduler_type ke 'constant'")
    print("  3. Matikan weight_decay (set ke 0.0)")
    print("  4. Tambahkan lebih banyak data training (variasi pertanyaan)")
print("=" * 60)
```

### Step 6.4 — Laporan hasil ke pengguna

> *"Hasil Fine-Tuning:*
> *- Skor: [X]% dari [N] test case*
> *- Status: [BERHASIL / CUKUP / GAGAL]*
> *- Loss akhir: [X.XX] (target: 0.055)*
> *- Platform: [MLX / Unsloth]*
>
> *[Jika BERHASIL]: Model siap dipakai di Ollama! Jalankan: `ollama run {OLLAMA_MODEL_NAME}`*
> *[Jika CUKUP/GAGAL]: Saya rekomendasikan: [rekomendasi spesifik]"*

---

## Stage 7 — Export ke GGUF (untuk Ollama)

> **Catatan:** Jika menggunakan Path A (MLX), export GGUF sudah dilakukan di Step 4A.5. Jika menggunakan Path B (Unsloth/Colab), ikuti langkah di bawah.

### Step 7.1 — Export GGUF (Unsloth/Colab only)

```python
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"
os.environ["HF_HUB_DISABLE_XET"] = "1"

# Export ke GGUF format q4_k_m (optimal untuk lokal)
model.save_pretrained_gguf("model", tokenizer=tokenizer, quantization_method="q4_k_m")
print("Model berhasil di-export ke GGUF!")
print("File ada di folder 'model/' - cari file *.gguf")
```

### Step 7.2 — Import ke Ollama

Setelah file GGUF siap (baik dari MLX maupun Unsloth):

```bash
# Buat Modelfile dengan chat template Qwen2.5
cat > Modelfile << 'EOF'
FROM ./fused_model/ggml-model-f16.gguf

TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
{{ .Response }}<|im_end|>
"""

PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
PARAMETER temperature 0.7
PARAMETER top_p 0.85
PARAMETER top_k 30
PARAMETER repeat_penalty 1.1
EOF

# Buat model Ollama
ollama create "{OLLAMA_MODEL_NAME}" -f Modelfile

# Jalankan
ollama run "{OLLAMA_MODEL_NAME}"
```

---

## Stage 8 — Troubleshooting

### Loss tidak mencapai 0.055

| Gejala | Penyebab | Solusi |
|---|---|---|
| Loss > 0.060 | Iterasi/epochs kurang | Naikkan iterasi/epochs 20%, retrain |
| Loss < 0.030 | Overfit | Turunkan iterasi/epochs 20%, retrain |
| Loss tidak turun | Learning rate terlalu kecil | Naikkan learning_rate ke 2e-4 atau 5e-4 |
| Loss naik-turun ekstrem | Data terlalu sedikit | Tambah minimal 50 baris data |
| Loss = 0.000 | Parah overfit | Setengah iterasi, tambah anchor data |

### MLX (Mac) — `num_iters` diabaikan

**Masalah:** Config `num_iters: 100` tidak berdampak, training jalan 1000 iterasi.
**Solusi:** Gunakan key `iters` (BUKAN `num_iters`). MLX 0.31+ menggunakan `iters`.

### MLX (Mac) — Fuse gagal: "incomplete snapshot"

**Masalah:** Model BF16 belum ter-download sempurna.
**Solusi:**
```bash
mlx_env/bin/python -c "from huggingface_hub import snapshot_download; snapshot_download('mlx-community/Qwen2.5-1.5B-Instruct-bf16')"
```
Lalu jalankan ulang fuse.

### MLX (Mac) — GGUF convert error: tokenizer

**Masalah:** `transformers` version conflict antara mlx-lm dan llama.cpp.
**Solusi:**
```bash
mlx_env/bin/pip install "transformers>=4.46.0" --upgrade
```
Lalu jalankan ulang convert.

### Unsloth (Windows/Colab) — CUDA out of memory

```python
per_device_train_batch_size = 1
gradient_accumulation_steps = 8  # Naikkan untuk kompensasi
max_seq_length = 1024  # Kurangi panjang sequence
```

### Model masih halusinasi (jawab sembarangan)

1. Tambah lebih banyak variasi pertanyaan di `train.jsonl` (minimal 50+ baris)
2. Pastikan ada 40-50% anchor data (pengetahuan umum)
3. Tambahkan disambiguasi: "Apakah X punya 17 tahun?" → "Tidak, 7 tahun"
4. Tambahkan negative examples: "Apakah Bill Gates cybersecurity?" → "Tidak"
5. Pastikan loss akhir di range 0.030-0.060

### Dataset format error

```bash
python3 -c "
import json
with open('train.jsonl') as f:
    for i, line in enumerate(f, 1):
        try: json.loads(line)
        except: print(f'Error baris {i}: {line[:50]}')
"
```

---

## Referensi

- [MLX LoRA documentation](https://ml-explore.github.io/mlx-lm/)
- [MLX GitHub](https://github.com/ml-explore/mlx-examples)
- [Unsloth GitHub](https://github.com/unslothai/unsloth)
- [Unsloth dokumentasi](https://docs.unsloth.ai)
- [Unsloth fine-tuning guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide) — "loss 0.5-1.0 umum, 0 = overfit, 1-3 epochs recommended"
- [llama.cpp GGUF converter](https://github.com/ggml-org/llama.cpp)
- [Dataset format Alpaca](https://github.com/tatsu-lab/stanford_alpaca)
- [Notebook training di repo ini](../../curriculum/day2/ai_train/unsloth_train_qwen.ipynb)
- [Contoh train.jsonl](../../curriculum/day2/ai_train/train.jsonl)
- [Skill Unsloth (referensi cepat)](../unsloth/SKILL.md)
- [Guide MLX fine-tuning (Alessandro)](../../participants/Alessandro%20Rumampuk/ai_train/GUIDE_MLX_FINE_TUNING.md)

---

## Catatan Penting

> **Skill ini berlaku untuk semua dataset.** Apapun topik `train.jsonl` kamu — profil orang, FAQ produk, pengetahuan domain, gaya bahasa — prosesnya sama. Yang berbeda hanya:
> 1. Jumlah baris data → menentukan `iters` (MLX) atau `num_train_epochs` (Unsloth)
> 2. Tujuan fine-tuning → menentukan `lr_scheduler_type` dan `weight_decay`
> 3. Ukuran model → menentukan kebutuhan VRAM
> 4. Platform → MLX (Mac) atau Unsloth (Windows/Colab)

> **Target loss: 0.055.** Loss ini adalah sweet spot: cukup untuk hafal fakta spesifik, tapi tidak overfit sehingga pre-training tetap terjaga. Jika loss > 0.060, model belum hafal. Jika loss < 0.030, model overfit dan akan halusinasi.

> **Commander-Executor:** Kamu adalah komandan — kamu yang menentukan data dan tujuan. AI adalah eksekutor — AI yang menghitung konfigurasi, generate kode, dan mengevaluasi hasilnya. AI tidak mengarang data atau mengubah data training kamu.
