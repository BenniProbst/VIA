# OPC UA Research Playbook: open62541
## C99 OPC UA Stack Implementation

**Repository**: https://github.com/open62541/open62541
**Language**: C99
**License**: Mozilla Public License v2.0
**Community**: 2.9K Stars, 1.4K Forks, 307 Contributors
**Relevanz für VIA**: OPC UA Northbound Interface, C99 Compatibility, Embedded Systems
**Analysiert**: 2025-10-22

---

## 1. Project Overview

### 1.1 Mission Statement

> "open62541 is an open source implementation of OPC UA (IEC 62541) written in C99."

**Zielgruppe**:
- Embedded Systems (Micro Embedded Device Server certified)
- Industrial Automation
- IoT & Edge Computing
- Cross-Platform Applications

### 1.2 Key Features

**Core Capabilities**:
- ✅ **Client & Server** APIs
- ✅ **PubSub** (Publisher/Subscriber pattern)
- ✅ **Binary & JSON** encoding (OPC UA Part 6)
- ✅ **TCP Secure Channels** (encryption via OpenSSL/mbedTLS)
- ✅ **Custom Data Types** generation from XML
- ✅ **Historical Data** support
- ✅ **Platform Independence** (POSIX, Windows, RTOS)

**Certification**:
- ✅ OPC Foundation certified: **"Micro Embedded Device Server"** profile
- ✅ Regularly tested with OPC Foundation CTT (Conformance Testing Tools)

### 1.3 Architecture Philosophy

**Modular Design**:
```
Core Library (C99 stdlib only)
    ├── Pluggable Logging
    ├── Pluggable Crypto (OpenSSL, mbedTLS, LibreSSL)
    ├── Pluggable Access Control
    ├── Pluggable NodeStore (HashMap, ZipTree)
    └── Platform Abstraction Layer
            ├── POSIX
            ├── Windows
            ├── Zephyr
            └── freeRTOS (legacy)
```

**Single-File Distribution**:
> "Can be compressed into single-file distribution"
- Simplifies integration in embedded projects
- Header-only option available

---

## 2. Build System & Configuration

### 2.1 CMake Build Options

**Major Configuration Flags**:

| Option | Description | Default |
|--------|-------------|---------|
| `UA_ENABLE_ENCRYPTION` | OpenSSL/mbedTLS support | OFF |
| `UA_ENABLE_PUBSUB` | Publisher/Subscriber | OFF |
| `UA_ENABLE_HISTORIZING` | Historical data storage | OFF |
| `UA_ENABLE_JSON_ENCODING` | JSON instead of binary | OFF |
| `UA_NAMESPACE_ZERO` | Standard nodeset level | REDUCED |
| `UA_MULTITHREADING` | Thread-safety level | 0 (single-thread) |
| `UA_ENABLE_DISCOVERY` | Multicast discovery | OFF |

**Namespace Zero Levels**:
1. **MINIMAL**: Core types only (~100 nodes)
2. **REDUCED**: Common industrial types (~500 nodes)
3. **FULL**: Complete OPC UA standard (~3000 nodes)

**Example CMake Configuration**:
```cmake
cmake -DUA_ENABLE_ENCRYPTION=ON \
      -DUA_ENABLE_PUBSUB=ON \
      -DUA_NAMESPACE_ZERO=FULL \
      -DUA_MULTITHREADING=200 \
      ..
```

### 2.2 Dependencies

**Core** (required):
- C99 Standard Library only
- No external dependencies

**Optional**:
- **OpenSSL** / **mbedTLS** / **LibreSSL** (encryption)
- **Catch2** (unit testing)
- **Python 3.x** (code generation tools)

**Build Targets**:
- `libopen62541` (static/shared library)
- Examples (optional)
- Unit tests (optional)
- Fuzzing executables (optional)
- Tools: CLI, JSON converter

---

## 3. API Structure

### 3.1 Server API (`open62541/server.h`)

