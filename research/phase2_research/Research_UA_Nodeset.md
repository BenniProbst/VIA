# OPC UA Research: UA-Nodeset Repository
## OPC Foundation Standard NodeSets & Companion Specifications

**Repository**: https://github.com/OPCFoundation/UA-Nodeset
**Maintainer**: OPC Foundation
**License**: OPC Foundation License (varies by NodeSet)
**Branches**: latest (v1.05), v1.04, v1.03
**Relevanz für VIA**: Standard Information Models, AAS Integration, Custom NodeSet Templates
**Analysiert**: 2025-10-22

---

## 1. Repository Overview

### 1.1 Purpose

> "This repository contains UANodeSets and other normative files which are released with a specification."

**Mission**:
- Provide official OPC UA NodeSet definitions
- Distribute Companion Specifications
- Enable standardized information modeling across industries
- Support code generation tools (e.g., open62541 nodeset_compiler)

### 1.2 Repository Structure

**Main Components**:
```
UA-Nodeset/
├── Schema/                  # Base OPC UA schemas
│   ├── Opc.Ua.NodeSet2.xml
│   ├── Opc.Ua.Types.xsd
│   └── ...
│
├── DI/                      # Device Integration
├── PLCopen/                 # PLC programming
├── I4AAS/                   # Asset Administration Shell
├── Robotics/               # Robotics specification
├── AutoID/                 # Auto Identification
├── CNC/                    # CNC machines
├── MTConnect/              # Machine monitoring
├── ...                     # 76+ companion specifications
│
└── README.md
```

**File Types per Companion Spec**:
- `.NodeSet2.xml` - Formal node definitions (main file)
- `.Types.xsd` - XML Schema for DataTypes
- `.Types.bsd` - OPC Binary Schema (obsolete)
- `.NodeIds.csv` - NodeId assignments
- `.Classes.cs` - C# node classes (optional)
- `.DataTypes.cs` - C# DataType classes (optional)
- `.Constants.cs` - C# constant declarations (optional)
- `.PredefinedNodes.uanodes` - Binary UANodeSet representation (optional)

---

## 2. Standard NodeSets

### 2.1 Base OPC UA Types (Namespace 0)

**File**: `Schema/Opc.Ua.NodeSet2.xml`

**Contains**:
- Core OPC UA types (Int32, String, DateTime, etc.)
- Base object types (BaseObjectType, FolderType, etc.)
- Standard variable types
- Standard reference types (HasComponent, Organizes, etc.)
- Standard method types

**Namespace**: `http://opcfoundation.org/UA/` (Namespace 0)

**Usage**:
- **Required** for all OPC UA servers
- Foundation for all custom information models
- Loaded by open62541 via `UA_NAMESPACE_ZERO` config

**Size Options** (open62541):
- MINIMAL: ~100 nodes
- REDUCED: ~500 nodes
- FULL: ~3000 nodes

### 2.2 NodeSet XML Structure

**Root Element**: `<UANodeSet>`
```xml
<UANodeSet xmlns="http://opcfoundation.org/UA/2011/03/UANodeSet.xsd">
    <NamespaceUris>
        <Uri>http://example.com/MyModel</Uri>
    </NamespaceUris>

    <Aliases>
        <Alias Alias="Boolean">i=1</Alias>
        <Alias Alias="Int32">i=6</Alias>
        <!-- ... -->
    </Aliases>

    <!-- Node Definitions -->
    <UAObject>...</UAObject>
    <UAVariable>...</UAVariable>
    <UAMethod>...</UAMethod>
    <UAObjectType>...</UAObjectType>
    <UAVariableType>...</UAVariableType>
    <UADataType>...</UADataType>

</UANodeSet>
```

**Node Elements**:
1. **UAObject**: Object instances
2. **UAVariable**: Variable instances
3. **UAMethod**: Method instances
4. **UAObjectType**: Object type definitions
5. **UAVariableType**: Variable type definitions
6. **UADataType**: Custom data type definitions
7. **UAReferenceType**: Custom reference type definitions

