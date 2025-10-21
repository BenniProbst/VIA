# VIA — Virtual Industry Automation

**Asset Administration Shell (AAS) Industrial Measurement Data Management**

VIA is a command-line tool for processing and managing industrial automation measurement data using the Asset Administration Shell (AAS) standard from Industrie 4.0.

---

## Quick Start

```bash
VIA input.xlsx output.xlsx
```

---

## Features

✅ **AAS Data Management**: Full support for Asset Administration Shell standards
✅ **Industrial Measurement Processing**: Automated handling of sensor and machine data
✅ **Data Validation**: Real-time validation with Excel write-back
✅ **Type-Safe**: Automatic validation with error detection
✅ **Third-Party Integration**: Modular architecture for third-party components
✅ **Complete History**: Track all measurement data and events
✅ **C++23**: Modern C++ implementation with high performance

---

## Documentation

### 📖 For Users

**German (Deutsch):**
- [Benutzerhandbuch](docs/german/BENUTZERHANDBUCH.md) - Vollständiges Handbuch mit Schritt-für-Schritt-Anleitung
- [README](docs/german/README.md) - Übersicht und Schnellstart
- [CHANGELOG](docs/german/CHANGELOG.md) - Versionshistorie

**English:**
- [User Manual](docs/english/USER_MANUAL.md) - Complete manual with step-by-step instructions
- [README](docs/english/README.md) - Overview and quick start
- [CHANGELOG](docs/english/CHANGELOG.md) - Version history

### 🛠️ For Developers

**English:**
- [Contributing Guide](docs/english/CONTRIBUTING.md)
- [Architecture Documentation](docs/english/ARCHITECTURE.md)
- [Implementation Verification](docs/IMPLEMENTATION_VERIFICATION.md)
- [Code of Conduct](docs/english/CODE_OF_CONDUCT.md)
- [Security Policy](docs/english/SECURITY.md)

**German:**
- [Mitwirken](docs/german/CONTRIBUTING.md)
- [Architektur-Dokumentation](docs/german/ARCHITECTURE.md)
- [Implementierungsverifizierung](docs/IMPLEMENTATION_VERIFICATION.md)
- [Verhaltenskodex](docs/german/CODE_OF_CONDUCT.md)
- [Sicherheitsrichtlinie](docs/german/SECURITY.md)

---

## Installation

### Binaries (Recommended)

Download the latest release from [GitHub Releases](https://github.com/BEP-Venture/VIA/releases).

### Build from Source

**Prerequisites:**
- CMake ≥ 3.20
- C++23 compiler (GCC 12+, Clang 15+, MSVC 2022+)

**Windows:**
```cmd
configure.bat --build-type=Release
build.bat
build.bat install
```

**Linux/macOS:**
```bash
./configure --build-type=Release
make -j$(nproc)
sudo make install
```

---

## System Requirements

- **OS**: Windows 10/11 (64-bit), Linux, macOS
- **RAM**: 512 MB minimum
- **Disk**: 50 MB free space
- **Excel Software**: Microsoft Excel, LibreOffice Calc, or compatible

---

## Example Usage

1. **Export measurement data** from your industrial systems
2. **Prepare Excel file** with required sheets (see [User Manual](docs/english/USER_MANUAL.md))
3. **Run program:**
   ```bash
   VIA VIA.xlsx VIA_output.xlsx
   ```
4. **Review output** in the generated log sheets

---

## Project Structure

```
VIA/
├── docs/
│   ├── english/          # English documentation
│   │   ├── README.md
│   │   ├── USER_MANUAL.md
│   │   ├── CHANGELOG.md
│   │   ├── CONTRIBUTING.md
│   │   ├── CODE_OF_CONDUCT.md
│   │   ├── SECURITY.md
│   │   └── ARCHITECTURE.md
│   └── german/           # German documentation
│       ├── README.md
│       ├── BENUTZERHANDBUCH.md
│       ├── CHANGELOG.md
│       ├── CONTRIBUTING.md
│       ├── CODE_OF_CONDUCT.md
│       ├── SECURITY.md
│       └── ARCHITECTURE.md
├── playbooks/            # Implementation playbooks
├── include/              # C++ headers
├── src/                  # C++ source files
├── tests/                # Unit tests
├── examples/             # Example Excel files
├── third_party/          # Third-party dependencies
├── CMakeLists.txt
└── README.md             # This file
```

---

## License

This project is subject to a proprietary End User License Agreement (EULA).

**Important:** This software is provided for internal use only. Redistribution, reverse engineering, or commercial use without explicit permission is prohibited.

For licensing inquiries: bep.venture.ug@gmail.com

---

## Support

- **Email**: bep.venture.ug@gmail.com
- **Address**: BEP Venture UG, Chemnitzer Straße 69, 01187 Dresden, Germany
- **Issues**: [GitHub Issues](https://github.com/BEP-Venture/VIA/issues)
- **Documentation**: [docs/](docs/)

---

## Version

**Current Version**: 0.1.0
**Release Date**: 21.10.2025

See [CHANGELOG](docs/english/CHANGELOG.md) for full version history.

---

**Copyright © 2025 BEP Venture UG (haftungsbeschränkt)**