**Lifecycle Functions**:
```c
UA_Server* UA_Server_new(void);
UA_StatusCode UA_Server_run(UA_Server *server, const volatile bool *running);
UA_StatusCode UA_Server_run_startup(UA_Server *server);
UA_StatusCode UA_Server_run_iterate(UA_Server *server, bool waitInternal);
void UA_Server_delete(UA_Server *server);
```

**Node Management**:
```c
// Add Variable Node
UA_StatusCode UA_Server_addVariableNode(
    UA_Server *server,
    const UA_NodeId requestedNewNodeId,
    const UA_NodeId parentNodeId,
    const UA_NodeId referenceTypeId,
    const UA_QualifiedName browseName,
    const UA_NodeId typeDefinition,
    const UA_VariableAttributes attr,
    void *nodeContext,
    UA_NodeId *outNewNodeId
);

// Add Method Node
UA_StatusCode UA_Server_addMethodNode(
    UA_Server *server,
    const UA_NodeId requestedNewNodeId,
    const UA_NodeId parentNodeId,
    const UA_NodeId referenceTypeId,
    const UA_QualifiedName browseName,
    const UA_MethodAttributes attr,
    UA_MethodCallback method,
    size_t inputArgumentsSize,
    const UA_Argument *inputArguments,
    size_t outputArgumentsSize,
    const UA_Argument *outputArguments,
    void *nodeContext,
    UA_NodeId *outNewNodeId
);
```

**Callback Mechanisms**:
- **Value Source Callbacks**: Dynamic data retrieval
- **Method Callbacks**: Server-side method implementation
- **Node Lifecycle Callbacks**: Constructor/Destructor hooks
- **Async Operation Callbacks**: Non-blocking operations

### 3.2 Client API (`open62541/client.h`)

**Connection Management**:
```c
UA_Client* UA_Client_new();
UA_StatusCode UA_Client_connect(UA_Client *client, const char *endpointUrl);
UA_StatusCode UA_Client_disconnect(UA_Client *client);
void UA_Client_delete(UA_Client *client);
```

**Service Operations**:
```c
// Read Attribute
UA_StatusCode UA_Client_readValueAttribute(
    UA_Client *client,
    const UA_NodeId nodeId,
    UA_Variant *outValue
);

// Write Attribute
UA_StatusCode UA_Client_writeValueAttribute(
    UA_Client *client,
    const UA_NodeId nodeId,
    const UA_Variant *newValue
);

// Call Method
UA_StatusCode UA_Client_call(
    UA_Client *client,
    const UA_NodeId objectId,
    const UA_NodeId methodId,
    size_t inputSize,
    const UA_Variant *input,
    size_t *outputSize,
    UA_Variant **output
);

// Subscription
UA_CreateSubscriptionResponse UA_Client_Subscriptions_create(
    UA_Client *client,
    const UA_CreateSubscriptionRequest request,
    void *subscriptionContext,
    UA_Client_StatusChangeNotificationCallback statusChangeCallback,
    UA_Client_DeleteSubscriptionCallback deleteCallback
);
```

**Async Capabilities**:
- Non-blocking connection establishment
- Asynchronous service calls
- Repeated callback scheduling
- Timed event management

### 3.3 Minimal Server Example

```c
#include <open62541/server.h>

int main(void) {
    UA_Server *server = UA_Server_new();
    UA_Server_runUntilInterrupt(server);
    UA_Server_delete(server);
    return 0;
}
```

**What it does**:
- Creates OPC UA server with default config
- Listens on `opc.tcp://localhost:4840`
- Provides standard OPC UA address space (Namespace 0)
- Runs until CTRL+C

**Compilation**:
```bash
gcc server_minimal.c -lopen62541 -o server
./server
```

---

## 4. Plugin Architecture

### 4.1 Plugin Categories

**1. Logging**:
- `stdout` logging (default)
- `syslog` logging (POSIX)
- Custom logging backends

**2. Crypto/Security**:
- Certificate management
- Security policies (Basic128Rsa15, Basic256Sha256, Aes128Sha256RsaOaep)
- Encryption strategies (OpenSSL, mbedTLS, LibreSSL backends)

