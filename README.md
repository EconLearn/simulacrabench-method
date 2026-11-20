# SimulacraBench (NeurIPS 2026 competition): team "Jude Wallis" method code

This repository holds the source code for our SimulacraBench Test (Final) submission, `P1kg38xwrcknfdt3bck6n2`. The method is described in our 4-page write-up on OpenReview (NeurIPS.cc/2026/Competition/SimulacraBench).

**Status:** `main.py` and `requirements.txt` are the exact files of the uploaded zip (identity below). Reproduce: put the two weight files next to `main.py`, zip the folder, and run the official repository's `tools/check_submission_zip.py` and `score.py`.

## Licence

- **Our code:** PolyForm Noncommercial License 1.0.0 (`LICENSE`). Required Notice: Copyright 2026 Jude Wallis.
- **Third-party model weights:** these are NOT redistributed here, and they keep their own licences:
  - TabPFN-3.5-fast: TABPFN-3.5 License v1.0, non-commercial (`LICENSES/TABPFN-3.5-LICENSE.txt`, `NOTICE`).
  - TabPFN-v2 classifier checkpoint: Prior Labs License 1.1 (`LICENSES/TabPFN-v2-clf-LICENSE.txt`).

## Pretrained weights (download separately; place next to `main.py`)

| File | Public source @ fixed commit | sha256 |
|---|---|---|
| `tabpfn-v3.5-fast-20260909.safetensors` (334,181,708 B) | https://huggingface.co/Prior-Labs/tabpfn_3_5 @ `06bf2ba35c80a92a3b9abb436b99cf49e7a0365e` | `14e0b81285bca7a6d1ef121169f27f651f76dff49cad6c0b8779d5c836018550` |
| `tabpfn-v2-classifier-finetuned-zk73skhh.ckpt` (29,009,539 B) | https://huggingface.co/Prior-Labs/TabPFN-v2-clf @ `275f19d2add9c2c0de38f9ebaded3856599fa2e7` | `cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49` |

## Submission identity

- Submitted zip: `simulacra_final_P1kg38xwrcknfdt3bck6n2_c1L.zip` (md5 `e07351cdaeb622a676c31e0769748495`, sha256 `8f5e9c125738e65a54dc0947139e1bc76e57e897c2a0bf29976ae39d5712300e`).
- `main.py` md5: `6a96416842dc7b9dd9a033ecaf91fd26`.
