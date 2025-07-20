# RML2025 Series Dataset

## 📌 Overview

The **RML2025 Series** dataset is a benchmark collection specifically designed for evaluating **cross-domain automatic modulation classification (AMC)** methods under realistic and progressively complex communication environments.



We simulate a variety of physical impairments commonly present in real-world communication systems. These impairments are combined in a structured manner to generate domain shifts with hierarchical complexity, offering a more challenging and realistic benchmark for evaluating cross-domain AMC methods.

These impairments, including various combinations of **noise, multipath fading, carrier frequency offset (CFO), sampling rate offset (SRO), and Doppler shift**, introduce significant distributional shifts and structural damage in the received signals, thereby posing considerable challenges for robust modulation classification. 


---

## 🧠 Motivation

While existing datasets are useful for standard AMC validation, they fall short in simulating diverse real-world conditions. Specifically:

- Domain shifts in prior benchmarks are often **simplistic or unrealistic**, leading to performance overestimation.
- Publicly available datasets typically lack **structured cross-domain settings**, limiting the development of domain generalization or adaptation techniques.

To address these gaps, RML2025 Series incorporates multiple types and levels of **channel impairments**, structured across domains with increasing complexity.

---

## 📁 Dataset Structure

Each dataset in the RML2025 Series contains:

- **11 modulation types**:  
  8PSK, AM-DSB, AM-SSB, BPSK, CPFSK, GFSK, PAM4, QAM16, QAM64, QPSK, WB-FM
- **20 SNR levels**:  
  From -20 dB to +18 dB in steps of 2 dB
- **220,000 total samples** per subset  
  (1000 samples × 11 modulations × 20 SNR levels)

Each sample consists of **128 complex-valued IQ points**, and all samples are **energy-normalized** to ensure consistency across channel conditions.

---



---

## 🌐 Domains and Subsets

The RML2025 Series includes **7 domains**, grouped by channel type and impairment severity:

| Channel | Domain Name | Impairments                     |
|---------|-------------|----------------------------------|
| AWGN    | `AWGN`      | Gaussian noise only             |
| Rician  | `Ri1`       | Rician fading                   |
| Rician  | `Ri2`       | + CFO + SRO                     |
| Rician  | `Ri3`       | + stronger multipath + Doppler  |
| Rayleigh| `Ray1`      | Rayleigh fading                 |
| Rayleigh| `Ray2`      | + CFO + SRO                     |
| Rayleigh| `Ray3`      | + stronger multipath + Doppler  |

> Each dataset introduces increasingly complex domain shifts and structural distortions, enabling **hierarchical evaluation** of model robustness.

---

## 🔬 Channel Impairment Details

The following table summarizes the specific impairment parameters across different domains:

Channel Impairment Summary

- **MDS (Hz)**: Maximum Doppler Shift  
- **Delay (ms)**: Multipath delay profile  
- **Gains**: Corresponding amplitude weights of multipath components  
- **CFO / SRO**: Carrier Frequency Offset and Sampling Rate Offset; specified as mean (std)

> All Rician and Rayleigh channels use fixed delay/gain profiles with increasing Doppler, CFO, and SRO levels for more realistic simulation of mobile or non-stationary conditions.

## 🔬 Channel Impairment Details

The following table summarizes the impairment configurations for each dataset variant:

| **Dataset** | **MDS (Hz)** | **Delay (ms)**                                      | **Gains**                                         | **CFO / SRO**       |
|-------------|--------------|------------------------------------------------------|---------------------------------------------------|---------------------|
| AWGN        | /            | /                                                    | /                                                 | /                   |
| Ri1         | 4            | [0, 0.9, 1.7]                                         | [1, 0.8, 0.3]                                     | /                   |
| Ri2         | 4            | [0, 0.9, 1.7]                                         | [1, 0.8, 0.3]                                     | 50 (std 0.01)       |
| Ri3         | 30           | [0, 0.05, 0.12, 0.2, 0.23, 0.5, 1.6, 2.3, 5]          | [0.8, 0.8, 0.8, 0.7, 0.6, 0.4, 0.4, 0.4, 0.3]      | 50 (std 0.01)       |
| Ray1        | 1            | [0, 0.9, 1.7]                                         | [1, 0.8, 0.3]                                     | /                   |
| Ray2        | 3            | [0, 0.9, 1.7]                                         | [1, 0.8, 0.3]                                     | 50 (std 0.01)       |
| Ray3        | 30           | [0, 0.05, 0.12, 0.2, 0.23, 0.5, 1.6, 2.3, 5]          | [0.8, 0.8, 0.8, 0.7, 0.6, 0.4, 0.4, 0.4, 0.3]      | 50 (std 0.01)       |

- **MDS**: Maximum Doppler Shift  
- **CFO / SRO**: Carrier Frequency Offset and Sampling Rate Offset  
- All time delays and gain values are normalized and represent the tap profiles in multipath fading scenarios.


## 📥 Dataset Download

You can download the RML2025Series datasets from the following sources:

- **Google Drive**: [Download Link](https://drive.google.com/drive/folders/1M4MKGNUSWZrToL2u507NQbPTNcLKIR-0?usp=drive_link)
- **Baidu Netdisk**: [Download Link](https://pan.baidu.com/s/1alhSU_boq4kBlpH_9A7g5g?pwd=fire) (Extraction Code: `fire`)
(waiting load...)
> ⚠️ Note: Please make sure to unzip the files into the `data/` directory to use the provided loading scripts.



---

## 🚀 Usage

Please refer to the corresponding `load_dataset.py` scripts for how to use each dataset.


---

## 🤖 AI Assistance

This README file was prepared with the assistance of AI tools to enhance clarity and quality. All technical content and dataset descriptions were reviewed and verified by the authors to ensure accuracy.