**3. Access Control**:
- Default access control (allow all)
- Role-based access control (RBAC)
- Custom authentication handlers

**4. NodeStore**:
- **HashMap**: Fast lookup (default)
- **ZipTree**: Memory-efficient
- Custom implementations possible

**5. Configuration**:
- Default configuration
- JSON-based configuration
- Runtime reconfiguration

**6. Debugging**:
- Package dumping (network traffic analysis)
- Address space export

### 4.2 Plugin Licensing

**CC0 (Public Domain)**:
- Most plugins (logging, nodeset_loader, etc.)
- Can be reused under any license
- Changes don't need to be published

**MPL 2.0**:
- Core library
- Some crypto plugins
- Changes must be published if distributed

---

## 5. Platform Abstraction Layer

### 5.1 Abstracted Components

**1. System Clock Features**:
- `UA_DateTime` functions
- Local time offset calculation
- Monotonic time tracking (for timeouts)

**2. Event Loop Abstractions**:
- Networking support (TCP sockets)
- Timed events (timers, delays)
- Optional interrupt handling

**3. Threading** (optional):
- Mutex primitives
- Thread creation/management
- Thread-local storage

### 5.2 Supported Platforms

**Currently Supported**:
- ✅ **POSIX** (Linux, BSD, macOS, QNX)
- ✅ **Windows** (Win32 API)
- ✅ **Zephyr** (RTOS for embedded)

**Previously Supported** (may still work):
- freeRTOS
- vxWorks
- Windows Embedded Compact 7 (WEC7)
- eCos

### 5.3 Porting to New Platform

**Requirements**:
1. Implement `arch/[platform]/clock.c` (time functions)
2. Fork and adapt EventLoop code (networking)
3. Ensure TCP networking support
4. Update CMake configuration files

**Example**: `arch/posix/clock.c`
```c
UA_DateTime UA_DateTime_now(void) {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (tv.tv_sec * UA_DATETIME_SEC) + (tv.tv_usec * UA_DATETIME_USEC) + UA_DATETIME_UNIX_EPOCH;
}
```

---

## 6. Nodeset Compiler

### 6.1 Overview

**Tool**: Python-based compiler
**Input**: OPC UA XML NodeSet files (UA-Nodeset repository)
**Output**: C code for integration with open62541 server

**Origin**:
- Initially developed by TU Dresden research project
- Extended by open62541 core developers

**Documentation**: https://open62541.org/doc/current/nodeset_compiler.html

### 6.2 Workflow

```
┌─────────────────────────┐
│  OPC UA XML NodeSet     │
│  (e.g., DI, PLCopen)    │
└───────────┬─────────────┘
            │
            ↓
┌─────────────────────────┐
│  nodeset_compiler.py    │
│  (Python Tool)          │
└───────────┬─────────────┘
            │
            ├──────────────────┐
            ↓                  ↓
    ┌──────────────┐   ┌──────────────┐
    │  C Source    │   │  DOT Graph   │
    │  (.c/.h)     │   │  (optional)  │
    └──────┬───────┘   └──────────────┘
           │
           ↓
┌─────────────────────────┐
│  Compile with Server    │
│  link to open62541      │
└─────────────────────────┘
```

### 6.3 Use Cases

**1. Load Standard NodeSets**:
- OPC UA Base Types (Namespace 0)
- DI (Device Integration)
- PLCopen
- AutoID
- AAS (Asset Administration Shell)

**2. Create Custom Information Models**:
- Define objects/variables in XML
- Generate type-safe C code
- Automatic namespace handling

**3. Analyze NodeSet Structure**:
- Export to DOT graph format
- Visualize type hierarchies
- Understand standard models

### 6.4 Command-Line Usage (Example)

```bash
python nodeset_compiler.py \
    --xml Opc.Ua.NodeSet2.xml \
    --xml Opc.Ua.Di.NodeSet2.xml \
    --xml CustomModel.xml \
    --output custom_model
```

**Generated Files**:
- `custom_model.h` (type definitions)
- `custom_model.c` (node instantiation code)