**Example UAObject**:
```xml
<UAObject NodeId="ns=1;i=5001" BrowseName="1:MyDevice">
    <DisplayName>My Device</DisplayName>
    <Description>Example device object</Description>
    <References>
        <Reference ReferenceType="HasTypeDefinition">i=58</Reference>
        <Reference ReferenceType="HasComponent">ns=1;i=5002</Reference>
        <Reference ReferenceType="Organizes" IsForward="false">i=85</Reference>
    </References>
</UAObject>
```

**Example UAVariable**:
```xml
<UAVariable NodeId="ns=1;i=5002" BrowseName="1:Temperature" DataType="Double">
    <DisplayName>Temperature</DisplayName>
    <References>
        <Reference ReferenceType="HasTypeDefinition">i=63</Reference>
        <Reference ReferenceType="HasComponent" IsForward="false">ns=1;i=5001</Reference>
    </References>
    <Value>
        <uax:Double>25.0</uax:Double>
    </Value>
</UAVariable>
```

---

## 3. Companion Specifications

### 3.1 Overview (76+ Specifications)

**Major Companion Specs**:

| Specification | Namespace | Domain |
|--------------|-----------|--------|
| **DI** (Device Integration) | `http://opcfoundation.org/UA/DI/` | Generic device integration |
| **PLCopen** | `http://PLCopen.org/OpcUa/IEC61131-3/` | PLC programming |
| **I4AAS** | `http://opcfoundation.org/UA/I4AAS/` | Asset Administration Shell |
| **Robotics** | `http://opcfoundation.org/UA/Robotics/` | Industrial robots |
| **AutoID** | `http://opcfoundation.org/UA/AutoID/` | RFID, barcode, etc. |
| **CNC** | `http://opcfoundation.org/UA/CNC/` | CNC machines |
| **MTConnect** | `http://opcfoundation.org/UA/MTConnect/` | Machine monitoring |
| **PackML** | `http://opcfoundation.org/UA/PackML/` | Packaging machines |
| **EUROMAP** | `http://opcfoundation.org/UA/EUROMAP/` | Injection molding |
| **ISA-95** | `http://www.opcfoundation.org/UA/2013/01/ISA95/` | MES integration |

**Emerging Specs**:
- CommercialKitchenEquipment
- Glass/Flat (glass manufacturing)
- Scales (weighing systems)
- Woodworking
- AMB (Additive Manufacturing)
- BACnet (building automation)

### 3.2 Device Integration (DI)

**Repository Path**: `DI/`

**Purpose**:
- Generic device modeling
- Base for many other companion specs
- Device parameters, diagnostics, asset management

**Files**:
- `Opc.Ua.DI.NodeSet2.xml`
- `Opc.Ua.Di.NodeIds.csv`
- `Opc.Ua.DI.NodeSet2.documentation.csv`
- `Opc.Ua.Di.Types.xsd`
- `Opc.Ua.Di.Types.bsd` (obsolete)

**Key ObjectTypes**:
- `DeviceType` - Base for all devices
- `BlockType` - Functional block
- `ConfigurableObjectType` - Configurable components
- `TopologyElementType` - Network topology

**Typical Device Hierarchy**:
```
DeviceSet (Folder)
└── MyDevice (DeviceType)
    ├── DeviceHealth (Variable)
    ├── ParameterSet (Object)
    │   ├── Parameter1 (Variable)
    │   └── Parameter2 (Variable)
    └── MethodSet (Object)
        ├── Start (Method)
        └── Stop (Method)
```

**VIA Relevance**:
> DI provides template for modeling VIA Processes as OPC UA devices

### 3.3 Industrie 4.0 AAS (I4AAS)

**Repository Path**: `I4AAS/`

**Purpose**:
- Map Asset Administration Shell to OPC UA
- Enable I4.0 interoperability
- Expose AAS Submodels via OPC UA

