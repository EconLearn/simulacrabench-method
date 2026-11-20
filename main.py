"""SimulacraBench final_P1kg38xwrcknfdt3bck6s_c1L (SB2 bake of sb2/p35x/main_P1kg38xwrcknfdt3bck6b_lab.py d57db853; baked: SIM_TWEV_SB=.2 SIM_TAIL_OFF=1).
Was: SimulacraBench P1kg38xwrcknfdt3bc = dt3b (sb2/p35x/main_P1kg38xwrcknfdt3b_lab.py b0bce532) + CH4m (SBN; hunks from main_P1kg38xwrcknfdt_ch_lab.py 5a106984 v dt main.py 1ea7babf; 5/7 hunks clean, header + call line by hand). SB2 19 Nov 05:20Z.
Was: SimulacraBench P1kg38xwrcknfdt3_lab = v2 (xwrcknfdt2) + cx_stkrisk tt_cleanup (TT pool stopped on every predict exit) + SBQ R4b (CUDA / OOM re-raise; SIM_RERAISE_CUDA=0 = off). SB2 19 Nov.
Was: SimulacraBench P1kg38xwrcknfdt2_lab = xwrcknfdt (1ea7babf) + cx_ADV native-failure guard (narrowed: fail:restore-protection stays usable) + SBQ R6 writable-dir fallback + SBV kinship budget guard (hand-merged on the cx_DEADL tail). All byte-identical on a healthy host. SB2 19 Nov.
Was: SimulacraBench final_P1kg38xwrcknfdt_c1L (SB2 bake of sb2/p35x/main_P1kg38xwrcknfdt_src.py 68155ddb; baked: none).
Was: SimulacraBench final_P1kg38xwrcknf_c1L (SB2 bake of crp_drift/builds/main_P1kg38xwrck_lab.py 5f560f0f; baked: SIM_AVL=0).
Was: SimulacraBench P1kg38xwrck_lab = xwrf (f31427d4) + SBV cpat3 + residual kinship (crp_drift, SIM_TWEV_CPAT 3 / SIM_TWEV_KIN 1; 0 / 0 = xwrf exactly).
Was: SimulacraBench P1kg38xwrf_lab = P35xwf (xwg + VSC Fix 1/2, ce7073c4) + SBT2 C8Esoft (crp_twinx/builds/main_P1kg38xwr_lab.py a700add3 diff v xwg 06d0f2a4; 6 code hunks, 0 fuzz; SIM_TWEV_RECIP 1 / SIM_TWEV_KDW .25; 0 / 0 = xwf). SB2 18 Nov; PREPARED, not zipped until SBT2 PASS.
Was: SimulacraBench P1kg38xwf_lab = P35xwg + VSC_WALL_AUDIT Fix 1 (predictive linkage world check) + Fix 2 (whole-run belt: donor loop stops at T0+LIMIT+150, chain skipped after T0+LIMIT+170). Main 15:46Z. SB2 18 Nov.
Was: SimulacraBench P1kg38xwg_lab = P35xsg (P35xs + erg, aa4c9394) + SBU 4 one-to-one exclusion in the twin stage, xw version (crp_unhcr2/builds/xw_vs_P35xs.patch; code hunks verified identical; SIM_TWEV_XCL 1, 0 = P35xsg). SB2 18 Nov.
Was: SimulacraBench P1kg38xsg_lab = P35xs + erg graceful linkage cut (SB2 18 Nov; REPORT_SB2 erg rounds 1-3).
Was: SimulacraBench P1kg38xs_lab = P35x + SF1 fix (twev bounded by the absolute clock T0+LIMIT+AVL_OVER+TWEV_RES; sb2/review/REVIEW_P35x.md). Was: P1kg38x_lab = P35x (red team update 11, REDTEAM_MAIN_1118.md l.38; SB2 18 Nov): P1kg35e_lab (a8a48b61: P35 + fix A + C1, no raise) + E-fixed twev stage (main_P1kg38twevb_lab.py d858a530 diff v 31821260, applied with patch, 0 fuzz) + AVL_TMAX 150 -> 240.
Was: SimulacraBench P1kg35e_lab (SB2, 18 Nov) = P1kg35d_lab 3e78b01b with the import-time raise on cbfix fail:* removed (SBZ 47; log only).
Was: SimulacraBench P1kg35d_lab (SB2, 18 Nov) = final_P1kg35_capsJ48h 31821260 + fix A (linkage stage budget min(AVL_TMAX, T0 + LIMIT + AVL_OVER - start), skip under AVL_MIN; SIM_AVL_OVER 100, SIM_AVL_MIN 30) + CatBoost race fix C1 (cx_sb2cb cb_fix_c1.py b9eb601a; SIM_CBFIX, default on).
Was: SimulacraBench final_P1kg35_capsJ48h (SB2 build 17 Nov of SBZ lab 1d6de98b) = P1kg28avl chunked agreement arrays (SBZ 32) + linkage caps lifted (SIM_AVL_MAXP 9e6, SIM_AVL_MAXC 9e8; SBZ 24-29) + J 48 agreement items (SIM_AVL_MAXJ 48; SBZ 31/33) + home-safe env lines (SBY 26/27, b8edc76a).
Was: SimulacraBench P1kg28avl26_lab (SBX H2, 16 Nov) = final_P1kg26 + AVL: answer-verified learned linkage as one more key of the donor back-off menu (SIM_AVL; 0 = final_P1kg26).
Was (final_P1kg26): SimulacraBench final_P1kg26 (SB-PUSH4 16 Nov) = final_P1kg25 + C1 1:1 linkage exclusion in TT's twin codes (SIM_TT_CLAIM; 0 = final_P1kg25).
Was: SimulacraBench final_P1kg25 (SB-PUSH3 15 Nov) = final_P1kg24 + T1 twin-vector TREES (TT): per-item one-hot CatBoost on GIVEN + the twin's whole answer vector, fitted on 2 own background threads, per-item per-kind 2-SE OOF-gated geometric pool on twin rows after TM. SIM_TT=0 = final_P1kg24.
Was: SimulacraBench final_P1kg24 (SB-PUSH2, 15 Nov) = P1kg23tm_lab (f45c3ebc) with only this docstring line and the log tag renamed. Was: SimulacraBench P1kg23tm_lab (SB-PUSH2 15 Nov) = final_P1kg23 + I1 twin-vector MLP (TM): the multi-task Net with the twin's whole answer vector as extra GIVEN-like columns, per-item 2-SE OOF-gated geometric pool on twin rows right after the donor stage (post-donor OOF base). SIM_TM=0 = final_P1kg23.
Was: SimulacraBench final_P1kg23 (SB-PUSH takeover, 15 Nov) = P1kg22tstf_lab with TF OFF by default (SIM_SVTF=1 turns it on): final_P1kg22 + SB2's twin stack ON (menu_bo, deep kappas, transition form, rate guard). SIM_DONOR_MODE=menu SIM_BO_KDEEP=0 SIM_BO_TRANS=0 SIM_GUARD_RATE=0 = final_P1kg22.
Was: SimulacraBench P1kg22tstf_lab (SB-PUSH 15 Nov) = final_P1kg22 + SB2's twin stack ON (menu_bo, deep kappas, transition form, rate guard) + twin-feature TabPFN on donor cells gated on svnp's H (SIM_SVTF); svlr arms OFF; TabPFN cache inert unless SIM_PFN_CACHE is set.\nWas: SimulacraBench final_P1kg22 (FINAL candidate, lane SB4 15 Nov) = P1kg17svnp4_lab (UNHCR-arm svnp v4; Jude 14 Nov 22:2xZ: take svnp) + the UNICEF-arm uw65 micro-patch (pool weight .65 on the 12-item instrument; SIM_W35_U=.75 = off). SIM_SVNP=0 SIM_W35_U=.75 = P1kg17 exactly.\nWas: SimulacraBench P1kg17svnp4_lab (lab, UNHCR-arm 14 Nov) = P1kg17svnp3_lab with a side TabPFN fit for H on the first 48 V3.5 items (hidden fits untouched: lam 1 = P1kg17 exactly); H any twin candidate.\nWas: SimulacraBench P1kg17svnp3_lab (lab, UNHCR-arm 14 Nov) = P1kg17svnp2_lab with H drawn only from visible twin candidates sharing no key with a hidden row (no hidden twin loses its TabPFN context neighbour); SIM_SVNP_HSAFE=0 = v2.\nWas: SimulacraBench P1kg17svnp2_lab (lab, UNHCR-arm 14 Nov) = P1kg17svnp_lab + donor-after-pool arms (pooled x donor ratio^rho) in the same held-out check; SIM_SVNP_RHO=0 = svnp v1; SIM_SVNP_SEED picks H (default 11 = v1).\nWas: SimulacraBench P1kg17svnp_lab (lab, UNHCR-arm 14 Nov) = final_P1kg17gnp with the donor-cell pool weight chosen on held-out visible twin rows (svnp); SIM_SVNP=0 = P1kg17.\nWas: SimulacraBench final_P1kg17gnp (10 Nov; push 10 C1) = the build below + GUARD-GATED NO-POOL: where the household donors ran and the transfer guard reads no gap on every key, donor-served hidden cells skip the TabPFN pool (REAL CPS: +.0085 cpsHi, +.0045 drift, +.0078 fresh drift; sabotage protected by the gate); SIM_GNP=0 restores P1kg17.\nWas: SimulacraBench final_P1kg17 (10 Nov; DECISION_6NOV 04:39Z) = the build below + SB2's donor TRANSFER GUARD v1 (label-free shrink of hidden rows' donor posteriors toward the model when their donors disagree with it more than visible rows' donors do); SIM_DON_GUARD=0 restores P1kg15; DONOR_MODE stays menu.\nWas: SimulacraBench final_P1kg15 (9 Nov; MAIN_TO_SB_2302b + 2342 + 2344) = the build below + four fault-path fixes, inert without a GPU / TabPFN error: a CUDA out-of-memory skips that item and keeps the GPU (was: rest of the run on CPU, TabPFN off); the upgrade pass never falls through to V2; only CUDA-runtime errors (not a bare 'cuda' in an error text) move the run to CPU; a non-CUDA V3.5 error costs one item (V2), a second one turns V3.5 off for the stage.\nWas: SimulacraBench final_P1kg14 (9 Nov; MAIN_TO_SB_2049, SB ledger 349-350) = the build below + SB2's donor key MENU: per item the best visible-OOF of exact_hh, exact-only and two other-round keys without governorate / counts (country + origin + respondent fields, +- adults), each 2-SE gated; REAL CPS drift: +.02 when the governorate is recoded.\nWas: SimulacraBench final_P1kg13 (9 Nov; MAIN_TO_SB_1803, SB ledger 338) = the build below with 6 MLP seeds (was 3); SIM_SEEDS=3 restores it exactly.\nWas: SimulacraBench final_P1kg12 (9 Nov; MAIN_TO_SB_1423, SB ledger 332; the last donor change) = the build below with donor POOL-PURITY weighting: each row's donor counts count as ONE pseudo-observation, (c/n + kappa x model) / (1 + kappa); real CPS +.005 to +.007 over the pick, no-harm >= -.00006.\nWas: SimulacraBench final_P1kg11 (9 Nov; MAIN_TO_SB_1117 optional, SB ledger 330) = the build below with DONOR_MODE pick: per item, the better visible-row OOF score of exact_hh and exact-only donors (each with its own 2-SE switch); real CPS: +.038 over exact_hh with respondent turnover, +.003 to +.006 elsewhere, no-harm on cross-sections.\nWas: SimulacraBench final_P1kg10 (9 Nov; MAIN_TO_SB_1004, SB ledger 328-329) = the build below with DONOR_MODE exact_hh: other-round donors from the row's exact-key group (all GIVEN minus wave) when it has any, else from its household-key group (real CPS 1-month panel: +.072 over the household mode at 85% twins, +.03 to +.04 with respondent turnover, 0 with no twins).\nWas: SimulacraBench final_P1kg9 (9 Nov; MAIN_TO_SB_0400 H1, AUDIT_FINALPATH_2026-11-09) = the build below + hardening that leaves every fault-free run unchanged: F3 no V2 upgrades once V3.5 is off; F4 the CatBoost pool is shut down when predict() returns; F6 a V2 fallback error skips that item; F5 a CUDA error moves the rest of the run to CPU with TabPFN off.\nWas: SimulacraBench final_P1kg8 (7 Nov; ledger 302-304) = the build below + a context-dependent V3.5-fast weight: an item fitted on m of n visible rows blends at ICL_W x min(1, 1.45 m / n) (SIM_WM_K; 0 = off).\nWas: SimulacraBench final_P1kg6 (7 Nov; MAIN_TO_SB_0446) = the build below + 11+ class items to V3.5-fast (SIM_PFN_BIG, default 1, on instruments with 76,120 items) + V3.5-fast categorical columns (SIM_V35_CAT, default none); ledger 260-265.
Was: SimulacraBench final_P1kg5 (7 Nov; MAIN_TO_SB_0042 item 6, ledger 257) = final_P1kg + ONE change: TabPFN V3.5-fast (bundled safetensors, n_estimators 4, same tabpfn 9.2.0) replaces TabPFN V2 as the foundation-model source, geometric blend weight W35 = .75; TabPFN V2 at .35 is only the per-item fallback (a V3.5-fast exception or an invalid output). Time guards unchanged in kind. CANARY 0.
SimulacraBench final_P1kg (6 Nov; main 10:28Z) = final_P1k (household donors ON) + the final_P1g output guards (G1-G9), nothing else. FINAL ONLY: needs Jude's yes (the donor question). CANARY 0.
SimulacraBench final_P1g (6 Nov, audit P1) = final_P1 + output guards that leave every valid run unchanged (ChatGPT Pro audit of e2783e81, finding 1, reproduced there: a gate rate a hair above 1 gives a negative answer share, which the TabPFN geometric blend / tempered mix turns into NaN, and one NaN vector fails the whole submission). G1: _swap_na clips the new NA probability to [0, 1]. G2: _mix / the mix picks clip p at 0 before the tempering power. G3: _sane repairs any non-finite / negative / massless row before and after the floor inverse (marginal if nothing is left). G4: predict() wraps the stack; an exception or an invalid result returns this instrument's crowd marginal instead of failing the submission. G5: a TabPFN probe that never ran (single-class context) is not taken as a ~0 s timing. From the Claude audit of the same file (crp/p2/audit_P1/AUDIT_P1_claude.md): G6: a non-finite TabPFN output skips TabPFN for that item; G7: a TabPFN fit that never ran records no time ratio (three in a row switched the time check off); G8: no load_state_dict(None) after a NaN first validation loss; G9: no TabPFN warm-up / probe once its stage is over. FINAL ONLY: needs Jude's yes. CANARY 0.
SimulacraBench final_P1 (6 Nov, Lead 33) = final_P with the UNHCR CatBoost rate .2 -> .1 (300 r lr .2 FAILS the real-answer gate at the Final: gss2018 -.00066; 300 r lr .1 passes -.00016 / +.00065, ledger 213). FINAL ONLY: needs Jude's yes. CANARY 0.
SimulacraBench final_P (Final candidate P, 6 Nov) = final_G0k + CatBoost pools on UNHCR and WB fitted beside the GPU stages (Leads 29-31) + UNHCR trees at 300 rounds, lr .2, depth 4 (ledger 190, 194-195: +1.37 UNHCR bucket over final_G0k on u2c3, 2 seeds). FINAL ONLY: needs Jude's yes. CANARY 0.
SimulacraBench v16o5 (DEV, 6 Nov) = v16o4 with UNHCR CatBoost depth 4 -> 5 (ledger 189: +.17 / +.18 bucket over v16o4 on u2c3). CANARY 0.
SimulacraBench v16o4 (DEV, 6 Nov; next UNHCR capacity step) = v16o3w with the UNHCR CatBoost learning rate .2 -> .3 (ledger 188: +.20 / +.18 bucket on u2c3, no coverage cost). UNHCR-only rounds / depth knobs default to v16o3w (150, 4). CANARY 0.
SimulacraBench v16o3w (DEV, 5 Nov; Lead 31b) = v16o3 + the concurrent CatBoost pool on WORLD BANK too (CONC_BY {213, 76}); UNICEF untouched. CANARY 0.
SimulacraBench v16o3 (DEV, 5 Nov; Lead 30) = v16o + UNHCR CatBoost learning rate .1 -> .2 (v16t3's tree setting). UNHCR only. CANARY 0.
SimulacraBench v16o (DEV, 5 Nov; Lead 29) = v16k + UNHCR CatBoost fits in a BACKGROUND pool (NTHR-1 workers) from the window start, concurrent with the MLP / wide / TabPFN (GPU) stages; items ordered by the marginal's loss per option; the per-item OOF blend runs after TabPFN, as before. v16k time shares. UNHCR only. CANARY 0.
SimulacraBench v16k (DEV, 5 Nov; Leads 16-17 follow-up) = v16c with both overrides AGREE-GATED: the structural zero and the pure-cell rules act only on cells where the model already sides with the group (P(NA) on the group's side of .5; top class = the pure answer), never against the model. All instruments. gss: identical to v16c (+.00000, 3 years x 2 seeds); u1: +.00260 skill (z 3.5; 94% of overrides-off). CANARY 0.
SimulacraBench final_G (Final candidate G, 4 Nov) = final_F + pure-cell rules after the structural zero (Final item #3: +.0002 to +.0004 skill on 3 gss years, sabotage loses; ledger 122). FINAL ONLY: needs Jude's yes. CANARY 0.
SimulacraBench final_F (Final candidate F, 4 Nov) = final_E + the exact floor inverse inside the mix pick and on the output (Lead 8: +.00047 skill pooled over 3 gss years, z 7.9; sabotage f 1e-2 loses). FINAL ONLY: needs Jude's yes. CANARY 0.
SimulacraBench final_E (Final candidate E, 4 Nov) = final_D with the GEOMETRIC TabPFN pool (q-floor guard): +.00023 skill pooled over 3 gss years (z 9.3; +.00016 without each year's top item), sabotage loses (ledger 118). FINAL ONLY: needs Jude's yes. CANARY 0.
SimulacraBench final_D (Final candidate D, 4 Nov) = final_C with 3 MLP seeds (SIM_SEEDS default 3; Lead 7, accepted on main's amended bar 19:21Z). FINAL ONLY: needs Jude's yes. CANARY 0.
SimulacraBench final_C (Final candidate C, 4 Nov) = final_B + Lead 5's SEPARATE unique +-1 household pass for UNHCR rows without an exact other-round match (own kappa, 2-SE on its own rows; ledger 107-108). FINAL ONLY: needs Jude's yes; RULING 4: YES covers the +-1 key ("may one of the counts also differ by one?" -> "No problems with doing anything in predict()"). Canary 0.
SimulacraBench final_B (Final candidate B, 4 Nov) = final_A + v14h household donors for UNHCR (household-exact key, other-round donors, 2-SE), with DONORS_FIRST from Lead 3. FINAL ONLY: needs RULING 4: YES and Jude's yes.
SimulacraBench final_A (Final candidate A, 4 Nov) = v11k (Final profile LIMIT 3300, shares .15/.30/.55, PFN_FRAC .5, canary 0; hurdle trees, structural zero, wave-free exact donors) + audit fixes 1/2/7 with the PASS SB2 corrections (as v15h; fix 3 not carried) + the 2-SE donor switch-on (as v14h). NO household key. FINAL ONLY: needs Jude's yes.
SimulacraBench v11k (Final draft 7 = v11j with the donor key = all GIVEN columns except wave (organiser ruling 2, 4 Nov). Canary off).
SimulacraBench v11i (Final draft 5) = v11h + HURDLE trees on gated items (gate = Logloss CatBoost on the NA flag over all rows x content = MultiClass on the answered rows; ledger 68: quality +.0005/+.0005/-.0001 vs joint at .47-.59 of the CPU). Items without an NA slot, or with too few NA/answered rows, keep the joint fit.
v11h (Final draft 4) = v11g + the structural-zero override (RANK "DECIDED"; measured +.0016/+.0004/+.0003 on gss, lab/crp_sb/psychometrics_gates/structzero.py): on held-out cells whose gate one GIVEN column fixes (visible group n >= 20, NA rate >= .99 or <= .01), P(NA) <- the group KT rate (c + .5)/(n + 1), answer shares kept. Applied last, label-free.
v11g (Final draft 3): v11f with per-instrument deadlines instead of first-come budgets.

Why: in v11f's sandbox run (ledger 53) World Bank used 2593 s and UNHCR got no wide, no trees and no TabPFN.
v11g reserves each instrument a share of LIMIT (SHARE by PREDICT item count, unknown instruments split the rest
evenly). Its deadline is absolute, T0 + LIMIT * (shares of the instruments run so far, this one included), so time an
instrument leaves unused rolls forward, and no instrument can spend the reserve of those still to come.
Inside an instrument's window: MLP (5 folds, each fold stops at its own deadline), wide model (same), TabPFN (at most
PFN_FRAC of the time left), CatBoost trees (the rest), gate chain, temperature / marginal mix, TabPFN blend.
TabPFN is capped by measured time: a warm-up and a timed probe on a small context give a conservative (quadratic)
estimate for an item; each item's context is the largest that fits (time left) / (items left), never below
PFN_MIN_CTX rows; the estimate is corrected by each finished item's measured time. Items go most uncertain first.
Canary (SIM_CANARY, off by default): 2 = the v11c timing canary (see _canary).
Earlier: v11f = v10k (vectorised loss) + K^2 tree split + TabPFN V2 at weight .35 (ledger 39, 50); v10k = v8e +
vectorised loss; v8 = per-item CatBoost on threads inside predict(), no child process, no temp files; v5 = v4 + wide
additive softmax; v3 = v1 (multi-task MLP, 5-fold, per-item marginal blend) + gate chain.
Everything is fitted inside predict() on the visible rows.
"""
import os
import time
def _wdir(sub, bases=None):   # SBQ STACK_RISK R6: first WRITABLE base wins; /tmp first, so a writable /tmp gives exactly the old paths
    import tempfile
    for b in (bases or ("/tmp", tempfile.gettempdir(), "/dev/shm", os.getcwd(), os.path.dirname(os.path.abspath(__file__)))):
        try:
            p_ = os.path.join(b, sub); os.makedirs(p_, exist_ok=True)
            with open(os.path.join(p_, ".w"), "w"):
                pass
            return p_
        except Exception:
            pass
    return os.path.join("/tmp", sub)
os.environ.setdefault("SKB_DATA_DIRECTORY", _wdir("skb_data"))   # SBY 26: tabpfn imports skrub, which mkdirs its data dir at import; an unwritable dir silently switches TabPFN off (MEASURED, SBQ R6)
os.environ.setdefault("MPLCONFIGDIR", _wdir("mpl_cfg"))
# Cap future library initialization, preserving stricter valid host limits.
_BLAS_CAP_RAW = os.environ.get("SIM_BLAS_CAP", "8")
_BLAS_CAP = None
if _BLAS_CAP_RAW != "0":
    try:
        _BLAS_CAP = min(8, max(1, int(_BLAS_CAP_RAW)))
    except (TypeError, ValueError):
        _BLAS_CAP = 8
    for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
        try:
            _prior_cap = int(os.environ.get(_v, _BLAS_CAP))
        except (TypeError, ValueError):
            _prior_cap = _BLAS_CAP
        os.environ[_v] = str(min(_BLAS_CAP, _prior_cap) if _prior_cap > 0 else _BLAS_CAP)
