# Vollständige Zitationen: arXiv Papers

**Zweck**: Ergänzung zu `LITERATURE_RESEARCH_DATABASE.md` mit vollständigen arXiv-IDs, Autoren und Jahren
**Status**: 10/30 Papers vervollständigt
**Letzte Aktualisierung**: 2025-10-23

---

## Microservices Performance & Optimization

### 1. PBScaler
**arXiv-ID**: 2303.14620
**Titel**: PBScaler: A Bottleneck-aware Autoscaling Framework for Microservice-based Applications
**Autoren**: Shuaiyu Xie, Jian Wang, Bing Li, Zekun Zhang, Duantengchuan Li, Patrick C. K. Hung
**Jahr**: 2023 (submitted March)
**URL**: https://arxiv.org/abs/2303.14620
**Relevanz**: Autoscaling für VIA Microservices, Bottleneck-Detection relevant für Process-Group-Protocol

### 2. ChainsFormer
**arXiv-ID**: 2309.12592
**Titel**: ChainsFormer: A Chain Latency-aware Resource Provisioning Approach for Microservices Cluster
**Autoren**: Chenghao Song, Minxian Xu, Kejiang Ye, Huaming Wu, Sukhpal Singh Gill, Rajkumar Buyya, Chengzhong Xu
**Jahr**: 2023 (submitted September)
**URL**: https://arxiv.org/abs/2309.12592
**Relevanz**: Latency-aware Provisioning - direkt relevant für H1-Hypothese (Latenz-Optimierung)

---

## Inter-Process Communication (IPC)

### 3. TZC: Efficient IPC for Robotics Middleware
**arXiv-ID**: 1810.00556
**Titel**: TZC: Efficient Inter-Process Communication for Robotics Middleware with Partial Serialization
**Autoren**: Yu-Ping Wang, Wende Tan, Xu-Qiang Hu, Dinesh Manocha, Shi-Min Hu
**Jahr**: 2018 (submitted October)
**URL**: https://arxiv.org/abs/1810.00556
**Relevanz**: Partial Serialization für IPC - Optimierungsansatz für VIA Process-Group-Protocol
**ROS-Bezug**: ✅ Direkt relevant für ROS-VIA-Integration (Abschnitt 3.0.2 im Exposé)

---

## Asset Administration Shell (AAS)

### 4. Generation of AAS with LLM Agents
**arXiv-ID**: 2403.17209
**Titel**: Generation of Asset Administration Shell with Large Language Model Agents
**Autoren**: Yuchen Xia, Zhewen Xiao, Nasser Jazdi, Michael Weyrich
**Jahr**: 2024 (published in IEEE Access)
**URL**: https://arxiv.org/abs/2403.17209
**GitHub**: https://github.com/YuchenXia/AASbyLLM
**Relevanz**: AI-gestützte AAS-Generierung - potenzielle Extension für VIA SITL (M3-Texttransformation)
**Key Findings**: 62-79% effective generation rate für Digital Twin Instances

---

## Compiler Optimization für Distributed Systems

### 5. DeepCompile
**arXiv-ID**: 2504.09983
**Titel**: DeepCompile: A Compiler-Driven Approach to Optimizing Distributed Deep Learning Training
**Autoren**: Masahiro Tanaka, Du Li, Umesh Chand, Ali Zafar, Haiying Shen, Olatunji Ruwase
**Jahr**: 2025 (submitted April)
**URL**: https://arxiv.org/abs/2504.09983
**Relevanz**: Profiling-guided optimization passes für distributed training - Ansatz übertragbar auf VIA-M2-Compiler
**Key Findings**: Communication-Computation Overlap Optimization

### 6. Triton-distributed
**arXiv-ID**: 2504.19442
**Titel**: Triton-distributed: Programming Overlapping Kernels on Distributed AI Systems with the Triton Compiler
**Autoren**: Size Zheng et al. (21 authors)
**Jahr**: 2025 (submitted April)
**URL**: https://arxiv.org/abs/2504.19442
**Relevanz**: Compiler-Extension für distributed workloads - ähnlich VIA-M3-Compiler-Extensions für Prozesskommunikation

---

## Distributed Consensus Protocols

### 7. Ocior: Ultra-Fast Leaderless Consensus
**arXiv-ID**: 2509.01118
**Titel**: Ocior: Ultra-Fast Asynchronous Leaderless Consensus with Two-Round Finality, Linear Overhead, and Adaptive Security
**Autoren**: Jinyuan Chen
**Jahr**: 2025 (submitted September)
**URL**: https://arxiv.org/abs/2509.01118
**Relevanz**: Byzantine Fault Tolerance für VIA Master Active Management, optimal resilience O(n) communication
**Key Findings**: Toleriert bis zu t faulty nodes, O(n) total expected communication per transaction

