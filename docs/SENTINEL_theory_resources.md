# 📖 Theoretical Foundations & Literature Resources for SENTINEL
> **Curated Theory, Official Standards, and Frameworks to Identify Architecture Flaws & Deepen Technical Rigor**

---

## 🎯 Why Theoretical Rigor Matters
To ensure SENTINEL is robust, compliant, and ready for an **IEEE/USENIX paper submission**, your team must ground its design in established cybersecurity, AI safety, and privacy theory. 

Studying these theoretical frameworks will help you **rectify system flaws** before writing production code.

---

## 📚 1. Cybersecurity Operations & SIEM Theory (SOC Fundamentals)

### Key Frameworks & Standards
* **MITRE ATT&CK® Knowledge Base** ([attack.mitre.org](https://attack.mitre.org))
  - **Theory**: Standardized taxonomy of 14 adversary tactics (e.g., *Initial Access*, *Execution*, *Persistence*) and hundreds of techniques (e.g., `T1110 - Brute Force`).
  - **How it fixes flaws**: Ensures SENTINEL's alert outputs map to universally recognized hacker behaviors rather than generic labels.
* **NIST SP 800-61 Rev. 2** (*Computer Security Incident Handling Guide*)
  - **Theory**: The gold standard for incident response lifecycles: **Preparation ➡️ Detection & Analysis ➡️ Containment, Eradication & Recovery ➡️ Post-Incident Activity**.
  - **How it fixes flaws**: Helps structure SENTINEL's automated incident report generator to follow official NIST incident categories.

### Recommended Books
* *"Crafting the InfoSec Playbook: Security Monitoring and Incident Response Master Plan"* (O'Reilly Media)
* *"Applied Network Security Monitoring"* by Chris Sanders & Jason Smith

---

## 🔒 2. Data Privacy & Anonymization Theory (Zero-Trust PII Scrubbing)

### Key Frameworks & Standards
* **NIST SP 800-188** (*De-Identification of Government Datasets*)
  - **Theory**: Concepts of **k-anonymity**, **l-diversity**, and **deterministic token replacement** for data sanitization.
  - **How it fixes flaws**: Ensures [src/sanitizer.py](file:///c:/Users/siva2/Projects/SENTINEL/src/sanitizer.py) completely eliminates PII leakage without breaking the structural logic required by LLMs.
* **GDPR Article 32 & HIPAA Security Rule**
  - **Theory**: Strict mandates on data minimization and preventing confidential corporate data from leaving local boundaries.

### Recommended Reading
* *"Privacy-Preserving Machine Learning"* (Manning Publications / Springer)

---

## 🤖 3. LLM Security, Safety & Vulnerability Theory

### Key Frameworks & Standards
* **OWASP Top 10 for LLM Applications** ([owasp.org/www-project-top-10-for-large-language-model-applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/))
  - **Theory**: Detailed analysis of the top vulnerabilities in AI systems:
    - **LLM01: Prompt Injection** (Attacking models via malicious log payloads)
    - **LLM06: Sensitive Information Disclosure** (Leaking data in output)
    - **LLM08: Excessive Agency** (Giving AI too much authority without human approval)
  - **How it fixes flaws**: Directly addresses SENTINEL's prompt injection vulnerability and validates our **Human-in-the-Loop (HITL)** approval requirement.
* **NIST AI Risk Management Framework (AI RMF 1.0)**
  - **Theory**: Guidelines for building **Valid & Reliable, Safe, Secure & Resilient, Explainable, and Accountable** AI systems.

---

## 🧠 4. RAG & Vector Memory Theory (Dense Embeddings)

### Key Academic Foundation
* **Seminal Paper**: *"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"* (Lewis et al., NeurIPS)
  - **Theory**: Combines parametric memory (pre-trained LLMs) with non-parametric memory (dense vector stores) using cosine similarity search.
  - **How it fixes flaws**: Provides the theoretical basis for SENTINEL's planned **ChromaDB vector store**, allowing the model to recall past incident tickets.

---

## 🔍 5. Where to Search for Top Academic Literature

Use these digital libraries to search for peer-reviewed papers to cite in your Semester 6 submission:

1. **IEEE Xplore Digital Library** ([ieeexplore.ieee.org](https://ieeexplore.ieee.org))
   - *Search Keywords*: `"Security Operations Center"`, `"LLM alert triage"`, `"autonomous incident response"`, `"privacy-preserving cyber intelligence"`.
2. **arXiv.org (Computer Science)** ([arxiv.org/archive/cs](https://arxiv.org/archive/cs))
   - *Subcategories*: `cs.CR` (Cryptography and Security), `cs.AI` (Artificial Intelligence).
3. **USENIX Security Symposium & ACM CCS** ([usenix.org](https://www.usenix.org))
   - Premier conferences for real-world computer security tools and empirical benchmarks.