_BLAS_RT_LIM = max(1, min(8, int(os.environ.get("SIM_BLAS_RT", "1") or 1)))   # SBH 17: BLAS (OpenBLAS / MKL) single-threaded; OpenMP (torch) keeps the cap. SIM_BLAS_RT=8 = the 8-thread cap (dt3bck5's)
if _BLAS_CAP is not None:
    for _v in ("MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
        os.environ[_v] = str(min(int(os.environ[_v]), _BLAS_RT_LIM))
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

TAG = "final_P1kg38xwrcknfdt3bck6s_c1L"
_C1_SRC = '"""Exact-wheel CatBoost interrupt patches. Call ONCE before starting workers.\n\nOnly Linux x86-64 / CPython 3.13 / catboost 1.2.10 cp313 wheel is accepted.\nNo on-disk library is changed. A mismatch returns skip:* before any write.\nThe caller must treat fail:* as fatal and must never patch during training.\n"""\nimport hashlib\nimport os\nimport platform\nimport struct\nimport sys\nimport threading\n\nSO_SHA256 = "8219dfd20a95dee3c8b9592c5a4e35f0ed27ce4081ddb58d1d55a506c9666f6a"\nSET = 0xE958240\nRESET = 0xE958250\nCHECK = 0xE958260\nHANDLER = 0xE731980\nGLOBAL = 0xFBBC758\nORIGINAL = {\n    SET: bytes.fromhex("488d0511452601488938c3"),\n    RESET: bytes.fromhex("488d050145260148c70000000000c3"),\n    CHECK: bytes.fromhex("488d05f1442601488338007402ff20c3"),\n    HANDLER: bytes.fromhex("4157415653e85601320189c3e87f04320183f8ff740d89dfe8530132015b415e415fc3"),\n}\n_lock = threading.Lock()\n\n\ndef _sha256(path):\n    h = hashlib.sha256()\n    with open(path, "rb") as f:\n        for chunk in iter(lambda: f.read(1 << 20), b""):\n            h.update(chunk)\n    return h.hexdigest()\n\n\ndef _proposal(variant):\n    if variant == "C1":\n        # mov rax,[rip+disp32]; test rax,rax; je ret; jmp rax; ret; nop\n        return CHECK, bytes.fromhex("488b05f14426014885c07402ffe0c390")\n    if variant == "C2":\n        return CHECK, b"\\xc3" + ORIGINAL[CHECK][1:]\n    raise ValueError("variant")\n\n\ndef _valid_proposal(variant, addr, code):\n    # Independent semantic validation: corrupted proposed bytes cannot pass.\n    if addr != CHECK or len(code) != 16:\n        return False\n    if variant == "C1":\n        return (code[:3] == b"\\x48\\x8b\\x05"\n                and CHECK + 7 + struct.unpack("<i", code[3:7])[0] == GLOBAL\n                and code[7:] == b"\\x48\\x85\\xc0\\x74\\x02\\xff\\xe0\\xc3\\x90")\n    if variant == "C2":\n        return code == bytes.fromhex("c38d05f1442601488338007402ff20c3")\n    return False\n\n\ndef _mappings(path):\n    base, regions = None, []\n    with open("/proc/self/maps") as f:\n        for line in f:\n            p = line.rstrip().split(None, 5)\n            if len(p) == 6 and p[5] == os.path.realpath(path):\n                lo, hi = (int(x, 16) for x in p[0].split("-"))\n                regions.append((lo, hi, p[1]))\n                if int(p[2], 16) == 0:\n                    base = lo\n    return base, regions\n\n\ndef _write(address, code):\n    import ctypes\n    try:\n        fd = os.open("/proc/self/mem", os.O_RDWR)\n    except OSError:\n        fd = None\n    if fd is not None:\n        try:\n            n = os.pwrite(fd, code, address)\n            if n != len(code):\n                return "fail:short-write"\n            return "patched:mem" if ctypes.string_at(address, len(code)) == code else "fail:verify"\n        except OSError:\n            # No fallback if any partial write is possible; caller must abort.\n            if ctypes.string_at(address, len(code)) != ORIGINAL[CHECK]:\n                return "fail:write"\n        finally:\n            os.close(fd)\n    libc = ctypes.CDLL(None, use_errno=True)\n    libc.mprotect.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int]\n    libc.mprotect.restype = ctypes.c_int\n    page = os.sysconf("SC_PAGE_SIZE")\n    lo = address // page * page\n    size = ((address + len(code) + page - 1) // page * page) - lo\n    if libc.mprotect(lo, size, 7):\n        return "skip:mprotect"\n    ctypes.memmove(address, code, len(code))\n    if libc.mprotect(lo, size, 5):\n        return "fail:restore-protection"\n    return "patched:mprotect" if ctypes.string_at(address, len(code)) == code else "fail:verify"\n\n\ndef patch(variant="C1"):\n    """Return patched:*, already, skip:* or fail:*; never raise.\n\nskip means unchanged; fail means caller must abort. Only a fresh, single-thread\nimport-time call is supported, including when other native modules spawn threads.\n"""\n    try:\n        with _lock:\n            return _patch(variant)\n    except Exception as exc:\n        return "skip:" + type(exc).__name__\n\n\ndef _patch(variant):\n    import ctypes\n    if (sys.platform != "linux" or platform.machine() != "x86_64"\n            or sys.implementation.name != "cpython" or sys.version_info[:2] != (3, 13)\n            or getattr(sys, "_is_gil_enabled", lambda: True)() is not True):\n        return "skip:platform"\n    if variant not in ("C1", "C2"):\n        return "skip:variant"\n    import catboost\n    if catboost.__version__ != "1.2.10":\n        return "skip:version"\n    so = os.path.realpath(catboost._catboost.__file__)\n    if _sha256(so) != SO_SHA256:\n        return "skip:wheel"\n    base, regions = _mappings(so)\n    if base is None:\n        return "skip:maps"\n    addr, code = _proposal(variant)\n    if not _valid_proposal(variant, addr, code):\n        return "skip:proposal"\n    for off, expected in ORIGINAL.items():\n        a = base + off\n        if not any(lo <= a and a + len(expected) <= hi and perm == "r-xp"\n                   for lo, hi, perm in regions):\n            return "skip:text"\n        actual = ctypes.string_at(a, len(expected))\n        if off == CHECK and actual == code:\n            continue\n        if actual != expected:\n            return "skip:bytes"\n    # Independent RIP-relative target check on all three original functions.\n    for off in (SET, RESET, CHECK):\n        if off + 7 + struct.unpack("<i", ORIGINAL[off][3:7])[0] != GLOBAL:\n            return "skip:global"\n    if ctypes.string_at(base + addr, len(code)) == code:\n        return "already"\n    try:\n        return _write(base + addr, code)\n    except Exception as exc:\n        return "fail:" + type(exc).__name__\n\n\nif __name__ == "__main__":\n    print(patch())\n'
def _c1_patch():
    if os.environ.get("SIM_CBFIX", "1") != "1":
        return "off"
    try:
        import catboost  # noqa: F401  (C1 must run after catboost import, before any fit thread)
        ns = {"__name__": "cb_fix_c1"}; exec(compile(_C1_SRC, "cb_fix_c1.py", "exec"), ns); return str(ns["patch"]())
    except Exception as e:
        return f"skip:{type(e).__name__}"
CBFIX_ST = _c1_patch()
_CB_THR = "off"
if os.environ.get("SIM_CB_THR1", "1") == "1":                    # SB2 19 Nov (SBK c_bck2 livelock): every CatBoost fit implicitly calls get_feature_importance(thread_count=-1); with 7-8 concurrent fits that is ~8 teams on an 8-CPU quota. Force 1 thread there; the importances are never used, so predictions are unchanged.
    try:
        import catboost.core as _cbc
        _cb_gfi0 = _cbc.CatBoost.get_feature_importance
        def _cb_gfi(self, *a, **k):
            if len(a) < 4 and k.get("thread_count", -1) in (-1, None):
                k["thread_count"] = 1
            return _cb_gfi0(self, *a, **k)
        _cbc.CatBoost.get_feature_importance = _cb_gfi
        _CB_THR = "fi1"
    except Exception as _e:
        _CB_THR = f"skip:{type(_e).__name__}"

# pandas may have loaded NumPy in the driver before this module. Environment
# settings cannot reconfigure that existing BLAS pool. This limits active
# concurrency, not the number of already-created native OS threads.
_BLAS_LIMIT_HANDLE = None
_BLAS_RT = "off"
if _BLAS_CAP is not None:
    try:                                                  # SB2: threadpoolctl ships with scikit-learn (no new requirement); a failure is LOGGED, never claimed as protection
        from threadpoolctl import ThreadpoolController
        _BLAS_CONTROLLER = ThreadpoolController()
        _BLAS_LIMIT_HANDLE = [
            _BLAS_CONTROLLER.select(filepath=p["filepath"]).limit(
                limits=min(_BLAS_CAP, _BLAS_RT_LIM, p["num_threads"]), user_api="blas")
            for p in _BLAS_CONTROLLER.info()
            if p["user_api"] == "blas" and p["num_threads"] > 0
        ]
        _BLAS_RT = "limited:" + ",".join(f"{p.get('internal_api')}={p.get('num_threads')}" for p in _BLAS_CONTROLLER.info() if p.get("user_api") == "blas")
    except Exception as _e:
        _BLAS_RT = f"unavailable:{type(_e).__name__}"
CB_UNSAFE = CBFIX_ST.startswith("fail:") and CBFIX_ST != "fail:restore-protection"   # SB2 (cx_ADV native guard, narrowed): restore-protection = the full code IS written, only the page protection was not restored; every other fail:* may leave partial bytes
print(f"[{TAG}] cbfix {CBFIX_ST}", flush=True)
print(f"[{TAG}] blascap {_BLAS_RT}", flush=True)
print(f"[{TAG}] cbthr {_CB_THR}", flush=True)                      # SB2: runtime BLAS limit state (threadpoolctl), logged once at import
# P1kg35e (SBZ 47): no raise on fail:* -- a raise at import fails every retry deterministically; logging keeps the run alive (worst case = the same crash risk as unpatched).
CAT_RND_BY = {213: int(os.environ.get("SIM_CAT_ROUNDS_U", 300))}   # final_P: UNHCR 300 rounds (others CAT_ROUNDS = 150)
CAT_DEP_BY = {213: int(os.environ.get("SIM_CAT_DEPTH_U", 4))}      # final_P: UNHCR depth 4
CAT_RND = [150]; CAT_DEP = [4]
CAT_LR_BY = {213: float(os.environ.get("SIM_CAT_LR_U", .1))}   # final_P1 / Q1: UNHCR lr .1 (Lead 33 real-answer gate)
CAT_LR = [0.1]                                         # set per instrument in predict() before any tree fit
CONC_BY = {int(k): 1 for k in os.environ.get("SIM_CONC_KEYS", "213,76").split(",") if k}   # v16o3w: pool on UNHCR (213) and WB (76); env only for bench tests
CONC_DISCARD = {int(k) for k in os.environ.get("SIM_CONC_DISCARD", "").split(",") if k}  # SABOTAGE arms only: these keys fit, then throw the trees away
OV_AGREE = 1                                           # v16k: overrides only where the model agrees with the group (ledger 148)
DONORS = 1                                             # final_P1k: donor stages ON (= final_Gk v final_G0k)
TAIL_OFF = int(os.environ.get("SIM_TAIL_OFF", 1))       # SBM T1: 1 = no structural zero / pure-cell rules on the keys below; 0 = the lead exactly
TAIL_OFF_KEYS = tuple(int(k) for k in os.environ.get("SIM_TAIL_OFF_KEYS", "213").split(",") if k)   # bench tests may add e.g. 212 (rgH) or 118 (rgT)
PURE_RULES = 1                                         # Final item #3: pure-cell rules after the structural zero (ledger 122)
FLOOR_INV = 1                                          # Lead 8: exact inverse of the grader floor, inside the mix pick and on the output (ledger 117, 121)
PFN_GEO = 1                                            # geometric TabPFN pool with the q-floor guard (Final item #1; ledger 118)
NEAR_PASS = 1                                          # Lead 5: separate unique +-1 household pass (ledger 108)
# Household-key donors for UNHCR (as v14h). FINAL ONLY, and ONLY after a written organiser yes to question 4 (RULING 4: YES).
DONOR_MODE = os.environ.get("SIM_DONOR_MODE", "menu_bo")   # SB2: "menu" adds drift-tolerant keys                                   # P1kg11: per-item OOF pick, exact_hh v exact-only (ledger 330)
DONORS_FIRST = 1                                       # donor stage BEFORE the gate chain: Lead 3 arm A, +.0030/+.0039/+.0035 nats/cell v v14h on 3 seeds, sabotage 0 (ledger 98)
HH_LOC = ["s1_2_country_asylum_lbl", "governorate_col", "s2_4a_origin_governorate_lbl"]
HH_CNT = ["s2_3_boys_0_5", "s2_3_girls_0_5", "s2_3_boys_6_17", "s2_3_girls_6_17", "s2_3_men_18_59", "s2_3_women_18_59",
          "s2_3_men_60plus", "s2_3_women_60plus"]
FIX1, FIX2, FIX7 = (int(os.environ.get(f"SIM_FIX{i}", 1)) for i in (1, 2, 7))   # audit fixes (v15h); fix 3 not carried (neutral)
TREE_RAISED = [0]
# GIVEN columns left out of the exact-match donor key: wave (organiser ruling 2, 4 Nov 03:14 UTC).
DONOR_DROP = ("wave",)
FLOOR = 1e-3
FOLDS = 5
SEEDS = int(os.environ.get("SIM_SEEDS", 6))   # 9 Nov (SB ledger 338): 3 -> 6 MLP seeds (+.000078 pooled real, no-harm + time gates PASS)
CHAIN = int(os.environ.get("SIM_CHAIN", 1))
WIDE = int(os.environ.get("SIM_WIDE", 1))
LIMIT = float(os.environ.get("SIM_LIMIT", 3300))      # seconds from import; the Final allows 3600 for all three
SHARE = {12: .15, 76: .30, 213: .55}                  # reserved share of LIMIT by PREDICT item count (UNICEF, WB, UNHCR)
N_INST = 3
MLP_FRAC = .45                                        # MLP may use at most this share of the instrument's window
WIDE_FRAC = .15                                       # wide model: at most this share of what is left after the MLP
PFN_FRAC = float(os.environ.get("SIM_PFN_FRAC", .5))  # TabPFN: at most this share of the time left for TabPFN + trees
PFN_W = float(os.environ.get("SIM_PFN_W", .35))
PFN_MIN_CTX = 2000                                    # contexts of at least the gss sizes the .35 weight was tested on
PFN_PROBE = 1024
PFN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tabpfn-v2-classifier-finetuned-zk73skhh.ckpt")
# TabPFN V3.5-fast replaces TabPFN V2 as the foundation-model source (ledger 257: v TabICL +.0004 at .45 on both gss pools;
# v V2 +.0013 at .45). Licence: TABPFN-3.5 non-commercial (Data Science Competitions allowed), text bundled. V2 = fallback.
PFN_MODEL = os.environ.get("SIM_PFN_MODEL", "v35f")
ICL_W = float(os.environ.get("SIM_W35", .75))
ICL_W_U = float(os.environ.get("SIM_W35_U", .65))   # UNICEF-arm: pool weight on the 12-item instrument (wgu benches, z 3.6)
PFN_NEST_U = int(os.environ.get("SIM_PFN_NEST_U", 2))     # SBM S2b: V3.5-fast estimators on the keys below; 4 = the pick exactly, 2 = half cost (full context at n_est 2 = n_est 4 within -.00006, uncut rgG / rgH)
PFN_NEST_KEYS = tuple(int(k) for k in os.environ.get("SIM_PFN_NEST_KEYS", "213").split(",") if k)
WM_K = float(os.environ.get("SIM_WM_K", 1.45))      # ledger 303-304: capped-context V3.5-fast weight ICL_W x min(1, WM_K m / n); 0 = off
PFN_BIG = os.environ.get("SIM_PFN_BIG", "1") == "1"        # 0442 C: 11+ class items to V3.5-fast (no V2 fallback)
PFN_BIG_KEYS = {int(k) for k in os.environ.get("SIM_PFN_BIG_KEYS", "76,120").split(",") if k}   # instruments (by item count) where C is on
V35_CAT = os.environ.get("SIM_V35_CAT", "none")              # 0414: V3.5-fast categorical columns: all | none
ICL_CK = "tabpfn-v3.5-fast-20260909.safetensors"
ICL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ICL_CK)
QW = {}                                               # per-item blend weight of the source that filled Q[j]
CAT_ROUNDS = int(os.environ.get("SIM_CAT_ROUNDS", 150))
TWEV_KDW = float(os.environ.get("SIM_TWEV_KDW", .25))           # SBT2 Esoft: key-donor rows served at pc x KDW instead of skipped; 0 = skipped (= xwg)
TWEV_RECIP = int(os.environ.get("SIM_TWEV_RECIP", 1))           # SBT2 C8: reciprocal-gap feature in the twin stage's link-confidence model; 0 = off (= xwg), 2 = sabotage
TWEV_XCL = int(os.environ.get("SIM_TWEV_XCL", 1))
TWEV_CH = int(os.environ.get("SIM_TWEV_CH", 4))                   # SBN CH: directed value-transition channel (bits 1 counts [only when cpat is off], 2 governorates, 4 respondent fields); 0 = off (= xwrck)
TWEV_CHA = float(os.environ.get("SIM_TWEV_CHA", 320.0))            # SBN CH: empirical-Bayes prior strength toward the binary 'differs' llr
TWEV_CHSEL = int(os.environ.get("SIM_TWEV_CHSEL", 1))              # SBN CH-sel: keep the channel only if it raises the held-out softmax log-lik of visible silver partners
TWEV_CHSAB = int(os.environ.get("SIM_TWEV_CHSAB", 0))
TWEV_CHMIN = float(os.environ.get("SIM_TWEV_CHMIN", .02))         # SBN CH-sel margin: switch on only if the held-out partner log-lik gain >= CHMIN nats/row              # SBN sabotage: transition llrs shuffled within each field
TWEV_CPAT = int(os.environ.get("SIM_TWEV_CPAT", 3))              # SBV DA2: signed count-change flags in the twin stage; 0 = off, 3 on, 4 sabotage
TWEV_RAMP = int(os.environ.get("SIM_TWEV_RAMP", 1))              # SBR R1: soften the twin stage's file gate (pc x r near the gate instead of switching off); 0 = hard gate (= dt3bck2 exactly), 2 = sabotage
TWEV_KIN = int(os.environ.get("SIM_TWEV_KIN", 1))
TWEV_KMIN = float(os.environ.get("SIM_TWEV_KMIN", 150))    # SB2 dt3b: kinship only if the twin stage starts with >= KMIN s of allowance (normal hosts: 180); a slow host keeps the stage without kinship (lane SB 04:43Z: dt lost the stage at hog50)                # SBV + cx_SBUH1: residual-kinship re-link of visible pairs; 0 off, 2 sabotage               # SBU 4: exclusion of claimed visible rows inside the twin stage; 0 = off (= P35xs), 2 = sabotage
CANARY = int(os.environ.get("SIM_CANARY", 0))
TWEV = int(os.environ.get("SIM_TWEV", 1))                    # SBX 46a lab: twin-evidence stage on the final vectors; 0 = off (base path), 2 = sabotage
TWEV_RES, TWEV_TMAX = 45.0, float(os.environ.get("SIM_TWEV_TMAX", 180))   # SB2 19 Nov (SBZ TWEV_TIMEOUT): 90 -> 180 s cap; the absolute bound _tm (T0+LIMIT+AVL_OVER+TWEV_RES) still ends the stage by T0+3445; 90 = old                             # seconds reserved at the end of predict / hard stop of the stage
NTHR = int(os.environ.get("SIM_THREADS", min(8, os.cpu_count() or 1)))
T0 = time.time()
DONE_SHARE = []                                       # shares of the instruments already started
FAIL = {}
DEV = "cuda" if torch.cuda.is_available() else "cpu"
CUDA_DEAD = [False]                                   # H1 F5: set by _cuda_fault; TabPFN off and DEV = cpu for the rest of the run
CUR_TT = [None]  # own executor and callback stop token, including exceptional exits
CUR_POOL = [None]                                     # H1 F4: the running instrument's CatBoost pool


CUDA_RT = ("CUDA error", "CUDA driver error", "CUBLAS_STATUS", "CUDNN_STATUS", "cuDNN error", "device-side assert", "NCCL error")


def _is_acc(e):
    ac = getattr(torch, "AcceleratorError", None)
    return ac is not None and isinstance(e, ac)


def _is_oom(e):
    """P1kg15: torch's OutOfMemoryError (or its text) = a recoverable allocation failure, not a poisoned CUDA context."""
    oe = getattr(torch, "OutOfMemoryError", None) or getattr(getattr(torch, "cuda", None), "OutOfMemoryError", None)
    return (oe is not None and isinstance(e, oe)) or "out of memory" in f"{e!r}".lower()


def _cuda_fault(e):
    """H1 F5: a CUDA-side error can poison the CUDA context; move the rest of the run to CPU and turn TabPFN off."""
    global DEV
    s_ = f"{type(e).__name__} {e!r}"
    if _is_oom(e):                                            # P1kg15: an OOM is recoverable; skip the item, keep the GPU
        try:
            torch.cuda.empty_cache()
        except Exception:
            pass
        FAIL["cuda_oom"] = 1
        print(f"[{TAG}] CUDA out of memory ({s_[:120]}): item skipped, GPU kept", flush=True)
        return True
    if DEV == "cuda" and (_is_acc(e) or any(k in s_ for k in CUDA_RT)):      # P1kg15 (2342): CUDA-runtime failures only
        DEV = "cpu"; CUDA_DEAD[0] = True; FAIL["cuda_err"] = 1
        print(f"[{TAG}] CUDA error ({s_[:120]}): rest of the run on CPU, TabPFN off", flush=True)
        return True
    return False
torch.set_num_threads(NTHR)


def _opts(schema, k):
    r = schema["items"][k]
    return list(r["values"]) + ([schema["gated_value"]] if r.get("gate") else [])


def _encode(col, opts):
    m = {o: i for i, o in enumerate(opts)}
    return np.array([m.get(v, len(opts)) for v in col], dtype=np.int64)   # unseen / NaN -> extra code


class Net(nn.Module):
    def __init__(self, cards, widths, hid=256, emb=16, drop=0.3):
        super().__init__()
        self.embs = nn.ModuleList([nn.Embedding(c + 1, emb) for c in cards])
        self.body = nn.Sequential(nn.Linear(emb * len(cards), hid), nn.GELU(), nn.Dropout(drop),
                                  nn.Linear(hid, hid), nn.GELU(), nn.Dropout(drop))
        self.head = nn.Linear(hid, int(sum(widths)))

    def forward(self, x):
        return self.head(self.body(torch.cat([e(x[:, i]) for i, e in enumerate(self.embs)], 1)))


class Wide(nn.Module):
    """Additive model: each GIVEN value adds a fixed score to every option."""

    def __init__(self, cards, widths):
        super().__init__()
        self.embs = nn.ModuleList([nn.Embedding(c + 1, int(sum(widths))) for c in cards])
        for e in self.embs:
            nn.init.zeros_(e.weight)
        self.bias = nn.Parameter(torch.zeros(int(sum(widths))))

    def forward(self, x):
        return self.bias + sum(e(x[:, i]) for i, e in enumerate(self.embs))


class VLoss:
    """Mean over items of per-item mean cross entropy (y = -1 means no label); items padded to Kmax, one logsumexp."""

    def __init__(self, offs):
        w = np.diff(offs); K = int(w.max()); J = len(w)
        idx = np.zeros((J, K), np.int64); msk = np.zeros((J, K), bool)
        for j in range(J):
            idx[j, :w[j]] = np.arange(offs[j], offs[j + 1]); msk[j, :w[j]] = True
        self.idx = torch.as_tensor(idx, device=DEV); self.neg = torch.as_tensor(~msk, device=DEV)
        self.off = torch.as_tensor(np.asarray(offs[:-1], np.int64), device=DEV)

    def __call__(self, logits, y):
        lse = torch.logsumexp(logits[:, self.idx].masked_fill(self.neg, float("-inf")), 2)
        ok = y >= 0
        nll = (lse - torch.gather(logits, 1, self.off + y.clamp(min=0))) * ok
        return (nll.sum(0) / ok.sum(0)).mean()


def _probs(logits, offs):
    return [torch.softmax(logits[:, offs[j]:offs[j + 1]], 1).cpu().numpy() for j in range(len(offs) - 1)]


def _fit(Xtr, Ytr, Xva, Yva, cards, widths, offs, seed, deadline, max_ep=300, patience=20, bs=512, wide=False):
    """Early stopping on the validation fold; also stops at the deadline (after at least one epoch). Returns (net, cut)."""
    torch.manual_seed(seed)
    net = (Wide(cards, widths) if wide else Net(cards, widths)).to(DEV)
    opt = torch.optim.AdamW(net.parameters(), lr=1e-2 if wide else 2e-3, weight_decay=1e-3 if wide else 1e-4)
    Xtr, Ytr, Xva, Yva = (torch.as_tensor(a, device=DEV) for a in (Xtr, Ytr, Xva, Yva))
    _losses = VLoss(offs)
    best, best_state, bad, cut = np.inf, None, 0, False
    n = Xtr.shape[0]
    for ep in range(max_ep):
        net.train()
        perm = torch.randperm(n, device=DEV)
        for s in range(0, n, bs):
            b = perm[s:s + bs]
            opt.zero_grad(); _losses(net(Xtr[b]), Ytr[b]).backward(); opt.step()
        net.eval()
        with torch.no_grad():
            v = float(_losses(net(Xva), Yva))
        if v < best - 1e-5:
            best, bad = v, 0
            best_state = {k: t.detach().clone() for k, t in net.state_dict().items()}
        else:
            bad += 1
            if bad >= patience:
                break
        if time.time() > deadline:
            cut = True
            break
    if best_state is not None:                 # G8: a NaN first validation loss leaves no saved state
        net.load_state_dict(best_state)
    net.eval()
    return net, cut


def _folds(Xv, Yv, Xh, cards, widths, offs, fold, end, wide=False):
    """5-fold fit; fold f must end by now + (end - now) / (folds left). Returns oof, test, cut."""
    n = len(Xv)
    oof = [np.zeros((n, w)) for w in widths]
    test = [np.zeros((len(Xh), w)) for w in widths]
    cut = False
    for f in range(FOLDS):
        tr, va = fold != f, fold == f
        for sd in range(1 if wide else SEEDS):
            k = f * (1 if wide else SEEDS) + sd
            dl = time.time() + max(0.0, end - time.time()) / (FOLDS * (1 if wide else SEEDS) - k)
            net, c = _fit(Xv[tr], Yv[tr], Xv[va], Yv[va], cards, widths, offs, seed=f + 100 * sd, deadline=dl,
                          patience=8 if wide else 20, wide=wide)
            cut |= c
            with torch.no_grad():
                pv = _probs(net(torch.as_tensor(Xv[va], device=DEV)), offs)
                ph = _probs(net(torch.as_tensor(Xh, device=DEV)), offs)
            div = 1 if wide else SEEDS
            for j in range(len(widths)):
                oof[j][va] += pv[j] / div; test[j] += ph[j] / (FOLDS * div)
    return oof, test, cut


def _mix(p, m, t, w):
    q = np.clip(p, 0.0, None) ** (1.0 / t); q /= q.sum(1, keepdims=True)   # G2: a negative share would give NaN
    return w * q + (1 - w) * m


def floor_inverse(Q, f=1e-3):
    """Q: (n, K) rows summing to 1 (renormalised here). Returns P (n, K) on the simplex."""
    Q = np.asarray(Q, float); Q = Q / Q.sum(1, keepdims=True); n, K = Q.shape; c = 1 - K * f
    A = np.ones_like(Q, bool)
    for _ in range(K + 1):
        QA = np.where(A, Q, 0).sum(1, keepdims=True); nA = A.sum(1, keepdims=True)
        lam = (nA * f + c) / np.clip(QA, 1e-300, None)
        newA = A & (Q * lam > f)
        if np.array_equal(newA, A):
            break
        A = newA
    P = np.where(A, (Q * lam - f) / c, 0.0)
    P = np.clip(P, 0, None); return P / P.sum(1, keepdims=True)


def _pick_mix_inv(p, m, y):
    """_pick_mix with the floor inverse inside the loss: score log(f + c * inverse(mix)[y])."""
    K, r = p.shape[1], np.arange(len(y)); best = (-np.inf, 1.0, 0.0)
    for tt in (0.8, 0.9, 1.0, 1.1, 1.25):
        q = np.clip(p, 0.0, None) ** (1.0 / tt); q = q / q.sum(1, keepdims=True)   # G2
        for w in (0.0, 0.5, 0.7, 0.85, 0.95, 1.0):
            P = floor_inverse(w * q + (1 - w) * m[None, :], FLOOR)
            s_ = np.log(FLOOR + (1 - K * FLOOR) * P[r, y]).mean()
            if s_ > best[0]:
                best = (s_, tt, w)
    return best


def _pick_mix(p, m, y):
    """Same grid and the same pick as v11f's loop over _logscore(_mix(...)), with one power per temperature."""
    K, r = p.shape[1], np.arange(len(y))
    best = (-np.inf, 1.0, 0.0)
    for tt in (0.8, 0.9, 1.0, 1.1, 1.25):
        q = np.clip(p, 0.0, None) ** (1.0 / tt); qy = q[r, y] / q.sum(1)   # G2
        for w in (0.0, 0.5, 0.7, 0.85, 0.95, 1.0):
            s = np.log(FLOOR + (1 - K * FLOOR) * (w * qy + (1 - w) * m[y])).mean()
            if s > best[0]:
                best = (s, tt, w)
    return best


def _logscore(p, y):
    K = p.shape[1]
    p = p / p.sum(1, keepdims=True)
    return np.log(FLOOR + (1 - K * FLOOR) * p[np.arange(len(y)), y])


class _Stop:
    def __init__(self, t):
        self.t = t

    def after_iteration(self, info):
        return time.time() < self.t


def _cb(loss, rounds):
    if CB_UNSAFE:
        raise RuntimeError("CatBoost native patch incomplete; tree stage disabled")
    from catboost import CatBoostClassifier
    return CatBoostClassifier(iterations=rounds, depth=CAT_DEP[0], learning_rate=CAT_LR[0], l2_leaf_reg=5, loss_function=loss,
                              boosting_type="Plain", thread_count=1, verbose=0, random_seed=0, allow_writing_files=False)


def _cat_hurdle(Xv, y, Xh, K, na, fold, rounds, hard):
    """Hurdle fit for a gated item: P(NA) from a binary gate, answer shares from a MultiClass fit on answered rows."""
    oof, test, folds = np.zeros((len(y), K)), np.zeros((len(Xh), K)), int(fold.max()) + 1
    cats = list(range(Xv.shape[1]))
    for f in range(folds):
        tr, va = fold != f, fold == f
        z = (y[tr] == na).astype(int); op = tr & (y != na)
        cl, yt = np.unique(y[op], return_inverse=True)
        if z.min() == z.max() or len(cl) < 2:
            return "unfit"
        g = _cb("Logloss", rounds); g.set_params(cat_features=cats); g.fit(Xv[tr], z, callbacks=[_Stop(hard)])
        if time.time() >= hard:
            return "cut"
        c = _cb("MultiClass", rounds); c.set_params(cat_features=cats); c.fit(Xv[op], yt, callbacks=[_Stop(hard)])
        if time.time() >= hard:
            return "cut"
        gv_, gh_ = g.predict_proba(Xv[va], **({'thread_count': 1} if FIX7 else {}))[:, 1], g.predict_proba(Xh, **({'thread_count': 1} if FIX7 else {}))[:, 1]
        cv_, ch_ = c.predict_proba(Xv[va], **({'thread_count': 1} if FIX7 else {})), c.predict_proba(Xh, **({'thread_count': 1} if FIX7 else {}))
        o = np.zeros((va.sum(), K)); o[:, cl] = cv_ * (1 - gv_)[:, None]; o[:, na] = gv_; oof[va] = o
        t_ = np.zeros((len(Xh), K)); t_[:, cl] = ch_ * (1 - gh_)[:, None]; t_[:, na] = gh_; test += t_ / folds
    return oof, test


def _cat_item(Xv, y, Xh, K, fold, rounds, hard, na=-1):
    """Returns (oof, test), 'unfit' (a fold has one class) or 'cut' (stopped at the hard deadline). na >= 0: hurdle
    fit when the item has enough NA and answered rows (>= 30 each and >= 2 answer classes), else the joint fit."""
    if CB_UNSAFE:
        raise RuntimeError("CatBoost native patch incomplete; tree stage disabled")
    from catboost import CatBoostClassifier
    if na >= 0:
        z = y == na
        if z.sum() >= 30 and (~z).sum() >= 30 and len(np.unique(y[~z])) >= 2:
            r = _cat_hurdle(Xv, y, Xh, K, na, fold, rounds, hard)
            if not (isinstance(r, str) and r == "unfit"):
                return r
    oof, test, folds = np.zeros((len(y), K)), np.zeros((len(Xh), K)), int(fold.max()) + 1
    for f in range(folds):
        tr, va = fold != f, fold == f
        cl, yt = np.unique(y[tr], return_inverse=True)
        if len(cl) < 2:
            return "unfit"
        m = CatBoostClassifier(iterations=rounds, depth=CAT_DEP[0], learning_rate=CAT_LR[0], l2_leaf_reg=5, loss_function="MultiClass",
                               cat_features=list(range(Xv.shape[1])), boosting_type="Plain", thread_count=1, verbose=0,
                               random_seed=0, allow_writing_files=False)
        m.fit(Xv[tr], yt, callbacks=[_Stop(hard)])
        if time.time() >= hard:
            return "cut"
        oof[np.ix_(va, cl)] = m.predict_proba(Xv[va], **({'thread_count': 1} if FIX7 else {})); test[:, cl] += m.predict_proba(Xh, **({'thread_count': 1} if FIX7 else {})) / folds
    return oof, test


