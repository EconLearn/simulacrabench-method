# SimulacraBench (NeurIPS 2026 competition): team "Jude Wallis" method code

This repository holds the source code for our SimulacraBench Test (Final) submission, `final_P1kg17`. The method is described in our 4-page write-up on OpenReview (NeurIPS.cc/2026/Competition/SimulacraBench).

**Status:** the source (`main.py`, `requirements.txt`) will be published here after the Test phase closes (20 November 2026, 12:00 UTC). Until then this repository holds the licences and the weight references only.

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

- Submitted zip: `simulacra_final_P1kg17_guard.zip` (md5 `8f3ded81580b7ae6f128d15b42d5bfdd`).
- `main.py` md5: `020d4658a562f6ddff462496101102ae`.