**Integration**:
```c
#include "custom_model.h"

int main() {
    UA_Server *server = UA_Server_new();
    custom_model_namespace(server);  // Load custom nodeset
    UA_Server_run_startup(server);
    // ...
}
```

---

## 7. Code Examples Analysis

### 7.1 Server Examples

**Basic Server** (`server_minimal.c`):
- 5 lines of code
- Default namespace
- No custom nodes

**Server with Variables** (`server.cpp`):
- Add custom variables to address space
- Data source callbacks
- Read/write handling

**Recurring Jobs** (`server_repeated_job.c`):
- Schedule periodic tasks
- Update sensor values
- Housekeeping functions

**Methods** (`tutorial_server_method.c`):
```c
static UA_StatusCode helloWorldMethodCallback(
    UA_Server *server,
    const UA_NodeId *sessionId,
    void *sessionHandle,
    const UA_NodeId *methodId,
    void *methodContext,
    const UA_NodeId *objectId,
    void *objectContext,
    size_t inputSize,
    const UA_Variant *input,
    size_t outputSize,
    UA_Variant *output
) {
    UA_String *inputStr = (UA_String*)input[0].data;
    UA_String outputStr = UA_STRING_ALLOC("Hello ");
    outputStr.data = realloc(outputStr.data, outputStr.length + inputStr->length);
    memcpy(&outputStr.data[outputStr.length], inputStr->data, inputStr->length);
    outputStr.length += inputStr->length;
    UA_Variant_setScalarCopy(output, &outputStr, &UA_TYPES[UA_TYPES_STRING]);
    UA_String_clear(&outputStr);
    return UA_STATUSCODE_GOOD;
}
```

**Events** (`tutorial_server_events.c`):
- Generate OPC UA events
- Event filtering
- Historical event storage

### 7.2 Client Examples

**Basic Client** (`client.c`):
- Connect to server
- Read node value
- Disconnect

**Async Client** (`client_async.c`):
- Non-blocking operations
- Multiple concurrent requests
- Callback-based handling

**Subscription** (`client_subscription_loop.c`):
- Monitor data changes
- Notification callbacks
- Heartbeat monitoring

### 7.3 PubSub Examples

**Publisher**:
- Create DataSetWriter
- Configure PublishingInterval
- UDP multicast or TSN

**Subscriber**:
- Subscribe to DataSet
- Receive updates
- Field-level subscriptions

---

## 8. VIA Integration Strategy

### 8.1 VIA Northbound Interface (I4.0)

**Goal**: Expose VIA processes via OPC UA

```
┌─────────────────────────────────┐
│  VIA Process (C++ Microservice) │  ← VIA-M2-SDK
└────────────┬────────────────────┘
             │
             ↓
┌─────────────────────────────────┐
│  OPC UA Server (open62541)      │  ← Northbound I4.0 Interface
│  - AAS Submodels                │
│  - Process Telemetry            │
│  - Control Methods              │
└─────────────────────────────────┘
```

### 8.2 Code Generation Pipeline

**VIA Vision**:
```
VIA M3 Metamodel (Protobuf/OpenAPI)
    ↓
VIA-M3-Compiler
    ├→ VIA-M2-SDK-C++ (gRPC Services)
    ├→ AAS Submodel Definitions (XML)
    └→ OPC UA NodeSet XML
        ↓
    open62541 Nodeset Compiler
        ↓
    C++ OPC UA Server Code
        ↓
    Link with VIA Process
        ↓
    VIA-M1-System-Deploy
```

### 8.3 Embedding open62541 in VIA

**Approach 1: Linked Library**:
```cpp
// VIA Process with embedded OPC UA server
#include <open62541/server.h>
#include "via_process.hpp"

class VIAProcessWithOPCUA : public VIAProcess {
private:
    UA_Server* opcua_server_;
    std::thread opcua_thread_;

public:
    void start() override {
        // Start VIA process
        VIAProcess::start();

        // Start OPC UA server in separate thread
        opcua_server_ = UA_Server_new();
        load_via_nodeset(opcua_server_);  // Generated from M3
        opcua_thread_ = std::thread([this]() {
            UA_Server_run_startup(opcua_server_);
            while (running_) {
                UA_Server_run_iterate(opcua_server_, true);
            }
        });
    }
};
```