def _blend_trees(stop, hard, Xv, Yv, Xh, widths, fold, oof, test, nas=None):
    """CatBoost per item on NTHR threads, most loss per answer option first. Items start until `stop`; a fit still
    going at `hard` is dropped. Returns used, done, total, complete."""
    scale = [_logscore(oof[j], Yv[:, j]).mean() for j in range(len(widths))]
    d, st = {}, {}

    def job(j):
        if time.time() >= stop:
            return j, "late"
        if not FIX1:
            return j, _cat_item(Xv, Yv[:, j], Xh, int(widths[j]), fold, CAT_RND[0], hard, -1 if nas is None else int(nas[j]))
        try:                                   # audit #1: one failing item must not drop every other item's fits
            return j, _cat_item(Xv, Yv[:, j], Xh, int(widths[j]), fold, CAT_RND[0], hard, -1 if nas is None else int(nas[j]))
        except Exception:
            TREE_RAISED[0] += 1
            return j, "raised"

    try:
        with ThreadPoolExecutor(NTHR) as ex:
            for j, r in ex.map(job, [int(j) for j in np.argsort(np.array(scale) / np.array(widths))]):
                if isinstance(r, str):
                    st[j] = r
                    if r == "raised":              # PASS SB2 #1: a caught item raise still reaches FAIL
                        FAIL["trees_raised"] = 1
                else:
                    d[j] = r
    except Exception as e:
        print(f"[{TAG}] trees skipped: {e!r}"[:300], flush=True)
        FAIL["trees_raised"] = 1
        return 0, 0, len(widths), False
    used = 0
    for j, (o, h) in d.items():
        best, a = scale[j] + 1e-4, 0.0
        for c in (0.25, 0.5, 0.75, 1.0):
            s = _logscore((1 - c) * oof[j] + c * o + 1e-9, Yv[:, j]).mean()
            if s > best:
                best, a = s, c
        if a:
            oof[j] = (1 - a) * oof[j] + a * o; test[j] = (1 - a) * test[j] + a * h; used += 1
    complete = not any(v in ("late", "cut", "raised") for v in st.values())
    return used, len(d), len(widths), complete


def _pool_start(stop, hard, Xv, Yv, Xh, widths, fold, marg, nas):
    """v16o: start the per-item CatBoost fits in a background pool (NTHR-1 workers) now; same deadline rule as
    _blend_trees. Order: most MARGINAL loss per answer option first (the MLP's oof is not known yet)."""
    scale = [_logscore(np.tile(marg[j], (len(Yv), 1)), Yv[:, j]).mean() for j in range(len(widths))]

    def job(j):
        if time.time() >= stop:
            return j, "late"
        try:
            return j, _cat_item(Xv, Yv[:, j], Xh, int(widths[j]), fold, CAT_RND[0], hard, int(nas[j]))
        except Exception:
            TREE_RAISED[0] += 1
            return j, "raised"
    ex = ThreadPoolExecutor(max(1, NTHR - 1)); CUR_POOL[0] = ex                   # H1 F4
    futs = [ex.submit(job, int(j)) for j in np.argsort(np.array(scale) / np.array(widths))]
    return ex, futs


def _pool_blend(ex, futs, Yv, widths, oof, test, discard=False):
    """v16o: collect the background fits (each stops itself at `hard`) and run _blend_trees' per-item OOF blend."""
    d, st = {}, {}
    try:
        for f in futs:
            j, r = f.result()
            if isinstance(r, str):
                st[j] = r
                if r == "raised":
                    FAIL["trees_raised"] = 1
            else:
                d[j] = r
    except Exception as e:
        print(f"[{TAG}] trees skipped: {e!r}"[:300], flush=True)
        FAIL["trees_raised"] = 1
        ex.shutdown(wait=False)
        return 0, 0, len(widths), False
    ex.shutdown(wait=True)
    if discard:
        d = {}
    used = 0
    for j, (o, h) in d.items():
        best, a = _logscore(oof[j], Yv[:, j]).mean() + 1e-4, 0.0
        for c in (0.25, 0.5, 0.75, 1.0):
            s = _logscore((1 - c) * oof[j] + c * o + 1e-9, Yv[:, j]).mean()
            if s > best:
                best, a = s, c
        if a:
            oof[j] = (1 - a) * oof[j] + a * o; test[j] = (1 - a) * test[j] + a * h; used += 1
    complete = not any(v in ("late", "cut", "raised") for v in st.values())
    return used, len(d), len(widths), complete


def _pfn_q(Xv, Yv, Xh, marg, stop, Q, info):
    """TabPFN V2 class probabilities for eligible items (2-10 visible classes), most uncertain first, into Q[j] = (cl, P).
    Per-item time is capped: context = the largest whose predicted time fits (time left) / (items left)."""
    from tabpfn import TabPFNClassifier
    from tabpfn.constants import ModelVersion
    QW.clear()
    icl = [None]
    strikes = [0]                                                 # P1kg15 (2344): non-CUDA V3.5 errors this stage
    if CUDA_DEAD[0]:                                              # H1 F5
        return
    if PFN_MODEL == "v35f" and os.path.exists(ICL_FILE):
        icl[0] = lambda: TabPFNClassifier.create_default_for_version(
            ModelVersion.V3_5_FAST, model_path=ICL_FILE, n_estimators=(PFN_NEST_U if Yv.shape[1] in PFN_NEST_KEYS else 4), device=DEV,   # SBM S2b
            categorical_features_indices=list(range(Xv.shape[1])) if V35_CAT != "none" else [], ignore_pretraining_limits=True)
    n, nh = len(Xv), len(Xh)
    order = [int(j) for j in np.argsort([(m * np.log(m)).sum() for m in marg]) if 2 <= len(np.unique(Yv[:, j])) <= 10]
    if PFN_BIG and icl[0] is not None and Yv.shape[1] in PFN_BIG_KEYS:                            # 0442 C: then the 11+ class items, same entropy order
        order += [int(j) for j in np.argsort([(m * np.log(m)).sum() for m in marg]) if len(np.unique(Yv[:, j])) > 10]
    info.update(elig=len(order), done=0, ctx=n, probe=0.0, item=0.0)
    if not order:
        return
    perm = np.random.default_rng(1).permutation(n)

    def run(j, idx, Xq, no_v2=False):
        cl, yt = np.unique(Yv[idx, j], return_inverse=True)
        if len(cl) < 2:
            return None
        if icl[0] is not None:
            try:
                m = icl[0]()
                m.fit(Xv[idx], yt); P = np.asarray(m.predict_proba(Xq), float)
                if P.shape == (len(Xq), len(cl)) and np.isfinite(P).all():
                    return cl, P, ICL_W
                FAIL["icl_bad"] = 1                               # invalid output: this item falls back to V2
            except Exception as e:                                # a TabICL failure turns it off for this stage
                if _is_oom(e):                                    # P1kg15: OOM skips this item; V3.5 stays on
                    _cuda_fault(e)
                    return None
                strikes[0] += 1                                   # P1kg15 (2344): two strikes per stage before V3.5 is off
                if strikes[0] >= 2 or (DEV == "cuda" and (_is_acc(e) or any(k in f"{type(e).__name__} {e!r}" for k in CUDA_RT))):
                    print(f"[{TAG}] v35f stopped: {e!r}"[:300], flush=True); FAIL["icl_off"] = 1; icl[0] = None
                else:
                    print(f"[{TAG}] v35f item error (strike 1, V3.5 kept): {e!r}"[:300], flush=True); FAIL["icl_item"] = 1
                if _cuda_fault(e):                                # H1 F5: no V2 on a poisoned context
                    return None
        if no_v2 or len(cl) > 10:                                 # P1kg15: upgrades never fall to V2; 0442 C: V2 takes <= 10 classes
            return None
        if CUDA_DEAD[0]:                                          # H1 F5
            return None
        try:                                                      # H1 F6: a V2 error skips this item, the stage continues
            m = TabPFNClassifier.create_default_for_version(ModelVersion.V2, model_path=PFN_FILE, n_estimators=4, device=DEV,
                                                            categorical_features_indices=list(range(Xv.shape[1])),
                                                            ignore_pretraining_limits=True)
            m.fit(Xv[idx], yt)
            return cl, m.predict_proba(Xq), PFN_W
        except Exception as e:
            print(f"[{TAG}] v2 item skipped: {e!r}"[:300], flush=True); FAIL["v2_err"] = 1; _cuda_fault(e)
            return None

    if time.time() >= stop:                                       # G9: no warm-up or probe once the stage is over
        return
    npb, nhb = min(n, PFN_PROBE), min(nh, 512)
    run(order[0], perm[:min(n, 128)], Xh[:64])                    # warm-up: first-call cost (CUDA init, kernels)
    t = time.time(); r0 = run(order[0], perm[:npb], Xh[:nhb])
    tp = max(time.time() - t, 1e-3) if r0 is not None else 1.0  # G5: a probe that never ran is no timing (1 s, conservative)
    info["probe"] = tp

    def est(m):                                                   # quadratic in context: conservative (ledger 59)
        return tp * m * (m + nh) / (npb * (npb + nhb))

    ratios, lo, ctx_of = [], min(n, PFN_MIN_CTX), {}

    def one(j, m, no_v2=False):
        t = time.time()
        idx_, Hs = (np.sort(perm[:m]) if m < n else np.arange(n)), SV_H[0]
        r = run(j, idx_, Xh, no_v2)                               # the build's own fit: hidden rows untouched
        dt = time.time() - t
        if r is not None and Hs is not None and r[2] == ICL_W and (j in QH or len(QH) < SV_NITEMS):
            try:                                                  # svnp v4: side fit on (context minus H), queries = H only
                rH = run(j, np.setdiff1d(idx_, Hs, assume_unique=True), Xv[Hs], True)
                if rH is not None and np.array_equal(rH[0], r[0]) and np.isfinite(rH[1]).all():
                    QH[j] = np.asarray(rH[1], float)
                else:
                    QH.pop(j, None)
            except Exception:                                     # the side fit is optional
                QH.pop(j, None)
        if r is not None:                                         # G7: a fit that never ran is no timing
            ratios.append(dt / est(m))
        info["item"] = max(info["item"], dt)
        if r is not None:
            Q[j], QW[j], ctx_of[j] = r[:2], (r[2] * min(1.0, WM_K * m / n) if (WM_K > 0 and r[2] == ICL_W) else r[2]), m
            if Yv.shape[1] == 12 and r[2] == ICL_W:
                QW[j] *= ICL_W_U / ICL_W
            info["done"], info["ctx"] = len(Q), min(ctx_of.values())

    for c, j in enumerate(order):
        if CUDA_DEAD[0]:                                          # H1 F5
            break
        left = stop - time.time()
        corr = max(ratios[-3:]) if ratios else 1.0
        if corr * est(lo) * 1.2 > left:
            break                                                 # not even the smallest context fits the time left
        cap = left / (len(order) - c)
        m = n
        if corr * est(n) > cap:
            a, b = lo, n
            while b - a > 32:
                mid = (a + b) // 2
                a, b = (mid, b) if corr * est(mid) <= cap else (a, mid)
            m = a
        one(j, m)
    for j in [j for j in order if ctx_of.get(j, n) < n]:          # upgrade pass: refit reduced-context items in full
        if icl[0] is None or CUDA_DEAD[0]:                        # H1 F3: never replace a V3.5 fit by V2 at .35
            break
        if max(ratios[-3:]) * est(n) * 1.1 > stop - time.time():
            break
        one(j, n, no_v2=True)                                     # P1kg15: an upgrade keeps the earlier fit unless V3.5 succeeds


# SBV + cx_SBUH1: residual-kinship comparison for the twin stage's visible pairs (copied from cx_sbuh1/round2/residual_kinship.py md5 7d8d24d8, synthetic_check dropped)
def _effective_dimension(terms):
    terms = np.asarray(terms, float)
    terms -= terms.mean(0)
    cov = terms.T @ terms / max(len(terms) - 1, 1)
    return float(np.trace(cov) ** 2 / max(np.sum(cov * cov), 1e-15))


class _ResidualModel:
    def __init__(self, given, answers, widths, sabotage=False, check=lambda: None):
        self.check = check
        check()
        started = time.monotonic()
        self.y = np.asarray(answers)
        self.widths = np.asarray(widths)
        n, J = self.y.shape
        self.offsets = np.r_[0, np.cumsum(widths)]
        onehot = np.zeros((n, int(self.offsets[-1])), np.float64)
        for j, k in enumerate(widths):
            check()
            good = (self.y[:, j] >= 0) & (self.y[:, j] < k)
            onehot[np.flatnonzero(good), self.offsets[j] + self.y[good, j]] = 1
        g = pd.get_dummies(given.astype(str), dtype=float).to_numpy()
        g = (g - g.mean(0)) / np.maximum(g.std(0), .1)
        g = np.c_[np.ones(n), g]
        halves = np.array_split(np.random.default_rng(42).permutation(J), 2)
        fold = np.arange(n) % 2
        predicted = np.empty_like(onehot)
        for group in range(2):
            check()
            targets = np.concatenate([np.arange(self.offsets[j], self.offsets[j+1]) for j in halves[group]])
            context = np.concatenate([np.arange(self.offsets[j], self.offsets[j+1]) for j in halves[1-group]])
            b = onehot[:, context]
            b = (b - b.mean(0)) / np.maximum(b.std(0), .1)
            _, directions = np.linalg.eigh(b.T @ b / n)
            check()
            pc = b @ directions[:, -min(8, len(context)):]
            pc /= np.maximum(pc.std(0), .1)
            X = np.c_[g, pc]
            penalty = np.eye(X.shape[1]) * 10
            penalty[0, 0] = 0
            for held in range(2):
                check()
                train = fold != held
                fit = np.linalg.solve(X[train].T @ X[train] + penalty,
                                      X[train].T @ onehot[train][:, targets])
                check()
                predicted[np.ix_(~train, targets)] = X[~train] @ fit
        for j, k in enumerate(widths):
            check()
            a, b = self.offsets[j:j+2]
            predicted[:, a:b] = np.maximum(predicted[:, a:b], .001)
            predicted[:, a:b] /= predicted[:, a:b].sum(1, keepdims=True)
        if sabotage:
            rng = np.random.default_rng(71)
            blocks = given[["wave", "s1_2_country_asylum_lbl"]].astype(str).to_numpy()
            key = pd.factorize(pd.MultiIndex.from_arrays(blocks.T))[0]
            original = predicted.copy()
            for block in np.unique(key):
                rows = np.flatnonzero(key == block)
                predicted[rows] = original[rng.permutation(rows)]
        self.r = (onehot - predicted).astype(np.float32)
        self.denom = np.sqrt(np.maximum(J - (predicted * predicted).sum(1), 1e-6)).astype(np.float32)
        self.info = dict(null_fit_s=time.monotonic()-started, items=J,
                         categories=int(self.offsets[-1]), predictor_columns=int(g.shape[1]),
                         item_folds=2, row_folds=2, context_pc=8, sabotage=bool(sabotage))

    def raw(self, i, candidates):
        return (self.r[candidates] @ self.r[i]) / (self.denom[candidates] * self.denom[i])

    def pair_values(self, a, b):
        return np.einsum("ij,ij->i", self.r[a], self.r[b]) / (self.denom[a] * self.denom[b])

    def fit_scale(self, positive_a, positive_b, random_a, random_b):
        self.check()
        pos = self.pair_values(positive_a, positive_b)
        neg = self.pair_values(random_a, random_b)
        self.mu0 = float(neg.mean())
        self.scale = max(0.0, float(pos.mean() - neg.mean())) / max(float((pos.var()+neg.var()) / 2), 1e-6)
        terms = np.stack([
            np.einsum("ij,ij->i", self.r[random_a, a:b], self.r[random_b, a:b])
            / (self.denom[random_a] * self.denom[random_b])
            for a, b in zip(self.offsets[:-1], self.offsets[1:])], 1)
        self.info.update(raw_effective_dimension=_effective_dimension((self.y[random_a] == self.y[random_b]).astype(float)),
                         residual_effective_dimension=_effective_dimension(terms),
                         positive_mean=float(pos.mean()), random_mean=float(neg.mean()),
                         positive_sd=float(pos.std()), random_sd=float(neg.std()), scale=self.scale)

    def scores(self, i, candidates):
        return (self.raw(i, candidates) - self.mu0) * self.scale