**Files**:
- `Opc.Ua.I4AAS.NodeSet2.xml`
- `NodeIds.csv`

**Key Concepts** (from AAS standard):
- **AssetAdministrationShell** → OPC UA Object
- **Submodel** → OPC UA Object
- **SubmodelElement** → OPC UA Variable/Object
- **Property** → OPC UA Variable
- **Operation** → OPC UA Method

**Example Mapping**:
```xml
<!-- AAS Shell -->
<UAObject NodeId="ns=2;i=1000" BrowseName="2:MyAssetAAS">
    <DisplayName>My Asset AAS</DisplayName>
    <References>
        <Reference ReferenceType="HasTypeDefinition">ns=2;i=1001</Reference>
        <Reference ReferenceType="HasComponent">ns=2;i=1100</Reference> <!-- Submodel -->
    </References>
</UAObject>

<!-- AAS Submodel -->
<UAObject NodeId="ns=2;i=1100" BrowseName="2:TechnicalDataSubmodel">
    <DisplayName>Technical Data</DisplayName>
    <References>
        <Reference ReferenceType="HasTypeDefinition">ns=2;i=1002</Reference>
        <Reference ReferenceType="HasProperty">ns=2;i=1101</Reference> <!-- Property -->
    </References>
</UAObject>

<!-- AAS Property -->
<UAVariable NodeId="ns=2;i=1101" BrowseName="2:ManufacturerName" DataType="String">
    <DisplayName>Manufacturer Name</DisplayName>
    <Value>
        <uax:String>ACME Corp</uax:String>
    </Value>
</UAVariable>
```

**VIA Integration**:
```
VIA Process Metadata (AAS Submodel)
    ↓
VIA-M3-Compiler generates I4AAS NodeSet
    ↓
open62541 Nodeset Compiler → C code
    ↓
Embedded in VIA Process OPC UA Server
```

### 3.4 PLCopen

**Repository Path**: `PLCopen/`

**Purpose**:
- IEC 61131-3 PLC programming integration
- Function blocks, programs, tasks
- PLC diagnostics and control

**Key ObjectTypes**:
- `CtrlProgramOrganizationUnitType`
- `CtrlTaskType`
- `CtrlFunctionBlockType`
- `CtrlConfigurationType`

**VIA Relevance**:
> VIA Scheduler could expose task scheduling via PLCopen-inspired model

### 3.5 Other Notable Specs

**Robotics**:
- Robot motion control
- Safety functions
- Task programming

**AutoID**:
- RFID readers, barcode scanners
- Useful for VIA asset tracking

**MTConnect**:
- Machine tool monitoring
- Standardized machine data model

**ISA-95**:
- MES (Manufacturing Execution System) integration
- Level 2/3 automation (aligns with VIA vision)

---

## 4. NodeSet Versioning

### 4.1 Semantic Versioning

**Format**: `v1.0x` (e.g., v1.05, v1.04)

**Branches**:
- `latest` - Current released version (v1.05)
- `v1.04` - Previous stable
- `v1.03` - Legacy

**Compatibility**:
- Minor version updates (v1.04 → v1.05): Backward compatible
- Major version updates (v1.x → v2.x): Breaking changes

### 4.2 NodeSet Updates

**Release Cycle**:
- Companion Specs updated independently
- OPC Foundation reviews and publishes
- GitHub repository updated after formal release

**Issue Tracking**:
- Report errors via OPC Foundation Mantis system
- GitHub Issues **not used** for bug reports

---

## 5. NodeSet Generation & Usage

### 5.1 Using NodeSets with open62541

**Workflow**:
```bash
# 1. Download NodeSet from UA-Nodeset repository
wget https://raw.githubusercontent.com/OPCFoundation/UA-Nodeset/latest/DI/Opc.Ua.DI.NodeSet2.xml

# 2. Compile with open62541 nodeset_compiler
python nodeset_compiler/nodeset_compiler.py \
    --xml Opc.Ua.NodeSet2.xml \
    --xml Opc.Ua.DI.NodeSet2.xml \
    --output di_nodeset

# 3. Generated files: di_nodeset.c, di_nodeset.h

# 4. Integrate in server
gcc server.c di_nodeset.c -lopen62541 -o server
```

