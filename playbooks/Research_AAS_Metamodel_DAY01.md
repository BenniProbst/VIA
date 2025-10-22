# Research Playbook: Asset Administration Shell (AAS) Metamodel Architecture

**Date:** 2025-10-22
**Research Focus:** AAS M3 Metamodel, SDK Generation, and Compiler Architecture
**Sources:** aas-core-works repositories, Dr. Santiago Olaya's research, IDTA specifications

---

## 1. Executive Summary

The Asset Administration Shell (AAS) provides a **three-layer metamodel architecture (M3-M2-M1)** that enables standardized digital twin representations of industrial assets. This research analyzes the AAS metamodel structure, the `aas-core-codegen` compiler architecture, and multiple SDK implementations to understand how metamodels can be systematically compiled into executable code.

**Key Findings:**
- AAS uses a **formalized M3 metamodel** written in simplified Python
- **aas-core-codegen** acts as a multi-target compiler generating SDKs for 6+ languages
- The architecture supports **automatic code generation** from model definitions
- Current implementations exist in C++, C#, Python, TypeScript, Java, and Golang

---

## 2. AAS Metamodel Layers (M3-M2-M1)

### 2.1 M3 Layer: Meta-Metamodel (Grundebene)

**Definition:** The M3 layer defines **what kinds of modeling elements exist** and their fundamental properties.

**Key Components in AAS M3:**
- **Classes:** `AssetAdministrationShell`, `Submodel`, `SubmodelElement`
- **Relationships:** Composition, Reference, Association
- **Constraints:** Multiplicity rules, type constraints, validation rules
- **Properties:** Attributes, operations, events

**Repository:** `aas-core-meta`
- Contains formalized meta-models based on IDTA publications
- Written in **simplified Python** for model description
- Versioned releases (date-based schema: YYYY.MM.DD)
- Provides the **canonical definition** for all code generators

**M3 Structure Example:**
```python
# Simplified representation from aas-core-meta
class AssetAdministrationShell:
    """Meta-level definition of AAS"""
    id: Identifier
    asset_information: AssetInformation
    submodels: List[Reference[Submodel]]
    # ... constraints and validation rules
```

**Critical for VIA:** This is the **template for our M3 Compiler** – we need similar metamodel definitions for industrial communication protocols.

---

### 2.2 M2 Layer: Domain-Specific Models (Anwendungsmodelle)

**Definition:** M2 defines **domain-specific types and structures** using M3 building blocks.

**AAS M2 Examples:**
- **Submodel Templates:** Technical Data, Digital Nameplate, Handover Documentation
- **Industry-Specific Models:** Predictive Maintenance, Energy Efficiency, Carbon Footprint
- **Protocol-Specific Models:** OPC UA Companion Specifications, AutomationML mappings

**Key Characteristics:**
- Built using M3 metaclasses
- Can be **vendor-specific** or **standardized**
- Define concrete object types for specific industrial domains
- Include validation rules and semantic constraints

**In VIA Context:**
- M2 will define: **Edge Device Models**, **Message Broker Configurations**, **Process Communication Patterns**
- Customer project definitions live at M2 level
- SDK generation happens M3→M2

---

### 2.3 M1 Layer: Runtime Instances (Laufzeitinstanzen)

**Definition:** M1 contains **actual runtime objects** created from M2 types.

**AAS M1 Examples:**
- A specific motor (Asset ID: `motor-4217-line-3`)
- Its temperature sensor submodel instance
- Current runtime values and states

**In VIA Context:**
- Deployed microservices and edge modules
- Running OPC UA servers with live data
- Concrete industrial system configurations

---

## 3. AAS Code Generator Architecture: aas-core-codegen

### 3.1 Compiler Overview

**Repository:** `aas-core-works/aas-core-codegen`

**Purpose:** "Generate different implementations and schemas based on an AAS meta-model"

**Input:** M3 metamodel written in simplified Python
**Output:** SDKs in multiple languages + schema definitions

---

### 3.2 Supported Target Languages (SDK Generation)

| Language | Repository | Status |
|----------|-----------|--------|
| **C++** | aas-core3.0-cpp | ✅ Production |
| **C#** | aas-core3.0-csharp | ✅ Production |
| **Python** | aas-core3.0-python | ✅ Production |
| **TypeScript** | aas-core3.0-typescript | ✅ Production |
| **Java** | aas-core3.0-java | ✅ Production |
| **Golang** | aas-core3.0-golang | ✅ Production |

---

### 3.3 Supported Schema Generation