def _twev(out, frame, giv, hid, Yv, widths, loc, cnt, tau=.5, sab=0, nthr=8, tmax=240.0, cmin=.3, rmin=.6, pmin=300, excl=0, xcl=0, xsab=0, recip=0, kdw=0.0, cpat=0, kin=0, ch=0, cha=320.0, chsel=0, chsab=0, chmin=.02):
    t0 = time.time(); info = {"gate": "on"}; rng = np.random.default_rng(0)
    def late():
        if time.time() - t0 > tmax: raise TimeoutError("twev over time")
    if "wave" not in frame.columns or not all(c in frame.columns for c in loc + cnt):
        info["gate"] = "cols"; return out, info
    w = pd.factorize(frame["wave"].astype(str), sort=True)[0]
    if len(np.unique(w)) != 2:
        info["gate"] = "waves"; return out, info
    N = len(frame); vi = np.where(~hid)[0]; hi = np.where(hid)[0]; nv = len(vi); J = Yv.shape[1]; K = np.asarray(widths, int)
    pos = np.full(N, -1); pos[vi] = np.arange(nv)
    cty = pd.factorize(frame[loc[0]].astype(str))[0]
    Cn = np.stack([pd.to_numeric(frame[c], errors="coerce").fillna(-9).to_numpy(float) for c in cnt], 1)
    resp = [g for g in giv if g != "wave" and g not in loc + cnt]
    Gs = np.stack([pd.factorize(frame[c].astype(str))[0] for c in loc[1:] + resp], 1); F = Cn.shape[1] + Gs.shape[1]
    Ya = np.where(Yv >= K[None], -1, Yv).astype(np.int16)                       # nv x J, -1 = not a listed option
    pools = {}
    for i in vi: pools.setdefault((w[i], cty[i]), []).append(i)
    pools = {k: np.array(v) for k, v in pools.items()}
    def cands(i):
        late()
        p = pools.get((1 - w[i], cty[i]))
        return p[np.abs(Cn[p] - Cn[i]).max(1) <= 1] if p is not None else np.zeros(0, int)
    CD = [cands(i) for i in range(N)]; late()
    MODE = ["bin"]; CPL = [(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]          # SBV DA2: count fields in schema order (boys/girls 0-5, 6-17, men/women 18-59, 60+)
    def gf(i, c):                                                                # len(c) x F, 1 = differs; after the first pass (cpat) counts = up / down flags + adjacent-band coupling flags
        late()
        if MODE[0] == "bin":
            return np.concatenate([Cn[c] != Cn[i], Gs[c] != Gs[i]], 1).astype(np.float32)
        d = (Cn[c] - Cn[i]) * (1 if w[i] == 0 else -1)                           # signed change round 2 - round 1
        if cpat == 4: d = d * rng.choice([-1, 1], size=d.shape)                   # SBV sabotage: signs scrambled
        cp = np.stack([(d[:, a_] < 0) & (d[:, b_] > 0) for a_, b_ in CPL], 1) if Cn.shape[1] == 8 else np.zeros((len(c), 0), bool)
        return np.concatenate([d > 0, d < 0, cp, Gs[c] != Gs[i]], 1).astype(np.float32)
    V = np.concatenate([np.stack([pd.factorize(Cn[:, k])[0] for k in range(Cn.shape[1])], 1), Gs], 1).astype(np.int64); MF = V.max(0) + 1; nc_ = Cn.shape[1]; nG_ = Gs.shape[1]
    def chf(width):                                                              # SBN CH: channel fields and their gf column (Gs columns are always the LAST nG_ columns; counts only in the binary layout)
        o = []
        for f in range(nc_ + nG_):
            if f < nc_:
                if ch & 1 and width == nc_ + nG_: o.append((f, f))
            elif (f < nc_ + len(loc) - 1 and ch & 2) or (f >= nc_ + len(loc) - 1 and ch & 4): o.append((f, width - nG_ + f - nc_))
        return o
    def SC(i, c, tab):                                                           # SBN CH: pair score; the stage's comparator + directed (earlier, later) value-transition llr on differing channel fields
        d_ = (tab[1] - tab[0]).astype(np.float32); s_ = gf(i, c) @ d_ + float(tab[0].sum())
        if len(tab) > 2:
            for (f, col), LL in tab[2].items():
                pcd = V[i, f] * MF[f] + V[c, f] if w[i] == 0 else V[c, f] * MF[f] + V[i, f]
                s_ = s_ + np.where(V[c, f] != V[i, f], LL[pcd] - d_[col] - tab[0][col], 0.0)
        return s_
    okv = np.array([i for i in vi if len(CD[i]) >= 2])
    if len(okv) < 200:
        info["gate"] = "few"; return out, info
    sm = rng.choice(okv, min(4000, len(okv)), replace=False); sc = np.array([rng.choice(CD[i]) for i in sm])
    ug = np.clip(np.stack([gf(i, np.array([c]))[0] for i, c in zip(sm, sc)]).mean(0), 1e-3, 1 - 1e-3)
    ua = np.clip((Ya[pos[sm]] == Ya[pos[sc]]).mean(0), 1e-3, .98)
    def link(mg, ma):
        lg0, lg1 = np.log((1 - mg) / (1 - ug)), np.log(mg / ug); la0, la1 = np.log((1 - ma) / (1 - ua)), np.log(ma / ua)
        dg = (lg1 - lg0).astype(np.float32); da = (la1 - la0).astype(np.float32); best = np.full(N, -1); bp = np.zeros(N)
        def work(rows):
            for i in rows:
                c = CD[i]; s = gf(i, c) @ dg + (Ya[pos[c]] == Ya[pos[i]]).astype(np.float32) @ da
                k = int(np.argmax(s)); best[i] = c[k]; bp[i] = 1 / np.exp(s - s[k]).sum()
        with ThreadPoolExecutor(nthr) as ex: list(ex.map(work, np.array_split(okv, nthr * 4)))
        late()
        return [(i, best[i]) for i in okv if bp[i] >= .9 and i < best[i] and best[best[i]] == i and bp[best[i]] >= .9]
    mg = np.full(F, .1); ma = np.minimum(.995, np.maximum(.8, ua + .01))
    for _ in range(2):
        pairs = link(mg, ma)
        if len(pairs) < 50:
            info.update(gate="nopairs", pairs=len(pairs)); return out, info
        pa = np.array(pairs)
        if cpat and MODE[0] == "bin":                                            # SBV DA2: switch to the signed encoding once self-made pairs exist
            MODE[0] = "pat"; ug = np.clip(np.stack([gf(i, np.array([c]))[0] for i, c in zip(sm, sc)]).mean(0), 1e-3, 1 - 1e-3)
        mg = np.clip(np.stack([gf(i, np.array([j]))[0] for i, j in pairs]).mean(0), .005, .6); ma = np.minimum(.995, np.maximum((Ya[pos[pa[:, 0]]] == Ya[pos[pa[:, 1]]]).mean(0), ua + .01))
    pairs = link(mg, ma)
    if len(pairs) < 50:
        info.update(gate="nopairs", pairs=len(pairs)); return out, info
    if kin:                                                                      # SBV / cx_SBUH1: re-link visible pairs with residual kinship (answer agreement beyond what each row's GIVEN predicts)
        tk0 = time.time(); kb = .6 * (tmax - (tk0 - t0))                         # SBV xwrck2 guard, merged by SB2 onto the cx_DEADL tail: kinship gets <= 60% of the stage time left; over budget = keep the stage's own pairs (a ramp, not a cliff)
        class _KinBudget(Exception): pass
        def kchk():                                                             # stage deadline first (late() raises TimeoutError and still drops the stage), then the kinship budget
            late()
            if time.time() - tk0 > kb: raise _KinBudget()
        try:
            model = _ResidualModel(frame.iloc[vi][giv], Ya, K, sabotage=kin == 2, check=kchk); pa_ = np.asarray(pairs)
            model.fit_scale(pos[pa_[:, 0]], pos[pa_[:, 1]], pos[sm], pos[sc]); kchk()
            dgk = (np.log(mg / ug) - np.log((1 - mg) / (1 - ug))).astype(np.float32); bk, bpk = np.full(N, -1), np.zeros(N)
            for n_, i in enumerate(okv):
                if n_ % 256 == 0: kchk()
                c = CD[i]; sk = gf(i, c) @ dgk + model.scores(pos[i], pos[c]); k_ = int(np.argmax(sk)); bk[i] = c[k_]; bpk[i] = 1 / np.exp(sk - sk[k_]).sum()
            kp = [(i, bk[i]) for i in okv if bpk[i] >= .9 and i < bk[i] and bk[bk[i]] == i and bpk[bk[i]] >= .9]; kchk()
            if len(kp) >= 50: pairs = kp; info["kin"] = len(kp)
            else: info["kin"] = "few"                                           # SBV xwrck2: keep the stage's own pairs (was: drop the stage)
        except _KinBudget:
            info["kin"] = "skipped_time"
        info["kin_s"] = round(time.time() - tk0, 1)
    ptw = np.full(N, -1); grp = np.arange(N)
    for i, j in pairs: ptw[i] = j; ptw[j] = i; grp[j] = grp[i]
    if xcl:                                                                      # SBU 4: one-to-one exclusion. A visible row the stage has paired with ANOTHER visible row is nobody else's candidate.
        tp = ptw.copy()
        if xsab:                                                                 # sabotage: the same number of visible rows flagged as taken, at random
            k_ = int((tp >= 0).sum()); tp = np.full(N, -1); tp[rng.choice(vi, k_, replace=False)] = -2
        tk = tp != -1; CD0 = CD
        CD = [c[~(tk[c] & (tp[c] != i))] for i, c in enumerate(CD)]; late()
        info["xcl"] = int(tk.sum())
    hf = np.zeros(N, int); hf[vi] = pd.factorize(grp[vi])[0] % 2
    def tables(rows):
        ps, ng = [], []; pi_l, pj_l, ni_l, nj_l = [], [], [], []
        for i in rows:
            if ptw[i] < 0 or len(CD[i]) < 2: continue
            o = CD[i][CD[i] != ptw[i]]
            if len(o) == 0: continue
            ps.append(gf(i, np.array([ptw[i]]))[0]); nn_ = rng.choice(o, min(3, len(o)), replace=False); ng.append(gf(i, nn_))
            pi_l.append(i); pj_l.append(ptw[i]); ni_l.extend([i] * len(nn_)); nj_l.extend(nn_.tolist())
        ps, ng = np.array(ps), np.concatenate(ng); a = (ps.sum(0) + .5) / (len(ps) + 1); b = (ng.sum(0) + .5) / (len(ng) + 1)
        t0_, t1_ = np.log((1 - a) / (1 - b)), np.log(a / b)                      # llr of 'same', 'differs'
        CHF = chf(len(t0_)) if ch else []
        if not CHF: return t0_, t1_
        LLs = {}; pi_ = np.array(pi_l); pj_ = np.array(pj_l); ni_ = np.array(ni_l); nj_ = np.array(nj_l); rs_ = np.random.default_rng(11)
        for f, col in CHF:                                                       # SBN CH: P(directed transition | silver pair, differs) v the same for in-block non-partners, EB-shrunk (cha) to the binary llr
            P2 = int(MF[f]) ** 2
            def codes(ii, jj):
                e = np.where(w[ii] == 0, ii, jj); l_ = np.where(w[ii] == 0, jj, ii); return V[e, f] * MF[f] + V[l_, f], V[e, f] != V[l_, f]
            cp_, dp = codes(pi_, pj_); cn_, dn = codes(ni_, nj_)
            npos = np.bincount(cp_[dp], minlength=P2).astype(float); nneg = np.bincount(cn_[dn], minlength=P2).astype(float)
            q = (nneg + .5) / (nneg.sum() + .5 * P2); LL = t1_[col] + np.log((npos + cha * q) / ((npos.sum() + cha) * q))
            if chsab: LL = LL[rs_.permutation(P2)]
            LLs[(f, col)] = LL.astype(np.float32)
        return t0_, t1_, LLs
    if recip:                                                                    # SBT2 C8: all rows (visible + hidden) by (round, country) for the reciprocal check
        apool = {}
        for i_ in range(N): apool.setdefault((w[i_], cty[i_]), []).append(i_)
        apool = {k_: np.array(v_) for k_, v_ in apool.items()}
    def feats(i, tab):
        c = CD[i]; s_ = SC(i, c, tab); s = np.sort(s_)[::-1]
        f_ = [s[0], s[0] - (s[1] if len(s) > 1 else s[0] - 12.0), s[0] - (s[min(4, len(s) - 1)] if len(s) > 1 else s[0] - 12.0), np.log(len(c)), 1 / np.exp(s - s[0]).sum(), float((s >= s[0] - 2).sum()), float(w[i])]
        if recip:                                                                # gap between my score with my top candidate and that candidate's best score with another row of my round (claimed visible rows excluded)
            v_ = int(c[np.argmax(s_)]); p_ = apool.get((w[i], cty[v_])); u_ = p_[np.abs(Cn[p_] - Cn[v_]).max(1) <= 1] if p_ is not None else np.zeros(0, int); u_ = u_[u_ != i]
            if xcl: u_ = u_[~(tk[u_] & (tp[u_] != v_))]
            f_.append((float(s[0]) - float(SC(v_, u_, tab).max())) if len(u_) else 12.0)
        return f_, int(c[np.argmax(s_)])
    try:
        tabs = [tables(vi[hf[vi] == 1]), tables(vi[hf[vi] == 0])]; taball = tables(vi)
    except ValueError:                                                           # review S1: exclusion left a half without pairs or negatives -> run the stage as in the base
        if not xcl: raise
        CD = CD0; xcl = 0; info["xcl"] = -1
        tabs = [tables(vi[hf[vi] == 1]), tables(vi[hf[vi] == 0])]; taball = tables(vi)
    late()
    if len(taball) > 2 and chsel:                                                # SBN CH-sel: keep the channel only if it raises the held-out (other-half tables) softmax log-lik of visible silver partners
        lb, lc_ = [], []
        for i in vi:
            if ptw[i] < 0 or len(CD[i]) < 2 or not (CD[i] == ptw[i]).any(): continue
            tb = tabs[hf[i]]; k_ = int(np.flatnonzero(CD[i] == ptw[i])[0])
            for tt_, L_ in ((tb[:2], lb), (tb, lc_)):
                s_ = SC(i, CD[i], tt_); m_ = s_.max(); L_.append(s_[k_] - m_ - np.log(np.exp(s_ - m_).sum()))
        dl = float(np.mean(lc_) - np.mean(lb)) if lb else -1.0; info["chdl"] = round(dl, 4)
        if dl < chmin: tabs = [t[:2] for t in tabs]; taball = taball[:2]; info["ch"] = "off"
        else: info["ch"] = "on"
        late()
    elif len(taball) > 2: info["ch"] = "forced"
    if xcl: okv = np.array([i for i in vi if len(CD[i]) >= 1])
    fv = [feats(i, tabs[hf[i]]) for i in okv]; Xv = np.array([f[0] for f in fv]); yv = np.array([f[1] == ptw[i] for f, i in zip(fv, okv)], float)
    okh = np.array([i for i in hi if len(CD[i]) >= (1 if xcl else 2)])
    if len(okh) == 0 or yv.sum() < 30:
        info["gate"] = "nolabels"; return out, info
    fh = [feats(i, taball) for i in okh]; Xh = np.array([f[0] for f in fh]); top = np.array([f[1] for f in fh]); late()
    if recip == 2:                                                               # SBT2 sabotage: the reciprocal feature permuted across rows
        rs_ = np.random.default_rng(7); Xv[:, 7] = Xv[rs_.permutation(len(Xv)), 7]; Xh[:, 7] = Xh[rs_.permutation(len(Xh)), 7]
    mu, sd = Xv.mean(0), Xv.std(0) + 1e-9; A = np.c_[np.ones(len(Xv)), (Xv - mu) / sd]; B = np.c_[np.ones(len(Xh)), (Xh - mu) / sd]; beta = np.zeros(A.shape[1]); reg = np.eye(A.shape[1]); reg[0, 0] = 0
    for _ in range(50):                                                          # ridge logistic by Newton steps (C = 1)
        late()
        p = 1 / (1 + np.exp(-A @ beta)); g = A.T @ (p - yv) + reg @ beta; H = (A * (p * (1 - p))[:, None]).T @ A + reg; st = np.linalg.solve(H, g); beta -= st
        if np.abs(st).max() < 1e-8: break
    late()
    pv = 1 / (1 + np.exp(-A @ beta)); c = float(pv[yv > 0].mean()); pc = np.minimum(1.0, (1 / (1 + np.exp(-B @ beta))) / max(c, 1e-6))
    rate = float(pc.mean() / max(np.minimum(1.0, pv / max(c, 1e-6)).mean(), 1e-9))   # hidden v visible posterior mass
    info.update(pairs=len(pairs), c=round(c, 3), rate=round(rate, 3))
    if TWEV_RAMP and (c < cmin or rate < rmin or len(pairs) < pmin):             # SBR R1 ramp: only where the hard gate would fire; r = 1 never reached here
        r_ = min(1.0, c / cmin) * min(1.0, rate / rmin) ** 2 * min(1.0, len(pairs) / pmin); info["r"] = round(r_, 3)
        if r_ < .25:
            info["gate"] = "file"; return out, info
        pc = pc * r_; info["gate"] = "ramp"
        if TWEV_RAMP == 2: top = rng.permutation(top)                            # sabotage
    elif c < cmin or rate < rmin or len(pairs) < pmin:                           # file-level gates: self-made labels not learnable, or hidden rows look twin-less
        info["gate"] = "file"; return out, info
    if excl:                                                                     # SBX 46: skip hidden rows that already have a key donor
        kc = (loc + cnt) if excl == 2 else [g for g in giv if g != "wave"]
        code = pd.factorize(pd.Series(list(map(tuple, frame[kc].astype(str).to_numpy()))))[0]; have = set(zip(code[vi], w[vi]))
        keep = np.array([(code[i], 1 - w[i]) not in have for i in okh]); info["excl"] = int((~keep).sum())
        if kdw > 0:                                                              # SBT2 Esoft: serve key-donor rows weakly (their key donor is already in the stack)
            pc = np.where(keep, pc, pc * kdw); info["kdw"] = kdw; keep = np.ones(len(okh), bool)
        okh, top, pc = okh[keep], top[keep], pc[keep]
    if sab: top = rng.permutation(top)
    a_ = np.flatnonzero(ptw >= 0); b_ = ptw[a_]; hpos = np.full(N, -1); hpos[hi] = np.arange(len(hi)); rows = hpos[okh]; x = tau * pc; yd_all = Ya[pos[top]]
    _sb = float(os.environ.get("SIM_TWEV_SB", .2))                                # SBF 12 lab: same-respondent exponent bonus; 0 = off (= the pick); SIM_TWEV_SBSAB=1 permutes the flag
    if _sb and Gs.shape[1] > len(loc) - 1:                                      # SBF guard: no respondent GIVEN field -> skip (= dt3bck2)
        _same = (Gs[okh][:, len(loc) - 1:] == Gs[top][:, len(loc) - 1:]).all(1)
        if os.environ.get("SIM_TWEV_SBSAB", "0") == "1": _same = np.random.default_rng(5).permutation(_same)
        x = (tau + _sb * _same) * pc; info["sb"] = (_sb, int(_same.sum()))
    new = [o.copy() for o in out]
    for j in range(J):
        late()
        k = K[j]; ya, yb = Ya[pos[a_], j], Ya[pos[b_], j]; m = (ya >= 0) & (yb >= 0); T = np.full((k, k), .5); np.add.at(T, (ya[m], yb[m]), 1); T /= T.sum(1, keepdims=True)
        yv_ = Ya[:, j]; mv = np.bincount(yv_[yv_ >= 0], minlength=k) + .5; mv = mv / mv.sum()
        yd = yd_all[:, j]; u = yd >= 0
        if not u.any(): continue
        r = rows[u]; o = np.maximum(np.asarray(new[j][r], float)[:, :k], 1e-12); tot = o.sum(1, keepdims=True)
        v = o * (T[:, yd[u]].T / mv[yd[u]][:, None]) ** x[u][:, None]; new[j][r, :k] = v / v.sum(1, keepdims=True) * tot
    late()
    info.update(pairs=len(pairs), c=round(c, 3), hid=len(okh), ge8=int((pc >= .8).sum()), mass=round(float(pc.sum()), 1), s=round(time.time() - t0, 1))
    return new, info


def _sane(o, m):
    """G3: rows with a non-finite or negative entry, or no mass, are repaired (non-finite and negative -> 0, then
    renormalised; nothing left -> the crowd marginal m). Valid rows come back untouched (the same array)."""
    o = np.asarray(o, float)
    with np.errstate(invalid="ignore"):
        bad = ~np.isfinite(o).all(1) | (o < 0).any(1) | ~(o.sum(1) > 0)
    if not bad.any():
        return o
    FAIL["sane"] = 1
    o = o.copy(); b = np.where(np.isfinite(o[bad]), np.clip(o[bad], 0.0, None), 0.0); s = b.sum(1, keepdims=True)
    o[bad] = np.where(s > 0, b / np.where(s > 0, s, 1.0), m[None, :])
    return o


def _fallback(frame, schema):
    """G4: this instrument's crowd marginal (visible counts + .5) for every blank cell, in the grader's order."""
    items = schema["items"]
    pre = [k for k, r in items.items() if r["class"] == "PREDICT"]
    hid = frame[pre].isna().all(axis=1).to_numpy()
    vec = []
    for k in pre:
        o = _opts(schema, k); ix = {v: i for i, v in enumerate(o)}
        c = np.full(len(o), 0.5)
        for v in frame.loc[~hid, k].to_numpy():
            if v in ix:
                c[ix[v]] += 1
        vec.append(list(map(float, c / c.sum())))
    return [vec[j] for _ in range(int(hid.sum())) for j in range(len(pre))]


def _valid(res, frame, schema):
    """G4: one vector per blank cell, each as long as its item's options, finite, >= 0, with mass."""
    items = schema["items"]
    pre = [k for k, r in items.items() if r["class"] == "PREDICT"]
    nh, J = int(frame[pre].isna().all(axis=1).sum()), len(pre)
    if not isinstance(res, list) or len(res) != nh * J:
        return False
    for j, k in enumerate(pre):
        a = res[j::J]
        w = len(_opts(schema, k))
        if any(len(v) != w for v in a):
            return False
        a = np.asarray(a, float).reshape(nh, w)
        if not (np.isfinite(a).all() and (a >= 0).all() and (a.sum(1) > 0).all()):
            return False
    return True


def predict(frame, schema):
    """G4: the stack in _predict; an exception or an invalid result returns this instrument's crowd marginal instead of
    failing the whole submission. A valid result is returned as is."""
    try:
        res = _predict(frame, schema)
        if _valid(res, frame, schema):
            return res
        print(f"[{TAG}] invalid result: crowd marginal", flush=True)
    except Exception as e:
        if os.environ.get("SIM_RERAISE_CUDA", "1") == "1" and (isinstance(e, MemoryError) or _is_oom(e) or _is_acc(e) or any(k in f"{type(e).__name__} {e!r}" for k in CUDA_RT)):
            print(f"[{TAG}] predict raised a CUDA / OOM fault: re-raised so the run FAILS and can be retried (SBQ R4b): {e!r}"[:300], flush=True)
            raise                                                 # SBQ STACK_RISK R4 option (b): a transient GPU fault -> failed (retryable) run, not a final marginal instrument
        print(f"[{TAG}] predict raised: {e!r}"[:300] + ": crowd marginal", flush=True)
        _cuda_fault(e)                                            # H1 F5: the next instruments run on CPU
    finally:                                                      # request pool cancellation on every exit
        if CUR_TT[0] is not None:
            _ex, _sl = CUR_TT[0]; _sl[0] = 0.0; TT_LIVE[0] = False
            try:
                _ex.shutdown(wait=False, cancel_futures=True)
            except Exception:
                pass
            CUR_TT[0] = None
        if CUR_POOL[0] is not None:
            try:
                CUR_POOL[0].shutdown(wait=False, cancel_futures=True)
            except Exception:
                pass
            CUR_POOL[0] = None
    return _fallback(frame, schema)


def _predict(frame, schema):
    t0 = time.time()
    items = schema["items"]
    giv = [k for k, r in items.items() if r["class"] == "GIVEN" and k in frame.columns]
    pre = [k for k, r in items.items() if r["class"] == "PREDICT"]
    key = len(pre)
    share = SHARE[key] if key in SHARE and sum(DONE_SHARE) + SHARE[key] <= 1.0 + 1e-9 else \
        max(0.0, 1.0 - sum(DONE_SHARE)) / max(1, N_INST - len(DONE_SHARE))
    DONE_SHARE.append(share)
    D = T0 + LIMIT * min(1.0, sum(DONE_SHARE))                  # this instrument's absolute deadline
    FAIL.clear()
    if D - t0 < 30:
        FAIL["late"] = 1
    W = max(D - t0, 1.0)
    tail = 30 + .03 * W + 5e-6 * len(pre) * len(frame) + (TWEV_RES if (TWEV and 'wave' in frame.columns and all(c in frame.columns for c in HH_LOC + HH_CNT)) else 0)   # SBX 46a fix: no reserve where the stage cannot run           # chain, mix, TabPFN blend, packing
    ST = {}

    hid = frame[pre].isna().all(axis=1).to_numpy()
    X = np.stack([_encode(frame[g].to_numpy(), list(items[g]["values"]) + (
        [schema["gated_value"]] if items[g].get("gate") else [])) for g in giv], 1)
    cards = [int(X[:, i].max()) + 1 for i in range(X.shape[1])]
    opts = [_opts(schema, k) for k in pre]
    widths = [len(o) for o in opts]
    offs = np.concatenate([[0], np.cumsum(widths)]).astype(int)
    Xv, Xh = X[~hid], X[hid]
    Yv = np.stack([_encode(frame.loc[~hid, k].to_numpy(), opts[j]) for j, k in enumerate(pre)], 1)
    Yv[Yv >= np.array(widths)] = -1       # should not happen: every visible cell is a real option
    n = len(Xv)
    marg = [np.bincount(Yv[:, j][Yv[:, j] >= 0], minlength=widths[j]) + 0.5 for j in range(len(pre))]
    marg = [m / m.sum() for m in marg]
    if n < 10 * FOLDS or len(Xh) == 0:                          # a tiny smoke-check frame: the crowd marginal
        vecs = [list(map(float, marg[j])) for _ in range(len(Xh)) for j in range(len(pre))]
        print(f"[{TAG}] tiny frame n_vis {n} n_hid {len(Xh)}: marginal", flush=True)
        return vecs
    fold = np.random.default_rng(0).permutation(n) % FOLDS

    CAT_LR[0] = CAT_LR_BY.get(key, 0.1)                       # v16o3: before the pool starts
    CAT_RND[0] = CAT_RND_BY.get(key, CAT_ROUNDS); CAT_DEP[0] = CAT_DEP_BY.get(key, 4)
    nas_ = [o.index(schema["gated_value"]) if schema.get("gated_value") in o else -1 for o in opts]
    POOL = None
    if CONC_BY.get(key):                                       # v16o: trees start now, beside the GPU stages
        h_ = D - tail
        POOL = _pool_start(h_ - min(60.0, .25 * max(h_ - time.time(), 0.0)), h_, Xv, Yv, Xh, widths, fold, marg, nas_)
    TTF = None; TTI.clear(); TT_LIVE[0] = False
    if (TT or MT) and DONORS:
        try:
            TTF = _tt_start(frame, giv, hid, X, Yv, widths, fold, D - tail)
            TT_LIVE[0] = TTF is not None
        except Exception as e:                 # optional stage: the build's path
            print(f"[{TAG}] tt skipped: {e!r}"[:300], flush=True); TTF = None; TT_LIVE[0] = False
    t = time.time()
    oof, test, cut = _folds(Xv, Yv, Xh, cards, widths, offs, fold, t0 + MLP_FRAC * W)
    if cut:
        FAIL["mlp_cut"] = 1
    ST["mlp"] = time.time() - t
    TMR = None; TMI.clear()
    if TM and DONORS:
        t = time.time()
        try:
            TMR = _tm_fit(frame, giv, hid, X, Yv, widths, offs, fold, t + TM_FRAC * W)
        except Exception as e:                 # optional stage: the build's path
            print(f"[{TAG}] tm skipped: {e!r}"[:300], flush=True); TMR = None
        ST["tm"] = time.time() - t

    t, w_used = time.time(), 0
    if WIDE and D - t < tail + 60:
        FAIL["no_wide_time"] = 1
    elif WIDE:
        w_oof, w_test, cut = _folds(Xv, Yv, Xh, cards, widths, offs, fold, t + WIDE_FRAC * (D - t - tail), wide=True)
        if cut:
            FAIL["wide_cut"] = 1
        for j in range(len(pre)):
            y = Yv[:, j]
            best, a = _logscore(oof[j], y).mean() + 1e-4, 0.0
            for c in (0.25, 0.5, 0.75, 1.0):
                s = _logscore((1 - c) * oof[j] + c * w_oof[j] + 1e-9, y).mean()
                if s > best:
                    best, a = s, c
            if a:
                oof[j] = (1 - a) * oof[j] + a * w_oof[j]; test[j] = (1 - a) * test[j] + a * w_test[j]; w_used += 1
    ST["wide"] = time.time() - t

    SV_H[0] = None; QH.clear()
    if SVNP and DONORS and all(c in frame.columns for c in HH_LOC + HH_CNT) and "wave" in frame.columns:
        try:
            SV_H[0] = _sv_pick(frame, schema, giv, hid)
        except Exception as e:                 # optional: no holdout, the build's path
            print(f"[{TAG}] svnp pick skipped: {e!r}"[:300], flush=True); SV_H[0] = None
    t, Q, pinfo = time.time(), {}, {"elig": 0, "done": 0, "ctx": n, "probe": 0.0, "item": 0.0}
    left = D - t - tail
    if left > 0:
        try:
            _pc = os.environ.get("SIM_PFN_CACHE", "")
            if _pc and os.path.exists(_pc):                       # SB-PUSH lab cache: the TabPFN stage does not depend on donors
                import pickle
                _c = pickle.load(open(_pc, "rb"))
                assert _c["shape"] == (Xv.shape, Xh.shape) and (_c["H"] is None) == (SV_H[0] is None) and (_c["H"] is None or np.array_equal(_c["H"], SV_H[0]))
                Q.update(_c["Q"]); QH.clear(); QH.update(_c["QH"]); QW.clear(); QW.update(_c["QW"]); pinfo.update(_c["pinfo"])
                print(f"[{TAG}] tabpfn cache loaded {_pc}: {len(Q)} items, QH {len(QH)}", flush=True)
            else:
                _pfn_q(Xv, Yv, Xh, marg, t + PFN_FRAC * left, Q, pinfo)
                if _pc:
                    import pickle
                    pickle.dump(dict(shape=(Xv.shape, Xh.shape), H=SV_H[0], Q=dict(Q), QH=dict(QH), QW=dict(QW), pinfo=dict(pinfo)), open(_pc, "wb"))
        except Exception as e:                # a failed TabPFN stage leaves the other vectors usable
            print(f"[{TAG}] tabpfn stopped: {e!r}"[:300], flush=True); _cuda_fault(e)
            FAIL["pfn_raised"] = 1
    if pinfo["done"] < pinfo["elig"] or pinfo["ctx"] < n:
        FAIL["pfn_partial"] = 1
    ST["pfn"] = time.time() - t

    t = time.time()
    budget = D - t - tail
    c_used, c_done, c_all, c_full = 0, 0, len(pre), False
    if POOL is not None:
        c_used, c_done, c_all, c_full = _pool_blend(POOL[0], POOL[1], Yv, widths, oof, test, key in CONC_DISCARD)
    elif budget <= 0:
        FAIL["no_tree_budget"] = 1
    else:
        c_used, c_done, c_all, c_full = _blend_trees(t + budget - min(60.0, .25 * budget), t + budget,
                                                     Xv, Yv, Xh, widths, fold, oof, test,
                                                     [o.index(schema["gated_value"]) if schema.get("gated_value") in o else -1 for o in opts])
    if c_done == 0:
        FAIL["no_tree_fit"] = 1
    if not c_full:
        FAIL["trees_partial"] = 1
    ST["cat"] = time.time() - t

    GNP_OK[0] = False; _t0 = [t_.copy() for t_ in test] if GNP else None; VMASK = None; RV = RT = None
    _o0 = [o_[SV_H[0]].copy() for o_ in oof] if (GNP and SV_H[0] is not None) else None
    _sb_o0 = _sb_t0 = _no = _nt = None
    _sb_copy_s = 0.0
    if SBO_CLM and DONORS and DONORS_FIRST:
        _sb_started = time.time()
        try:
            _sb_o0 = [np.array(o_, float, copy=True) for o_ in oof]
            _sb_t0 = [np.array(t_, float, copy=True) for t_ in test]
        except Exception as e:
            _sb_o0 = _sb_t0 = None
            SBO_INFO.clear(); SBO_INFO["gate"] = "snapshot_error"
            print(f"[{TAG}] sbo_clm snapshot skipped: {e!r}"[:300], flush=True)
        _sb_copy_s = time.time() - _sb_started
    n_don = _run_donors(frame, schema, giv, hid, pre, Yv, oof, test, fold, widths) if (DONORS and DONORS_FIRST) else 0
    if _sb_o0 is not None and n_don and n_don > 0:
        _sb_started = time.time()
        try:
            _no, _nt = _sbo_claim(frame, giv, hid, Yv, widths, oof, test, _sb_o0, _sb_t0, SV_H[0] if SV_H[0] is not None else None)
            for j_ in range(len(oof)):
                oof[j_], test[j_] = _no[j_], _nt[j_]
        except Exception as e:
            print(f"[{TAG}] sbo_clm skipped: {e!r}"[:300], flush=True); SBO_INFO["gate"] = "error"
        finally:
            _sb_o0 = _sb_t0 = _no = _nt = None
            SBO_INFO["s_total"] = round(_sb_copy_s + time.time() - _sb_started, 3)
        print(f"[{TAG}] sbo_clm {SBO_INFO}{' SABOTAGE' if SBO_CLM == 2 else ''}", flush=True)
    _sb_o0 = _sb_t0 = None
    if TMR is not None:                         # SB-PUSH2 I1: TM pooled on top of the donor posteriors
        try:
            TMI["on"] = _tm_apply(TMR, Yv, oof, test)
        except Exception as e:
            print(f"[{TAG}] tm apply skipped: {e!r}"[:300], flush=True)
        print(f"[{TAG}] tm {TMI} twin rows vis {int(TMR[2].sum())} hid {int(TMR[3].sum())}{' SABOTAGE' if TM_SAB else ''} {ST.get('tm', 0):.0f}s", flush=True)
    if TTF is not None:                        # SB-PUSH3 T1: twin-vector trees pooled on top of donors + TM
        t_tt = time.time()
        try:
            TTI["on"] = _tt_apply(TTF, min(t_tt + TT_WAIT, D - tail - 5), Yv, oof, test)
        except Exception as e:
            print(f"[{TAG}] tt apply skipped: {e!r}"[:300], flush=True)
        MTI.clear()
        if MT:
            try:
                _mt_apply(TTF, min(time.time() + TT_WAIT, D - tail - 5), Yv, oof, test, fold, widths)
            except Exception as e:
                print(f"[{TAG}] mt skipped: {e!r}"[:300], flush=True)
            print(f"[{TAG}] mt {MTI}{' SABOTAGE' if MT_SAB else ''}", flush=True)
        TTF[7][0] = 0.0; TT_LIVE[0] = False       # stop this instrument's twin-tree threads
        try:
            TTF[3].shutdown(wait=False, cancel_futures=True)
        except Exception:
            pass
        print(f"[{TAG}] tt {TTI}{' SABOTAGE' if TT_SAB else ''} wait {time.time() - t_tt:.0f}s", flush=True)
    DMASK = [np.abs(test[j_] - _t0[j_]).max(1) > 1e-12 for j_ in range(len(pre))] if (GNP and GNP_OK[0]) else None
    if DMASK is not None and _o0 is not None:
        VMASK = [np.abs(oof[j_][SV_H[0]] - _o0[j_]).max(1) > 1e-12 for j_ in range(len(pre))]
        RV = [(oof[j_][SV_H[0]] + 1e-9) / (_o0[j_] + 1e-9) for j_ in range(len(pre))]        # svnp2: donor ratio, H rows
        RT = [(test[j_] + 1e-9) / (_t0[j_] + 1e-9) for j_ in range(len(pre))]                # svnp2: donor ratio, hidden rows
    t, n_chain = time.time(), 0
    if CHAIN and time.time() < T0 + LIMIT + 170:      # SB2 xwf Fix 2 (VSC_WALL_AUDIT): skip the chain when the run is already past T0+LIMIT+170
        try:
            oof, test, n_chain = _chain(frame, hid, giv, pre, opts, Yv, fold, oof, test, schema)
        except Exception as e:
            print(f"[{TAG}] chain skipped: {e!r}"[:300], flush=True)
            FAIL["chain_raised"] = 1
    ST["chain"] = time.time() - t
    if DONORS and not DONORS_FIRST:
        _t1 = [t_.copy() for t_ in test] if GNP else None
        n_don = _run_donors(frame, schema, giv, hid, pre, Yv, oof, test, fold, widths)
        DMASK = [np.abs(test[j_] - _t1[j_]).max(1) > 1e-12 for j_ in range(len(pre))] if (GNP and GNP_OK[0]) else None

    ST["don"] = n_don
    ST["gnp"] = int(sum(m_.sum() for m_ in DMASK)) if DMASK is not None else -1
    LAM, BEST, SVI = 1.0, {}, {}
    if (SVLR or SVTF) and VMASK is not None and QH:
        try:
            _sv_lr(frame, schema, giv, hid, pre, Yv, widths, SV_H[0], [j_ for j_ in range(len(pre)) if DMASK[j_].any() or VMASK[j_].any()])
        except Exception as e:                 # optional: no likelihood arms
            print(f"[{TAG}] svlr skipped: {e!r}"[:300], flush=True); LRH.clear(); LRT.clear()
    if VMASK is not None and QH:
        try:
            LAM, SVI = _sv_decide(pre, Q, QH, QW, oof, marg, Yv, widths, VMASK, SV_H[0], BEST, RV)
        except Exception as e:                 # optional: lam 1 = the build's pool
            print(f"[{TAG}] svnp decide skipped: {e!r}"[:300], flush=True); LAM = 1.0
    if SV_FORCE and DMASK is not None:
        LAM = float(SV_FORCE)
    print(f"[{TAG}] svnp H {0 if SV_H[0] is None else len(SV_H[0])} gate {DMASK is not None} lam {LAM:.3f} {SVI}", flush=True)
    ST["lam"] = LAM
    TFV, TFI = 0.0, {}
    if SVTF and VMASK is not None and QH and GH and SV_H[0] is not None:
        try:
            cand = [j_ for j_ in range(len(pre)) if j_ in Q and (LAM, j_) in GH and DMASK[j_].any()]
            ent = {j_: float(-(test[j_][DMASK[j_]] / test[j_][DMASK[j_]].sum(1, keepdims=True) * np.log(test[j_][DMASK[j_]] / test[j_][DMASK[j_]].sum(1, keepdims=True) + 1e-12)).sum()) for j_ in cand}
            items_ = sorted(cand, key=lambda j_: -ent[j_])[:SVTF_M]
            nf_ = _sv_tf(Xv, Xh, Yv, widths, SV_H[0], items_, hid, D - tail - 30)
            H_ = SV_H[0]; Sv = {v: np.zeros(len(H_)) for v in (0.0, .25, .5, .75)}; used_ = np.zeros(len(H_), bool)
            for j_ in [j_ for j_ in items_ if j_ in QTH and j_ in QT]:
                g0, ok_, yy_, K_ = GH[(LAM, j_)]; P_, hq_ = QTH[j_]; ok2 = ok_ & hq_
                for v in Sv:
                    g = g0 ** (1 - v) * P_ ** v; g = g / g.sum(1, keepdims=True)
                    if FLOOR_INV:
                        g = floor_inverse(g, FLOOR)
                    Sv[v][ok2] += np.log(FLOOR + (1 - K_ * FLOOR) * g[np.arange(len(H_)), yy_][ok2])
                used_ |= ok2
            TFI = {"fits": nf_, "items": len(items_), "rows": int(used_.sum())}
            if used_.sum() >= 30:
                bm = 0.0
                for v in (.25, .5, .75):
                    d_ = (Sv[v] - Sv[0.0])[used_]; m_, se_ = d_.mean(), d_.std(ddof=1) / np.sqrt(len(d_))
                    TFI[f"{v:.2f}"] = (round(float(m_), 6), round(float(m_ / (se_ + 1e-12)), 2))
                    if m_ > 2 * se_ and m_ > bm:
                        TFV, bm = v, m_
        except Exception as e:                     # optional: svlr path
            print(f"[{TAG}] svtf skipped: {e!r}"[:300], flush=True); TFV = 0.0
        if os.environ.get("SIM_SVTF_FORCE", ""):
            TFV = float(os.environ["SIM_SVTF_FORCE"])
        print(f"[{TAG}] svtf v {TFV:.2f} {TFI}{' SABOTAGE' if SVTF_SAB else ''}", flush=True)
    ST["tfv"] = TFV
    t, out, ARM = time.time(), [], {}
    for j in range(len(pre)):
        best = BEST[j] if j in BEST else (_pick_mix_inv if FLOOR_INV else _pick_mix)(oof[j], marg[j], Yv[:, j])
        o = _mix(test[j], marg[j], best[1], best[2]); o_pre = o / o.sum(1, keepdims=True)
        if j in Q and np.isfinite(Q[j][1]).all():   # G6: a non-finite TabPFN output skips TabPFN for this item
            cl, P = Q[j]
            if PFN_GEO:                             # p ∝ base^(1-w) q^w; TabPFN abstains outside its classes; q floored at 1e-4
                base = o / o.sum(1, keepdims=True)
                qq = base.copy()
                qq[:, cl] = P / np.clip(P.sum(1, keepdims=True), 1e-12, None) * base[:, cl].sum(1, keepdims=True)
                qq = np.maximum(qq, 1e-4)
                w = QW.get(j, PFN_W)
                g = base ** (1 - w) * qq ** w; o = g / g.sum(1, keepdims=True)
                if DMASK is not None and DMASK[j].any():          # svnp: donor-served cells pool at w x lam (lam 1 = the build)
                    if SV_DUMP:
                        ARM[j] = (base, qq, w, RT[j])
                    if LAM >= 20:                                  # SB-PUSH svlr
                        fk = (1 if LAM < 30 else 2, j)
                        gd = base * np.maximum(LRT[fk], 1e-12) ** ((LAM - 20) if LAM < 30 else (LAM - 30)) if fk in LRT else base
                        gd = gd / gd.sum(1, keepdims=True); o = np.where(DMASK[j][:, None], gd, o)
                    elif LAM >= 10:                                # svnp2: donor-after-pool
                        gd = o * RT[j] ** ((LAM - 10) - (1 - w)); o = np.where(DMASK[j][:, None], gd / gd.sum(1, keepdims=True), o)
                    elif LAM < 1.0:
                        wd = w * LAM; gd = base ** (1 - wd) * qq ** wd; o = np.where(DMASK[j][:, None], gd / gd.sum(1, keepdims=True), o)
            else:
                q = np.full_like(o, 1e-6); q[:, cl] = P
                w = QW.get(j, PFN_W)
                o = (1 - w) * o / o.sum(1, keepdims=True) + w * q / q.sum(1, keepdims=True)
        if TFV > 0 and j in QT and DMASK is not None and DMASK[j].any():
            P_, hq_ = QT[j]; m_ = DMASK[j] & hq_
            g_ = o ** (1 - TFV) * P_ ** TFV; g_ = g_ / g_.sum(1, keepdims=True); o = np.where(m_[:, None], g_, o)
        out.append(o)

    def _fin(out):
      _toff = TAIL_OFF and key in TAIL_OFF_KEYS       # SBM T1 (19 Nov): UNHCR (213) skips both hard overrides; they lose on the uncut lead (rgG / rgH)
      try:
        out, n_sz = (out, 0) if _toff else _structzero(out, frame, hid, giv, opts, Yv, schema)
      except Exception as e:                     # the override is optional: keep the vectors on any failure
        print(f"[{TAG}] structzero skipped: {e!r}"[:300], flush=True); n_sz = -1
      if PURE_RULES and not _toff:
        try:
            out = _pure_rules(out, frame, hid, giv, Yv)
        except Exception as e:                 # optional stage: keep the vectors on any failure
            print(f"[{TAG}] rules skipped: {e!r}"[:300], flush=True)
      _tm = min(TWEV_TMAX, T0 + LIMIT + AVL_OVER + TWEV_RES - time.time())   # SB2 P35xs (review REVIEW_P35x SF1): twev ends by T0+LIMIT+OVER+RES even if avl used the reserve
      if TWEV and _tm < 10:
        print(f"[{TAG}] twev skipped: time {_tm:.0f}s", flush=True)
      elif TWEV:                               # SBX 46a: optional stage, vectors kept on any failure
        if TWEV_KIN and _tm < TWEV_KMIN: print(f"[{TAG}] twev kin off: _tm {_tm:.0f}s", flush=True)
        try:
            _tw_lim = None
            if os.environ.get("SIM_TWEV_BLAS1", "1") == "1":       # SB2 19 Nov: BLAS single-threaded while the twin stage runs its Python thread pool (8 threads x BLAS teams spun under the quota); restored right after
                try:
                    from threadpoolctl import threadpool_limits as _tpl
                    _tw_lim = _tpl(limits=1, user_api="blas")
                except Exception:
                    _tw_lim = None
            try:
                out, twi_ = _twev(out, frame, giv, hid, Yv, widths, HH_LOC, HH_CNT, tau=float(os.environ.get("SIM_TWEV_TAU", .5)), sab=int(TWEV == 2), nthr=NTHR, tmax=_tm, excl=1, rmin=.8, xcl=int(TWEV_XCL > 0), xsab=int(TWEV_XCL == 2), recip=TWEV_RECIP, kdw=TWEV_KDW, cpat=TWEV_CPAT, kin=(TWEV_KIN if _tm >= TWEV_KMIN else 0), ch=TWEV_CH, cha=TWEV_CHA, chsel=TWEV_CHSEL, chsab=TWEV_CHSAB, chmin=TWEV_CHMIN)
            finally:
                if _tw_lim is not None:
                    try: _tw_lim.restore_original_limits()
                    except Exception: pass
            print(f"[{TAG}] twev {twi_}", flush=True)
        except Exception as e:
            print(f"[{TAG}] twev skipped: {e!r}"[:300], flush=True)
      out = [_sane(o, marg[j]) for j, o in enumerate(out)]          # G3
      if FLOOR_INV:                              # last step: return the vector whose floored version the grader scores best
        out = [floor_inverse(o, FLOOR) for o in out]
        out = [_sane(o, marg[j]) for j, o in enumerate(out)]      # G3
      out, code = _canary(out, marg, widths, len(Xh), key)
      vecs = np.empty(len(Xh) * len(pre), dtype=object)
      for j in range(len(pre)):
        vecs[j::len(pre)] = list(out[j])
      return [list(map(float, v)) for v in vecs], n_sz, code

    if SV_DUMP and ARM:                        # lab only: the same assembly at forced lam on the donor cells
        for l in (1.0, 2 / 3, 1 / 3, 0.0, 10.5, 10.75, 11.0) + ((20.5, 21.0, 30.5, 31.0) if SVLR else ()):
            o_l = [x.copy() for x in out]
            for j, (b_, q_, w_, rt_) in ARM.items():
                if l >= 20:
                    fk = (1 if l < 30 else 2, j)
                    g_ = b_ * np.maximum(LRT[fk], 1e-12) ** ((l - 20) if l < 30 else (l - 30)) if fk in LRT else b_
                elif l >= 10:
                    g_ = b_ ** (1 - w_) * q_ ** w_; g_ = g_ / g_.sum(1, keepdims=True); g_ = g_ * rt_ ** ((l - 10) - (1 - w_))
                else:
                    g_ = b_ ** (1 - w_ * l) * q_ ** (w_ * l)
                g_ = g_ / g_.sum(1, keepdims=True)
                o_l[j] = np.where(DMASK[j][:, None], g_, o_l[j])
            r_l = _fin(o_l)[0]; d_ = f"{SV_DUMP}_l{l:.3f}"; os.makedirs(d_, exist_ok=True)
            a_ = np.empty(len(r_l), dtype=object); a_[:] = [np.asarray(v, float) for v in r_l]
            np.save(os.path.join(d_, os.environ.get("SIM_SVNP_INST", "unhcr") + ".npy"), a_, allow_pickle=True)
    res, n_sz, code = _fin(out)
    ST["sz"] = n_sz
    ST["mix"] = time.time() - t
    print(f"[{TAG}] fail {sorted(FAIL)} canary {code} dev {DEV} thr {NTHR} n_vis {n} n_hid {len(Xh)} items {len(pre)} "
          f"window {t0 - T0:.0f}-{D - T0:.0f}s wide {w_used} cat {c_used}/{c_done}/{c_all} chain {n_chain} "
          f"pfn {pinfo['done']}/{pinfo['elig']} ctx {pinfo['ctx']} probe {pinfo['probe']:.1f}s item<= {pinfo['item']:.1f}s "
          f"| " + " ".join(f"{k} {v:.0f}" for k, v in ST.items()) + f" | {time.time() - t0:.1f}s", flush=True)
    return res


RAISED = ("trees_raised", "pfn_raised", "chain_raised")
CUT_ALL = ("late", "mlp_cut", "no_wide_time", "wide_cut", "pfn_partial")
CUT_FULL = CUT_ALL + ("no_tree_budget", "no_tree_fit", "trees_partial")
CANARY_NEEDS = {12: CUT_FULL}            # v11c: UNICEF must run every stage to the end; WB and UNHCR the TabPFN stage


def _structzero(out, frame, hid, giv, opts, Yv, schema):
    """Structural-zero override (see the module docstring). Returns (out, cells touched)."""
    gv = schema.get("gated_value")
    if gv is None:
        return out, 0
    Gall = np.stack([pd.factorize(frame[g].astype(str))[0] for g in giv], 1)
    Gv, Gh = Gall[~hid], Gall[hid]
    out = [o.copy() for o in out]; touched = 0
    for j, o in enumerate(opts):
        if gv not in o:
            continue
        na = o.index(gv); z = (Yv[:, j] == na).astype(float)
        if z.mean() in (0.0, 1.0):
            continue
        best, who = _h(z, np.zeros(len(z), int), 1) - 1e-6, -1
        for g in range(Gv.shape[1]):
            k = int(Gall[:, g].max()) + 1
            e = _h(z, Gv[:, g], k)
            if e < best:
                best, who = e, g
        if who < 0:
            continue
        k = int(Gall[:, who].max()) + 1
        n = np.bincount(Gv[:, who], minlength=k); c = np.bincount(Gv[:, who], weights=z, minlength=k)
        rate = np.where(n > 0, c / np.maximum(n, 1), z.mean())
        nh, rh = n[Gh[:, who]], rate[Gh[:, who]]
        det = (nh >= 20) & ((rh >= .99) | (rh <= .01))
        p = out[j] / out[j].sum(1, keepdims=True)
        if OV_AGREE:                               # never against the model: the model's P(NA) must already be on the group's side
            det &= np.where(rh >= .99, p[:, na] >= .5, p[:, na] < .5)
        if not det.any():
            continue
        new = np.where(det, (c[Gh[:, who]] + .5) / (nh + 1), p[:, na])
        out[j] = _swap_na(p, new, na); touched += int(det.sum())
    return out, touched


def _canary(out, marg, widths, nh, key):
    """CANARY 0: off (the Final). 2 (v11c): this instrument returns the uniform distribution if one of its stages
    raised, else the crowd marginal if its required path was cut by time, else its normal vectors. The signal comes
    only from our own code path, never from labels."""
    if CANARY == 0 or not FAIL:
        return out, "off" if CANARY == 0 else "full"
    if any(k in FAIL for k in RAISED):
        return [np.full((nh, w), 1.0 / w) for w in widths], "uniform"
    if any(k in FAIL for k in CANARY_NEEDS.get(key, CUT_ALL)):
        return [np.tile(marg[j], (nh, 1)) for j in range(len(widths))], "marginal"
    return out, "full"


KAPPAS = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0)