**C Integration**:
```c
#include <open62541/server.h>
#include "di_nodeset.h"

int main() {
    UA_Server *server = UA_Server_new();

    // Load DI nodeset
    UA_StatusCode retval = di_nodeset_namespace(server);
    if (retval != UA_STATUSCODE_GOOD) {
        printf("Failed to load DI nodeset\n");
        return EXIT_FAILURE;
    }

    UA_Server_run_startup(server);
    // ...
}
```

### 5.2 Creating Custom NodeSets

**Approach 1: XML Authoring** (Manual)
```xml
<?xml version="1.0" encoding="utf-8"?>
<UANodeSet xmlns="http://opcfoundation.org/UA/2011/03/UANodeSet.xsd">
    <NamespaceUris>
        <Uri>http://example.com/VIA/</Uri>
    </NamespaceUris>

    <UAObjectType NodeId="ns=1;i=1001" BrowseName="1:VIAProcessType">
        <DisplayName>VIA Process Type</DisplayName>
        <References>
            <Reference ReferenceType="HasSubtype" IsForward="false">i=58</Reference>
            <Reference ReferenceType="HasComponent">ns=1;i=1002</Reference>
        </References>
    </UAObjectType>

    <UAVariable NodeId="ns=1;i=1002" BrowseName="1:ProcessState" DataType="Int32">
        <DisplayName>Process State</DisplayName>
        <References>
            <Reference ReferenceType="HasTypeDefinition">i=63</Reference>
        </References>
    </UAVariable>
</UANodeSet>
```

**Approach 2: UaModeler** (Graphical Tool)
- OPC Foundation's official modeling tool
- Visual NodeSet design
- Export to .NodeSet2.xml
- Commercial license required

**Approach 3: Code Generation** (VIA-M3-Compiler)
```
VIA M3 Metamodel
    ↓
VIA-M3-Compiler (custom tool)
    ↓
VIA.NodeSet2.xml (generated)
    ↓
open62541 nodeset_compiler
    ↓
via_nodeset.c/.h (C code)
```

---

## 6. VIA Custom Companion Specification

### 6.1 VIA NodeSet Vision

**Goal**: Define VIA-specific OPC UA information model

**VIA Companion Spec Structure**:
```
VIA/ (Custom Companion Spec)
├── Opc.Ua.VIA.NodeSet2.xml
├── Opc.Ua.VIA.NodeIds.csv
├── Opc.Ua.VIA.Types.xsd
└── README.md
```

### 6.2 VIA ObjectTypes

**Core VIA Types**:

1. **VIAProcessType** (extends DeviceType)
   - ProcessID (String)
   - ProcessType (Enum: Worker, Router, Scheduler, Registry)
   - State (Enum: Running, Stopped, Error)
   - Telemetry (Object: CPU, Memory, Network)
   - Start() (Method)
   - Stop() (Method)
   - Configure() (Method)

2. **VIARouterType** (extends VIAProcessType)
   - RoutingTable (Array of Routes)
   - ActiveConnections (UInt32)
   - MessagesRouted (UInt64)

3. **VIASchedulerType** (extends VIAProcessType)
   - TaskQueue (Array of Tasks)
   - ScheduledTasks (UInt32)
   - CompletedTasks (UInt64)

4. **VIARegistryType** (extends VIAProcessType)
   - RegisteredProcesses (Array)
   - DiscoverProcess() (Method)
   - RegisterProcess() (Method)

### 6.3 Example VIA NodeSet (Excerpt)

