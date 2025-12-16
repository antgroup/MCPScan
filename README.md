# MCPScan

> **A multi-stage security scanner for Model Context Protocol (MCP) based on the Agents.**

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![Version](https://img.shields.io/badge/version-0.0.0-orange)
![LLM-Powered](https://img.shields.io/badge/LLM-DeepSeek-yellow)

> 📝 **Paper coming soon**

---

## 🔍 Overview

`MCP Scanner` is a lightweight but powerful tool for auditing AI agent tools and plugin ecosystems.

It integrates **static taint analysis** (via Semgrep rules) and **dynamic LLM evaluation** to detect:
- Malicious metadata (used in prompt injection)
- Insecure tool implementations (e.g., unsafe file reads)
- Code-level vulnerabilities in MCP-compatible services

Supports scanning local codebases or remote GitHub repositories.
![overview](image/overview.png)

[📄 中文版文档 (Chinese README)](README_CN.md)

---

## ✨ Features

+ **Stage 1 (Semgrep Taint Scan)**  
  Detects taint sources and sinks via static rules.

+ **Stage 2 (Metadata Description Monitoring, Optional)**  
  Uses LLM to assess `description` fields — outputs labels: `malicious`, `safe`, `suspect`.

+ **Stage 3 (Cross-file Flow Extraction & Risk Judgment, Optional)**  
  Reconstructs code flow for high-risk patterns and gets final LLM risk verdicts (`HIGH`/`LOW`).

+ **Flexible CLI Control**  
  Toggle each stage, specify rulesets, customize output format.

---

## 🧠 Risks Detected

| Category | Examples |
|----------|----------|
| 🧬 Tool Metadata Pollution | LLM-injectable `description` content |
| 🧪 Tool Poisoning | Malicious URLs or shell code embedded in tools |
| 🔁 Indirect Prompt Injection | Unsafe tool output returns to LLM |
| 🧰 Shadow Tool | Tool defined without proper registration |
| 📤 Data Exfiltration | Sensitive file/network reads exposed to user |
| ☠️ Malicious Code Snippets | Hardcoded command injection, eval(), os.system(), etc. |

---

## 🧰 Installation

### Prerequisites

+ Python 3.8 or higher
+ Semgrep
+ DeepSeek API key

```bash
pip install semgrep
export DEEPSEEK_API_KEY="your_actual_api_key_here"
```

### Install MCP Scanner

```bash
git clone https://github.com/antgroup/Trustworthy_LM.git
cd mcp-scanner
pip install -e .
```

After install, use `mcpscan` as a global CLI command.

---

## ⚙️ Configuration (Optional)

+ Custom Semgrep rules: place in `config/semgrep_rules.yml`
+ Specify alternate config: `--config <FILE>`

---

## 🚀 Usage

### Basic Check
```bash
mcpscan --version
# mcpscan 0.1.0
```

### CLI Options

| Flag | Description | Default |
|------|-------------|---------|
| `<code_address>` | Path or GitHub repo to scan | - |
| `--config <FILE>` | Custom Semgrep ruleset | config/semgrep_rules.yml |
| `--monitor-desc / --no-monitor-desc` | Enable LLM metadata analysis | ✅ Enabled |
| `--monitor-code / --no-monitor-code` | Enable code flow scanning | ✅ Enabled |
| `--save / --no-save` | Save JSON output | ✅ Enabled |
| `--out <FILE>` | Output file name | triage_report.json |

### Commands
```bash
# Full scan of local repo
mcpscan scan ./my-repo

# Skip LLM metadata scan
mcpscan scan ./my-repo --no-monitor-desc

# Scan GitHub repo, no file save
mcpscan scan https://github.com/you/repo --no-monitor-code --no-save

# Custom rules + language override
mcpscan scan ./project -c config/semgrep_rules.yml --lang javascript
```

### Example Commands
```bash

# SFull scan of local repo
mcpscan scan example/fetch


# Scan GitHub repo, no file save
mcpscan scan https://github.com/smithery-ai/mcp-fetch.git


```

---

## 🧭 Scan Workflow

| Stage | Screenshot |
|-------|------------|
| Stage 1: Semgrep Scan Result | ![semgrep-scan](image/semgrep.png) |
| Stage 2: LLM Metadata Scan | ![llm-metadata](image/metadata_scan.png) |
| Stage 3: Code Detection | ![flow-graph](image/code_detection.png) |
| Stage 4: Code Relate and Rist Judgement | ![flow-graph](image/code_relate.png) |
| Final Output (Terminal + JSON) | ![final-output](image/result.png) |


You can toggle stages with `--monitor-desc`, `--monitor-code`, and `--save`.

---

## 👨‍💻 Authors

This project is developed and maintained by:
Zeyang Sha, Hongcheng Li, Changhua Chen, Run Xiong, Shiwen Cui, Changhua Meng, Weiqiang Wang.

---

## 🤝 Contributing

We welcome contributions via Issues or Pull Requests.
If you're building secure LLM agents or need advanced MCP evaluation tooling, feel free to connect.

---

## 📄 Citation

If you use **MCP Scanner** in your research or product, please cite:

```bibtex
@misc{sha2025mcpscan,
  title={MCPSCAN},
  author={Zeyang Sha and Hongcheng Li and Changhua Chen and Run Xiong and Shiwen Cui and Changhua Meng and Weiqiang Wang},
  year={2025},
  url={https://github.com/antgroup/Trustworthy_LM/mcp-scan}
}
```

---

## 📜 License

This project is licensed under the Apache License 2.0.