def _donor(kv, kh, y, oof, test, fold, K):
    """Exact-match donor blend for one item. Returns (oof', test', kappa); kappa = inf means off (vectors unchanged)."""
    ok = y >= 0
    nf = int(fold.max()) + 1; nk = int(max(kv.max(), kh.max())) + 1
    tot = np.zeros((nk, K)); np.add.at(tot, (kv[ok], y[ok]), 1)
    per = np.zeros((nf, nk, K))
    for f in range(nf):
        m = ok & (fold == f); np.add.at(per[f], (kv[m], y[m]), 1)
    c_oof = tot[kv] - per[fold, kv]; n_oof = c_oof.sum(1, keepdims=True)
    yy = np.where(ok, y, 0)

    def ls(P):
        P = P / P.sum(1, keepdims=True)
        return np.log(FLOOR + (1 - K * FLOOR) * P[np.arange(len(y)), yy])[ok].mean()
    c_oof, n_oof = _pur(c_oof)                                 # purity: the pool counts as one observation (ledger 332)
    kap = _pick_kappa(lambda P: _lsr(P, yy, K)[ok], oof, c_oof, n_oof)
    if np.isinf(kap):
        return oof, test, kap
    c_t = tot[kh]; n_t = c_t.sum(1, keepdims=True)
    c_t, n_t = _pur(c_t)
    return (c_oof + kap * oof) / (n_oof + kap), (c_t + kap * test) / (n_t + kap), kap


def _lsr(P, yy, K):
    P = P / P.sum(1, keepdims=True)
    return np.log(FLOOR + (1 - K * FLOOR) * P[np.arange(len(yy)), yy])


def _pur(c):
    """purity: per-row donor counts normalised to a distribution (weight 1 per row with any donor, 0 without)."""
    n = c.sum(1, keepdims=True)
    return c / np.where(n > 0, n, 1.0), (n > 0).astype(float)


def _pick_kappa(lsr, oof, c_oof, n_oof):
    """kappa with the best mean OOF score; ON only if its per-row gain over the base exceeds 2 standard errors (v14h,
    main's v14g audit item 3: the old 1e-5 rule switched on items that lost at test). inf = off."""
    base = lsr(oof); best, kap, bd = base.mean(), np.inf, None
    for k in KAPPAS:
        d = lsr((c_oof + k * oof) / (n_oof + k)) - base
        if base.mean() + d.mean() > best + 1e-5:
            best, kap, bd = base.mean() + d.mean(), k, d
    if bd is None or len(bd) < 3 or bd.mean() <= 2 * bd.std(ddof=1) / np.sqrt(len(bd)):
        return np.inf
    return kap


def _hh_groups(frame, schema, pm1):
    """(n x M) household group ids per row (column 0 = own group); id G = empty sentinel. Keys exist only in memory."""
    loc = np.unique(np.stack([pd.factorize(frame[c].astype(str))[0] for c in HH_LOC], 1), axis=0, return_inverse=True)[1].reshape(-1)
    cnt = np.stack([frame[c].astype(str).map({v: i for i, v in enumerate(schema["items"][c]["values"])}).fillna(-1).astype(int).to_numpy()
                    for c in HH_CNT], 1)
    full = np.concatenate([loc[:, None], cnt], 1)
    uniq, own = np.unique(full, axis=0, return_inverse=True); own = own.reshape(-1); G = len(uniq)
    if not pm1:
        return own[:, None], G
    index = {tuple(r): i for i, r in enumerate(uniq)}
    nb = np.full((len(full), 1 + 2 * len(HH_CNT)), G, np.int64); nb[:, 0] = own
    for i, r in enumerate(full):
        k = 1
        for c in range(len(HH_CNT)):
            for d in (-1, 1):
                q = r.copy(); q[1 + c] += d; nb[i, k] = index.get(tuple(q), G); k += 1
    return nb, G


def _lsr(P, yy, K):
    P = P / P.sum(1, keepdims=True)
    return np.log(FLOOR + (1 - K * FLOOR) * P[np.arange(len(yy)), yy])


def _pick_kappa(lsr, oof, c_oof, n_oof):
    """kappa with the best mean OOF score; ON only if its per-row gain over the base exceeds 2 standard errors (v14h,
    main's v14g audit item 3: the old 1e-5 rule switched on items that lost at test). inf = off."""
    base = lsr(oof); best, kap, bd = base.mean(), np.inf, None
    for k in KAPPAS:
        d = lsr((c_oof + k * oof) / (n_oof + k)) - base
        if base.mean() + d.mean() > best + 1e-5:
            best, kap, bd = base.mean() + d.mean(), k, d
    if bd is None or len(bd) < 3 or bd.mean() <= 2 * bd.std(ddof=1) / np.sqrt(len(bd)):
        return np.inf
    return kap


def _donor_nb(nbv, nbh, G, y, oof, test, fold, K, wv, wh):
    """_donor over household neighbour groups, donors from the OTHER round only (a same-round match is always a different
    household; wv / wh = 0/1 round codes); own fold excluded for OOF; kappa by _pick_kappa (inf = off)."""
    ok = y >= 0; yy = np.where(ok, y, 0); nf = int(fold.max()) + 1
    tot = np.zeros((G + 1, 2, K)); np.add.at(tot, (nbv[ok, 0], wv[ok], y[ok]), 1)
    per = np.zeros((nf, G + 1, 2, K))
    for f in range(nf):
        m = ok & (fold == f); np.add.at(per[f], (nbv[m, 0], wv[m], y[m]), 1)
    sv, sh = (1 - wv)[:, None], (1 - wh)[:, None]
    c_oof = tot[nbv, sv].sum(1) - per[fold[:, None], nbv, sv].sum(1); n_oof = c_oof.sum(1, keepdims=True)
    c_oof, n_oof = _pur(c_oof)                                 # purity: the pool counts as one observation (ledger 332)
    kap = _pick_kappa(lambda P: _lsr(P, yy, K)[ok], oof, c_oof, n_oof)
    if np.isinf(kap):
        return oof, test, kap
    c_t = tot[nbh, sh].sum(1); n_t = c_t.sum(1, keepdims=True)
    c_t, n_t = _pur(c_t)
    return (c_oof + kap * oof) / (n_oof + kap), (c_t + kap * test) / (n_t + kap), kap


def _donor_eh(kv, kh, nbv, nbh, G, y, oof, test, fold, K, wv, wh):
    """exact_hh: other-round donors from the row's EXACT-key group when it has any, else from its household group."""
    ok = y >= 0; yy = np.where(ok, y, 0); nf = int(fold.max()) + 1; nk = int(max(kv.max(), kh.max())) + 1
    def counts(gv, ng):
        tot = np.zeros((ng + 1, 2, K)); np.add.at(tot, (gv[ok], wv[ok], y[ok]), 1)
        per = np.zeros((nf, ng + 1, 2, K))
        for f in range(nf):
            m_ = ok & (fold == f); np.add.at(per[f], (gv[m_], wv[m_], y[m_]), 1)
        return tot, per
    tE, pE = counts(kv, nk); tH, pH = counts(nbv[:, 0], G)
    cE = tE[kv, 1 - wv] - pE[fold, kv, 1 - wv]; cH = tH[nbv[:, 0], 1 - wv] - pH[fold, nbv[:, 0], 1 - wv]
    useE = cE.sum(1, keepdims=True) > 0
    c_oof = np.where(useE, cE, cH); n_oof = c_oof.sum(1, keepdims=True)
    c_oof, n_oof = _pur(c_oof)                                 # purity: the pool counts as one observation (ledger 332)
    kap = _pick_kappa(lambda P: _lsr(P, yy, K)[ok], oof, c_oof, n_oof)
    if np.isinf(kap):
        return oof, test, kap
    ctE = tE[kh, 1 - wh]; ctH = tH[nbh[:, 0], 1 - wh]
    c_t = np.where(ctE.sum(1, keepdims=True) > 0, ctE, ctH); n_t = c_t.sum(1, keepdims=True)
    c_t, n_t = _pur(c_t)
    return (c_oof + kap * oof) / (n_oof + kap), (c_t + kap * test) / (n_t + kap), kap


TOL_COLS = [c for c in os.environ.get("SIM_TOL_COLS", "s1_2_country_asylum_lbl,s2_4a_origin_governorate_lbl,s2_1_hh_relationship_lbl,"
            "s2_1b_age,s2_1c_education_level_lbl,s2_1d_marital_status_lbl,s2_2_single_parent_lbl").split(",") if c]
TOL_ADULTS = [c for c in os.environ.get("SIM_TOL_ADULTS", "s2_3_men_18_59,s2_3_women_18_59").split(",") if c]


def _donor_other(gv_all, hid, y, oof, test, fold, K, wv, wh):
    """SB2: other-round donors on one key (codes gv_all over all rows); purity; kappa by _pick_kappa (inf = off)."""
    kv, kh = gv_all[~hid], gv_all[hid]
    ok = y >= 0; yy = np.where(ok, y, 0); nf = int(fold.max()) + 1; ng = int(gv_all.max()) + 1
    tot = np.zeros((ng, 2, K)); np.add.at(tot, (kv[ok], wv[ok], y[ok]), 1)
    per = np.zeros((nf, ng, 2, K))
    for f in range(nf):
        m_ = ok & (fold == f); np.add.at(per[f], (kv[m_], wv[m_], y[m_]), 1)
    c_oof = tot[kv, 1 - wv] - per[fold, kv, 1 - wv]; n_oof = c_oof.sum(1, keepdims=True)
    c_oof, n_oof = _pur(c_oof)
    kap = _pick_kappa(lambda P: _lsr(P, yy, K)[ok], oof, c_oof, n_oof)
    if np.isinf(kap):
        return oof, test, kap
    c_t = tot[kh, 1 - wh]; n_t = c_t.sum(1, keepdims=True); c_t, n_t = _pur(c_t)
    return (c_oof + kap * oof) / (n_oof + kap), (c_t + kap * test) / (n_t + kap), kap


BO_T3 = os.environ.get("SIM_BO_T3", "0") == "1"
BO_MIN = 30


DON_GUARD = os.environ.get("SIM_DON_GUARD", "1") == "1"   # DECISION_6NOV 04:39Z: guard v1 ON by default
GUARD_RATE = os.environ.get("SIM_GUARD_RATE", "1") == "1"
GUARD_REF = os.environ.get("SIM_GUARD_REF", "perm")   # perm: a random visible row's donors; same: same-round same-key rows


def _guard_f(klist, hid, Yv, oof, test, widths, wv, wh):
    """stranger share f per key (see patches/guard_patch.py); zeros when hidden donors look like visible donors."""
    nv, nh, S = int((~hid).sum()), int(hid.sum()), len(klist); rng = np.random.default_rng(0)
    Av, Nv, As, Ns = np.zeros((S, nv)), np.zeros((S, nv)), np.zeros((S, nv)), np.zeros((S, nv)); Ah, Nh = np.zeros((S, nh)), np.zeros((S, nh))
    perm = rng.permutation(nv)
    for j in range(len(oof)):
        y = Yv[:, j]; ok = y >= 0; K = int(widths[j])
        lo = np.log(FLOOR + (1 - K * FLOOR) * oof[j] / oof[j].sum(1, keepdims=True)); lt = np.log(FLOOR + (1 - K * FLOOR) * test[j] / test[j].sum(1, keepdims=True))
        for si, g in enumerate(klist):
            kv, qv, kh, ng_ = _kq(g, hid); tot = np.zeros((ng_, 2, K)); np.add.at(tot, (kv[ok], wv[ok], y[ok]), 1)
            cv = tot[qv, 1 - wv]; n = cv.sum(1); hv = n > 0; cv = cv / np.where(hv, n, 1)[:, None]
            Av[si, hv] += (cv[hv] * lo[hv]).sum(1); Nv[si, hv] += 1
            if GUARD_REF == "same":            # v2: stranger = SAME-round rows with the same key (never the same household), self removed
                cs = tot[kv, wv]; cs[np.where(ok)[0], y[ok]] -= 1; n2 = cs.sum(1); hs = n2 > 0; cs = cs / np.where(hs, n2, 1)[:, None]
                As[si, hs] += (cs[hs] * lo[hs]).sum(1); Ns[si, hs] += 1
            else:
                hs = hv & hv[perm]; As[si, hs] += (cv[perm][hs] * lo[hs]).sum(1); Ns[si, hs] += 1
            ch = tot[kh, 1 - wh]; n = ch.sum(1); hh_ = n > 0; ch = ch / np.where(hh_, n, 1)[:, None]
            Ah[si, hh_] += (ch[hh_] * lt[hh_]).sum(1); Nh[si, hh_] += 1
    f = np.zeros(S)
    for si in range(S):
        a, b, c = Av[si][Nv[si] > 0] / Nv[si][Nv[si] > 0], Ah[si][Nh[si] > 0] / Nh[si][Nh[si] > 0], As[si][Ns[si] > 0] / Ns[si][Ns[si] > 0]
        if min(len(a), len(b), len(c)) < 30:
            continue
        d = a.mean() - b.mean(); se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b)); gap = a.mean() - c.mean()
        if d > 3 * se and d > .02 and gap > 0:
            f[si] = float(np.clip(d / gap, 0, 1))
        print(f"[{TAG}] guard key {si}: vis {a.mean():.4f} (n {len(a)}) hid {b.mean():.4f} (n {len(b)}) stranger {c.mean():.4f} z {-d / (se + 1e-12):+.1f} f {f[si]:.3f}", flush=True)
    if GUARD_RATE:
        for si, g in enumerate(klist):
            kv, qv, kh, ng_ = _kq(g, hid); cnt = np.zeros((ng_, 2)); np.add.at(cnt, (kv, wv), 1)
            mv, mh = cnt[qv, 1 - wv] > 0, cnt[kh, 1 - wh] > 0; rv, rh = mv.mean(), mh.mean()
            nw = np.bincount(wv, minlength=2).astype(float); same = cnt[kv, wv] - 1 > 0
            sw = [1 - (1 - min(same[wv == w_].mean(), .999999)) ** (nw[1 - w_] / max(nw[w_] - 1, 1)) if (wv == w_).any() else 0.0 for w_ in (0, 1)]
            s_ = float(np.clip((sw[0] * (wv == 0).sum() + sw[1] * (wv == 1).sum()) / len(wv), 0, .999))
            se = np.sqrt(rv * (1 - rv) / len(mv) + rh * (1 - rh) / len(mh)); g_ = 0.0
            if rv > 0 and rh > 0 and rh < rv - 3 * se and rh < .9 * rv:
                tv, th = max(rv - s_, 0) / (1 - s_), max(rh - s_, 0) / (1 - s_)
                Fv, Fh = min((1 - tv) * s_ / rv, 1.0), min((1 - th) * s_ / rh, 1.0)
                g_ = float(np.clip((Fh - Fv) / max(1 - Fv, 1e-9), 0, 1))
            print(f"[{TAG}] rate guard key {si}: match vis {rv:.3f} hid {rh:.3f} coincidence {s_:.3f} z {(rh - rv) / (se + 1e-12):+.1f} g {g_:.3f}", flush=True)
            f[si] = 1 - (1 - f[si]) * (1 - g_)
    return f


AVL = os.environ.get("SIM_AVL", '0') == "1"; AVL_SAB = os.environ.get("SIM_AVL_SAB", "0") == "1"   # SBX H2: answer-verified learned linkage
AVL_THR = float(os.environ.get("SIM_AVL_THR", .8)); AVL_POS = os.environ.get("SIM_AVL_POS", "tw")
AVL_MAXP = int(os.environ.get("SIM_AVL_MAXP", 9000000)); AVL_MAXC = int(os.environ.get("SIM_AVL_MAXC", 900000000)); AVL_MAXJ = int(os.environ.get("SIM_AVL_MAXJ", 48))   # P1kg35: caps lifted + J 48 (SBZ 31/33)
AVL_KMIN = int(os.environ.get("SIM_AVL_KMIN", 2))   # SB2 erg: min fold worlds kept on a time cut (below it the stage is skipped as before)
AVL_OVER = float(os.environ.get("SIM_AVL_OVER", 100)); AVL_MIN = float(os.environ.get("SIM_AVL_MIN", 30))   # P1kg35d fix A: the stage must end by T0 + LIMIT + AVL_OVER; skip if < AVL_MIN s left
AVL_TMAX = float(os.environ.get("SIM_AVL_TMAX", 240)); AVL_LOOPS = int(os.environ.get("SIM_AVL_LOOPS", 2)); AVL_NNEG = int(os.environ.get("SIM_AVL_NNEG", 30))
AVLI = {}; AVO = [0]


def _kq(g, hid):
    """donor key -> (count ids of the visible rows, lookup ids visible, lookup ids hidden, number of ids). An array is a group key
    (the build's keys: all three are the same codes); a tuple is a pointer key (AVL: each row looks up ONE donor row)."""
    if isinstance(g, tuple):
        return g[0], g[1], g[2], len(g[0]) + 1
    return g[~hid], g[~hid], g[hid], int(g.max()) + 1


def _avl_fit(X, y):
    """ridge logistic by Newton on standardised columns (float32 products); returns (coefficients on the raw columns, intercept)."""
    mu = X.mean(0, dtype=np.float64); sd = X.std(0, dtype=np.float64) + 1e-6
    Xs = torch.from_numpy(np.ascontiguousarray((X - mu.astype(np.float32)) / sd.astype(np.float32))); F = Xs.shape[1]; b = np.zeros(F + 1)
    yf = torch.from_numpy(y.astype(np.float32))
    for _ in range(25):
        p = torch.sigmoid(torch.clamp(Xs @ torch.from_numpy(b[:F].astype(np.float32)) + float(b[F]), -30, 30)); r = p - yf; wt = p * (1 - p)
        g = np.r_[(Xs.T @ r).numpy().astype(np.float64) + b[:F], float(r.sum(dtype=torch.float64))]
        XW = Xs * wt[:, None]; H = np.empty((F + 1, F + 1)); H[:F, :F] = (XW.T @ Xs).numpy(); H[:F, F] = H[F, :F] = XW.sum(0, dtype=torch.float64).numpy()
        H[F, F] = float(wt.sum(dtype=torch.float64)); H[np.arange(F), np.arange(F)] += 1.0; H[np.arange(F + 1), np.arange(F + 1)] += 1e-8
        st = np.linalg.solve(H, g); b -= st
        if np.abs(st).max() < 1e-4:
            break
    cf = b[:F] / sd
    return cf.astype(np.float32), float(b[F] - (cf * mu).sum())