```xml
<UAObjectType NodeId="ns=2;i=1001" BrowseName="2:VIAProcessType">
    <DisplayName>VIA Process Type</DisplayName>
    <Description>Base type for all VIA processes</Description>
    <References>
        <Reference ReferenceType="HasSubtype" IsForward="false">ns=1;i=1002</Reference> <!-- DeviceType from DI -->

        <!-- Properties -->
        <Reference ReferenceType="HasProperty">ns=2;i=2001</Reference> <!-- ProcessID -->
        <Reference ReferenceType="HasProperty">ns=2;i=2002</Reference> <!-- ProcessType -->
        <Reference ReferenceType="HasProperty">ns=2;i=2003</Reference> <!-- State -->

        <!-- Components -->
        <Reference ReferenceType="HasComponent">ns=2;i=3001</Reference> <!-- Telemetry -->

        <!-- Methods -->
        <Reference ReferenceType="HasComponent">ns=2;i=4001</Reference> <!-- Start -->
        <Reference ReferenceType="HasComponent">ns=2;i=4002</Reference> <!-- Stop -->
    </References>
</UAObjectType>

<UAVariable NodeId="ns=2;i=2001" BrowseName="2:ProcessID" DataType="String">
    <DisplayName>Process ID</DisplayName>
    <Description>Unique identifier for this VIA process</Description>
    <References>
        <Reference ReferenceType="HasTypeDefinition">i=68</Reference> <!-- PropertyType -->
        <Reference ReferenceType="HasModellingRule">i=78</Reference> <!-- Mandatory -->
    </References>
</UAVariable>

<UAMethod NodeId="ns=2;i=4001" BrowseName="2:Start">
    <DisplayName>Start</DisplayName>
    <Description>Start the VIA process</Description>
    <References>
        <Reference ReferenceType="HasProperty">ns=2;i=4011</Reference> <!-- InputArguments -->
        <Reference ReferenceType="HasProperty">ns=2;i=4012</Reference> <!-- OutputArguments -->
    </References>
</UAMethod>
```

---

## 7. Integration with VIA-M3-Compiler

### 7.1 Code Generation Pipeline

**Full Pipeline**:
```
┌─────────────────────────┐
│  VIA M3 Metamodel       │
│  (Protobuf/OpenAPI)     │
└───────────┬─────────────┘
            │
            ↓
┌─────────────────────────┐
│  VIA-M3-Compiler        │
│  (Python/C++ tool)      │
└───────────┬─────────────┘
            │
            ├──────────────────────────┐
            ↓                          ↓
┌─────────────────────────┐  ┌─────────────────────────┐
│  VIA-M2-SDK-C++         │  │  Opc.Ua.VIA.NodeSet2.xml│
│  (gRPC Services)        │  │  (OPC UA NodeSet)       │
└─────────────────────────┘  └───────────┬─────────────┘
                                         │
                                         ↓
                            ┌─────────────────────────┐
                            │  open62541              │
                            │  nodeset_compiler.py    │
                            └───────────┬─────────────┘
                                        │
                                        ↓
                            ┌─────────────────────────┐
                            │  via_nodeset.c/.h       │
                            │  (C Code)               │
                            └───────────┬─────────────┘
                                        │
                                        ↓
                            ┌─────────────────────────┐
                            │  VIA Process            │
                            │  + embedded OPC UA      │
                            └─────────────────────────┘
```

### 7.2 VIA-M3-Compiler Extensions

**Required Features**:
1. **Parse VIA M3 Metamodel** (Protobuf messages)
2. **Generate OPC UA NodeSet XML** (ObjectTypes, Variables, Methods)
3. **Assign NodeIds** (consistent namespace management)
4. **Generate .NodeIds.csv** (for documentation)
5. **Validate against OPC UA schemas** (XSD validation)