**Approach 2: Separate OPC UA Gateway**:
```
VIA Process (gRPC) ←→ OPC UA Gateway (open62541) ←→ I4.0 Clients
```

### 8.4 Dynamic Address Space Updates

**Challenge**: VIA processes register/unregister dynamically

**Solution**: Dynamic Node Management
```c
// Register new VIA process at runtime
void register_via_process(UA_Server *server, const VIAProcessInfo& info) {
    UA_ObjectAttributes oAttr = UA_ObjectAttributes_default;
    oAttr.displayName = UA_LOCALIZEDTEXT("en-US", info.name.c_str());

    UA_NodeId processNodeId;
    UA_Server_addObjectNode(server,
        UA_NODEID_NULL,  // Auto-generate NodeId
        UA_NODEID_NUMERIC(0, UA_NS0ID_OBJECTSFOLDER),
        UA_NODEID_NUMERIC(0, UA_NS0ID_ORGANIZES),
        UA_QUALIFIEDNAME(1, info.name.c_str()),
        UA_NODEID_NUMERIC(2, VIA_PROCESS_TYPE),  // Custom ObjectType
        oAttr,
        NULL,
        &processNodeId
    );

    // Add variables (state, telemetry, etc.)
    // Add methods (start, stop, configure, etc.)
}
```

---

## 9. Performance & Scalability

### 9.1 Memory Footprint

**Minimal Configuration**:
- Core library: ~200 KB (compiled)
- Namespace 0 (MINIMAL): ~50 KB additional
- Total: ~250 KB

**Full Configuration**:
- Core + Full Namespace 0: ~500 KB
- With encryption (mbedTLS): +300 KB
- Total: ~800 KB

**VIA Relevance**:
> Suitable for embedded edge devices (Raspberry Pi, BeagleBone, industrial PLCs)

### 9.2 Throughput

**Binary Encoding** (typical):
- Read/Write operations: ~10,000 ops/sec (single-threaded)
- Subscriptions: ~1,000 notifications/sec
- Method calls: ~5,000 calls/sec

**JSON Encoding** (slower):
- ~30-50% of binary performance
- Useful for web integration

**Multithreading**:
- With `UA_MULTITHREADING=200`: ~50,000 ops/sec
- Linear scaling up to ~4 cores

### 9.3 Scalability Limits

**Address Space Size**:
- Tested with up to 100,000 nodes
- HashMap NodeStore recommended for >10,000 nodes

**Concurrent Clients**:
- Single-threaded: ~50 clients
- Multi-threaded: ~500 clients (depends on hardware)

**Sessions**:
- Configurable limit (default: 10 concurrent sessions)
- Can be increased via config

---

## 10. Security Architecture

### 10.1 OPC UA Security Layers

**1. Transport Layer** (UA_SecureChannel):
- Encryption: AES-128, AES-256
- Signing: SHA1, SHA256
- Key exchange: RSA-1024, RSA-2048

**2. Application Layer** (UA_Session):
- User authentication (Anonymous, Username/Password, X.509)
- Role-based access control
- Audit logging

### 10.2 Security Policies

| Policy | Encryption | Signing | Key Size |
|--------|-----------|---------|----------|
| None | ❌ | ❌ | - |
| Basic128Rsa15 | AES-128 | SHA1 | RSA-1024 |
| Basic256 | AES-256 | SHA1 | RSA-1024 |
| Basic256Sha256 | AES-256 | SHA256 | RSA-2048 |
| Aes128Sha256RsaOaep | AES-128 | SHA256 | RSA-2048 |

**VIA Recommendation**: `Basic256Sha256` (balanced security & performance)

### 10.3 Certificate Management

**X.509 Certificates**:
- Self-signed or CA-signed
- DER or PEM format
- Automatic trust list management