---

## Model-Driven Engineering & DSL

### 8. M2QCode: Multi-Platform Quantum Programs
**arXiv-ID**: 2510.17110
**Titel**: M2QCode: A Model-Driven Framework for Generating Multi-Platform Quantum Programs
**Autoren**: Xiaoyu Guo, Shinobu Saito, Jianjun Zhao
**Jahr**: 2025 (submitted October)
**URL**: https://arxiv.org/abs/2510.17110
**Relevanz**: Model-Driven Code Generation - Parallel zu VIA M3→M2 Transformation
**Key Findings**: Automatic code generation across different quantum programming languages

---

## Noch zu vervollständigen (22 Papers)

### Multi-Objective Optimization (6 Papers)
- [ ] "Multi-Objective Genetic Algorithm for Healthcare Workforce Scheduling"
- [ ] "Metronome: Efficient Scheduling for Periodic Traffic Jobs"
- [ ] "Production Scheduling Framework for Reinforcement Learning"
- [ ] "Coordinated Battery Electric Vehicle Charging Scheduling"
- [ ] "Resource Scheduling for UAVs-aided D2D Networks" (NSGA-III)
- [ ] "CASPER: Carbon-Aware Scheduling for Distributed Web Services"

### Microservices (2 Papers)
- [ ] Kabamba et al. (2023) "Advanced Strategies for Precise and Transparent Debugging..."
- [ ] Henning & Hasselbring (2023) "Benchmarking scalability of stream processing frameworks..."

### IPC (2 Papers)
- [ ] "REACT: Distributed Mobile Microservice Execution"
- [ ] "Nyx-Net: Network Fuzzing with Incremental Snapshots"

### OPC UA & Digital Twins (4 Papers)
- [ ] "OPC UA for IO-Link Wireless in a Cyber Physical Finite Element Sensor Network"
- [ ] "Timeseries on IIoT Platforms: Requirements and Survey for Digital Twins"
- [ ] "An Architecture for Deploying Reinforcement Learning in Industrial Environments"
- [ ] "Towards Deterministic Communications in 6G Networks"

### AAS (2 Papers)
- [ ] Strakosova et al. (2025) "Product-oriented Product-Process-Resource Asset Network"
- [ ] da Silva et al. (2023) "Toward a Mapping of Capability and Skill Models"

### Compiler Optimization (4 Papers)
- [ ] "T10: Scaling Deep Learning Computation over the Inter-Core Connected Intelligence Processor"
- [ ] "Diffuse: Composing Distributed Computations Through Task and Kernel Fusion"
- [ ] "Matryoshka: Optimization of Dynamic Diverse Quantum Chemistry Systems"
- [ ] Layout-Agnostic MPI Abstraction for Distributed Computing in Modern C++

### MDE & DSL (4 Papers)
- [ ] "A Model-Driven Engineering Approach to AI-Powered Healthcare Platforms"
- [ ] "Model-Driven Quantum Code Generation Using Large Language Models"
- [ ] "MERLAN: A Domain-Specific Language (DSL) to specify requirements for multimodal interfaces"
- [ ] "LLM-based Iterative Approach to Metamodeling in Automotive"

### Distributed Consensus (2 Papers)
- [ ] "Functional Reasoning for Distributed Systems with Failures" (Byzantine Fault Tolerance)
- [ ] "pBeeGees: A Prudent Approach to Certificate-Decoupled BFT Consensus"

### Cloud Computing (5 Papers)
- [ ] "Propius: A Platform for Collaborative Machine Learning across the Edge and the Cloud"
- [ ] "CPU-Limits kill Performance: Time to rethink Resource Control"
- [ ] "Towards Efficient VM Placement: A Two-Stage ACO-PSO Approach for Green Cloud Infrastructure"
- [ ] "GFS: A Preemption-aware Scheduling Framework for GPU Clusters"
- [ ] "CloudFormer: An Attention-based Performance Prediction for Public Clouds"

---

## Nächste Schritte

1. **arXiv Search automatisieren**: Für jedes Paper obige Liste durchgehen
2. **DOIs ergänzen**: Für Papers die auch in Konferenzen/Journals publiziert wurden
3. **Abstracts extrahieren**: Key Findings für jedes Paper
4. **VIA-Relevanz bewerten**: 1-5 Sterne System einführen

**Update-Frequenz**: Täglich 10 Papers vervollständigen bis alle 30 fertig sind