def _avl_lse(z, z0, st, ln):
    mx = np.maximum(np.maximum.reduceat(z, st), z0)
    return mx + np.log(np.add.reduceat(np.exp(z - np.repeat(mx, ln)), st) + np.exp(z0 - mx))


def _avl_nm(f, x0, step, maxit=160, xtol=2e-3, ftol=1e-3):
    """Nelder-Mead (numpy only)."""
    n = len(x0); S = np.tile(np.asarray(x0, float), (n + 1, 1))
    for i in range(n):
        S[i + 1, i] += step[i]
    fv = np.array([f(x) for x in S])
    for _ in range(maxit):
        o = np.argsort(fv); S, fv = S[o], fv[o]
        if np.abs(S[1:] - S[0]).max() <= xtol and np.abs(fv[1:] - fv[0]).max() <= ftol:
            break
        c = S[:-1].mean(0); xr = 2 * c - S[-1]; fr = f(xr)
        if fr < fv[0]:
            xe = 3 * c - 2 * S[-1]; fe = f(xe)
            S[-1], fv[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < fv[-2]:
            S[-1], fv[-1] = xr, fr
        else:
            xc = c + .5 * ((xr if fr < fv[-1] else S[-1]) - c); fc = f(xc)
            if fc < min(fr, fv[-1]):
                S[-1], fv[-1] = xc, fc
            else:
                S[1:] = S[0] + .5 * (S[1:] - S[0]); fv[1:] = [f(x) for x in S[1:]]
    return S[int(np.argmin(fv))]


def _avl_gold(f, a, b, n=22):
    g = (5 ** .5 - 1) / 2; c = b - g * (b - a); d = a + g * (b - a); fc, fd = f(c), f(d)
    for _ in range(n):
        if fc < fd:
            b, d, fd = d, c, fc; c = b - g * (b - a); fc = f(c)
        else:
            a, c, fc = c, d, fd; d = a + g * (b - a); fd = f(d)
    return (a + b) / 2


def _avl_calib(s, la, logn, st, th0=None):
    """row model: prior over the row's candidates + a 'no twin visible' option = softmax(tau s_c ; b0 + b1 log n); LABEL-FREE fit:
    maximise the marginal likelihood of the answers, sum_rows log(sum_c prior_c exp(la_c) + prior_0) (avl.py calib_fit)."""
    ln = np.diff(np.r_[st, len(s)])
    if len(st) > 1200:                              # 3 parameters: a fixed sample of 1000 rows is plenty
        pick = np.zeros(len(st), bool); pick[np.random.default_rng(5).choice(len(st), 1000, replace=False)] = True
        e = np.repeat(pick, ln); s, la, logn = s[e], la[e], logn[e]; ln = ln[pick]; st = np.r_[0, np.cumsum(ln)[:-1]]
    lr = logn[st]

    def nll(th):
        zs = np.exp(min(max(th[0], -8.0), 8.0)) * s; z0 = th[1] + th[2] * lr
        return -float((_avl_lse(zs + la, z0, st, ln) - _avl_lse(zs, z0, st, ln)).sum())
    return _avl_nm(nll, np.array([-0.5, 0.0, 1.0]) if th0 is None else np.asarray(th0, float), (.4, .6, .3) if th0 is None else (.1, .15, .08))


def _avl_post(s, la, logn, st, th, shift=0.0):
    z = np.exp(min(max(th[0], -8.0), 8.0)) * s + la; z0 = th[1] + th[2] * logn[st] + shift; ln = np.diff(np.r_[st, len(s)])
    return np.exp(z - np.repeat(_avl_lse(z, z0, st, ln), ln))


def _avl_fmax(sc, st, ln, gid):
    """mask of the first maximum of sc inside each segment (segments = consecutive runs); -inf never wins."""
    e = np.flatnonzero((sc == np.repeat(np.maximum.reduceat(sc, st), ln)) & (sc > -np.inf)); out = np.zeros(len(sc), bool)
    if len(e):
        g = gid[e]; out[e[np.r_[True, g[1:] != g[:-1]]]] = True
    return out


def _avl_links(frame, schema, giv, hid, Yv, fold, widths, w):
    """SBX H2. Returns the pointer key (count ids, donor id per visible row from its fold-blind world, donor id per hidden row from the
    all-visible world; id nv = no donor), or None when gated. Reads GIVEN of all rows and the answers of visible rows only."""
    t0 = time.time(); N = len(frame); isv = ~hid; nv = int(isv.sum()); J = Yv.shape[1]; nf = int(fold.max()) + 1
    _tl = min(AVL_TMAX, T0 + LIMIT + AVL_OVER - t0); AVLI["tl"] = round(_tl, 1)       # P1kg35d fix A: deadline-aware budget
    if _tl < AVL_MIN:
        AVLI.update(gate="time"); return None
    cols = [g for g in giv if g not in DONOR_DROP]; Gc = np.zeros((N, len(cols)), np.int64)
    for k, c in enumerate(cols):
        vals = [str(v) for v in schema["items"][c]["values"]]
        Gc[:, k] = frame[c].astype(str).map({v: i for i, v in enumerate(vals)}).fillna(len(vals)).astype(int).to_numpy()
    logf = [np.log((np.bincount(Gc[:, k]) + .5) / (N + .5 * (Gc[:, k].max() + 1))) for k in range(len(cols))]
    ci, gi, oi = (cols.index(c) for c in HH_LOC); fa = np.full(N, -1); fa[isv] = fold; vpos = np.cumsum(isv) - 1
    # ---- blocks -> directed candidate pairs (q any row, c a visible row of the other round; country & (origin | governorate))
    PQ, PC, tot = [], [], 0
    for cc in np.unique(Gc[:, ci]):
        idx = np.where(Gc[:, ci] == cc)[0]
        for ww in (0, 1):
            q = idx[w[idx] == ww]; c = idx[(w[idx] != ww) & isv[idx]]
            if not len(q) or not len(c):
                continue
            a, b = np.nonzero((Gc[q, oi][:, None] == Gc[c, oi][None]) | (Gc[q, gi][:, None] == Gc[c, gi][None]))
            PQ.append(q[a]); PC.append(c[b]); tot += len(a)
            if tot > AVL_MAXP:
                AVLI.update(gate="pairs", pairs=int(tot)); return None
    if not PQ:
        AVLI.update(gate="nopairs"); return None
    PQ = np.concatenate(PQ); PC = np.concatenate(PC); o = np.argsort(PQ, kind="stable"); PQ, PC = PQ[o], PC[o]; M = len(PQ)
    # ---- comparison vectors on GIVEN only (once): per column equal, |difference| (ordered columns), rarity of the shared level; + 2 world columns
    ordc = set(HH_CNT) | {c for c in cols if c == "age" or c.endswith("_age")}
    F = sum(3 if c in ordc else 2 for c in cols) + 2; X = np.zeros((M, F), np.float32); f_ = 0
    hk = {cols.index(c) for c in HH_LOC + HH_CNT}; h = np.zeros(M, np.int64)
    for k, c in enumerate(cols):
        a, b = Gc[PQ, k], Gc[PC, k]; eq = a == b; X[:, f_] = eq; f_ += 1
        if c in ordc:
            X[:, f_] = np.minimum(np.abs(a - b), 3); f_ += 1
        X[:, f_] = np.where(eq, -logf[k][a], 0); f_ += 1
        if k in hk:
            h += eq
    nh_ = len(hk) + 2; rk = np.random.default_rng(0).random(M); fq, fc = fa[PQ], fa[PC]; d0M = w[PQ] == 0
    # ---- answer agreement of the visible x visible pairs (once)
    jj = np.arange(J) if J <= AVL_MAXJ else np.unique(np.linspace(0, J - 1, AVL_MAXJ).astype(int)); Jn = len(jj); wd = np.asarray(widths)[jj].astype(int)
    um = isv[PQ] & d0M; UA, UB = PQ[um], PC[um]; P = len(UA)
    if P < 50 or P * Jn > AVL_MAXC:
        AVLI.update(gate="cells", pairs=int(M)); return None
    offs = np.r_[0, np.cumsum(wd + 1)]; T = int(offs[-1]); ity = np.int16 if T < 32000 else np.int32
    Yx = np.zeros((N, Jn), ity); yv_ = Yv[:, jj]; Yx[isv] = np.where(yv_ >= 0, yv_, wd[None])
    AG = np.empty((P, Jn), np.float32); C = np.empty((P, Jn), ity); o_ = offs[:-1][None].astype(ity)      # SBZ 32: chunked build, same values
    for i_ in range(0, P, 262144):
        YA = Yx[UA[i_:i_ + 262144]]; AGb = YA == Yx[UB[i_:i_ + 262144]]; AG[i_:i_ + 262144] = AGb; C[i_:i_ + 262144] = np.where(AGb, YA + o_, ity(T))
    del YA, AGb
    AGt = torch.from_numpy(AG); agm = AG.mean(1); sa = np.r_[0, np.flatnonzero(UA[1:] != UA[:-1]) + 1]; lna = np.diff(np.r_[sa, P]); ga = np.repeat(np.arange(len(sa)), lna)
    ob = np.argsort(UB, kind="stable"); ubs = UB[ob]; sb = np.r_[0, np.flatnonzero(ubs[1:] != ubs[:-1]) + 1]; lnb = np.diff(np.r_[sb, P]); gb = np.repeat(np.arange(len(sb)), lnb)
    DV = np.flatnonzero(isv[PQ]); q_, c_ = PQ[DV], PC[DV]; key = UA * N + UB
    udM = np.full(M, -1); udM[DV] = np.searchsorted(key, np.where(w[q_] == 0, q_ * N + c_, c_ * N + q_)); del q_, c_, key
    AVLI.update(pairs=int(M), feat=int(F), t_pre=round(time.time() - t0, 1))

    def world(b):
        """fold b blind (b = -1: no fold): links for the rows of fold b (b = -1: the hidden rows) from GIVEN alone."""
        use = isv & (fa != b); tgt = hid if b < 0 else (fa == b); pw = use[UA] & use[UB]; Pw = int(pw.sum()); pwf = pw.astype(np.float32)
        uq, uc = use[PQ], use[PC]; inw = uc & (uq | tgt[PQ]); DVw = np.flatnonzero(uq & uc); udw = udM[DVw]; qd = PQ[DVw]
        if Pw < 50 or len(DVw) < 50:
            return None
        # world columns: candidates of the row at least as close on the household columns, and the number of candidates
        Hc = np.zeros((N, nh_)); np.add.at(Hc, (PQ[inw], h[inw]), 1); ge = Hc[:, ::-1].cumsum(1)[:, ::-1]; cnt = Hc.sum(1)
        X[:, F - 2] = np.where(inw, np.log1p(np.maximum(ge[PQ, h] - 1, 0)), 0); X[:, F - 1] = np.where(inw, np.log(np.maximum(cnt[PQ], 1)), 0)
        logn = X[:, F - 1].astype(np.float64); neg = rk < AVL_NNEG / np.maximum(cnt[PQ], 1)
        # answer model of this world: marginals from the rows outside the blind fold
        lfx = np.zeros(T + 1); u = np.zeros(Jn); ur = np.flatnonzero(use)
        for j in range(Jn):
            f = np.bincount(Yx[ur, j], minlength=wd[j] + 1) + .5; f = f / f.sum(); u[j] = (f ** 2).sum(); lfx[offs[j]:offs[j + 1]] = -np.log(f)
        R1 = np.zeros(P)
        for j in range(Jn):
            R1 += lfx[C[:, j]]
        l1u = np.log(1 - u)

        def llr(m):
            return R1 + (AGt @ torch.from_numpy((np.log(m) - np.log(1 - m) + l1u).astype(np.float32))).numpy() + (np.log(1 - m) - l1u).sum()

        def mutual(sc):
            sc = np.where(pw, sc, -np.inf); mb = np.zeros(P, bool); mb[ob[_avl_fmax(sc[ob], sb, lnb, gb)]] = True
            return _avl_fmax(sc, sa, lna, ga) & mb

        def m_from(g):
            return np.clip(((torch.from_numpy(g.astype(np.float32)) @ AGt).numpy().astype(np.float64) + 1) / (g.sum() + 2), 1e-3, 1 - 1e-3)

        def link_of(mask):
            lo = np.full(N, -1); lo[UA[mask]] = UB[mask]; lo[UB[mask]] = UA[mask]; return lo
        # answers alone: classification EM under the 1:1 constraint (avl.py fs_cem)
        g = mutual(agm + 1e-9 * R1); m = m_from(g); p = max(g.sum() / Pw, 1e-6)
        for it in range(15):
            L = llr(m); g2 = mutual(L) & (L + np.log(p / (1 - p)) > 0)
            if g2.sum() < 10 or (it > 0 and np.array_equal(g2, g)):
                break
            g = g2; m = m_from(g); p = min(max(g.sum() / Pw, 1e-9), .5)
        L = llr(m); link = mutual(L) & (1 / (1 + np.exp(-np.clip(np.log(p / (1 - p)) + L, -50, 50))) >= .95)
        cc_ = (np.log(m) - np.log(1 - m) + l1u).astype(np.float32); pa = (torch.from_numpy(pwf) @ AGt).numpy().astype(np.float64) / Pw; vv = (AGt @ torch.from_numpy(cc_)).numpy()
        kap_de = min(1.0, float((cc_ ** 2 * pa * (1 - pa)).sum()) / max(float(np.var(vv[pw])), 1e-9)); kap = kap_de
        folds = [f for f in range(nf) if f != b]

        def crossfit(lo, final):
            y = (lo[PQ] == PC) & uq; tr = np.flatnonzero(uq & uc & (lo[PQ] >= 0) & (y | neg)); Xt = X[tr]; yt = y[tr]; s = np.zeros(M)
            for f in folds:
                mk = (fq[tr] != f) & (fc[tr] != f); cf, ic = _avl_fit(Xt[mk], yt[mk]); te = np.flatnonzero(uq & uc & (fq == f)); s[te] = (torch.from_numpy(X[te]) @ torch.from_numpy(cf)).numpy() + ic
            if final:
                cf, ic = _avl_fit(Xt, yt); te = np.flatnonzero(tgt[PQ] & uc); s[te] = (torch.from_numpy(X[te]) @ torch.from_numpy(cf)).numpy() + ic
            return np.clip(s, -30, 30)
        st = np.r_[0, np.flatnonzero(qd[1:] != qd[:-1]) + 1]; ln = np.diff(np.r_[st, len(qd)]); d0 = d0M[DVw]; th = None
        for it in range(AVL_LOOPS):                       # co-training: GIVEN score (prior) x tempered answer LLR (likelihood)
            if link.sum() < 20:
                break
            s = crossfit(link_of(link), False)[DVw]; LAd = llr(m)[udw]; lg = logn[DVw]; th = _avl_calib(s, kap * LAd, lg, st, th)
            pri = _avl_post(s, 0.0, lg, st, th); ai = np.flatnonzero(_avl_fmax(pri, st, ln, np.repeat(np.arange(len(st)), ln))); conf = pri[ai] >= .9
            if conf.sum() >= 50 and kap_de < 1:               # temper refit: rows with a confident GIVEN-only prior label the answer view
                e = np.repeat(conf, ln); Le = LAd[e]; lne = ln[conf]; ste = np.r_[0, np.cumsum(lne)[:-1]]; La = LAd[ai][conf]; big = np.full(len(ste), -1e9)
                kap = float(_avl_gold(lambda k: float((_avl_lse(k * Le, big, ste, lne) - k * La).sum()), kap_de, 1.0))
                th = _avl_calib(s, kap * LAd, lg, st, th)
            r = _avl_post(s, kap * LAd, lg, st, th); ra = np.zeros(P); rb = np.zeros(P); ra[udw[d0]] = r[d0]; rb[udw[~d0]] = r[~d0]; pu = np.minimum(ra, rb)
            link = mutual(pu + 1e-9 * ra) & (pu >= .95)
            if link.sum() >= 20:
                m = m_from(link)
        npos = int(link.sum())
        if npos < 20:
            return npos, tgt, None, None
        lo = link_of(link); s = crossfit(lo, True); LA = kap * llr(m)
        keep = ~((lo[PC] >= 0) & (lo[PC] != PQ))                 # 1:1 claim step: a candidate linked to another row is not offered
        k = DVw[keep[DVw]]; qk = PQ[k]; stk = np.r_[0, np.flatnonzero(qk[1:] != qk[:-1]) + 1]
        th = _avl_calib(s[k], LA[udM[k]], logn[k], stk, th)
        nvw = int(use.sum()); Nw = nvw + int(tgt.sum()); pv = min(max(npos * 2 / nvw, 1e-6), 1 - 1e-6)
        ph = min(pv * (nvw / (Nw - 1)) / ((nvw - 1) / (Nw - 1)), 1 - 1e-6); shift = np.log((1 - ph) / ph) - np.log((1 - pv) / pv)
        kh = np.flatnonzero(tgt[PQ] & uc & keep); qh = PQ[kh]; top = np.full(N, -1); post = np.zeros(N)
        if len(kh):
            sth = np.r_[0, np.flatnonzero(qh[1:] != qh[:-1]) + 1]; lnh = np.diff(np.r_[sth, len(qh)]); pp = _avl_post(s[kh], 0.0, logn[kh], sth, th, shift)
            li = np.flatnonzero(_avl_fmax(pp, sth, lnh, np.repeat(np.arange(len(sth)), lnh))); top[qh[li]] = PC[kh][li]; post[qh[li]] = pp[li]
        if AVL_SAB:                                          # sabotage: the same rows stay linked, each to a random candidate of its own
            rs = np.random.default_rng(11 + b); ka = np.flatnonzero(tgt[PQ] & uc); qa = PQ[ka]; sta = np.r_[0, np.flatnonzero(qa[1:] != qa[:-1]) + 1]
            lna_ = np.diff(np.r_[sta, len(qa)]); pk = sta + (rs.random(len(sta)) * lna_).astype(np.int64); rq = qa[sta]; ok = top[rq] >= 0; top[rq[ok]] = PC[ka][pk[ok]]
        return npos, tgt, top, post

    kv = np.arange(nv); qv = np.full(nv, nv); qh_ = np.full(int(hid.sum()), nv); wl = []
    wt_ = []                                       # SB2 xwf Fix 1 (VSC_WALL_AUDIT): per-world seconds, for a predictive check
    for b in [-1] + list(range(nf)):
        if time.time() - t0 + (max(wt_) if wt_ else 0.0) > _tl:   # never START a world that would end past _tl (was: checked only at the start)
            if b < AVL_KMIN:                       # SB2 erg (review REVIEW_P1kg35er opt 1; Mac forced-cut read +.0033 z 5): need the hidden world + >= AVL_KMIN fold worlds
                raise RuntimeError(f"avl over {_tl:.0f}s at world {b}")
            AVLI["cut"] = b; break                 # keep the hidden links and the finished folds' visible links (was: raise = lose all)
        _tw0 = time.time(); r = world(b); wt_.append(time.time() - _tw0); wl.append(-1 if r is None else r[0])
        if b == -1 and (r is None or r[0] < 20):
            AVLI.update(gate="links<20", links=wl[0]); return None
        if r is None or r[2] is None:
            continue
        npos, tgt, top, post = r; lk = tgt & (top >= 0) & (post >= AVL_THR)
        if b < 0:
            lh = lk[hid]; qh_[lh] = vpos[top[hid][lh]]; AVLI["hid"] = int(lh.sum())
            if not lh.any():
                AVLI.update(gate="nohid", links=wl[0]); return None
        else:
            li = np.flatnonzero(lk); qv[vpos[li]] = vpos[top[li]]
    AVLI.update(gate="on", links=wl[0], fold_links=wl[1:], vis=int((qv < nv).sum()))
    return kv, qv, qh_


BO_KDEEP = os.environ.get("SIM_BO_KDEEP", "1") == "1"
BO_TRANS = os.environ.get("SIM_BO_TRANS", "1") == "1"
BO_FORM = [0, 0]


def _pick_kappa2(lsr, oof, c_oof, n_oof, grid):
    """_pick_kappa over a given grid; returns (kappa or inf, best OOF mean)."""
    base = lsr(oof); best, kap, bd = base.mean(), np.inf, None
    for k in grid:
        d = lsr((c_oof + k * oof) / (n_oof + k)) - base
        if base.mean() + d.mean() > best + 1e-5:
            best, kap, bd = base.mean() + d.mean(), k, d
    if bd is None or len(bd) < 3 or bd.mean() <= 2 * bd.std(ddof=1) / np.sqrt(len(bd)):
        return np.inf, base.mean()
    return kap, best


def _trans(c, y, w, rows, K, m):
    """T[direction, donor answer a, own answer b] from rows (donor distribution c, own label y), shrunk to the marginal m."""
    T = np.zeros((2, K, K)); r = np.where(rows)[0]
    for a in range(K):
        np.add.at(T[:, a, :], (w[r], y[r]), c[r, a])
    return (T + 2 * m) / (T.sum(2, keepdims=True) + 2)


def _donor_backoff(klist, hid, y, oof, test, fold, K, wv, wh, stat, gf=None):
    """SB2: per-row back-off over the keys in klist (specific -> general); see patches/backoff_patch.py."""
    ok = y >= 0; yy = np.where(ok, y, 0); nf = int(fold.max()) + 1
    o2, t2 = oof.copy(), test.copy(); fv = np.ones(len(y), bool); fh = np.ones(len(test), bool); kmin = np.inf
    for si, g in enumerate(klist):
        kv, qv, kh, ng = _kq(g, hid)
        tot = np.zeros((ng, 2, K)); np.add.at(tot, (kv[ok], wv[ok], y[ok]), 1)
        per = np.zeros((nf, ng, 2, K))
        for f in range(nf):
            m_ = ok & (fold == f); np.add.at(per[f], (kv[m_], wv[m_], y[m_]), 1)
        c_oof = tot[qv, 1 - wv] - per[fold, qv, 1 - wv]; c_oof, n_oof = _pur(c_oof)
        ev = fv & (n_oof[:, 0] > 0); sel = ev & ok
        if sel.sum() < BO_MIN:
            continue
        grid = ((.03, .0625, .125) if BO_KDEEP else ()) + tuple(KAPPAS)
        kap, bestA = _pick_kappa2(lambda P: _lsr(P, yy[sel], K), oof[sel], c_oof[sel], n_oof[sel], grid)
        c_t = None
        if BO_TRANS:
            mg = np.bincount(y[ok], minlength=K) + .5; mg = mg / mg.sum(); q_oof = np.zeros_like(c_oof)
            for f in range(nf):
                T = _trans(c_oof, yy, wv, sel & (fold != f), K, mg); r = np.where(ev & (fold == f))[0]
                q_oof[r] = np.einsum("ra,rak->rk", c_oof[r], T[wv[r]])
            kapT, bestT = _pick_kappa2(lambda P: _lsr(P, yy[sel], K), oof[sel], q_oof[sel], n_oof[sel], grid)
            if np.isfinite(kapT) and (np.isinf(kap) or bestT > bestA):
                T = _trans(c_oof, yy, wv, sel, K, mg)
                c_t = tot[kh, 1 - wh]; c_t, n_t = _pur(c_t); c_t = np.einsum("ra,rak->rk", c_t, T[wh]) * n_t
                c_oof, kap = q_oof, kapT; BO_FORM[1] += 1
        if np.isinf(kap):
            continue
        if c_t is None:
            c_t = tot[kh, 1 - wh]; c_t, n_t = _pur(c_t); BO_FORM[0] += 1
        eh = fh & (n_t[:, 0] > 0)
        o2[ev] = (c_oof[ev] + kap * oof[ev]) / (1 + kap); t2[eh] = (c_t[eh] + kap * test[eh]) / (1 + kap)
        if gf is not None and gf[si] > 0:
            t2[eh] = (1 - gf[si]) * t2[eh] + gf[si] * test[eh] / test[eh].sum(1, keepdims=True) * t2[eh].sum(1, keepdims=True)
        fv &= ~ev; fh &= ~eh; kmin = min(kmin, kap); stat[si] += int(eh.sum())
    return o2, t2, kmin


GNP = os.environ.get("SIM_GNP", "1") == "1" and os.environ.get("SIM_SVNP", "1") == "1"   # svnp: the gnp machinery, lam by H
SVNP = os.environ.get("SIM_SVNP", "1") == "1"          # UNHCR-arm: self-validated donor-cell pool weight
SV_HMAX, SV_HMIN = int(os.environ.get("SIM_SVNP_HMAX", 384)), 100
SVLR = os.environ.get("SIM_SVLR", "0") == "1"           # SB-PUSH: twin-likelihood arms (20 + beta same item, 30 + beta joint)
SVLR_SAB = os.environ.get("SIM_SVLR_SAB", "0") == "1"   # sabotage: permuted transition tables
SV_GRID = (0.0, 1 / 3, 2 / 3) + ((10.5, 10.75, 11.0) if os.environ.get("SIM_SVNP_RHO", "1") == "1" else ()) + ((20.5, 21.0, 30.5, 31.0) if SVLR else ())   # 10 + rho: donor-after-pool
LRH, LRT = {}, {}                                       # SB-PUSH: per (form, item) likelihoods on H rows / hidden rows
TM = os.environ.get("SIM_TM", "1") == "1"; TM_SAB = os.environ.get("SIM_TM_SAB", "0") == "1"
TM_SEEDS = int(os.environ.get("SIM_TM_SEEDS", 2)); TM_FRAC = float(os.environ.get("SIM_TM_FRAC", .12))
TMI = {}
TT = os.environ.get("SIM_TT", "1") == "1"; TT_SAB = os.environ.get("SIM_TT_SAB", "0") == "1"
TT_RND = int(os.environ.get("SIM_TT_RND", 150)); TT_WAIT = float(os.environ.get("SIM_TT_WAIT", 5)); TT_THR = int(os.environ.get("SIM_TT_THR", 2)); TT_LR = float(os.environ.get("SIM_TT_LR", .3))
TT_ALL = os.environ.get("SIM_TT_ALL", "1") == "1"   # 1: train on all visible rows; 0: on rows with a twin code only
TT_LINK = os.environ.get("SIM_TT_LINK", "1") == "1"
TM_LINK = os.environ.get("SIM_TM_LINK", "1") == "1"
TT_GRID = tuple(float(x) for x in os.environ.get("SIM_TT_GRID", ".25,.5,.75,1").split(","))
MT = os.environ.get("SIM_MT", "1") == "1"; MT_SAB = os.environ.get("SIM_MT_SAB", "0") == "1"; MTI = {}
TTI = {}; TT_LIVE = [False]
TT_CLAIM = os.environ.get("SIM_TT_CLAIM", "1") == "1"; TT_CLAIM_SAB = os.environ.get("SIM_TT_CLAIM_SAB", "0") == "1"
TT_CLAIM_TAU = float(os.environ.get("SIM_TT_CLAIM_TAU", .5)); TT_CLAIM_DEL = float(os.environ.get("SIM_TT_CLAIM_DEL", 0.0)); TT_CLAIM_CAP = int(os.environ.get("SIM_TT_CLAIM_CAP", 64))
SVTF_K = int(os.environ.get("SIM_SVTF_K", 1))
SVTF = os.environ.get("SIM_SVTF", "0") == "1"; SVTF_M = int(os.environ.get("SIM_SVTF_M", 24)); SVTF_SAB = os.environ.get("SIM_SVTF_SAB", "0") == "1"
TFC, QT, QTH, GH = {}, {}, {}, {}                       # svtf: svlr twin data; TF probs hidden / H; svnp H outputs per (lam, item)


class _StopTT:
    def __init__(self, t, sl):
        self.t = t; self.sl = sl

    def after_iteration(self, info):
        return time.time() < min(self.t, self.sl[0])


def _tt_start(frame, giv, hid, X, Yv, widths, fold, hard):
    """SB-PUSH3 T1: start the twin-vector tree fits on TT_THR own worker threads. Returns (futs, kvv, kdh, ex) or None."""
    if CB_UNSAFE:
        return None  # native CHECK bytes/protection may be partially changed
    if not (all(c in frame.columns for c in HH_LOC + HH_CNT) and "wave" in frame.columns):
        return None
    w = pd.factorize(frame["wave"].astype(str), sort=True)[0]
    if int(w.max()) != 1:
        return None
    kc = [g for g in giv if g not in DONOR_DROP] or list(giv)
    KEYS = [np.unique(np.stack([pd.factorize(frame[c].astype(str))[0] for c in cols], 1), axis=0, return_inverse=True)[1].reshape(-1)
            for cols in (kc, HH_LOC + HH_CNT)]
    vi = np.where(~hid)[0]; N = len(frame); J = len(widths); nv = len(vi)
    fv = np.full(N, -1); fv[vi] = fold
    Yall = np.full((N, J), -1, np.int64); Yall[vi] = Yv
    PAIRS = []
    if TT_CLAIM:                                 # SB-PUSH4 C1: visible cross-round pairs on each key + their answer agreement
        for key in KEYS:
            df = pd.DataFrame({"i": vi, "k": key[vi], "w": w[vi]}); gs = df.groupby(["k", "w"]).size().unstack(fill_value=0)
            gs = gs.reindex(columns=[0, 1], fill_value=0); okk = gs.index[(gs[0] > 0) & (gs[1] > 0) & (gs[0] * gs[1] <= TT_CLAIM_CAP)]
            df = df[df.k.isin(okk)]; m = df[df.w == 0].merge(df[df.w == 1], on="k")
            a_, b_ = m.i_x.to_numpy(), m.i_y.to_numpy(); ag = np.zeros(len(a_))
            for q in range(0, len(a_), 20000):
                ya, yb = Yall[a_[q:q + 20000]], Yall[b_[q:q + 20000]]; okp = (ya >= 0) & (yb >= 0)
                ag[q:q + 20000] = ((ya == yb) & okp).sum(1) / np.maximum(okp.sum(1), 1)
            if TT_CLAIM_SAB:
                ag = ag[np.random.default_rng(11).permutation(len(ag))]
            PAIRS.append((np.r_[a_, b_], np.r_[b_, a_], np.r_[ag, ag]))
    CLI = {}

    def codes(blind):
        TW = np.empty((N, J), np.int64); srv = np.zeros(N, bool); kd = np.zeros(N, np.int64)
        ND = np.zeros(N); NS = np.zeros(N); AG = np.zeros(N); NU = np.zeros(N); AC = np.zeros(N)
        use = (fv != blind) & (fv >= 0)
        for ki, key in enumerate(KEYS):
            ng = int(key.max()) + 1; u = np.where(use)[0]
            nd = np.zeros((ng, 2)); np.add.at(nd, (key[u], w[u]), 1)
            na = np.zeros((ng, 2)); np.add.at(na, (key, w), 1)       # every row (GIVEN only) on the key, by wave
            rows = np.where(~srv & (nd[key, 1 - w] > 0))[0]
            yu = Yall[u]
            if TT_CLAIM:                         # claims in this world: claimer s and donor d both outside the blind fold
                PS, PD, PA = PAIRS[ki]; v_ = use[PS] & use[PD]; s_, d_, a_ = PS[v_], PD[v_], PA[v_]
                own = np.full(N, -1); cc = np.zeros(N)
                if len(s_):
                    o_ = np.lexsort((-a_, s_)); s_, d_, a_ = s_[o_], d_[o_], a_[o_]
                    fi = np.where(np.r_[True, s_[1:] != s_[:-1]])[0]; nx = np.minimum(fi + 1, len(s_) - 1)
                    sec = np.where((fi + 1 < len(s_)) & (s_[nx] == s_[fi]), a_[nx], -1.0)
                    okc = (a_[fi] >= TT_CLAIM_TAU) & (a_[fi] - sec >= TT_CLAIM_DEL)
                    own[s_[fi][okc]] = d_[fi][okc]; np.add.at(cc, d_[fi][okc], 1)
                exr = use & (cc > 0); ne = np.zeros((ng, 2)); np.add.at(ne, (key[exr], w[exr]), 1)
                abk = (own[rows] >= 0) & (cc[np.maximum(own[rows], 0)] == 1)      # x's own claim alone never excludes for x
                nun = nd[key[rows], 1 - w[rows]] - ne[key[rows], 1 - w[rows]] + abk
                keep = nun > 0; ex_i = np.where(exr)[0]
                NU[rows] = np.where(keep, nun, 0); AC[rows] = ~keep
                if blind == -1:
                    CLI[ki] = (int(okc.sum()) if len(s_) else 0, int((~keep).sum()), int((keep & (nun < nd[key[rows], 1 - w[rows]])).sum()))
            for j in range(J):
                K = int(widths[j]); y = yu[:, j]; ok = y >= 0
                c = np.zeros((ng, 2, K)); np.add.at(c, (key[u][ok], w[u][ok], y[ok]), 1)
                cr = c[key[rows], 1 - w[rows]]
                if TT_CLAIM:
                    ye = Yall[ex_i, j]; oe = ye >= 0; ce = np.zeros((ng, 2, K)); np.add.at(ce, (key[ex_i][oe], w[ex_i][oe], ye[oe]), 1)
                    cu = cr - ce[key[rows], 1 - w[rows]]
                    ra = np.where(abk)[0]; ya = Yall[own[rows[ra]], j]; oa = ya >= 0; cu[ra[oa], ya[oa]] += 1
                    cr = np.where(keep[:, None], np.maximum(cu, 0), cr)
                TW[rows, j] = np.where(cr.sum(1) > 0, cr.argmax(1), K)
                AG[rows] += cr.max(1) / np.maximum(cr.sum(1), 1) / J
            srv[rows] = True; kd[rows] = ki + 1; ND[rows] = nd[key[rows], 1 - w[rows]]; NS[rows] = na[key[rows], w[rows]]
        for j in range(J):
            TW[~srv, j] = int(widths[j])
        if TT_SAB:
            rng = np.random.default_rng(5)
            for wv in (0, 1):
                r = np.where(srv & (w == wv))[0]; TW[r] = TW[rng.permutation(r)]
        if TT_LINK:                              # record-linkage strength: key kind, donors on the key, same-wave rows on the key, donor agreement
            TW = np.concatenate([TW, np.stack([kd, np.minimum(ND, 6), np.minimum(NS, 6), np.round(10 * AG)] + ([np.minimum(NU, 6), AC] if TT_CLAIM else []), 1).astype(np.int64)], 1)
        return TW, kd

    TWa, kda = codes(-1)
    if TT_CLAIM:
        TTI["claim"] = CLI
    if (kda[hid] > 0).sum() < 30 or (kda[~hid] > 0).sum() < 100:
        return None
    Fh = np.concatenate([X[hid], TWa[hid]], 1).astype(np.int32)
    Fv, kvv, mis = [], np.zeros(nv, np.int64), np.zeros(J)
    TWo = np.zeros((nv, J), np.int64); TGT = []; wj = np.array(widths)[None]
    for f in range(FOLDS):
        TWf, kdf = codes(f)
        Fv.append(np.concatenate([X[~hid], TWf[~hid]], 1).astype(np.int32)); va = fold == f
        kvv[va] = kdf[~hid][va]; TWo[va] = TWf[~hid][va][:, :J]
        tc = TWf[~hid][:, :J]; okc = (tc < wj) & (Yv >= 0)                 # mover target in the fold-f-blind world
        TGT.append((np.where(okc.sum(1) > 0, ((tc != Yv) & okc).sum(1) / np.maximum(okc.sum(1), 1), -1.0), kdf[~hid] > 0))
        tv = TWf[~hid][va][:, :J]; yv = Yv[va]
        mis += ((tv != yv) & (tv < np.array(widths)[None]) & (yv >= 0)).sum(0)
    cats = list(range(X.shape[1] + J))            # the LINK columns stay numeric
    sl = [float("inf")]                           # this instrument's stop time for its own worker threads

    def job(j):
        if time.time() >= min(hard, sl[0]):
            return j, "late"
        try:
            from catboost import CatBoostClassifier
            y = Yv[:, j]; K = int(widths[j]); oof = np.zeros((nv, K)); test = np.zeros((len(Fh), K))
            for f in range(FOLDS):
                tr, va = (fold != f) & (y >= 0), fold == f
                if not TT_ALL:
                    tr = tr & (Fv[f][:, X.shape[1] + j] < K)
                cl, yt = np.unique(y[tr], return_inverse=True)
                if len(cl) < 2:
                    return j, "unfit"
                m = CatBoostClassifier(iterations=TT_RND, depth=4, learning_rate=TT_LR, l2_leaf_reg=5, loss_function="MultiClass",
                                       cat_features=cats, one_hot_max_size=255, boosting_type="Plain", thread_count=1, verbose=0,
                                       random_seed=0, allow_writing_files=False)
                m.fit(Fv[f][tr], yt, callbacks=[_StopTT(hard, sl)])
                if time.time() >= min(hard, sl[0]):
                    return j, "cut"
                oof[np.ix_(va, cl)] = m.predict_proba(Fv[f][va], thread_count=1); test[:, cl] += m.predict_proba(Fh, thread_count=1) / FOLDS
            return j, (oof, test)
        except Exception:
            return j, "raised"
    def job_ms():
        from catboost import CatBoostRegressor
        ms_o = np.zeros(nv); ms_h = np.zeros(len(Fh))
        for f in range(FOLDS):
            tg, tw = TGT[f]; tr = (fold != f) & tw & (tg >= 0)
            if tr.sum() < 100:
                return None
            m = CatBoostRegressor(iterations=200, depth=4, learning_rate=.1, l2_leaf_reg=5, loss_function="RMSE", cat_features=cats,
                                  one_hot_max_size=255, boosting_type="Plain", thread_count=1, verbose=0, random_seed=0, allow_writing_files=False)
            m.fit(Fv[f][tr], tg[tr], callbacks=[_StopTT(hard, sl)])
            if time.time() >= min(hard, sl[0]):
                return None
            va = fold == f
            ms_o[va] = m.predict(Fv[f][va], thread_count=1); ms_h += m.predict(Fh, thread_count=1) / FOLDS
        return ms_o, ms_h
    ex = ThreadPoolExecutor(max(1, TT_THR)); CUR_TT[0] = (ex, sl)
    fms = ex.submit(job_ms) if MT else None
    futs = [ex.submit(job, int(j)) for j in np.argsort(-mis) if mis[j] > 0] if TT else []
    return futs, kvv, kda[hid], ex, fms, TWo, TWa[hid][:, :J], sl


def _tt_apply(R, until, Yv, oof, test):
    """collect the finished twin-vector tree fits; per item and twin kind a 2-SE OOF pick of a, geometric pool on twin rows."""
    futs, kvv, kdh = R[:3]; d = {}; st = {}
    for f in futs:
        try:
            j, r = f.result(timeout=max(0.0, until - time.time()))
        except Exception:
            f.cancel(); continue
        if isinstance(r, str):
            st[r] = st.get(r, 0) + 1
        else:
            d[j] = r
    def ls(P, y):
        P = P / P.sum(1, keepdims=True); K = P.shape[1]
        return np.log(FLOOR + (1 - K * FLOOR) * P[np.arange(len(y)), y])
    def pool(P, Q, a):
        P = P / P.sum(1, keepdims=True); Q = np.maximum(Q / np.maximum(Q.sum(1, keepdims=True), 1e-12), 1e-4); g = P ** (1 - a) * Q ** a
        return g / g.sum(1, keepdims=True)
    on = 0; onk = [0, 0]
    for j, (o_, t_) in d.items():
        y = Yv[:, j]; hit = False
        for gi, (hv, hh) in enumerate(((kvv == 1, kdh == 1), (kvv >= 2, kdh >= 2))):
            ok = (y >= 0) & hv
            if ok.sum() < 50:
                continue
            b = ls(oof[j][ok], y[ok]); best, ba = 0.0, 0.0
            for a in TT_GRID:
                dl = ls(pool(oof[j][ok], o_[ok], a), y[ok]) - b
                if dl.mean() > best and dl.mean() > 2 * dl.std(ddof=1) / np.sqrt(len(dl)):
                    best, ba = dl.mean(), a
            if ba > 0:
                oof[j][hv] = pool(oof[j][hv], o_[hv], ba); test[j][hh] = pool(test[j][hh], t_[hh], ba); hit = True; onk[gi] += 1
        on += hit
    TTI.update(fit=len(d), queued=len(futs), ex=onk[0], hh=onk[1], **st)
    return on


def _mt_apply(R, until, Yv, oof, test, fold, widths):
    """SB-PUSH3 T4 mover tilt: re-set p(twin answer) on twin cells from (logit p, mover score), cross-fitted, 2-SE gated."""
    kvv, kdh, fms, TWo, TWh = R[1], R[2], R[4], R[5], R[6]
    r_ = fms.result(timeout=max(0.0, until - time.time()))
    if r_ is None:
        MTI["ms"] = "none"; return
    ms_o, ms_h = r_; hv = kvv > 0; hh = kdh > 0; J = len(widths)
    if MT_SAB:
        rng = np.random.default_rng(7); ms_o = ms_o[rng.permutation(len(ms_o))]; ms_h = ms_h[rng.permutation(len(ms_h))]
    mu, sd = ms_o[hv].mean(), ms_o[hv].std() + 1e-9
    zo, zh = (ms_o - mu) / sd, (ms_h - mu) / sd
    def cells(P, tw, rows):
        P = P / P.sum(1, keepdims=True); K = P.shape[1]; r = rows[tw[rows] < K]
        pa = P[r, tw[r]]
        return r, pa
    def lg(p):
        p = np.clip(p, 1e-4, 1 - 1e-4); return np.log(p / (1 - p))
    def feats(l, z):
        return np.stack([np.ones_like(l), l, z, l * z], 1)
    def irls(Z, y):
        b = np.array([0.0, 1.0, 0.0, 0.0])
        for _ in range(30):
            p = 1 / (1 + np.exp(-np.clip(Z @ b, -30, 30))); g = Z.T @ (y - p) - 1e-3 * (b - np.array([0.0, 1.0, 0.0, 0.0]))
            H = (Z * (p * (1 - p))[:, None]).T @ Z + 1e-3 * np.eye(4)
            d = np.linalg.solve(H, g); b = b + d
            if np.abs(d).max() < 1e-7:
                break
        return b
    def ls(P, y):
        P = P / P.sum(1, keepdims=True); K = P.shape[1]
        return np.log(FLOOR + (1 - K * FLOOR) * P[np.arange(len(y)), y])
    def tilt(P, a, pa2):
        P = P / P.sum(1, keepdims=True); pa = P[np.arange(len(a)), a]; ok = pa < 1 - 1e-9
        Q = P * np.where(ok, (1 - pa2) / np.maximum(1 - pa, 1e-12), 1.0)[:, None]; Q[np.arange(len(a)), a] = np.where(ok, pa2, pa)
        return Q
    vr = np.where(hv)[0]; RR, JJ, LL, YY = [], [], [], []
    for j in range(J):
        y = Yv[:, j]; r, pa = cells(oof[j], TWo[:, j], vr[y[vr] >= 0])
        RR.append(r); JJ.append(np.full(len(r), j)); LL.append(lg(pa)); YY.append((y[r] == TWo[r, j]) * 1.0)
    RR, JJ, LL, YY = (np.concatenate(v) for v in (RR, JJ, LL, YY))
    if len(RR) < 2000:
        MTI["cells"] = int(len(RR)); return
    Z = feats(LL, zo[RR]); P2 = np.zeros(len(RR))
    for f in range(int(fold.max()) + 1):
        te = fold[RR] == f
        P2[te] = 1 / (1 + np.exp(-np.clip(Z[te] @ irls(Z[~te], YY[~te]), -30, 30)))
    P2 = np.clip(P2, 1e-4, 1 - 1e-4)
    gain = np.zeros(len(Yv)); new = {}
    for j in range(J):
        s_ = JJ == j; r = RR[s_]
        if len(r) == 0:
            continue
        Q = tilt(oof[j][r], TWo[r, j], P2[s_]); y = Yv[r, j]
        np.add.at(gain, r, ls(Q, y) - ls(oof[j][r], y)); new[j] = (r, Q)
    g = gain[hv] / J; z = g.mean() / (g.std(ddof=1) / np.sqrt(len(g)) + 1e-15)
    b = irls(Z, YY)
    MTI.update(cells=int(len(RR)), gain=round(float(g.mean()), 5), z=round(float(z), 1), b=[round(float(x), 3) for x in b])
    if not (g.mean() > 0 and z > 2):
        MTI["on"] = 0; return
    for j, (r, Q) in new.items():
        oof[j][r] = Q
    hr = np.where(hh)[0]
    for j in range(J):
        r, pa = cells(test[j], TWh[:, j], hr)
        if len(r):
            p2 = np.clip(1 / (1 + np.exp(-np.clip(feats(lg(pa), zh[r]) @ b, -30, 30))), 1e-4, 1 - 1e-4)
            test[j][r] = tilt(test[j][r], TWh[r, j], p2)
    MTI["on"] = 1


def _tm_fit(frame, giv, hid, X, Yv, widths, offs, fold, end):
    """SB-PUSH2 I1: twin-vector MLP. Returns (oof, test, has_v, has_h) or None."""
    if not (all(c in frame.columns for c in HH_LOC + HH_CNT) and "wave" in frame.columns):
        return None
    w = pd.factorize(frame["wave"].astype(str), sort=True)[0]
    if int(w.max()) != 1:
        return None
    kc = [g for g in giv if g not in DONOR_DROP] or list(giv)
    kex = np.unique(np.stack([pd.factorize(frame[c].astype(str))[0] for c in kc], 1), axis=0, return_inverse=True)[1].reshape(-1)
    khh = np.unique(np.stack([pd.factorize(frame[c].astype(str))[0] for c in HH_LOC + HH_CNT], 1), axis=0, return_inverse=True)[1].reshape(-1)
    vi = np.where(~hid)[0]; N = len(frame); J = len(widths); nv = len(vi)
    fv = np.full(N, -1); fv[vi] = fold                                  # hidden rows: fold -1 (never blinded)

    def codes(blind):
        """twin codes per row; donors in fold `blind` are not used (blind -1 = all visible donors)."""
        TW = np.empty((N, J), np.int64); srv = np.zeros(N, bool)
        LK = np.zeros((N, 4))
        use = (fv != blind) & (fv >= 0)
        for ki, key in enumerate((kex, khh)):
            ng = int(key.max()) + 1; u = np.where(use)[0]
            nd = np.zeros((ng, 2)); np.add.at(nd, (key[u], w[u]), 1)
            rows = np.where(~srv & (nd[key, 1 - w] > 0))[0]
            if TM_LINK:
                na = np.zeros((ng, 2)); np.add.at(na, (key, w), 1)
                LK[rows, 0] = ki + 1; LK[rows, 1] = np.minimum(nd[key[rows], 1 - w[rows]], 6); LK[rows, 2] = np.minimum(na[key[rows], w[rows]], 6)
            yu = Yall[u]
            for j in range(J):
                K = int(widths[j]); y = yu[:, j]; ok = y >= 0
                c = np.zeros((ng, 2, K)); np.add.at(c, (key[u][ok], w[u][ok], y[ok]), 1)
                cr = c[key[rows], 1 - w[rows]]
                TW[rows, j] = np.where(cr.sum(1) > 0, cr.argmax(1), K)
                if TM_LINK:
                    LK[rows, 3] += 10 * cr.max(1) / np.maximum(cr.sum(1), 1) / J
            srv[rows] = True
        for j in range(J):
            TW[~srv, j] = int(widths[j])
        if TM_SAB:
            rng = np.random.default_rng(5)
            for wv in (0, 1):
                r = np.where(srv & (w == wv))[0]; TW[r] = TW[rng.permutation(r)]
        if TM_LINK:
            TW = np.concatenate([TW, np.round(LK).astype(np.int64)], 1)
        return TW, srv

    Yall = np.full((N, J), -1, np.int64); Yall[vi] = Yv
    TWa, srva = codes(-1)
    if srva[hid].sum() < 30 or srva[~hid].sum() < 100:
        return None
    cards = [int(X[:, i].max()) + 1 for i in range(X.shape[1])] + [int(widths[j]) + 1 for j in range(J)] + ([3, 7, 7, 11] if TM_LINK else [])
    Xh = np.concatenate([X[hid], TWa[hid]], 1)
    oof = [np.zeros((nv, int(k))) for k in widths]; test = [np.zeros((int(hid.sum()), int(k))) for k in widths]
    hv = np.zeros(nv, bool); cut = False; nfit = FOLDS * TM_SEEDS; k = 0
    for f in range(FOLDS):
        TWf, srvf = codes(f)
        Xv = np.concatenate([X[~hid], TWf[~hid]], 1); tr, va = fold != f, fold == f
        hv[va] = srvf[~hid][va]
        for sd in range(TM_SEEDS):
            dl = time.time() + max(0.0, end - time.time()) / (nfit - k); k += 1
            net, c = _fit(Xv[tr], Yv[tr], Xv[va], Yv[va], cards, widths, offs, seed=f + 100 * sd + 7, deadline=dl)
            cut |= c
            with torch.no_grad():
                pv = _probs(net(torch.as_tensor(Xv[va], device=DEV)), offs)
                ph = _probs(net(torch.as_tensor(Xh, device=DEV)), offs)
            for j in range(J):
                oof[j][va] += pv[j] / TM_SEEDS; test[j] += ph[j] / nfit
            if time.time() > end:
                break
        if time.time() > end and f < FOLDS - 1:
            return None                                                # no complete OOF: the build's path
    TMI["cut"] = int(cut)
    return oof, test, hv, srva[hid]


def _tm_apply(R, Yv, oof, test):
    """per item 2-SE OOF pick of a, geometric pool on twin rows (visible OOF and hidden)."""
    o_, t_, hv, hh = R; on = 0
    def ls(P, y):
        P = P / P.sum(1, keepdims=True); K = P.shape[1]
        return np.log(FLOOR + (1 - K * FLOOR) * P[np.arange(len(y)), y])
    def pool(P, Q, a):
        P = P / P.sum(1, keepdims=True); Q = np.maximum(Q / Q.sum(1, keepdims=True), 1e-4); g = P ** (1 - a) * Q ** a
        return g / g.sum(1, keepdims=True)
    for j in range(len(oof)):
        y = Yv[:, j]; ok = (y >= 0) & hv
        if ok.sum() < 50:
            continue
        b = ls(oof[j][ok], y[ok]); best, ba = 0.0, 0.0
        for a in (.25, .5, .75, 1.0):
            d = ls(pool(oof[j][ok], o_[j][ok], a), y[ok]) - b
            if d.mean() > best and d.mean() > 2 * d.std(ddof=1) / np.sqrt(len(d)):
                best, ba = d.mean(), a
        if ba > 0:
            oof[j][hv] = pool(oof[j][hv], o_[j][hv], ba); test[j][hh] = pool(test[j][hh], t_[j][hh], ba); on += 1
    return on


def _sv_tf(Xv, Xh, Yv, widths, H, items, hid, stop):
    """twin-feature V3.5-fast fits: production (all visible twin rows -> hidden) and side (visible twin rows outside H -> H)."""
    from tabpfn import TabPFNClassifier
    from tabpfn.constants import ModelVersion
    QT.clear(); QTH.clear()
    if not os.path.exists(ICL_FILE) or "C" not in TFC:
        return 0
    C = TFC["C"]; nv = len(Xv); inH = np.zeros(nv, bool); inH[H] = True; rng = np.random.default_rng(5); done, t1 = 0, None
    def feats(tag_, j, rows):
        cj, hj = C[tag_][j]
        a = np.where(hj[rows], cj[rows].argmax(1), -1).astype(float)[:, None]
        for kb in TFC.get("kbs", {}).get((tag_, j), []):
            ck, hk = C[tag_][kb]; a = np.c_[a, np.where(hk[rows], ck[rows].argmax(1), -1)]
        return a, hj[rows]
    vidx = np.where(~hid)[0]; hidx = np.where(hid)[0]
    for j in items:
        if t1 is not None and time.time() + 2.5 * t1 > stop:
            FAIL["svtf_time"] = 1; break
        t = time.time()
        try:
            for tag_, ctx_rows, q_rows, Xc, Xq, dst_ in (("a", vidx, hidx, Xv, Xh, QT), ("h", vidx[~inH], vidx[H], Xv[~inH], Xv[H], QTH)):
                ac, hc = feats(tag_, j, ctx_rows); aq, hq = feats(tag_, j, q_rows)
                yc = Yv[:, j] if tag_ == "a" else Yv[~inH, j]
                sel = hc & (yc >= 0)
                if sel.sum() < 100 or not hq.any():
                    raise ValueError("few twin rows")
                if SVTF_SAB:
                    ac = ac[rng.permutation(len(ac))]; aq = aq[rng.permutation(len(aq))]
                cl, yt = np.unique(yc[sel], return_inverse=True)
                if len(cl) < 2:
                    raise ValueError("one class")
                m = TabPFNClassifier.create_default_for_version(ModelVersion.V3_5_FAST, model_path=ICL_FILE, n_estimators=4, device=DEV,
                                                                categorical_features_indices=[], ignore_pretraining_limits=True)
                m.fit(np.c_[Xc[sel], ac[sel]], yt)
                P = np.full((len(Xq), int(widths[j])), 1e-4); P[np.ix_(hq, cl)] = np.asarray(m.predict_proba(np.c_[Xq[hq], aq[hq]]), float)
                P = P / P.sum(1, keepdims=True)
                if not np.isfinite(P).all():
                    raise ValueError("non-finite")
                dst_[j] = (P, hq)
            done += 1
        except Exception as e:                    # optional: this item keeps the svlr path
            QT.pop(j, None); QTH.pop(j, None)
            if _is_oom(e) or _cuda_fault(e):
                break
        t1 = time.time() - t if t1 is None else max(t1, time.time() - t)
    return done


def _sv_lr(frame, schema, giv, hid, pre, Yv, widths, H, items):
    """SB-PUSH: twin transition likelihoods L(y) on H rows (T fitted without H) and on hidden rows (T on all visible)."""
    LRH.clear(); LRT.clear()
    kcols = [g for g in giv if g not in DONOR_DROP] or list(giv)
    kx = np.unique(np.stack([pd.factorize(frame[c].astype(str))[0] for c in kcols], 1), axis=0, return_inverse=True)[1].reshape(-1)
    kh_ = _hh_groups(frame, schema, False)[0][:, 0]
    wc = pd.factorize(frame["wave"].astype(str), sort=True)[0]
    vis = np.where(~hid)[0]; hrow = np.where(hid)[0]; nv = len(vis)
    inH = np.zeros(nv, bool); inH[H] = True
    rng = np.random.default_rng(7)

    def twin_dist(j, use):                 # c (all rows x K): other-round visible donors among `use`, on the key the menu chose for j
        K = int(widths[j]); y = Yv[:, j]; out = np.zeros((len(frame), K))
        u = use & (y >= 0); ci = DKI.get(j, 0); TK = DKEYS.get("T", [])
        seq = ((kx, True),) if ci == 1 else ((TK[ci - 2], True),) if 2 <= ci < 2 + len(TK) else ((kx, True), (kh_, False))
        for key, first in seq:
            ng = int(key.max()) + 1; tot = np.zeros((ng, 2, K)); np.add.at(tot, (key[vis[u]], wc[vis[u]], y[u]), 1)
            c = tot[key, 1 - wc]
            if first:
                out = c
            else:
                emp = out.sum(1) == 0; out[emp] = c[emp]
        n = out.sum(1, keepdims=True)
        return out / np.where(n > 0, n, 1), n[:, 0] > 0

    def fitT(y_own, cj, rows, K, cols):
        T = np.full((K, cols), .5)
        yo = y_own[rows]
        if SVLR_SAB:
            yo = rng.permutation(yo)
        np.add.at(T, yo, cj[rows])
        return T / T.sum(1, keepdims=True)

    noH, allv = ~inH, np.ones(nv, bool)
    C, AM = {}, {}
    TFC.clear(); TFC["C"] = C; TFC["kb"] = {}
    for tag_, use in (("h", noH), ("a", allv)):
        C[tag_] = [twin_dist(j, use) for j in range(len(pre))]
        AM[tag_] = [(c_[vis].argmax(1), h_[vis]) for c_, h_ in C[tag_]]
    for j in items:
        K = int(widths[j]); y = Yv[:, j]
        for tag_, use in (("h", noH), ("a", allv)):
            cj, hasj = C[tag_][j]; cv = cj[vis]
            fitrows = use & hasj[vis] & (y >= 0)
            if fitrows.sum() < 50:
                continue
            T1 = fitT(y, cv, fitrows, K, K)
            q = cj[vis[H]] if tag_ == "h" else cj[hrow]
            dst_ = LRH if tag_ == "h" else LRT
            dst_[(1, j)] = np.where((q.sum(1) > 0)[:, None], q @ T1.T, 1.0)
            best, kb = 0.0, -1; cands_ = []        # k_j by conditional MI on the fit rows (hard twin answers)
            aj = cv.argmax(1)
            for k in range(len(pre)):
                if k == j:
                    continue
                ak, hk = AM[tag_][k]; ok_ = fitrows & hk
                if ok_.sum() < 50:
                    continue
                Kk = int(widths[k])
                c3 = np.bincount((aj[ok_] * K + y[ok_]) * Kk + ak[ok_], minlength=K * K * Kk).reshape(K, K, Kk) + 1e-9
                c3 = c3 / c3.sum(); pj = c3.sum((1, 2), keepdims=True); pjy = c3.sum(2, keepdims=True); pjk = c3.sum(1, keepdims=True)
                mi = float((c3 * np.log(c3 * pj / (pjy * pjk))).sum()) - (K - 1) * (Kk - 1) * K / (2 * ok_.sum())   # minus a chance-level bias
                cands_.append((mi, k))
                if mi > best:
                    best, kb = mi, k
            TFC["kb"][(tag_, j)] = kb; TFC.setdefault("kbs", {})[(tag_, j)] = [k_ for m_, k_ in sorted(cands_, reverse=True)[:SVTF_K] if m_ > 0]
            if kb < 0:
                continue
            ck, hk = C[tag_][kb]; Kk = int(widths[kb]); ok_ = fitrows & hk[vis]
            cjk = (cv[:, :, None] * ck[vis][:, None, :]).reshape(nv, K * Kk)
            T2 = fitT(y, cjk, ok_, K, K * Kk)
            qk = ck[vis[H]] if tag_ == "h" else ck[hrow]
            qq = (q[:, :, None] * qk[:, None, :]).reshape(len(q), K * Kk)
            L2 = np.where((qq.sum(1) > 0)[:, None], qq @ T2.T, dst_[(1, j)])
            dst_[(2, j)] = L2
    print(f"[{TAG}] svlr likelihoods: H {sum(1 for f, _ in LRH if f == 1)} / {sum(1 for f, _ in LRH if f == 2)} items, hidden {sum(1 for f, _ in LRT if f == 1)} / {sum(1 for f, _ in LRT if f == 2)}{' SABOTAGE' if SVLR_SAB else ''}", flush=True)


def _lr_arm(g_pool, ratio, w, L, beta):
    """pool output without the donor stage (ratio = donor ratio) x L^beta"""
    g = g_pool * ratio ** (-(1 - w)) * np.maximum(L, 1e-12) ** beta
    return g / g.sum(1, keepdims=True)
SV_FORCE = os.environ.get("SIM_SVNP_FORCE", "")
SV_DUMP = os.environ.get("SIM_SVNP_DUMP", "")
SV_NITEMS = int(os.environ.get("SIM_SVNP_NITEMS", 48))   # v4: items with a side fit for H
SV_H = [None]                                           # visible positions held out of TabPFN contexts (or None)
QH = {}                                                 # TabPFN class probabilities for SV_H rows, per item


def _sv_pick(frame, schema, giv, hid):
    """label-free: visible rows with >= 1 OTHER-round visible row on the exact key or the household key; seeded sample."""
    kcols = [g for g in giv if g not in DONOR_DROP] or list(giv)
    codes = np.stack([pd.factorize(frame[c].astype(str))[0] for c in kcols], 1)
    keys = np.unique(codes, axis=0, return_inverse=True)[1].reshape(-1)
    nb, G = _hh_groups(frame, schema, False)
    wc = pd.factorize(frame["wave"].astype(str), sort=True)[0]
    if int(wc.max()) != 1:
        return None
    vis = ~hid; cand = np.zeros(len(frame), bool)
    for g in (keys, nb[:, 0]):
        ng = int(g.max()) + 1; c = np.zeros((ng, 2)); np.add.at(c, (g[vis], wc[vis]), 1)
        cand |= c[g, 1 - wc] > 0
        if os.environ.get("SIM_SVNP_HSAFE", "0") == "1":     # v3: never hold out a key-twin of a hidden row
            hk = np.zeros(ng, bool); hk[g[hid]] = True; cand &= ~hk[g]
    pos = np.where(cand[vis])[0]                        # positions in the visible arrays (Xv / Yv / oof)
    if len(pos) < SV_HMIN:
        return None
    return np.sort(np.random.default_rng(int(os.environ.get("SIM_SVNP_SEED", 11))).permutation(pos)[:SV_HMAX])


def _sv_decide(pre, Q, QH, QW, oof, marg, Yv, widths, VMASK, H, BEST, RV=None):
    """per-row gain of each lam over lam 1 on H's donor-changed cells (grader floor, after the floor inverse)."""
    lams = (1.0,) + SV_GRID; S = {l: np.zeros(len(H)) for l in lams}; used = np.zeros(len(H), bool); ni = 0; GH.clear()
    for j in range(len(pre)):
        if j not in Q or j not in QH or not VMASK[j].any() or not np.isfinite(QH[j]).all():
            continue
        y = Yv[H, j]; ok = VMASK[j] & (y >= 0)
        if not ok.any():
            continue
        best = BEST[j] = (_pick_mix_inv if FLOOR_INV else _pick_mix)(oof[j], marg[j], Yv[:, j])
        o = _mix(oof[j][H], marg[j], best[1], best[2]); base = o / o.sum(1, keepdims=True)
        cl, P = Q[j][0], QH[j]; qq = base.copy()
        qq[:, cl] = P / np.clip(P.sum(1, keepdims=True), 1e-12, None) * base[:, cl].sum(1, keepdims=True)
        qq = np.maximum(qq, 1e-4); w = QW.get(j, PFN_W); K = int(widths[j]); yy = np.where(y >= 0, y, 0)
        for l in lams:
            if l >= 20:                                   # SB-PUSH svlr: pool without donor x twin likelihood^beta
                fk = (1 if l < 30 else 2, j)
                if fk in LRH:                                 # lam-0 output (stack + donors, no pool) x L^beta
                    g = base * np.maximum(LRH[fk], 1e-12) ** ((l - 20) if l < 30 else (l - 30)); g = g / g.sum(1, keepdims=True)
                else:                                         # no likelihood for this item: the lam-0 output
                    g = base
            elif l >= 10:                                 # svnp2: full pool x donor ratio^(rho - (1 - w))
                g = base ** (1 - w) * qq ** w; g = g / g.sum(1, keepdims=True)
                g = g * RV[j] ** ((l - 10) - (1 - w)); g = g / g.sum(1, keepdims=True)
            else:
                g = base ** (1 - w * l) * qq ** (w * l); g = g / g.sum(1, keepdims=True)
            GH[(l, j)] = (g, ok, yy, K)
            if FLOOR_INV:
                g = floor_inverse(g, FLOOR)
            S[l][ok] += np.log(FLOOR + (1 - K * FLOOR) * g[np.arange(len(H)), yy][ok])
        used |= ok; ni += 1
    info = {"items": ni, "rows": int(used.sum())}
    if used.sum() < 30:
        return 1.0, info
    best_l, best_m = 1.0, 0.0
    for l in SV_GRID:
        d = (S[l] - S[1.0])[used]; m, se = d.mean(), d.std(ddof=1) / np.sqrt(len(d))
        info[f"{l:.2f}"] = (round(float(m), 6), round(float(m / (se + 1e-12)), 2))
        if m > 2 * se and m > best_m:
            best_l, best_m = l, m
    return best_l, info


GNP_OK = [False]                                        # set by _run_donors: household path + guard ran + no key tripped


DKI, DKEYS = {}, {}                                      # SB-PUSH: menu winner per item (0 exact_hh, 1 exact, 2+ tolerant keys)


SBO_CLM = int(os.environ.get("SIM_SBO_CLM", 1))      # SBO 5: donor trust for 'claimed' key rows (0 = off = lead; 2 = sabotage: flag permuted)
SBO_INFO = {}


def _sbo_claim(frame, giv, hid, Yv, widths, oof, test, o0, t0, hold=None):
    """SBO 5: a hidden row's key donors are 'claimed' when its key has at least as many visible rows in the row's own round as
    donors in the other round (one-to-one: the donors most likely belong to those rows). For claimed rows of each key class the
    donor step is applied at power t (geometric mix of the pre-donor and the donor vector); t is chosen on VISIBLE rows (same
    statistic, own row excluded) by the OOF log score summed over items, ON only if it beats t = 1 by 2 SE. Returns new (oof, test)."""
    SBO_INFO.clear(); SBO_INFO["gate"] = "on"; t_s = time.time()
    if "wave" not in frame.columns or not all(c in frame.columns for c in HH_LOC + HH_CNT):
        SBO_INFO["gate"] = "cols"; return oof, test
    W = pd.factorize(frame["wave"].astype(str), sort=True)[0]
    if W.max() != 1:
        SBO_INFO["gate"] = "waves"; return oof, test
    vis = ~np.asarray(hid, bool); vi = np.where(vis)[0]; hi = np.where(~vis)[0]
    def key(cols):
        return np.unique(np.stack([pd.factorize(frame[c].astype(str))[0] for c in cols], 1), axis=0, return_inverse=True)[1].reshape(-1)
    ex, hk = key([g for g in giv if g != "wave"]), key(HH_LOC + HH_CNT)
    def cnt(k):
        c = np.zeros((int(k.max()) + 1, 2)); np.add.at(c, (k[vis], W[vis]), 1); return c
    cE, cH = cnt(ex), cnt(hk); own = vis.astype(float)
    nEo, nEs, nHo, nHs = cE[ex, 1 - W], cE[ex, W] - own, cH[hk, 1 - W], cH[hk, W] - own
    cls = np.where(nEo > 0, 0, np.where(nHo > 0, 1, 2)); clm = np.where(cls == 0, nEs >= nEo, np.where(cls == 1, nHs >= nHo, False))
    if SBO_CLM == 2:
        kr = np.flatnonzero(cls < 2); clm = clm.copy(); clm[kr] = clm[np.random.default_rng(7).permutation(kr)]
    J = len(oof); G_ = (0.0, .25, .5, .75, 1.0); new_o, new_t = list(oof), list(test)
    def mix(a, b, t):
        b = np.asarray(b, float); tot = b.sum(1, keepdims=True); v = np.maximum(a, 1e-12) ** (1 - t) * np.maximum(b, 1e-12) ** t
        return v / v.sum(1, keepdims=True) * tot
    for c in (0, 1):
        rv = np.flatnonzero(clm[vi] & (cls[vi] == c)); rh = np.flatnonzero(clm[hi] & (cls[hi] == c))
        rv_all = rv
        if hold is not None and len(hold):
            rv = np.setdiff1d(rv, np.asarray(hold, int))      # SBO: svnp's held-out H rows never select t (no reuse)
        SBO_INFO[f"n{c}"] = (len(rv), len(rh))
        if len(rv) < 30 or len(rh) == 0:
            continue
        S = np.zeros((len(G_), len(rv)))
        for j in range(J):
            if np.abs(np.asarray(oof[j])[rv] - np.asarray(o0[j])[rv]).max() < 1e-12:
                continue
            K_ = int(widths[j]); y = Yv[rv, j]; ok = (y >= 0) & (y < K_); yy = np.where(ok, y, 0)
            for g, t in enumerate(G_):
                S[g] += np.where(ok, _lsr(mix(np.asarray(o0[j])[rv], np.asarray(oof[j])[rv], t), yy, K_), 0.0)
        b = int(S.sum(1).argmax()); d = S[b] - S[-1]; se = d.std(ddof=1) / np.sqrt(len(d)) if len(d) > 1 else np.inf
        t = G_[b] if (b != len(G_) - 1 and d.mean() > 2 * se) else 1.0; SBO_INFO[f"t{c}"] = t
        if t >= 1.0:
            continue
        for j in range(J):
            new_t[j] = np.array(new_t[j], float, copy=True); new_t[j][rh] = mix(np.asarray(t0[j])[rh], np.asarray(test[j])[rh], t)
            new_o[j] = np.array(new_o[j], float, copy=True); new_o[j][rv_all] = mix(np.asarray(o0[j])[rv_all], np.asarray(oof[j])[rv_all], t)
    SBO_INFO["s"] = round(time.time() - t_s, 1)
    return new_o, new_t


def _run_donors(frame, schema, giv, hid, pre, Yv, oof, test, fold, widths, avl=True):
    """Exact-match donor stage (rulings 1, 2; household key only with ruling 4). Mutates oof / test in place; returns
    the number of items switched on, or -1 if the stage raised (vectors kept)."""
    n_don = 0; DKI.clear(); DKEYS.clear(); avi_ = -1; AVLI.clear(); AVO[0] = 0; bak_ = (list(oof), list(test))
    try:
        kcols = [g for g in giv if g not in DONOR_DROP] or list(giv)
        codes = np.stack([pd.factorize(frame[c].astype(str))[0] for c in kcols], 1)   # audit #8: no delimiter join
        keys = np.unique(codes, axis=0, return_inverse=True)[1].reshape(-1)
        hh = DONOR_MODE in ("household", "household_pm1", "exact_hh", "pick", "menu", "menu_bo") and all(c in frame.columns for c in HH_LOC + HH_CNT)
        if hh:
            nb, G = _hh_groups(frame, schema, DONOR_MODE == "household_pm1")
            wcode = pd.factorize(frame["wave"].astype(str), sort=True)[0] if "wave" in frame.columns else np.zeros(len(frame), int)
            hh = int(wcode.max()) == 1
            TKEYS = []
            if DONOR_MODE in ("menu", "menu_bo"):
                for cols in (TOL_COLS, TOL_COLS + TOL_ADULTS):
                    cols = [c for c in cols if c in frame.columns]
                    if len(cols) >= 2:
                        cc = np.stack([pd.factorize(frame[c].astype(str))[0] for c in cols], 1)
                        TKEYS.append(np.unique(cc, axis=0, return_inverse=True)[1].reshape(-1))
            BOK = [keys, nb[:, 0]] + TKEYS[::-1]
            if BO_T3:
                cols = [c for c in TOL_COLS[:2] + HH_CNT if c in frame.columns]
                cc = np.stack([pd.factorize(frame[c].astype(str))[0] for c in cols], 1)
                BOK.insert(2, np.unique(cc, axis=0, return_inverse=True)[1].reshape(-1))
            if AVL and avl and hh and DONOR_MODE == "menu_bo":       # SBX H2: the AVL pointer key (optional: any error -> the build's menu)
                _ta = time.time()
                try:
                    ak_ = _avl_links(frame, schema, giv, hid, Yv, fold, widths, wcode)
                    if ak_ is not None:
                        cn_ = np.zeros((int(max(keys.max(), nb[:, 0].max())) + 1, 2, 2)); np.add.at(cn_, (keys[~hid], wcode[~hid], 0), 1); np.add.at(cn_, (nb[~hid, 0], wcode[~hid], 1), 1)
                        nd_ = (cn_[keys[hid], 1 - wcode[hid], 0] == 0) & (cn_[nb[hid, 0], 1 - wcode[hid], 1] == 0); AVLI["new_hid"] = int((nd_ & (ak_[2] < len(ak_[0]))).sum())
                        avi_ = 2 if AVL_POS == "tw" else len(BOK); BOK.insert(avi_, ak_); AVO[0] = int(avi_ == 2)
                except Exception as e:
                    print(f"[{TAG}] avl skipped: {e!r}"[:300], flush=True); AVLI["gate"] = "error"; avi_ = -1
                AVLI["s"] = round(time.time() - _ta, 1)
            bo_stat = np.zeros(len(BOK), int); bo_win = {}
            GF = _guard_f(BOK, hid, Yv, oof, test, widths, wcode[~hid], wcode[hid]) if (DON_GUARD and hh) else None
            GNP_OK[0] = bool(GNP and GF is not None and not (np.asarray([f_ for i_, f_ in enumerate(GF) if i_ != avi_]) > 0).any())   # SBX H2: the AVL key's own guard value acts on the AVL stage only
        for j in range(len(pre)):
            if time.time() > T0 + LIMIT + 150:       # SB2 xwf Fix 2 (VSC_WALL_AUDIT): whole-run belt; items not visited keep their model vectors
                FAIL["don_cut"] = 1; break
            if hh and DONOR_MODE in ("menu", "menu_bo"):
                y_ = Yv[:, j]; ok_ = y_ >= 0; yy_ = np.where(ok_, y_, 0); K_ = int(widths[j])
                cands = [_donor_eh(keys[~hid], keys[hid], nb[~hid], nb[hid], G, y_, oof[j], test[j], fold, K_, wcode[~hid], wcode[hid]),
                         _donor(keys[~hid], keys[hid], y_, oof[j], test[j], fold, K_)]
                for tk in TKEYS:
                    cands.append(_donor_other(tk, hid, y_, oof[j], test[j], fold, K_, wcode[~hid], wcode[hid]))
                sc_ = lambda r: -np.inf if np.isinf(r[2]) else _lsr(r[0] / r[0].sum(1, keepdims=True), yy_, K_)[ok_].mean()
                if DONOR_MODE == "menu_bo":
                    st_ = np.zeros(len(BOK), int)
                    cands.append(_donor_backoff(BOK, hid, y_, oof[j], test[j], fold, K_, wcode[~hid], wcode[hid], st_, GF))
                r_ = max(cands, key=sc_)
                DKI[j] = [c is r_ for c in cands].index(True); DKEYS.update(ex=keys, hh=nb[:, 0], T=TKEYS)
                if GF is not None and np.isfinite(r_[2]):
                    ci_ = [c is r_ for c in cands].index(True); nT_ = len(TKEYS)
                    f_ = max(GF[0], GF[1]) if ci_ == 0 else GF[0] if ci_ == 1 else GF[1 + nT_ - (ci_ - 2) + AVO[0]] if ci_ < 2 + nT_ else 0.0
                    if f_ > 0:
                        pt_ = test[j] / test[j].sum(1, keepdims=True); rt_ = r_[1] / r_[1].sum(1, keepdims=True)
                        r_ = (r_[0], (1 - f_) * rt_ + f_ * pt_, r_[2]); cands[ci_] = r_
                if DONOR_MODE == "menu_bo":
                    w_ = "off" if np.isinf(r_[2]) else (["exact_hh", "exact"] + [f"T{i + 1}" for i in range(len(TKEYS))] + ["backoff"])[[c is r_ for c in cands].index(True)]
                    bo_win[w_] = bo_win.get(w_, 0) + 1
                    if w_ == "backoff":
                        bo_stat += st_
                oof[j], test[j], kap = r_
            elif hh and DONOR_MODE == "pick":
                y_ = Yv[:, j]; ok_ = y_ >= 0; yy_ = np.where(ok_, y_, 0); K_ = int(widths[j])
                rA = _donor_eh(keys[~hid], keys[hid], nb[~hid], nb[hid], G, y_, oof[j], test[j], fold, K_, wcode[~hid], wcode[hid])
                rB = _donor(keys[~hid], keys[hid], y_, oof[j], test[j], fold, K_)
                sc_ = lambda r: -np.inf if np.isinf(r[2]) else _lsr(r[0] / r[0].sum(1, keepdims=True), yy_, K_)[ok_].mean()
                r_ = rA if sc_(rA) >= sc_(rB) else rB
                oof[j], test[j], kap = r_
            elif hh and DONOR_MODE == "exact_hh":
                oof[j], test[j], kap = _donor_eh(keys[~hid], keys[hid], nb[~hid], nb[hid], G, Yv[:, j], oof[j], test[j], fold, int(widths[j]), wcode[~hid], wcode[hid])
            elif hh:
                oof[j], test[j], kap = _donor_nb(nb[~hid], nb[hid], G, Yv[:, j], oof[j], test[j], fold, int(widths[j]), wcode[~hid], wcode[hid])
            else:
                oof[j], test[j], kap = _donor(keys[~hid], keys[hid], Yv[:, j], oof[j], test[j], fold, int(widths[j]))
            n_don += int(np.isfinite(kap))
        if hh and DONOR_MODE == "menu_bo":
            print(f"[{TAG}] back-off stage forms over all candidates (kappa, transition): {BO_FORM}", flush=True)
            print(f"[{TAG}] menu_bo winners per item {bo_win}; back-off hidden row-items per stage {bo_stat.tolist()} of {int(hid.sum())} rows", flush=True)
        if AVLI:
            if avi_ >= 0:
                AVLI.update(pos=avi_, served=int(bo_stat[avi_]), guard=round(float(GF[avi_]), 3) if GF is not None else -1.0)
            print(f"[{TAG}] avl {AVLI}{' SABOTAGE' if AVL_SAB else ''}", flush=True)
        if hh and NEAR_PASS:
            n_don += 1000 * _near_pass(frame, schema, hid, wcode, pre, Yv, oof, test, fold, widths)
    except Exception as e:                     # optional stage: keep the vectors on any failure
        if avi_ >= 0:                          # SBX H2: the stage raised with the AVL key in the menu -> restore, the build's menu
            print(f"[{TAG}] avl dropped after: {e!r}"[:300], flush=True)
            for j_ in range(len(oof)):
                oof[j_], test[j_] = bak_[0][j_], bak_[1][j_]
            return _run_donors(frame, schema, giv, hid, pre, Yv, oof, test, fold, widths, avl=False)
        print(f"[{TAG}] donors skipped: {e!r}"[:300], flush=True); n_don = -1
    return n_don


def _near_pass(frame, schema, hid, wcode, pre, Yv, oof, test, fold, widths):
    """Lead 5 (ledger 107-108): for rows whose own exact household group has NO other-round visible row, borrow from
    the ONE +-1-count neighbour group if exactly one other-round visible row sits across all neighbour groups (unique;
    ties / none -> no donor). Count index = each visible row's own exact group x round; lookup = borrowed group x other
    round. Own kappa per item; ON only if its OOF gain on its OWN rows beats 2 SE. Mutates oof / test; returns items on."""
    nbpm, G = _hh_groups(frame, schema, True)
    own = nbpm[:, 0]; vis = ~hid; other = 1 - wcode
    cnt = np.zeros((G + 1, 2), int); np.add.at(cnt, (own[vis], wcode[vis]), 1)
    exact_ok = cnt[own, other] > 0
    nbc = np.where(nbpm[:, 1:] < G, cnt[nbpm[:, 1:], other[:, None]], 0)
    use = ~exact_ok & (nbc.sum(1) == 1)
    near_g = nbpm[:, 1:][np.arange(len(own)), np.argmax(nbc, 1)]
    lk = np.where(use, near_g * 2 + other, 2 * G); cv = own * 2 + wcode
    rows = use[vis]
    if rows.sum() < 3:
        return 0
    on = 0
    for j in range(len(pre)):
        o2, t2, kap = _donor_split(cv[vis], lk[vis], lk[hid], 2 * G, Yv[:, j], oof[j], test[j], fold, int(widths[j]), rows)
        oof[j], test[j] = o2, t2; on += int(np.isfinite(kap))
    return on


def _donor_split(cv, lkv, lkh, GG, y, oof, test, fold, K, rows):
    """One-group donor blend with separate count (cv) and lookup (lkv / lkh) keys; GG = empty sentinel. kappa by OOF;
    ON only if the per-row OOF gain on `rows` (the rows that borrow) beats 2 SE. inf = off (vectors unchanged)."""
    ok = y >= 0; yy = np.where(ok, y, 0); nf = int(fold.max()) + 1
    tot = np.zeros((GG + 1, K)); np.add.at(tot, (cv[ok], y[ok]), 1)
    per = np.zeros((nf, GG + 1, K))
    for f in range(nf):
        m = ok & (fold == f); np.add.at(per[f], (cv[m], y[m]), 1)
    c_oof = tot[lkv] - per[fold, lkv]; n_oof = c_oof.sum(1, keepdims=True)
    base = _lsr(oof, yy, K); sel = rows & ok
    best, kap, bd = base[ok].mean(), np.inf, None
    for k in KAPPAS:
        d = _lsr((c_oof + k * oof) / (n_oof + k), yy, K) - base
        if base[ok].mean() + d[ok].mean() > best + 1e-5:
            best, kap, bd = base[ok].mean() + d[ok].mean(), k, d[sel]
    if bd is None or len(bd) < 3 or bd.mean() <= 2 * bd.std(ddof=1) / np.sqrt(len(bd)):
        return oof, test, np.inf
    c_t = tot[lkh]; n_t = c_t.sum(1, keepdims=True)
    return (c_oof + kap * oof) / (n_oof + kap), (c_t + kap * test) / (n_t + kap), kap


def _pure_rules(out, frame, hid, giv, Yv, wrong=False, nmin=20):
    """Pure-cell rules (row 65): a GIVEN level with >= nmin visible rows that ALL gave one answer y* -> held-out rows at that
    level get (1 - d) onehot(y*) + d out, d = 1/(n+2); first matching column wins. wrong=True: y* -> another option (SABOTAGE)."""
    rng = np.random.default_rng(99); new = [o.copy() for o in out]
    for j in range(len(out)):
        K = out[j].shape[1]; y = Yv[:, j]; hit = np.zeros(int(hid.sum()), bool)
        for g in giv:
            col = frame[g].astype(str).to_numpy(); cv, ch = col[~hid], col[hid]
            for v in np.unique(cv):
                ys = y[cv == v]
                if len(ys) >= nmin and (ys >= 0).all() and (ys == ys[0]).all():
                    m = (ch == v) & ~hit
                    if OV_AGREE:                   # never against the model: its own top class must be the pure answer
                        m &= new[j].argmax(1) == int(ys[0])
                    if m.any():
                        ys0 = int(ys[0]) if not wrong else int((ys[0] + 1 + rng.integers(K - 1)) % K)
                        d = 1.0 / (len(ys) + 2); oh = np.zeros(K); oh[ys0] = 1.0
                        new[j][m] = (1 - d) * oh + d * new[j][m] / new[j][m].sum(1, keepdims=True); hit |= m
    return new


def _parents(Yv, widths, Gv, gcards, nas):
    """For each gated item, the visible item whose value best explains its gating; parents must be answered more often."""
    n = len(Yv)
    answered = (Yv != nas).mean(0)              # nas[j] = -9 when j has no NA slot
    par = {}
    for j in np.where(nas >= 0)[0]:
        z = (Yv[:, j] == nas[j]).astype(float)
        if z.mean() in (0.0, 1.0):
            continue
        best, who = _h(z, np.zeros(n, int), 1) - 1e-4, None
        for i in range(Yv.shape[1]):
            if i != j and (answered[i], -i) > (answered[j], -j):
                h = _h(z, Yv[:, i], widths[i])
                if h < best:
                    best, who = h, ("p", i)
        for g in range(Gv.shape[1]):
            h = _h(z, Gv[:, g], gcards[g])
            if h < best:
                best, who = h, ("g", g)
        if who:
            par[j] = who
    return par


def _h(z, x, k):
    """Conditional entropy of binary z given category x."""
    c1 = np.bincount(x, weights=z, minlength=k) + 1e-9
    c = np.bincount(x, minlength=k) + 2e-9
    q = c1 / c
    return float((-(c1 * np.log(q)) - ((c - c1) * np.log(np.clip(1 - q, 1e-12, None)))).sum() / len(z))


def _rate(z, x, k, prior):
    return (np.bincount(x, weights=z, minlength=k) + 2.0 * prior) / (np.bincount(x, minlength=k) + 2.0)


def _swap_na(p, new_na, na):
    """Keep the answer shares, replace the NA probability."""
    new_na = np.clip(new_na, 0.0, 1.0)         # G1: float32 row sums a hair above 1 can push a gate rate past 1
    q = p.copy(); q[:, na] = 0.0
    if FIX2:                                   # audit #2 (+ PASS SB2 #2): uniform answer shares only when the mass is exactly 0
        z = q.sum(1) == 0
        if z.any():
            q[z] = 1.0; q[z, na] = 0.0
        q = q / q.sum(1, keepdims=True) * (1 - new_na)[:, None]
    else:
        q = q / np.clip(q.sum(1, keepdims=True), 1e-12, None) * (1 - new_na)[:, None]
    q[:, na] = new_na
    return q


def _chain(frame, hid, giv, pre, opts, Yv, fold, oof, test, schema):
    gv = schema["gated_value"]
    nas = np.array([o.index(gv) if gv in o else -9 for o in opts])
    widths = [len(o) for o in opts]
    Gall = np.stack([pd.factorize(frame[g].astype(str))[0] for g in giv], 1)
    Gv, Gh = Gall[~hid], Gall[hid]
    gcards = [int(Gall[:, i].max()) + 1 for i in range(Gall.shape[1])]
    par = _parents(Yv, widths, Gv, gcards, nas)
    answered = (Yv != nas).mean(0)
    order = sorted(par, key=lambda j: (-answered[j], j))
    used = 0
    oof = [a.copy() for a in oof]; test = [a.copy() for a in test]
    for j in order:
        y, na = Yv[:, j], nas[j]
        z = (y == na).astype(float)
        kind, i = par[j]
        px, K = (Gv[:, i], gcards[i]) if kind == "g" else (Yv[:, i], widths[i])
        pri = z.mean()
        c_oof = np.zeros(len(y))
        for f in range(FOLDS):
            tr, va = fold != f, fold == f
            r = _rate(z[tr], px[tr], K, pri)
            c_oof[va] = r[px[va]] if kind == "g" else oof[i][va] @ r
        r = _rate(z, px, K, pri)
        c_test = r[Gh[:, i]] if kind == "g" else test[i] @ r
        base = _logscore(oof[j], y).mean()
        best, pick = base + 1e-4, None
        for a in (0.5, 1.0):
            s = _logscore(_swap_na(oof[j], a * c_oof + (1 - a) * oof[j][:, na], na), y).mean()
            if s > best:
                best, pick = s, a
        if pick:
            oof[j] = _swap_na(oof[j], pick * c_oof + (1 - pick) * oof[j][:, na], na)
            test[j] = _swap_na(test[j], pick * c_test + (1 - pick) * test[j][:, na], na)
            used += 1
    return oof, test, used