| Schema Type | Purpose |
|-------------|---------|
| **JSON Schema** | API validation, data exchange |
| **XSD** | XML schema for legacy systems |
| **RDF SHACL** | Semantic web integration |
| **JSON-LD Context** | Linked data representations |
| **Protobuf** | High-performance serialization |
| **OPC UA NodeSets** | Industrial protocol integration |

---

### 3.4 Code Generation Pipeline

```
┌──────────────────────┐
│  M3 Metamodel        │
│  (simplified Python) │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  aas-core-codegen    │
│  Parser & Analyzer   │
└──────────┬───────────┘
           │
           ├───────────────┐
           ▼               ▼
    ┌──────────┐    ┌──────────┐
    │ Language │    │ Schema   │
    │ SDKs     │    │ Exports  │
    └──────────┘    └──────────┘
```

**Key Design Principles:**
1. **Single source of truth:** M3 metamodel is canonical
2. **Automated generation:** Reduces manual coding errors
3. **Scalability:** Easy to add new target languages
4. **Consistency:** All SDKs implement identical semantics
5. **Implementation snippets:** Custom code can be injected for language-specific optimizations

---

### 3.5 Analysis: How aas-core-codegen Works

**From README analysis:**

> "The generator uses a diagram-based workflow where a single Python meta-model serves as the source for generating multiple implementations."

**Critical Observations:**

1. **Meta-model changes are frequent** → Automated generation is essential
2. **Transformation Rules:**
   - Python classes → Target language classes
   - Python properties → Getters/setters in target language
   - Python constraints → Validation functions
   - Python documentation → API documentation

3. **Code Injection Points:**
   - Custom constructors
   - Serialization/deserialization logic
   - Performance optimizations
   - Platform-specific implementations

**Example Transformation (Python → C++):**
```python
# M3 Definition (simplified Python)
class Referable:
    id_short: Optional[str]
    category: Optional[str]
```

```cpp
// Generated C++ SDK
class Referable {
public:
    std::optional<std::string> id_short;
    std::optional<std::string> category;

    // Generated validation
    bool validate() const;

    // Generated serialization
    nlohmann::json to_json() const;
};
```

---

## 4. SDK Implementation Analysis

### 4.1 Python SDK: aas-core3.0-python

**Key Features:**
- Manipulation, verification, de/serialization of AAS
- **Majority of code automatically generated**
- Documentation: https://aas-core30-python.readthedocs.io/

**Architecture:**
```
aas_core3/
├── types.py          # Generated classes from M3
├── verification.py   # Generated constraint validators
├── jsonization.py    # JSON serialization
├── xmlization.py     # XML serialization
└── enhancing.py      # Runtime enhancement utilities
```

**Code Generation Evidence:**
> "The majority of the code has been automatically generated by aas-core-codegen"

**Implications for VIA:**
- We can auto-generate Python SDKs for our M2 models
- Validation logic can be embedded at generation time
- Multiple serialization formats supported out-of-the-box

---

### 4.2 C++ SDK: aas-core3.0-cpp

**Critical for VIA:** This is our **primary implementation language**.

**Key Characteristics:**
- Modern C++ (C++17/20 compatible)
- Header-only or compiled library options
- Zero-copy serialization support
- Template metaprogramming for type safety

**Generated Components:**
- Class hierarchy matching M3 structure
- Smart pointers for memory management
- Constraint validation at compile-time where possible
- JSON/XML/RDF serialization

**Performance Considerations:**
- Static type checking via templates
- Compile-time constraint verification
- Efficient memory layout
- SIMD-friendly data structures (where applicable)

---

### 4.3 Multi-Language Interoperability

**Key Insight:** All SDKs **implement identical semantics** from the same M3 definition.

**Interoperability Mechanisms:**
1. **JSON Exchange:** All SDKs can serialize/deserialize to JSON
2. **XML Exchange:** Legacy system compatibility
3. **Binary Protocols:** Protobuf for performance
4. **OPC UA:** Industrial protocol integration

**Example Workflow:**
```
C++ System → JSON → Python Analysis → JSON → TypeScript UI
```

All conversions are **lossless** because they share the M3 metamodel.

---

## 5. Comparison: AAS vs. VIA Requirements

### 5.1 Similarities

| Aspect | AAS | VIA |
|--------|-----|-----|
| **Metamodel Layers** | M3-M2-M1 | M3-M2-M1 |
| **Code Generation** | Automated | Automated |
| **Multi-Language** | 6+ languages | C++ primary, others via OPC UA |
| **Industrial Focus** | Digital Twins | Process Communication + Deployment |
| **Standardization** | IDTA/IEC | Custom + OPC UA standards |