**Example Implementation** (pseudo-code):
```python
class VIANodeSetGenerator:
    def generate(self, via_metamodel):
        nodeset = UANodeSet()
        nodeset.namespace_uri = "http://via-project.org/UA/"

        for process_type in via_metamodel.process_types:
            obj_type = self.create_object_type(process_type)
            nodeset.add_node(obj_type)

            for property in process_type.properties:
                var = self.create_variable(property)
                nodeset.add_node(var)
                nodeset.add_reference(obj_type, var, "HasProperty")

            for method in process_type.methods:
                meth = self.create_method(method)
                nodeset.add_node(meth)
                nodeset.add_reference(obj_type, meth, "HasComponent")

        nodeset.write_xml("Opc.Ua.VIA.NodeSet2.xml")
```

---

## 8. Erkenntnisse für VIA

### 8.1 Übernehmen von UA-Nodeset

**✅ Direct Adoption**:
1. **Standard Companion Specs**: Use DI as base for VIA processes
2. **I4AAS Integration**: Map VIA process metadata to AAS Submodels
3. **NodeSet XML Format**: Follow OPC Foundation standards
4. **Versioning Strategy**: Align with OPC Foundation v1.0x scheme
5. **open62541 Integration**: Use nodeset_compiler for code generation

### 8.2 VIA-Specific Innovations

**Custom VIA Companion Spec**:
- Define VIA-specific ObjectTypes (VIAProcessType, VIARouterType, etc.)
- Extend DI (Device Integration) as base
- Combine with I4AAS for Submodel exposure

**Dynamic Address Space**:
- VIA Registry registers/unregisters processes → dynamic OPC UA nodes
- Real-time address space updates (not covered by static NodeSets)

**Hybrid Model**:
- Static NodeSet: VIA types (VIAProcessType, etc.)
- Dynamic Instances: Created at runtime when VIA processes register

### 8.3 Development Roadmap

**Phase 1: Custom NodeSet Creation**:
- ✅ Analyze UA-Nodeset repository (DONE)
- 🔲 Design VIA ObjectTypes (VIAProcessType hierarchy)
- 🔲 Author `Opc.Ua.VIA.NodeSet2.xml` manually (v1.0)
- 🔲 Test with open62541 nodeset_compiler

**Phase 2: VIA-M3-Compiler Integration**:
- 🔲 Extend VIA-M3-Compiler to generate OPC UA NodeSet XML
- 🔲 Automate NodeId assignment
- 🔲 Validate generated XML against OPC UA schemas

**Phase 3: Dynamic Features**:
- 🔲 Implement runtime node creation (VIA Registry ↔ OPC UA)
- 🔲 Combine static types + dynamic instances
- 🔲 Test with industrial OPC UA clients (UAExpert, etc.)

**Phase 4: Submission to OPC Foundation**:
- 🔲 Document VIA Companion Specification
- 🔲 Submit to OPC Foundation for review
- 🔲 Potential official VIA Companion Spec release

---

## 9. Referenzen

**Repository**:
- https://github.com/OPCFoundation/UA-Nodeset

**OPC Foundation Standards**:
- OPC UA Part 3: Address Space Model
- OPC UA Part 5: Information Model
- OPC UA Part 6: Mappings (XML encoding)

**Companion Specifications**:
- DI (Device Integration): https://opcfoundation.org/developer-tools/specifications-opc-ua-information-models/opc-unified-architecture-companion-specification-for-device-integration-di/
- I4AAS: https://opcfoundation.org/markets-collaboration/i4-asset-administration-shell/
- PLCopen: https://opcfoundation.org/markets-collaboration/plcopen/

**Tools**:
- UaModeler (commercial): https://www.unified-automation.com/products/development-tools/uamodeler.html
- open62541 nodeset_compiler: https://github.com/open62541/open62541/tree/master/tools/nodeset_compiler

**Issue Tracking**:
- OPC Foundation Mantis: https://opcfoundation.org/mantis/

---

**Status**: ✅ VOLLSTÄNDIG ABGESCHLOSSEN (Phase 2 - UA-Nodeset Analysis)
**Token Usage**: ~10K
**Next**: OPC UA Research Playbook (Synthese aus open62541 + UA-Nodeset)