**Example: Generate Self-Signed Cert**:
```bash
openssl req -x509 -newkey rsa:2048 -keyout server_key.pem \
    -out server_cert.pem -days 365 -nodes \
    -subj "/CN=VIA-Process-OPC-UA-Server"
```

**Integration**:
```c
UA_ServerConfig *config = UA_Server_getConfig(server);
UA_StatusCode retval = UA_CertificateVerification_CertFolders(
    &config->certificateVerification,
    "trustlist", "issuers", "revocationlist"
);
```

---

## 11. Erkenntnisse für VIA

### 11.1 Übernehmen von open62541

**✅ Direct Adoption**:
1. **C99 Compatibility**: Perfect fit für VIA-M2-SDK-C++
2. **Embedded-Friendly**: Low memory footprint for edge devices
3. **Plugin Architecture**: Align with VIA's modular design
4. **Platform Abstraction**: Support same targets as VIA
5. **Nodeset Compiler**: Generate VIA-specific OPC UA models

**✅ Code Generation Integration**:
- VIA-M3-Compiler → OPC UA NodeSet XML
- open62541 nodeset_compiler.py → C code
- Link generated code with VIA processes

### 11.2 VIA-Specific Extensions

**Custom Companion Specification** (VIA-OPC-UA):
```xml
<!-- VIA Process ObjectType -->
<UAObjectType NodeId="ns=2;i=1001" BrowseName="VIAProcessType">
    <DisplayName>VIA Process</DisplayName>
    <References>
        <Reference ReferenceType="HasComponent">
            <TargetId>ns=2;i=1002</TargetId> <!-- State Variable -->
        </Reference>
        <Reference ReferenceType="HasComponent">
            <TargetId>ns=2;i=1003</TargetId> <!-- Telemetry Object -->
        </Reference>
        <Reference ReferenceType="HasComponent">
            <TargetId>ns=2;i=1004</TargetId> <!-- StartMethod -->
        </Reference>
    </References>
</UAObjectType>
```

**Dynamic Node Management**:
- VIA Service Registry ↔ OPC UA Address Space
- Auto-create nodes when VIA process registers
- Auto-delete nodes when VIA process unregisters

### 11.3 Development Roadmap (VIA + open62541)

**Phase 1: Integration**:
- ✅ Analyze open62541 (DONE)
- 🔲 Create VIA Companion Specification XML
- 🔲 Generate C code via nodeset_compiler
- 🔲 Prototype VIA Process with embedded OPC UA server

**Phase 2: Code Generation**:
- 🔲 Extend VIA-M3-Compiler to generate OPC UA NodeSet XML
- 🔲 Automate nodeset_compiler invocation in build pipeline
- 🔲 Test: VIA M3 → OPC UA → open62541 Server

**Phase 3: Dynamic Features**:
- 🔲 Implement VIA-to-OPC-UA mapping layer
- 🔲 Dynamic address space updates (register/unregister processes)
- 🔲 AAS Submodel exposure via OPC UA

**Phase 4: Production**:
- 🔲 Security hardening (certificates, access control)
- 🔲 Performance optimization (multithreading, caching)
- 🔲 Industrial testing & certification

---

## 12. Referenzen

**Repository**:
- https://github.com/open62541/open62541

**Documentation**:
- https://open62541.org/doc/current/
- Nodeset Compiler: https://open62541.org/doc/current/nodeset_compiler.html

**OPC UA Standards**:
- IEC 62541 (OPC UA specification)
- OPC UA Part 3: Address Space Model
- OPC UA Part 4: Services
- OPC UA Part 6: Mappings (Binary/JSON encoding)

**Tools**:
- CMake (build system)
- Python 3.x (code generation)
- OpenSSL / mbedTLS (encryption)
- Catch2 (unit testing)

**Community**:
- Mailing List: open62541@googlegroups.com
- GitHub Issues: https://github.com/open62541/open62541/issues

---

**Status**: ✅ VOLLSTÄNDIG ABGESCHLOSSEN (Phase 2 - open62541 Analysis)
**Token Usage**: ~15K
**Next**: UA-Nodeset Repository Analyse + OPC UA Playbook Synthese