---

### 5.2 Differences and VIA Innovations

| Aspect | AAS | VIA (Planned) |
|--------|-----|---------------|
| **Scope** | Asset description | Asset + Communication + Deployment |
| **Runtime** | Passive/Reactive | Proactive + Self-Orchestrating |
| **Deployment** | Manual/External | Automated Horse-Rider Model |
| **Protocol Extension** | OPC UA only | OPC UA + 3 Sub-Protocols |
| **Compiler Chain** | M3→SDKs | M3→M2→M1 (3-stage compilation) |
| **Target** | Digital Twin | **Complete System Orchestration** |

---

### 5.3 Critical Learnings for VIA

**What We Can Adopt:**

1. **Metamodel-First Approach:**
   - Define VIA M3 in a formal language (Python or custom DSL)
   - All code generation derives from M3

2. **Multi-Target Code Generation:**
   - VIA-M3-Compiler should generate C++ SDKs
   - Support future language bindings via same mechanism

3. **Validation at Generation Time:**
   - Embed constraint checking in generated code
   - Static analysis for industrial safety requirements

4. **Versioning Strategy:**
   - Date-based releases like AAS (YYYY.MM.DD)
   - Maintain compatibility matrices between M3 versions

5. **Test Generation:**
   - Use `aas-core3.0-testgen` approach
   - Auto-generate unit tests from M3 constraints

**What VIA Extends:**

1. **Three-Stage Compilation:**
   - M3 Compiler → M2 SDK → M1 System Deploy
   - Each stage is a **separate compiler**

2. **Deployment Integration:**
   - AAS describes assets; VIA **deploys and manages** them
   - Horse-Rider model for dynamic module loading

3. **Process Communication:**
   - Sub-protocols under OPC UA
   - Edge-Group-Protocol, Deploy-Protocol, Process-Group-Protocol

4. **AI-Driven System Generation:**
   - Future: Natural language → M3 definitions → Deployed system
   - Software-in-the-Loop for iterative refinement

---

## 6. Technical Deep-Dive: Code Generation Strategies

### 6.1 Template-Based Generation

**AAS Approach:**
- Uses implementation-specific snippets
- Templates for common patterns
- Allows custom code injection

**VIA Consideration:**
- C++ templates for metaprogramming
- Constexpr evaluation for static analysis
- C++20 Concepts for type constraints

---

### 6.2 Visitor Pattern for Transformation

**Observed in AAS:**
- Visitor pattern for traversing M3 models
- Generates different artifacts per visitor
- Extensible to new target languages

**VIA Implementation:**
```cpp
// Example VIA M3 Visitor Pattern
class M3_To_CPP_Visitor {
public:
    void visit(M3_Class& cls);
    void visit(M3_Property& prop);
    void visit(M3_Constraint& constraint);
    // ... generates C++ code
};
```

---

### 6.3 Constraint Compilation

**AAS Strategy:**
- Constraints defined in M3
- Compiled to validation functions
- Can be runtime or compile-time checks

**VIA Enhancement:**
```cpp
// Compile-time constraint checking in C++20
template<typename T>
concept ValidEdgeDevice = requires(T dev) {
    { dev.protocol() } -> std::convertible_to<ProtocolType>;
    { dev.max_latency() } -> std::convertible_to<std::chrono::microseconds>;
    requires dev.max_latency() < std::chrono::milliseconds(10);
};
```

---

## 7. AAS Object Model Reference

### 7.1 Core M3 Classes (Simplified)

```
AssetAdministrationShell
├── id: Identifier
├── asset_information: AssetInformation
├── submodels: List[Reference[Submodel]]
└── derived_from: Optional[Reference[AAS]]

Submodel
├── id: Identifier
├── semantic_id: Optional[Reference]
├── kind: ModelingKind (Template | Instance)
└── submodel_elements: List[SubmodelElement]

SubmodelElement (abstract)
├── Property
├── MultiLanguageProperty
├── Range
├── File
├── Blob
├── ReferenceElement
├── SubmodelElementCollection
└── Operation
```

---

### 7.2 Key Relationships

```
AAS --[1..*]--> Submodel: references
Submodel --[0..*]--> SubmodelElement: contains
SubmodelElement --[0..1]--> SemanticID: describes
Asset <--[1..1]-- AssetInformation: describes
```

---

### 7.3 Constraint Examples

1. **Uniqueness:** `id` must be unique within scope
2. **Multiplicity:** AAS must reference at least one submodel
3. **Type Safety:** Property values must match declared data type
4. **Semantic Consistency:** `semantic_id` must resolve to valid concept

---

## 8. Relevance to VIA M3 Compiler

### 8.1 Direct Applications

1. **Metamodel Definition Language:**
   - Use Python subset like AAS, or custom DSL
   - Define VIA industrial communication primitives

2. **Code Generator Architecture:**
   - Implement `via-core-codegen` similar to `aas-core-codegen`
   - Target: C++ SDKs primarily

3. **Testing Framework:**
   - Auto-generate tests from M3 constraints
   - Chaos testing for distributed systems

4. **Documentation Generation:**
   - Automatic API docs from M3 annotations
   - Interactive model browsers

---

### 8.2 VIA-Specific Extensions

**M3 Primitives for VIA:**
```python
# VIA M3 Metamodel (conceptual)
class CommunicationEndpoint:
    protocol: ProtocolType  # OPC_UA, MQTT, Modbus, etc.
    direction: Direction    # SEND, RECEIVE, BIDIRECTIONAL
    reliability: ReliabilityClass
    max_latency: TimeDuration

class ProcessGroup:
    members: List[ProcessEndpoint]
    communication_pattern: Pattern  # PUB_SUB, REQ_REP, PIPELINE
    deployment_strategy: Strategy   # HORSE_RIDER, CONTAINER, BARE_METAL
```

---

## 9. Open Research Questions

### 9.1 For VIA M3 Compiler

1. **How to model dynamic protocol switching?**
   - AAS is static; VIA needs runtime reconfiguration
   - Solution: State machines in M3?

2. **How to compile time-critical constraints?**
   - Industrial real-time requirements
   - Can we generate RTOS-compatible code?

3. **How to handle heterogeneous architectures?**
   - x86, ARM, RISC-V, MIPS
   - Cross-compilation strategies?

4. **How to model the Horse-Rider deployment pattern?**
   - Not present in AAS
   - Need new M3 metaclass: `DeploymentContainer`

---

### 9.2 For Further Investigation

1. **Performance of generated code:**
   - Benchmark AAS C++ SDK
   - Compare hand-written vs. generated

2. **Extensibility mechanisms:**
   - How to add custom behavior to generated classes?
   - Plugin architectures?

3. **Integration with CMake:**
   - How does code generation fit in build process?
   - On-demand vs. pre-generated?

---

## 10. Recommendations for VIA Project

### 10.1 Immediate Actions

1. ✅ **Clone and study aas-core-codegen repository**
   - Understand transformation pipeline
   - Identify reusable patterns

2. ✅ **Analyze C++ SDK structure**
   - Study class hierarchies
   - Review serialization mechanisms

3. 🔲 **Design VIA M3 Metamodel**
   - Define core primitives
   - Document constraints

4. 🔲 **Prototype simple code generator**
   - M3 → C++ for one simple class
   - Validate approach

---

### 10.2 Long-Term Strategy

1. **Reuse AAS Tooling Where Possible:**
   - ModelCompiler for OPC UA integration
   - JSON Schema validation

2. **Extend Beyond AAS:**
   - Add process communication primitives
   - Add deployment orchestration models

3. **Build VIA Ecosystem:**
   - via-core-meta (M3 definitions)
   - via-core-codegen (compiler)
   - via-core3.0-cpp (SDK)
   - via-deploy (runtime)

---

## 11. Related Work & Citations

### 11.1 AAS Specifications

- **IDTA:** Industrial Digital Twin Association
- **IEC 63278:** International standard for AAS
- **DIN SPEC 91345:** German specification (deprecated, replaced by IEC)

### 11.2 Relevant Papers

- Dr. Santiago Olaya: Dynamic Multi-Message Broker (MMB) for I4.0
- Comprehensive Management Function Model (CMFM) for HetIndNets

### 11.3 Related Standards

- OPC UA Part 1-14 (Information Model, Services, etc.)
- AutomationML for system engineering
- IEC 61131-3 for PLC programming

---

## 12. Appendix: Repository Links

- **Main Organization:** https://github.com/aas-core-works
- **Metamodel:** https://github.com/aas-core-works/aas-core-meta
- **Code Generator:** https://github.com/aas-core-works/aas-core-codegen
- **C++ SDK:** https://github.com/aas-core-works/aas-core3.0-cpp
- **Python SDK:** https://github.com/aas-core-works/aas-core3.0-python
- **Test Generator:** https://github.com/aas-core-works/aas-core3.0-testgen

---

**End of Research Playbook**

**Next Steps:**
1. Create OPC UA Research Playbook
2. Create CMFM Integration Playbook
3. Begin VIA M3 Metamodel Design Document
