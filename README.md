# Linux-Mastery: Complete Real-World Curriculum & Defensive Engineering Framework

> **A Production-Grade, Step-by-Step Training Architecture for Operating System Internals, Network Packet Forensics, Terminal Automation, Incident Response, and Authorized Bug Hunting.**
> *Compatible natively with GitHub Pages and Netlify Static Deployments. Completely Air-Gapped and Sandboxed for Local Container Execution.*

---

## Table of Contents

1. [Architectural Philosophy](https://www.google.com/search?q=%231-architectural-philosophy)
2. [Ethical Mandates & Legal Safe Harbor](https://www.google.com/search?q=%232-ethical-mandates--legal-safe-harbor)
3. [Zero-Dependency Web Delivery Model](https://www.google.com/search?q=%233-zero-dependency-web-delivery-model)
4. [Hardware & Software Prerequisites](https://www.google.com/search?q=%234-hardware--software-prerequisites)
5. [The Multi-Tier Isolated Lab Architecture](https://www.google.com/search?q=%235-the-multi-tier-isolated-lab-architecture)
6. [Complete Repository Layout](https://www.google.com/search?q=%236-complete-repository-layout)
7. [Step-by-Step Setup & Verification Guide](https://www.google.com/search?q=%237-step-by-step-setup--verification-guide)
8. [The 23-Level Structured Curriculum](https://www.google.com/search?q=%238-the-23-level-structured-curriculum)
* [Level -1: Junior Explorer (Visual-First System Exploration)](https://www.google.com/search?q=%23level--1-junior-explorer-visual-first-system-exploration)
* [Level 0: The Linux Mental Model & OS Architecture](https://www.google.com/search?q=%23level-0-the-linux-mental-model--os-architecture)
* [Level 1: Terminal Mastery, Data Streams & Pipeline Chaining](https://www.google.com/search?q=%23level-1-terminal-mastery-data-streams--pipeline-chaining)
* [Level 2: Filesystem Deep Dive, Inodes & Metadata Forensics](https://www.google.com/search?q=%23level-2-filesystem-deep-dive-inodes--metadata-forensics)
* [Level 3: Access Control, Permissions, SUID & POSIX Capabilities](https://www.google.com/search?q=%23level-3-access-control-permissions-suid--posix-capabilities)
* [Level 4: Process Lifecycle, Signals & Runtime Diagnostics](https://www.google.com/search?q=%23level-4-process-lifecycle-signals--runtime-diagnostics)
* [Level 5: System Administration, Services & systemd Internals](https://www.google.com/search?q=%23level-5-system-administration-services--systemd-internals)
* [Level 6: Core Networking, Packet Analysis & Socket Forensics](https://www.google.com/search?q=%23level-6-core-networking-packet-analysis--socket-forensics)
* [Level 7: Web Protocols, Raw HTTP & API Wrangling via CLI](https://www.google.com/search?q=%23level-7-web-protocols-raw-http--api-wrangling-via-cli)
* [Level 8: Defensive Shell Scripting & Infrastructure Automation](https://www.google.com/search?q=%23level-8-defensive-shell-scripting--infrastructure-automation)
* [Level 9: Systems & Security Automation with Python](https://www.google.com/search?q=%23level-9-systems--security-automation-with-python)
* [Level 10: Git Internals, Safe Workflows & Secret Sanitation](https://www.google.com/search?q=%23level-10-git-internals-safe-workflows--secret-sanitation)
* [Level 11: Secure Shell (SSH) Topologies, Hardening & Tunnels](https://www.google.com/search?q=%23level-11-secure-shell-ssh-topologies-hardening--tunnels)
* [Level 12: Linux Security Architecture & Mandatory Access Control](https://www.google.com/search?q=%23level-12-linux-security-architecture--mandatory-access-control)
* [Level 13: Containers, Namespaces & Isolation Auditing](https://www.google.com/search?q=%23level-13-containers-namespaces--isolation-auditing)
* [Level 14: Digital Forensics, Artifact Triage & Incident Response](https://www.google.com/search?q=%23level-14-digital-forensics-artifact-triage--incident-response)
* [Level 15: Bug Hunter Linux Flow & Structured Scope Recon](https://www.google.com/search?q=%23level-15-bug-hunter-linux-flow--structured-scope-recon)
* [Level 16: Resilient Recon Automation & Data Pipelines](https://www.google.com/search?q=%23level-16-resilient-recon-automation--data-pipelines)
* [Level 17: Kernel-to-Userspace Debugging Mastery](https://www.google.com/search?q=%23level-17-kernel-to-userspace-debugging-mastery)
* [Level 18: Binary Analysis, Dynamic Linking & ELF Internals](https://www.google.com/search?q=%23level-18-binary-analysis-dynamic-linking--elf-internals)
* [Level 19: Secure Coding, Script Auditing & Privilege Safety](https://www.google.com/search?q=%23level-19-secure-coding-script-auditing--privilege-safety)
* [Level 20: Full-Spectrum Multi-Host Assessment Capstone](https://www.google.com/search?q=%23level-20-full-spectrum-multi-host-assessment-capstone)
* [Level 21: The "Host-Ready" Operational Certification Standard](https://www.google.com/search?q=%23level-21-the-host-ready-operational-certification-standard)


9. [Automated Infrastructure Code (Docker Compose & Shell)](https://www.google.com/search?q=%239-automated-infrastructure-code-docker-compose--shell)
10. [Dual-Platform Deployment Engineering (GitHub Pages & Netlify)](https://www.google.com/search?q=%2310-dual-platform-deployment-engineering-github-pages--netlify)
11. [Verification Scripts & Automated Test Suite](https://www.google.com/search?q=%2311-verification-scripts--automated-test-suite)
12. [Contribution Governance & Engineering Rigor](https://www.google.com/search?q=%2312-contribution-governance--engineering-rigor)

---

## 1. Architectural Philosophy

The **Linux-Mastery** platform is founded on a singular engineering reality: **Abstract theory and blind command memorization fail the moment an engineer encounters an unfamiliar production host or an air-gapped target.**

A system administrator, site reliability engineer, defensive analyst, or authorized security auditor does not succeed by reciting syntax. They succeed by maintaining an accurate mental model of operating system primitives:

1. **Build Before You Break:** You cannot effectively analyze, secure, or reverse-engineer a service until you have compiled it, configured its network sockets, inspected its system calls, and observed its normal operational baseline.
2. **Deterministic Dataflow:** Every Linux interaction is a data stream. Files are byte arrays; devices are exposed as file nodes; process runtime state is represented as a synthetic filesystem (`/proc`); processes communicate across file descriptors, pipes, and sockets.
3. **Evidence-Driven Problem Solving:** When a system fails or exhibits anomalous behavior, guessing is strictly forbidden. The engineer forms a hypothesis, isolates the layer (kernel, syscall, userspace library, process environment, or network interface), gathers raw artifacts using diagnostic utilities (`strace`, `lsof`, `tcpdump`, `ss`), and verifies the root cause with empirical trace output.

---

## 2. Ethical Mandates & Legal Safe Harbor

This platform teaches the fundamental mechanics of operating systems and network interactions. With deep operational capability comes the non-negotiable imperative for strict ethical boundaries and adherence to legal frameworks.

```
+-----------------------------------------------------------------------------------+
|                            THE NON-NEGOTIABLE RED LINE                            |
|                                                                                   |
|  Interacting with any digital system, network interface, port, API endpoint,      |
|  or server without explicit, documented, and signed authorization from the legal   |
|  owner constitutes an immediate violation of domestic and international law       |
|  (e.g., US Computer Fraud and Abuse Act - CFAA 18 U.S.C. § 1030, Indian IT Act    |
|  Section 43/66, UK Computer Misuse Act 1990).                                     |
|                                                                                   |
|  THIS REPOSITORY IS STRICTLY DESIGNED TO RUN IN AIR-GAPPED LOCAL SANDBOXES.       |
|  TARGETING EXTERNAL INFRASTRUCTURE, PUBLIC DOMAINS, OR THIRD-PARTY ASSETS IS      |
|  CATEGORICALLY PROHIBITED.                                                       |
+-----------------------------------------------------------------------------------+

```

### Rules of Engagement for Learners

1. **Isolated Subnets Only:** All auditing, probing, packet-sniffing, and service diagnosis must remain bound to the private internal Docker bridge (`172.28.0.0/16`) or local hypervisor host-only networks.
2. **Defensive Mindset:** Security is the process of identifying architectural flaws, eliminating unnecessary privilege surfaces, and enforcing deterministic boundaries. Auditing without fixing is incomplete engineering.
3. **Responsible Reporting:** Every security finding identified inside our target containers must be documented using industry-standard vulnerability reporting models: Root Cause, Scope, Minimal Proof-of-Concept, Remediation Patch, and Post-Fix Validation.

---

## 3. Zero-Dependency Web Delivery Model

To ensure seamless distribution across modern hosting providers without build-step overhead, the documentation, visual interactive dashboards, and progress tracking mechanisms are built entirely on a **Zero-Dependency Static Architecture**:

* **No Compilers / Transpilers:** No Node.js runtime, no npm packages, no Webpack/Vite bundlers required to serve the frontend.
* **Pure Web Standards:** Pure semantic HTML5, modern CSS3 variables for clean high-contrast terminal styling, and vanilla ECMAScript for state tracking via the browser's `localStorage` API.
* **Dual-Platform Native Deployment:** Configured to deploy directly from root on both **Netlify** (via `netlify.toml`) and **GitHub Pages** (via `.github/workflows/deploy.yml` and `.nojekyll`).

---

## 4. Hardware & Software Prerequisites

The labs in this curriculum run real Linux kernels, process namespaces, and networked containers. They are not browser-simulated mock terminals.

### Minimum System Specifications

* **Operating System:** Any native Linux distribution (Ubuntu 22.04 LTS+, Debian 12+, Arch Linux, Fedora), macOS (Sonoma+ with Docker Desktop or Colima), or Windows 11 (with WSL2 Ubuntu 22.04).
* **CPU Architecture:** x86_64 or ARM64 (Apple Silicon / Raspberry Pi 4/5).
* **Processor:** Dual-core 2.0 GHz or higher.
* **Memory (RAM):** 8 GB minimum; 16 GB strongly recommended for running multi-container networks concurrently.
* **Disk Storage:** 25 GB of unallocated solid-state storage.

### Required Host Packages

Before beginning Level -1, verify the following packages are present on your host operating system:

```bash
# Debian / Ubuntu Systems
sudo apt-get update && sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    git \
    python3 \
    python3-pip \
    docker.io \
    docker-compose-v2 \
    mc \
    htop \
    strace \
    lsof \
    tcpdump \
    tshark \
    dnsutils \
    iproute2 \
    bsdmainutils \
    jq

# Enable and start the Docker service
sudo systemctl enable --now docker

# Add your current user to the docker group to run containers without sudo
sudo usermod -aG docker "$USER"
newgrp docker

```

---

## 5. The Multi-Tier Isolated Lab Architecture

The lab environment mirrors a real production enterprise network with an internal DMZ, an auditing workstation, and an intentionally vulnerable service node.

```
                                 [ HOST SYSTEM ]
                      (Linux Kernel / Hypervisor / WSL2)
                                      │
                                      ▼
             [ Docker Bridge Network: sandbox_net (172.28.0.0/16) ]
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
        ▼                             ▼                             ▼
┌───────────────────┐       ┌───────────────────┐       ┌───────────────────┐
│ mastery_auditor   │       │ mastery_target    │       │ mastery_webapp    │
│ 172.28.0.10       │       │ 172.28.0.20       │       │ 172.28.0.30       │
│                   │       │                   │       │                   │
│ • Debian Slim     │       │ • Ubuntu Server   │       │ • Multi-Tier Web  │
│ • Full Tooling    │       │ • Misconfigured   │       │ • Live REST API   │
│ • strace / lsof   │       │   Services / SUID │       │ • Local Traffic   │
│ • tcpdump / curl  │       │ • Crashing Init   │       │   Generator       │
│ • Python 3 Audit  │       │ • Unsafe Perms    │       │ • Port 3000 Open  │
└───────────────────┘       └───────────────────┘       └───────────────────┘
        ▲                             ▲                             ▲
        └────────────────────── Shared ─────────────────────────────┘
                               Volumes
                                  │
                                  ▼
                     [ ./lab-workspace/shared ]

```

---

## 6. Complete Repository Layout

```text
Linux-Mastery/
├── .github/
│   └── workflows/
│       ├── deploy.yml                 # Automated deployment pipeline for GitHub Pages
│       └── lint-check.yml             # Shellcheck automation for defensive Bash scripts
├── .nojekyll                          # Disables Jekyll processing on GitHub Pages
├── index.html                         # Unified Static Web Dashboard, Manual & Progress UI
├── netlify.toml                       # Netlify security headers and root publish routing
├── LICENSE                            # Open Source License (MIT / Apache 2.0)
├── README.md                          # Comprehensive Technical Documentation
│
├── lab-environment/
│   ├── docker-compose.yml             # Orchestration for the 3-node isolated lab
│   ├── auditor/
│   │   └── Dockerfile                 # Heavyweight diagnostic & auditing workstation image
│   ├── target/
│   │   ├── Dockerfile                 # Intentionally flawed break-fix server environment
│   │   ├── entrypoint.sh              # Fault injection orchestration engine
│   │   └── configs/                   # Misconfigured PAM, sudoers, and systemd units
│   └── webapp/
│       └── Dockerfile                 # Web target container with live HTTP endpoints
│
├── scripts/
│   ├── test-sandbox.sh                # Host compatibility, kernel verification & tool checker
│   ├── sysaudit.sh                    # Production-grade diagnostic collection script
│   └── reset-labs.sh                  # Instant rollback script to flush state & rebuild nodes
│
└── levels/
    ├── level-minus-1/                 # Interactive visual walkthroughs (mc, htop, pipes)
    ├── level-00-mental-model/         # Virtual filesystem forensics & kernel-space deep dives
    ├── level-01-terminal/             # Stream manipulation, redirection & pipeline logic
    ├── level-02-filesystem/           # Inode tracking, file recovery & hard/soft links
    ├── level-03-permissions/          # SUID exploitation, POSIX ACLs & Linux capabilities
    ├── level-04-processes/            # Zombie process mitigation & runtime descriptor traces
    ├── level-05-sysadmin/             # Service unit crash resolution & boot sequence fixes
    ├── level-06-networking/           # TCP packet disassembly, ARP inspection & socket dumps
    ├── level-07-web-protocols/        # Manual HTTP transaction construction & API extraction
    ├── level-08-bash-automation/      # Defensively structured shell pipelines with traps
    ├── level-09-python-automation/    # Socket manipulation & multi-megabyte log aggregators
    ├── level-10-git-workflow/         # Git reflog recovery & automated secret scrubbing
    ├── level-11-ssh-hardening/        # Bastion jump configs, SSH agent tunnels & hardening
    ├── level-12-security-arch/        # cgroups configuration & AppArmor profile authoring
    ├── level-13-containers/           # Namespace creation via unshare & container isolation
    ├── level-14-forensics/            # Volatile memory triage & auth log timeline sequencing
    ├── level-15-bug-hunter-flow/      # Scope validation & systematic target inventory
    ├── level-16-recon-pipelines/      # Crash-proof rate-limited reconnaissance engineering
    ├── level-17-debugging-mastery/    # Memory leak troubleshooting via gdb & strace hooks
    ├── level-18-binary-internals/     # ELF structure parsing & dynamic symbol extraction
    ├── level-19-secure-coding/        # Shell script auditing & command injection remediation
    ├── level-20-enterprise-capstone/  # Multi-node scenario assessment & verification
    └── level-21-host-ready/           # Seven blind, zero-guidance production missions

```

---

## 7. Step-by-Step Setup & Verification Guide

### Step 1: Clone the Engineering Repository

```bash
git clone https://github.com/toxictest/Linux-Mastery.git
cd Linux-Mastery

```

### Step 2: Run the Environmental Host Sanity Check

Execute the automated validator to confirm that your host machine possesses the necessary kernel features, virtualization support, and network tools:

```bash
chmod +x scripts/*.sh
./scripts/test-sandbox.sh

```

### Step 3: Bring Up the Air-Gapped Multi-Node Cluster

Launch the isolated environment using Docker Compose:

```bash
docker compose -f lab-environment/docker-compose.yml up -d --build

```

Verify that all three nodes are healthy and bound to their static IP allocations:

```bash
docker compose -f lab-environment/docker-compose.yml ps

```

### Step 4: Attach to the Auditing Workstation

To interact with the lab like a real terminal engineer, enter the primary auditing node:

```bash
docker exec -it mastery_auditor bash

```

From this shell, verify connectivity across the private bridge:

```bash
# Ping the target server across the private isolated bridge
ping -c 3 172.28.0.20

# Query the local web service running on the application container
curl -I http://172.28.0.30:3000

```

---

Linux-Mastery: The Deep Systems & Security Engineering Blueprint (HTB/THM Advanced Architecture Layer)

    No Simulated Commands. No Fluff. Pure Linux Systems Forensics, Memory Analysis, Dynamic Auditing, and Defensive Hardening.

Table of Contents

    Linux Memory Forensics & Runtime Subsystems (HTB CDSA Core)

    Process Injection & Dynamic Tracing Mechanics

    Network Layer 2/3 Attack Surfaces & Kernel Isolation

    Linux Privilege Boundaries & Capability Escalations (HTB CPTS Deep Dive)

    Log Tampering, Eviction Tracing & Detection Engineering

    Dynamic Linker Hijacking & Shared Object Internals

    Container Escape Mechanics & Kernel Attack Vectors

    Automated Diagnostic Tool: Memory, Network, and Inode Integrity Script

1. Linux Memory Forensics & Runtime Subsystems (HTB CDSA Core)

Industrial certifications jaise HTB Certified Defensive Security Analyst (CDSA) me process memory aur synthetic filesystems ka deep inspection core requirement hoti hai.
The /proc/<PID>/ Anatomy

Linux kernel har live process ke internal state ko memory me structure karke /proc/<PID>/ par expose karta hai:

    /proc/<PID>/maps: Process ka dynamic virtual memory layout. Isme text segment (executable code), heap (dynamically allocated memory via brk/mmap), stack (local variables, frame pointers), aur shared .so libraries ki starting and ending memory addresses hoti hain.

    /proc/<PID>/mem: Raw physical memory mapped into virtual memory space. Agar aapke paas CAP_SYS_PTRACE ya root access hai, to bina debugger ke bhi direct memory read/write kiya ja sakta hai.

    /proc/<PID>/fd/: Har open network connection, disk file, aur unnamed pipe ka active descriptor link.

    /proc/<PID>/environ: Process initialization ke time set kiye gaye environment variables (jisme aksar unencrypted credentials aur API tokens leak hote hain).

                      VIRTUAL ADDRESS SPACE (x86_64)
0x0000000000400000 +-----------------------------------+
                   | .text (Executable Code Instructions) | -> r-xp (Read, Exec)
                   +-----------------------------------+
                   | .rodata (Static Strings/Constants) | -> r--p (Read Only)
                   +-----------------------------------+
                   | .data / .bss (Global Variables)   | -> rw-p (Read, Write)
                   +-----------------------------------+
                   | [heap] (Grows UP via brk/mmap)     | -> rw-p (Read, Write)
                   +-----------------------------------+
                   | ... Shared Libraries (.so) ...    | -> r-xp / rw-p
                   +-----------------------------------+
                   | [stack] (Grows DOWN on function calls) -> rw-p (No Exec via NX bit)
0x7fffffffffffffff +-----------------------------------+

Deep Forensics Lab: Memory String Extraction Without Tools

Kisi chalte hue process ke RAM me se credentials ya API tokens direct extract karne ka workflow:
Bash

# Step 1: Ek background target process initiate karein jisme secret string ho
python3 -c '
import time, os
secret = "PRODUCTION_DB_PASS_X99201_DO_NOT_LEAK"
print(f"[+] Target running with PID: {os.getpid()}")
while True:
    time.sleep(1)
' &
TARGET_PID=$!

# Step 2: Process memory maps ko read karein aur heap/stack address verify karein
grep -E "\[heap\]|\[stack\]" /proc/$TARGET_PID/maps

# Step 3: Direct memory dumping through /proc/<pid>/mem using gdb/dd pipeline
cat /proc/$TARGET_PID/maps | awk '/\[heap\]/{print $1}' | IFS="-" read -r START END
# Convert hexadecimal memory offsets to decimal bytes for dd
START_DEC=$(printf "%d\n" 0x$START)
END_DEC=$(printf "%d\n" 0x$END)
MEM_LENGTH=$((END_DEC - START_DEC))

# Extract heap bytes safely
dd if=/proc/$TARGET_PID/mem bs=1 skip=$START_DEC count=$MEM_LENGTH of=/tmp/extracted_heap.bin 2>/dev/null

# Step 4: String forensics run karein
strings /tmp/extracted_heap.bin | grep "PRODUCTION_DB"

# Cleanup
kill -9 $TARGET_PID
rm -f /tmp/extracted_heap.bin

2. Process Injection & Dynamic Tracing Mechanics

Security assessments me jab koi binary crash hoti hai ya malicious behavior exhibit karti hai, tab native system calls ko inspect karna compulsory hota hai.
The System Call Interception Flow (ptrace)

System calls (read, write, openat, fork, execve) userspace applications ko hardware ke sath safely interact karne dete hain. Debuggers (gdb) aur tracers (strace) ptrace(2) syscall par depend karte hain:

[ Tracing Process: strace ] ──────── ptrace(PTRACE_ATTACH) ────────► [ Target Process ]
           │                                                               │
           │                                                               ▼
           │                                                       Executes Syscall
           │                                                               │
           ◄────────── Kernel suspends target with SIGTRAP ────────────────┤
           │                                                               │
     Reads Registers (RAX/RDI)                                             │
           │                                                               │
           ├────────── ptrace(PTRACE_SYSCALL) to continue ────────────────►│

    RAX: Syscall number hold karta hai (x86_64 architecture me 0 = sys_read, 1 = sys_write, 59 = sys_execve).

    RDI, RSI, RDX, R10, R8, R9: Syscall arguments hold karte hain.

    Syscall complete hone ke baad return value wapas RAX register me aati hai.

Hands-On Lab: Writing a Minimal Syscall Interceptor
Bash

# Monitor all network-related file access in real time without third-party network monitors
strace -f -e trace=network,openat,read,write -p 1 2>&1 | head -n 30

3. Network Layer 2/3 Attack Surfaces & Kernel Isolation

TryHackMe aur HTB ke advanced networking modules me standard port scanning ke bajay ARP spoofing detection aur Raw Socket filtering sikhayi jaati hai.
Address Resolution Protocol (ARP) Cache Poisoning Detection

L2 subnet par switch traffic ko MAC address ke base par forward karta hai. Agar ek machine fake ARP Reply frames bhejti hai, to router ka IP uske MAC address par bind ho jata hai (Man-In-The-Middle):

Normal State:
  Router (192.168.1.1)  ──► MAC: AA:BB:CC:DD:EE:01
  Target (192.168.1.50) ──► MAC: AA:BB:CC:DD:EE:50

Poisoned State (Adversary floods Gratuitous ARP):
  Router (192.168.1.1)  ──► MAC: FF:FF:FF:00:11:22 (Attacker MAC)

Forensic Defense Script: Real-Time Dynamic ARP Monitor
Bash

#!/usr/bin/env bash
# ARP Table Monitoring Daemon - Detects Dynamic MAC Swapping
set -euo pipefail

echo "[*] Monitoring ARP Table changes for gateway hijacking..."
GATEWAY_IP=$(ip r | awk '/default/ {print $3}')
INITIAL_MAC=$(ip neigh show "$GATEWAY_IP" | awk '{print $5}')

echo "[+] Monitored Gateway: $GATEWAY_IP | Baseline MAC: $INITIAL_MAC"

while true; do
    CURRENT_MAC=$(ip neigh show "$GATEWAY_IP" | awk '{print $5}')
    if [ "$CURRENT_MAC" != "$INITIAL_MAC" ] && [ -n "$CURRENT_MAC" ]; then
        echo -e "\a[CRITICAL ALERT] ARP POISONING DETECTED!"
        echo "Timestamp: $(date)"
        echo "Old Gateway MAC: $INITIAL_MAC -> Rogue MAC: $CURRENT_MAC"
        exit 1
    fi
    sleep 2
done

4. Linux Privilege Boundaries & Capability Escalations (HTB CPTS Deep Dive)

Traditional CTF platforms generic scripts run karwati hain (linpeas.sh), lekin enterprise audits me first-principles permission analysis chahiye hota hai.
Monolithic Root vs Granular Capabilities

Linux Kernel 2.2+ me root ke powers ko 40+ granular flags me toda gaya:

    CAP_SETUID: Process ko apna effective user ID change karne ki permission deta hai. Agar ye capability kisi binary ko mil jaye (e.g., Python ya Perl), to unprivileged user runtime par root ban sakta hai.

    CAP_DAC_OVERRIDE: Kernel ke classic Read/Write/Execute permission checks ko bypass kar deta hai. Process kisi bhi file ko overwrite kar sakti hai chahe permissions 000 kyu na ho.

    CAP_SYS_ADMIN: Sabse dangerous capability — mounts alter karna, cgroups modify karna, aur container escapes initiate karna allow karti hai.

Classic Permission Check Workflow:
  Process requests access to /etc/shadow
              │
              ▼
  Is Process UID == 0 (root)?
        ├── YES ──► Access Granted
        └── NO  ──► Check CAP_DAC_OVERRIDE?
                      ├── YES ──► Bypass rwx checks ──► Access Granted
                      └── NO  ──► Enforce POSIX Mode (rwx) ──► ACCESS DENIED

Hands-On Lab: Exploiting & Remediating Unsafe Capabilities
Bash

# Step 1: Simulate excessive capability assignment on a production node
sudo cp /usr/bin/python3 /tmp/python_cap
sudo setcap cap_setuid+ep /tmp/python_cap

# Step 2: Audit system for dangerous capabilities
getcap -r / 2>/dev/null

# Step 3: Demonstrate privilege bypass cleanly
/tmp/python_cap -c 'import os; os.setuid(0); print(f"[+] Effective UID: {os.geteuid()}"); os.system("id")'

# Step 4: Defense & Remediation
# Strip all extended capabilities from the binary
sudo setcap -r /tmp/python_cap
# Verify permissions returned to safe baseline
getcap /tmp/python_cap
rm -f /tmp/python_cap

5. Log Tampering, Eviction Tracing & Detection Engineering

Security incidents ke time attackers access logs delete karne ki koshish karte hain (shred, rm -rf /var/log/*, echo > /var/log/auth.log). Blue Team aur CDSA certification ka focus is baat par hota hai ki log tampering ko detect kaise karein.
The Inode Gap Analysis

Jab koi user file ko wipe karta hai ya truncate karta hai, to kernel ke metadata aur open file descriptors me evidence reh jata hai.

                    TAMPER DETECTION MECHANISM
  Normal State:
    /var/log/auth.log ──► Inode: 1048576, Size: 450 KB, Active Descriptors: 1

  Truncation Attack (echo "" > /var/log/auth.log):
    Inode remains 1048576, Size instantly 0 Bytes -> Truncation Alert!

  Unlink Attack (rm /var/log/auth.log):
    Directory entry removed, but rsyslogd holds /proc/<pid>/fd/3 open -> Ghost File Alert!

Defense Tool: Ghost Log Detector (Log Tampering Triage)
Bash

#!/usr/bin/env bash
# Detects deleted but active log handles (Evidence Preservation)
set -euo pipefail

echo "=== GHOST LOG AUDIT: DETECTING UNLINKED LOGS HELD OPEN IN RAM ==="

# Search lsof for open files in /var/log that are marked (deleted)
DELETED_LOGS=$(lsof +L1 /var/log 2>/dev/null | awk 'NR>1 {print $1, $2, $4, $NF}')

if [ -n "$DELETED_LOGS" ]; then
    echo "[!] ANOMALY DETECTED: Files have been unlinked to cover tracks!"
    echo "$DELETED_LOGS" | while read -r COMMAND PID FD FILE; do
        FD_NUM=$(echo "$FD" | tr -dc '0-9')
        echo "[*] Recovering from Process: $COMMAND (PID: $PID, Descriptor: $FD_NUM)..."
        cp "/proc/$PID/fd/$FD_NUM" "/tmp/RECOVERED_$(basename "$FILE")_${PID}.log"
        echo "[+] Saved evidence to /tmp/RECOVERED_$(basename "$FILE")_${PID}.log"
    done
else
    echo "[✔] All open system logs have valid directory pointers. No unlinking detected."
fi

6. Dynamic Linker Hijacking & Shared Object Internals

HTB CPTS aur Linux Internals modules dynamic linker (ld.so) ki search order ko misuse karke hone wale privilege issues ko cover karte hain.
The Library Loading Order

Jab koi dynamically linked binary run hoti hai, to linker shared libraries (.so) ko is order me khojta hai:

    Binary ke internal RPATH / RUNPATH tags.

    Environment variable: LD_PRELOAD (Highest priority override).

    Environment variable: LD_LIBRARY_PATH.

    /etc/ld.so.cache (binary index of system libraries).

    Default paths: /lib/x86_64-linux-gnu, /usr/lib.

[ Binary Executed ]
        │
        ▼
Is LD_PRELOAD configured? ──► YES ──► Load custom library BEFORE all standard C calls
        │ (NO)
        ▼
Search DT_RPATH in ELF header
        │ (Missing)
        ▼
Search /etc/ld.so.conf.d/ entries

Hands-On Lab: Understanding Preload Defenses
Bash

# 1. Inspect dynamic dependencies of any standard binary
ldd /bin/ls

# 2. Verify security mechanism: SUID binaries automatically ignore LD_PRELOAD!
# When AT_SECURE is set in the kernel auxiliary vector, ld.so drops unsafe environment variables.
LD_PRELOAD=/tmp/fake.so /usr/bin/passwd 2>&1 | grep -q "ignored" && echo "[✔] Hardened against LD_PRELOAD"

7. Container Escape Mechanics & Kernel Attack Vectors

Container isolation tootne ka primary reason hota hai host resources ka container ke andar bind-mount hona.
The Docker Socket (docker.sock) Disaster

Docker daemon (dockerd) ek REST API expose karta hai over the Unix domain socket /var/run/docker.sock. Ye socket root user ke equivalent hota hai. Agar koi container is socket ko mount karta hai:

[ Compromised Container ]
           │
  (Mounts /var/run/docker.sock)
           │
           ▼
[ Talk to Host Docker Daemon API ]
           │
           ▼
Launch New Container with:
  -v /:/host_root --privileged
           │
           ▼
[ FULL COMPROMISE OF HOST OPERATING SYSTEM ]

Container Hardening Verification Checklist

    Container me non-root user use karein: USER 1000:1000.

    Saare Linux capabilities drop karein: --cap-drop=ALL.

    Root filesystem ko Read-Only banayein: --read-only.

    Privilege escalation disable karein: --security-opt=no-new-privileges:true.

8. Automated Diagnostic Tool: Memory, Network, and Inode Integrity Script

Ye script system par run karke real-time memory leaks, rogue listening sockets, aur capability misconfigurations ko detect karti hai:
Bash

#!/usr/bin/env bash
# ==============================================================================
# Script Name : deep_system_audit.sh
# Purpose     : Enterprise Grade Linux Threat Detection & Internals Verification
# ==============================================================================

set -euo pipefail

echo "========================================================"
echo "    LINUX SYSTEM THREAT & INTERNALS INTEGRITY CHECK     "
echo "========================================================"

# Check 1: Inode Exhaustion & Hidden Large Directories
echo -e "\n[*] Auditing Inode Saturation across mounts..."
df -i | awk '$5+0 > 80 {print "[WARNING] High Inode Usage: "$0}'

# Check 2: Raw Socket Listeners (Unattributed processes)
echo -e "\n[*] Auditing Active Listening Sockets..."
if command -v ss &>/dev/null; then
    ss -tulpn | awk 'NR>1 {print "  Protocol: "$1" | Local: "$5" | Process: "$7}'
fi

# Check 3: SUID Binaries with Write Permissions for Others (Critical Misconfig)
echo -e "\n[*] Scanning for World-Writable SUID binaries..."
DANGEROUS_SUID=$(find / -type f -perm -4002 2>/dev/null || true)
if [ -n "$DANGEROUS_SUID" ]; then
    echo "[ALERT] Found World-Writable SUID File(s):"
    echo "$DANGEROUS_SUID"
else
    echo "[✔] No world-writable SUID binaries located."
fi

# Check 4: Linux Capabilities Audit
echo -e "\n[*] Enumerating Extended Capabilities..."
if command -v getcap &>/dev/null; then
    getcap -r / 2>/dev/null || true
else
    echo "[-] getcap utility not installed."
fi

# Check 5: Active Promiscuous Network Interfaces (Sniffer Detection)
echo -e "\n[*] Checking for Promiscuous Network Interfaces..."
PROMISC_INTERFACES=$(ip link | grep -i "PROMISC" || true)
if [ -n "$PROMISC_INTERFACES" ]; then
    echo "[WARNING] Promiscuous interface detected (Active Sniffing):"
    echo "$PROMISC_INTERFACES"
else
    echo "[✔] No interfaces operating in promiscuous packet capture mode."
fi

echo -e "\n========================================================"
echo "    AUDIT COMPLETED: SYSTEM BASELINE CONFIRMED           "
echo "========================================================"

What You Learned / आपने क्या सीखा

    Hindi: Aapne samjha ki real-world Linux security CTF tools run karne ka naam nahi hai. Process memory (/proc/<pid>/mem), network frames, system calls (ptrace), aur Kernel Capabilities ke actual behavior ko inspect aur defend karna hi real Linux mastery hai.

    English: You now understand that deep Linux systems security is grounded in operating system primitives: inspecting live process memory, analyzing dynamic linking execution order, intercepting syscalls, and strictly enforcing kernel capability limits.

## 8. The 23-Level Structured Curriculum

---

### Level -1: Junior Explorer (Visual-First System Exploration)

#### 1. Core Intuition & Visual Analogies

Before running complex commands blindly on a terminal, you must develop an accurate mental model of what the system looks like under the hood.

* **The Operating System as a Massive Library:** The hard drive is the library archive; directories are rooms; files are physical books; file permissions are the physical access keys carried by patrons and staff.
* **The Kernel as the Chief Librarian:** Nobody touches the books directly from the shelves. You ask the librarian via a slip of paper (a **System Call**), and the librarian retrieves or updates the book for you.
* **The Shell as the Communication Intercom:** The terminal prompt is the microphone. When you type words into it, the shell interprets your sentence, verifies what you asked for, and passes the request to the Chief Librarian.
* **Pipes as Physical Plumbing Tubes:** Imagine water running through pipes. Command 1 pours water (data) into a tube (`|`), and Command 2 receives that exact same water to filter it or clean it.

```
       [ Terminal Intercom (Shell) ]
                     │
         (Sends System Call Request)
                     │
                     ▼
       [ Chief Librarian (Kernel) ]
        │            │           │
        ▼            ▼           ▼
   [ Hard Drive ] [ Memory ] [ Network Card ]

```

#### 2. Visual-First Utilities (Bridging Sight to Text)

* **Midnight Commander (`mc`):** Launch a dual-pane visual file manager directly inside the terminal. Use arrow keys to navigate directories, press `F3` to view file contents, and press `F5` to copy files. This visually maps the Unix file tree into distinct panes.
* **Interactive System Monitoring (`htop`):** View your computer's memory, CPU load bars, and active processes in color. Visually identify what takes up computing power, sort by memory consumption, and send a termination signal (`F9` followed by `SIGTERM`) without writing manual process IDs.
* **Pipes Visualized with `pv`:** Run data pipelines through the pipe viewer utility (`pv`) to watch bytes flowing through stdout in real time.

#### 3. Hands-On Practical Lab

1. Open the terminal and type `mc`. Navigate to `/var/log` using the arrow keys.
2. Select any file ending in `.log` and press `F3`. Observe how text files are stored line-by-line. Press `F10` to exit.
3. Open `htop`. Locate the process taking the most memory. Press `F6` to change the sort order. Press `q` to quit.
4. Run the visual pipeline test:
```bash
cat /dev/urandom | pv | head -c 10M > /dev/null

```


Watch the live data transfer rate indicator measure byte execution across standard streams.

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne dekha ki Linux koi jaadu ya complex black screen nahi hai, balki ek organized library ki tarah hai jisme files folders me rehti hain aur programs screen par live run hote hain.
* **English:** You now understand that Linux is not an abstract black box; it is an organized, visible structure of files, directories, and live processes that can be inspected visually before running commands blind.

---

### Level 0: The Linux Mental Model & OS Architecture

#### 1. Technical Concepts

* **Architecture Overview:** The separation between Ring 0 (Kernel Space) and Ring 3 (User Space). Applications cannot touch hardware directly; they must transition through the system call boundary.
* **The Virtual Filesystems:** `/proc` and `/sys`. These are not disks filled with storage sectors; they are synthetic memory interfaces exposed by the Linux kernel as files.
* **Hardware Abstraction:** Devices are represented as character or block nodes inside `/dev`.
* **System Calls (`syscalls`):** The standardized software interrupts used by binaries to request services from the kernel (`read`, `write`, `openat`, `fork`, `execve`, `socket`).

```
+-------------------------------------------------------------+
|                 USER SPACE (Ring 3)                         |
|   Applications    CLI Tools (ls, cat)    Python Runtime     |
+-------------------------------------------------------------+
                              │
                    [ System Call Boundary ]
                    (e.g., sys_open, sys_read)
                              │
+-------------------------------------------------------------+
|                KERNEL SPACE (Ring 0)                        |
|   Process Scheduler    Memory Manager    VFS   Net Stack    |
+-------------------------------------------------------------+
                              │
                      [ Hardware Layer ]
           CPU          Memory (RAM)          NIC / Disks

```

#### 2. Deep-Dive Command Specifications

* `uname -a`: Prints the running kernel version, compiler build, architecture, and network node hostname.
* `cat /proc/version`: Inspects the precise GCC version and kernel compilation parameters.
* `cat /proc/cpuinfo`: Reads live processor features, flags, cache sizes, and core counts directly from kernel structures.
* `strace <binary>`: Intercepts and logs every single system call made by a process and the signals it receives.

#### 3. Hands-On Lab: Tracing the Anatomy of a Command

Execute `strace` on a minimal command to observe the system call interface in action:

```bash
# Trace the execution of the basic true command
strace -e trace=openat,read,write,execve /bin/echo "Hello Linux Kernel"

```

Observe how the binary begins with an `execve` call, loads dynamic libraries via `openat`, maps them to memory, issues a single `write(1, "Hello Linux Kernel\n", 19)` syscall to standard output, and exits via `exit_group(0)`.

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne jana ki applications hardware se directly baat nahi kar sakti; har operation ke liye Kernel ko system call bhejna padta hai. `/proc` aur `/sys` real hard drive files nahi balki live memory data hain.
* **English:** You now understand that applications must transition to kernel space via system calls to perform I/O, and that `/proc` and `/sys` are dynamic virtual interfaces reflecting live kernel state.

---

### Level 1: Terminal Mastery, Data Streams & Pipeline Chaining

#### 1. Technical Concepts

* **The POSIX File Descriptor Model:**
* `0`: Standard Input (`stdin`)
* `1`: Standard Output (`stdout`)
* `2`: Standard Error (`stderr`)


* **Redirection Primitives:**
* `>`: Overwrite destination file with stdout.
* `>>`: Append stdout to destination file.
* `<`: Read stdin from a file.
* `2>`: Redirect only error messages.
* `&>` or `2>&1`: Combine stdout and stderr into a single stream.


* **Data Flow Chaining:** The Unix Philosophy—write programs that do one thing well and connect them using pipes (`|`). A pipe takes the file descriptor 1 (`stdout`) of the upstream process and binds it directly to file descriptor 0 (`stdin`) of the downstream process via kernel memory buffers.

```
[ Command A ] ─── fd 1 (stdout) ───► [ Kernel Pipe Buffer ] ───► fd 0 (stdin) ───► [ Command B ]
      │
  fd 2 (stderr)
      │
      ▼
[ error.log ]

```

#### 2. Deep-Dive Command Specifications

* `grep [options] PATTERN [FILE]`: Searches inputs for matching regular expressions.
* `-i`: Case-insensitive search.
* `-v`: Invert match (print lines that do NOT match).
* `-E`: Use extended regular expressions.
* `-r`: Recursive directory traversal.


* `sort`: Orders textual data alphabetically or numerically (`-n` for numeric, `-k` for column selection, `-r` for reverse).
* `uniq`: Deduplicates adjacent lines (`-c` to prefix lines with occurrence counts, `-u` to print only unique lines).
* `tee`: Duplicates standard input to standard output and one or more files simultaneously.

#### 3. Hands-On Lab: Multistage Log Filtering

Process an intentionally bloated sample web log file to extract the top 3 most active IP addresses generating 404 errors:

```bash
# Generate dummy log data
cat << 'EOF' > /tmp/access.log
192.168.1.50 - - [01/Jan/2026:10:00:01] "GET /index.html HTTP/1.1" 200
10.0.0.15 - - [01/Jan/2026:10:00:02] "GET /admin HTTP/1.1" 404
172.16.0.4 - - [01/Jan/2026:10:00:03] "GET /login HTTP/1.1" 404
10.0.0.15 - - [01/Jan/2026:10:00:04] "GET /config.php HTTP/1.1" 404
192.168.1.50 - - [01/Jan/2026:10:00:05] "GET /style.css HTTP/1.1" 200
10.0.0.15 - - [01/Jan/2026:10:00:06] "GET /secret HTTP/1.1" 404
172.16.0.4 - - [01/Jan/2026:10:00:07] "GET /backup.zip HTTP/1.1" 404
EOF

# Execute multi-stage pipeline: Filter 404s -> Extract IP column -> Sort -> Count -> Sort Descending -> Head
cat /tmp/access.log \
  | grep " 404" \
  | cut -d ' ' -f 1 \
  | sort \
  | uniq -c \
  | sort -nr \
  | head -n 3

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki terminal me complex programs likhe bina, chhote tools ko `|`, `>`, aur `2>&1` ke through jodh kar kisi bhi data stream ko inspect aur transform kiya ja sakta hai.
* **English:** You can confidently route streams using POSIX file descriptors, filter raw data through deterministic pipelines, and process server logs without running complex code.

---

### Level 2: Filesystem Deep Dive, Inodes & Metadata Forensics

#### 1. Technical Concepts

* **The Inode (Index Node):** The fundamental data structure of the Linux filesystem. An inode stores file metadata: file size, physical storage block pointers, owner UID, group GID, access mode permissions, link count, and timestamps (atime, mtime, ctime). **The filename is not stored in the inode; it is stored inside directory entries.**
* **Hard Links vs. Symbolic Links:**
* *Hard Link:* A directory entry pointing directly to an existing inode number on the same filesystem. Deleting the original file does not delete the data until the link counter hits zero.
* *Symbolic (Soft) Link:* A special file containing a text string pointing to another filesystem path. If the target file is removed, the link breaks (dangles).


* **VFS Layout Hierarchy (FHS):**
* `/etc`: Host-specific static configuration files.
* `/var`: Variable data files (logs, spools, caches).
* `/bin` & `/sbin`: Core binaries (often symlinked to `/usr/bin` in modern distributions).
* `/dev`: Device nodes managed dynamically by `udev`.



```
[ Directory Entry: "file.txt" ] ───┐
                                   ├──► [ Inode #10542 ] ───► [ Storage Blocks: "Hello World" ]
[ Directory Entry: "hard.lnk" ] ───┘    (Ref Count: 2)

[ Directory Entry: "soft.lnk" ] ──────► [ Inode #10543 ] ───► [ Text Path: "file.txt" ]

```

#### 2. Deep-Dive Command Specifications

* `stat [file]`: Displays comprehensive inode status including exact allocation blocks, timestamps down to the nanosecond, and access permissions.
* `ls -i`: Lists files alongside their filesystem inode index numbers.
* `ln [target] [link_name]`: Creates a physical hard link.
* `ln -s [target] [link_name]`: Creates a symbolic path link.
* `df -h` & `df -i`: Inspects filesystem disk space and inode availability. A disk can run out of inodes even if it has gigabytes of free physical space.

#### 3. Hands-On Lab: Live Data Recovery from an Unlinked Open File

When an active process has an open file handle, deleting the directory entry with `rm` does not immediately free the blocks from the disk. Recover the data using kernel descriptors:

```bash
# 1. Create a dummy file and keep an open read descriptor using a background sleep process
echo "CRITICAL TRANSACTION DATA - DO NOT LOSE" > /tmp/trans.log
exec 3< /tmp/trans.log

# 2. Delete the file from the filesystem tree
rm -f /tmp/trans.log
ls -la /tmp/trans.log  # Confirms: No such file or directory

# 3. Locate the lingering open descriptor via /proc
ls -l /proc/$$/fd/3

# 4. Recover the deleted contents directly from the open file descriptor
cat /proc/$$/fd/3 > /tmp/trans_recovered.log
cat /tmp/trans_recovered.log

# 5. Clean up the descriptor
exec 3<&-

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne samjha ki file ka naam sirf ek pointer hota hai. Asli file Inode aur blocks me hoti hai. Jab tak koi process file ko open rakhta hai, usse `/proc/<pid>/fd` se recover kiya ja sakta hai.
* **English:** You understand that directory entries are merely pointers to inodes. Even if a file is deleted from the namespace, active file descriptors retain access to physical disk blocks via the `/proc` filesystem.

---

### Level 3: Access Control, Permissions, SUID & POSIX Capabilities

#### 1. Technical Concepts

* **The Traditional Permission Triad:** Owner (User), Group, and Others across Read (`r=4`), Write (`w=2`), and Execute (`x=1`).
* **Special Permission Bits:**
* **Setuid (SUID, Octal 4000):** Executes the target binary with the privileges of the file owner rather than the executing user. Crucial for utilities like `/usr/bin/passwd`.
* **Setgid (SGID, Octal 2000):** Executes with group owner rights or inherits group ownership on newly created directory members.
* **Sticky Bit (Octal 1000):** Applied to directories (like `/tmp`) to restrict file deletion to only the file owner or root, regardless of directory write permissions.


* **Linux Capabilities (`cap_get_proc`):** Splitting root's monolithic power into granular privileges (`CAP_NET_BIND_SERVICE`, `CAP_SYS_ADMIN`, `CAP_SETUID`). A process can be granted permission to bind to low ports without receiving total root access.

```
       [ Monolithic Root (Dangerous) ]
                     │
                     ▼ (Decomposed into Granular Capabilities)
+--------------------------------------------------------------+
| CAP_NET_BIND_SERVICE : Bind to ports below 1024              |
| CAP_SYS_PTRACE       : Debug other processes with ptrace     |
| CAP_DAC_OVERRIDE     : Bypass filesystem read/write checks   |
| CAP_NET_RAW          : Craft arbitrary raw packets           |
+--------------------------------------------------------------+

```

#### 2. Deep-Dive Command Specifications

* `chmod [mode] [file]`: Alters standard or octal access masks.
* `chown [user]:[group] [file]`: Alters resource ownership identities.
* `getfacl` / `setfacl`: Reads and configures extended POSIX Access Control Lists for complex, multi-user access rules.
* `getcap -r / 2>/dev/null`: Recursively scans the entire filesystem for binaries holding explicit Linux capabilities.

#### 3. Hands-On Lab: Auditing and Remediating a Rogue SUID Binary

Identify and neutralize an unsafe SUID configuration in an isolated sandbox environment:

```bash
# 1. Simulate an insecure binary configuration
cp /bin/cp /tmp/rogue_cp
chmod 4755 /tmp/rogue_cp
ls -la /tmp/rogue_cp # Notice the -rwsr-xr-x permission pattern

# 2. Formulate a search pipeline to identify all SUID files across the system
find / -perm -4000 -type f -exec ls -ld {} + 2>/dev/null

# 3. Analyze the risk: Any non-root user can overwrite sensitive files using /tmp/rogue_cp
# Remediate by stripping the SUID bit
chmod u-s /tmp/rogue_cp
ls -la /tmp/rogue_cp # Confirms: -rwxr-xr-x
rm -f /tmp/rogue_cp

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki permissions sirf `chmod 777` nahi hoti. SUID aur Capabilities ka galat configuration normal user ko root bana sakta hai, aur isse audit karke theek karna hi hardening hai.
* **English:** You understand the principle of least privilege, the security risks associated with unvetted SUID/SGID binaries, and how to audit and enforce granular Linux capabilities.

---

### Level 4: Process Lifecycle, Signals & Runtime Diagnostics

#### 1. Technical Concepts

* **Process Creation & Execution:** Every new process in Linux is instantiated via two sequential syscalls: `fork()` (which clones the caller's address space and registers, creating a child PID) followed by `execve()` (which replaces the address space with a new program image).
* **Process States:**
* `R` (Running / Runnable on CPU queue)
* `S` (Interruptible Sleep — waiting for an event or I/O)
* `D` (Uninterruptible Sleep — usually waiting directly for disk controller I/O; cannot be killed with `SIGKILL`)
* `Z` (Zombie — terminated execution, but parent has not yet called `waitpid()` to read exit status)


* **Signals:** Standardized asynchronous software notifications sent to a process:
* `SIGHUP` (1): Terminal hangup or reload configuration.
* `SIGINT` (2): Interrupt from keyboard (`Ctrl+C`).
* `SIGQUIT` (3): Quit from keyboard with core dump (`Ctrl+\`).
* `SIGTERM` (15): Graceful termination request.
* `SIGKILL` (9): Uncatchable immediate process abort executed directly by the kernel scheduler.



```
       [ fork() ]                       [ execve() ]
Parent ─────────► Cloned Child Process ────────────► New Program Running
                        │
                        ▼ (Terminates)
               [ Zombie State (Z) ] ──(Parent calls waitpid())──► Deallocated

```

#### 2. Deep-Dive Command Specifications

* `ps aux`: Lists every active process across all users, displaying CPU/memory usage, runtime state, and command line.
* `pgrep [pattern]` / `pkill [pattern]`: Searches or signals processes by their execution name.
* `lsof -p <PID>`: Dumps every open file, regular library, terminal device, and active network socket mapped to a specific process ID.
* `kill -<SIGNAL> <PID>`: Dispatches explicit signals to runtime targets.

#### 3. Hands-On Lab: Diagnosing and Cleansing an Unresponsive Process

Create a simulated stuck background task, trace its environment, inspect its open sockets, and terminate it:

```bash
# 1. Launch a background task that simulates an infinite loop
python3 -c 'import time; open("/tmp/locked.txt", "w"); time.sleep(1000)' &
LOOP_PID=$!

# 2. Inspect process details via the /proc interface directly
cat /proc/$LOOP_PID/cmdline | tr '\0' ' '; echo
cat /proc/$LOOP_PID/status | grep State

# 3. Locate all files this specific PID currently holds open
lsof -p $LOOP_PID

# 4. Gracefully terminate, then verify clean destruction
kill -15 $LOOP_PID
sleep 1
kill -0 $LOOP_PID 2>/dev/null || echo "Process cleanly removed from scheduler"
rm -f /tmp/locked.txt

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne jana ki processes kaise bante hain (`fork` + `execve`), Zombie processes kyu bante hain, aur kisi process ko bina andaza lagaye `lsof` aur `/proc/<pid>` se kaise inspect kiya jata hai.
* **English:** You can inspect runtime process states, trace open file descriptors and active libraries, and handle unresponsive processes methodically using proper POSIX signals.

---

### Level 5: System Administration, Services & systemd Internals

#### 1. Technical Concepts

* **The Init System & Process ID 1:** When the Linux kernel completes hardware initialization, it mounts the root filesystem and executes PID 1 (`/lib/systemd/systemd`). PID 1 adopts all orphaned processes and manages service lifecycles.
* **systemd Units:** Declarative configuration files specifying how software should run, restart, isolate, and terminate.
* Unit types: `.service`, `.socket`, `.target`, `.timer`.


* **Target Sequencing:** System states representing milestones:
* `multi-user.target`: Standard text-mode networked multi-user system.
* `graphical.target`: Graphical desktop interface.
* `rescue.target`: Single-user emergency administrative shell.


* **Journal Logging Architecture:** `systemd-journald` captures binary structured logs directly from the kernel, stdout/stderr of services, syslog calls, and early boot execution before traditional logging daemons start.

```
                  [ Linux Kernel Boots ]
                            │
                            ▼
               [ systemd (PID 1 Active) ]
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
[ Basic.target ]   [ Network.target ]   [ Multi-user.target ]
        │                   │                   │
   Early Drivers       IP / Routing       Active Services (sshd)

```

#### 2. Deep-Dive Command Specifications

* `systemctl status <unit>`: Queries the active operational state, memory usage, main PID, and recent log snippets of a service.
* `systemctl start|stop|restart|reload <unit>`: Dispatches state-change commands to the systemd manager.
* `systemctl enable|disable --now <unit>`: Modifies symbolic links in `/etc/systemd/system/` to configure automatic startup at boot.
* `journalctl -u <unit> -xe --no-pager`: Dumps exhaustive, structured diagnostic logs for a specific service, jumping straight to failures.

#### 3. Hands-On Lab: Writing, Hardening, and Debugging a Custom Service Unit

Write a custom system service from scratch, configure security sandboxing flags, and manage its lifecycle:

```bash
# 1. Create a custom daemon script
cat << 'EOF' > /usr/local/bin/micro_daemon.sh
#!/usr/bin/env bash
trap "exit 0" SIGTERM
while true; do
    echo "Daemon active at $(date)" >> /var/log/micro_daemon.log
    sleep 5
done
EOF
chmod 755 /usr/local/bin/micro_daemon.sh

# 2. Author a hardened systemd service unit file
cat << 'EOF' > /etc/systemd/system/micro-daemon.service
[Unit]
Description=Production Hardened Micro Daemon Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/micro_daemon.sh
Restart=on-failure
RestartSec=3s
# Security Hardening Flags
ProtectSystem=strict
ProtectHome=true
NoNewPrivileges=true
ReadWritePaths=/var/log

[Install]
WantedBy=multi-user.target
EOF

# 3. Reload daemon configurations, start, and audit
systemctl daemon-reload
systemctl start micro-daemon.service
systemctl status micro-daemon.service --no-pager

# Clean up
systemctl stop micro-daemon.service
rm -f /etc/systemd/system/micro-daemon.service /usr/local/bin/micro_daemon.sh /var/log/micro_daemon.log
systemctl daemon-reload

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki Linux server par background services kaise likhi jati hain, unhe crash hone par auto-restart kaise kiya jata hai, aur `journalctl` se service errors ko root-cause kaise karte hain.
* **English:** You can author custom systemd service units, configure sandboxing controls (`ProtectSystem`, `NoNewPrivileges`), and debug failed services using structured journal logs.

---

### Level 6: Core Networking, Packet Analysis & Socket Forensics

#### 1. Technical Concepts

* **The TCP 3-Way Handshake & State Machine:**
1. Client sends `SYN` (Synchronize flag, sets initial sequence number).
2. Server returns `SYN-ACK` (Synchronize-Acknowledgment flags).
3. Client returns `ACK` (Acknowledgment flag). Sockets transition to `ESTABLISHED`.


* **Packet Headers (L2, L3, L4):**
* Layer 2 (Data Link): Ethernet frames, MAC addresses, ARP resolution.
* Layer 3 (Network): IPv4/IPv6 headers, TTL (Time to Live), fragmentation fields.
* Layer 4 (Transport): TCP/UDP segments, source/destination ports, checksums, window sizing.


* **Socket Abstraction:** An endpoint in kernel memory combining `Protocol + Local IP + Local Port + Remote IP + Remote Port`.

```
CLIENT                                              SERVER
  │                                                   │
  ├─────── [ TCP SYN: Seq=X ] ───────────────────────►│  (Server enters SYN-RECEIVED)
  │                                                   │
  │◄────── [ TCP SYN-ACK: Seq=Y, Ack=X+1 ] ───────────┤
  │                                                   │
  ├─────── [ TCP ACK: Ack=Y+1 ] ─────────────────────►│  (Socket transitions to ESTABLISHED)

```

#### 2. Deep-Dive Command Specifications

* `ip address show` (or `ip a`): Lists all interfaces, link layer statuses, and assigned subnets.
* `ip route show` (or `ip r`): Inspects kernel routing tables and default gateways.
* `ss -tulpn`: Displays all active listening (`-l`) TCP (`-t`) and UDP (`-u`) numeric (`-n`) sockets alongside their owning Process ID and program name (`-p`).
* `tcpdump -nnvv -i <interface> [filter]`: Captures raw link-layer and network-layer packets off the wire without performing slow DNS reverse lookups (`-nn`).

#### 3. Hands-On Lab: Live Network Packet Forensics

Capture a live TCP handshake across your local loopback interface and extract payload data:

```bash
# 1. Start a local listener in the background on port 9999
nc -l -p 9999 > /tmp/received.txt &
NC_PID=$!
sleep 1

# 2. Capture packets on the loopback interface using tcpdump
tcpdump -i lo -nn -vv "port 9999" -c 5 -w /tmp/handshake.pcap &
TCPDUMP_PID=$!
sleep 1

# 3. Transmit a message to trigger the 3-way handshake and data transfer
echo "SECURITY-PACKET-AUDIT-VERIFIED" | nc -N 127.0.0.1 9999

# 4. Wait for capture completion and inspect the PCAP structure
sleep 2
tcpdump -r /tmp/handshake.pcap -nn -X

# Clean up
rm -f /tmp/received.txt /tmp/handshake.pcap

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne network ko sirf IP address nahi, balki packet level par samjha. TCP handshake kaise banta hai aur `tcpdump` se wire ke andar se data ko live capture kaise kiya jata hai.
* **English:** You understand network packet framing across the OSI stack, can trace TCP connection states using `ss`, and know how to capture and inspect raw packet payloads with `tcpdump`.

---

### Level 7: Web Protocols, Raw HTTP & API Wrangling via CLI

#### 1. Technical Concepts

* **The Stateless HTTP Protocol:** HTTP/1.1 is plain text over a transport-layer TCP socket. A client connects, transmits an ASCII request block, and waits for the server's structured response.
* **Request Anatomy:**
* Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`).
* Path and Query Parameters (`/api/v1/users?role=admin`).
* Headers (`Host:`, `User-Agent:`, `Authorization: Bearer <token>`, `Content-Type:`).
* Empty line (`\r\n\r\n`) signaling header termination.
* Body payload (JSON, XML, multipart form data).


* **Response Anatomy:**
* Status Line (`HTTP/1.1 200 OK`, `401 Unauthorized`, `500 Internal Server Error`).
* Response Headers (`Set-Cookie:`, `Cache-Control:`, `Content-Length:`).
* Body data.



```
CLIENT                                          SERVER
  │                                               │
  │─── [ GET /index.html HTTP/1.1 ] ─────────────►│
  │─── [ Host: example.com        ] ─────────────►│
  │─── [ Accept: text/html        ] ─────────────►│
  │─── [ \r\n\r\n (Empty Line)    ] ─────────────►│
  │                                               │
  │◄── [ HTTP/1.1 200 OK          ] ──────────────┤
  │◄── [ Content-Type: text/html  ] ──────────────┤
  │◄── [ Content-Length: 125      ] ──────────────┤
  │◄── [ \r\n\r\n                 ] ──────────────┤
  │◄── [ <!DOCTYPE html>...       ] ──────────────┤

```

#### 2. Deep-Dive Command Specifications

* `curl [options] URL`: Swiss-army knife for raw HTTP/HTTPS queries.
* `-i`: Include protocol response headers in output.
* `-v`: Verbose mode (displays local socket connects, TLS handshakes, and outgoing request headers).
* `-X <METHOD>`: Specify explicit HTTP method.
* `-H "Header: Value"`: Add custom headers.
* `-d '{"key":"value"}'`: Send raw POST body data.


* `jq [filter]`: High-performance command-line JSON processor. Extracts keys, transforms arrays, and formats raw API responses.

#### 3. Hands-On Lab: Interacting with Local Web Endpoints via CLI

Deploy a minimal local server, make requests using `curl`, and parse JSON responses with `jq`:

```bash
# 1. Spawn a local Python HTTP test service
cat << 'EOF' > /tmp/mock_api.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"status": "operational", "node_id": 42, "services": ["auth", "database"]}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

HTTPServer(("127.0.0.1", 8888), SimpleAPI).serve_forever()
EOF

python3 /tmp/mock_api.py &
API_PID=$!
sleep 1

# 2. Query endpoint using verbose curl and pipe into jq for filtering
curl -s -v http://127.0.0.1:8888/api/status 2>&1 | grep -E "(> GET|< HTTP)"
curl -s http://127.0.0.1:8888/api/status | jq '.services[]' -r

# Clean up
kill -9 $API_PID
rm -f /tmp/mock_api.py

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne web application traffic ko browser ke bina terminal se inspect karna seekha. HTTP requests kaise banaye jate hain aur API response me se data `jq` se kaise filter hota hai.
* **English:** You can construct and debug raw HTTP requests using `curl`, inspect connection headers, and extract structured metrics from JSON API endpoints using `jq`.

---

### Level 8: Defensive Shell Scripting & Infrastructure Automation

#### 1. Technical Concepts

* **Strict Execution Mode:** The defensive Bash preamble: `set -euo pipefail`.
* `-e`: Exit immediately if any command returns a non-zero exit status.
* `-u`: Treat unset variables as an error and abort immediately.
* `-o pipefail`: Return the exit status of the *last command in the pipe that failed*, preventing errors from being masked.


* **Signal Trapping:** The `trap` builtin intercepts kernel signals (`EXIT`, `INT`, `TERM`) to guarantee temporary files are wiped and locked resources are freed upon script exit, regardless of crashes.
* **Input Sanitization & Safe Quoting:** Preventing Word Splitting and Glob Expansion by always wrapping shell parameter expansions in double quotes: `"${VARIABLE}"`.

```
BAD:
rm -rf /tmp/$DIR/*   (If DIR is unset, executes: rm -rf /tmp//* -> catastrophe!)

DEFENSIVE:
set -euo pipefail
target_dir="${1:?Error: Target directory must be supplied}"
rm -rf -- "${target_dir:?}"/*

```

#### 2. Deep-Dive Command Specifications

* `getopts`: Builtin command for parsing standard CLI flags (`-f`, `-h`, `-v`) with arguments.
* `trap 'cleanup_command' EXIT INT TERM`: Registers cleanup routines executed automatically on termination.
* `mktemp -d`: Creates secure, unguessable temporary directories in `/tmp` protected against symlink attacks.

#### 3. Hands-On Lab: Writing a Hardened System Health Collector

Build a production-grade Bash utility that gathers host metrics safely:

```bash
cat << 'EOF' > /tmp/sysaudit_mini.sh
#!/usr/bin/env bash
set -euo pipefail

# Initialize temporary scratch directory safely
TMP_DIR=$(mktemp -d /tmp/audit.XXXXXX)

# Guarantee removal of temporary files on script exit
cleanup() {
    rm -rf "${TMP_DIR}"
    echo "[*] Sandbox resources successfully freed."
}
trap cleanup EXIT INT TERM

echo "=== LINUX HOST MINI AUDIT ==="
echo "Collecting system statistics to: ${TMP_DIR}"

# Gather data defensive of exit codes
uname -srm > "${TMP_DIR}/kernel.txt"
uptime | awk -F'( |,|:)+' '{print "Uptime: "$4" hours"}' > "${TMP_DIR}/uptime.txt"
df -h / | awk 'NR==2 {print "Root Disk Usage: "$5}' > "${TMP_DIR}/disk.txt"

# Display compiled summary
cat "${TMP_DIR}/kernel.txt"
cat "${TMP_DIR}/uptime.txt"
cat "${TMP_DIR}/disk.txt"
echo "=== AUDIT COMPLETED ==="
EOF

chmod +x /tmp/sysaudit_mini.sh
/tmp/sysaudit_mini.sh
rm -f /tmp/sysaudit_mini.sh

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki production script kaise likhte hain jo kabhi beech me silent fail na ho (`set -euo pipefail`) aur crash hone par bhi `trap` ke zariye resources clean kar de.
* **English:** You can author resilient, portable Bash scripts equipped with defensive execution flags, input validation, and automatic cleanup routines using signal traps.

---

### Level 9: Systems & Security Automation with Python

#### 1. Technical Concepts

* **Python Systems Programming:** Moving beyond shell scripts when data structures, high-volume log parsing, raw TCP socket interactions, and concurrency are required.
* **Subprocess Execution Safety:** Utilizing `subprocess.run(["cmd", "arg1"], check=True, capture_output=True)` with list arguments instead of shell strings (`shell=True`), eliminating command injection vulnerabilities at the language level.
* **Socket Programming Primitives:** Interfacing with the POSIX socket layer using Python's native `socket` library to build custom probes, listeners, and protocol parsers.

```
Python Runtime
  │
  ├──► socket.socket(socket.AF_INET, socket.SOCK_STREAM) ──► Direct TCP Connection
  │
  └──► subprocess.run(["/usr/bin/ip", "route"], check=True) ──► Safe Subprocess Execution

```

#### 2. Deep-Dive Command Specifications

* `python3 -m venv [dir]`: Installs a modern, isolated virtual environment to manage external libraries without tainting global operating system packages.
* Native Python modules to master:
* `os` & `sys`: Process environment variables, exit codes, and standard streams.
* `pathlib`: Object-oriented, cross-platform filesystem path manipulations.
* `subprocess`: Controlled system binary invocation with standard stream redirection.
* `socket`: Raw network socket creation, binding, and data transmission.



#### 3. Hands-On Lab: Writing a High-Speed Local Socket Port Scanner

Write a pure Python utility that checks listening ports across your local loopback interface:

```bash
cat << 'EOF' > /tmp/port_probe.py
#!/usr/bin/env python3
import socket
import sys

TARGET_HOST = "127.0.0.1"
PORTS_TO_CHECK = [22, 80, 443, 3000, 8080, 9999]

print(f"[*] Scanning {TARGET_HOST} across target verification ports...")

for port in PORTS_TO_CHECK:
    # Instantiate a standard IPv4 streaming socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) # Fast 500ms timeout
    
    result = sock.connect_ex((TARGET_HOST, port))
    if result == 0:
        print(f" [+] Port {port:<5} : OPEN")
    else:
        print(f" [-] Port {port:<5} : CLOSED")
    sock.close()

print("[*] Scan execution completed.")
EOF

python3 /tmp/port_probe.py
rm -f /tmp/port_probe.py

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki Bash ke baad Python se system level par kaise kaam kiya jata hai, safe commands kaise chalaye jate hain, aur network sockets ko code se directly kaise connect kiya jata hai.
* **English:** You can build robust Python automation utilities that interface cleanly with operating system processes and network sockets without introducing command injection vulnerabilities.

---

### Level 10: Git Internals, Safe Workflows & Secret Sanitation

#### 1. Technical Concepts

* **The Git Object Model:** Git is a content-addressable key-value store. It stores data across four fundamental primitive object types inside `.git/objects/`:
* `blob`: Raw byte content of a file (identified by SHA-1/SHA-256 hash; does not contain file name or timestamps).
* `tree`: Represents a directory listing, associating filenames with blob or subtree hashes and access modes.
* `commit`: References a top-level tree object, parent commits, author, committer, and commit message.
* `tag`: An annotated reference to a specific commit object.


* **Secret Hygiene & Accidental Disclosure:** Committing sensitive files (private keys, API tokens, passwords) to a Git repository permanently burns them into the object database. **Deleting the file in a subsequent commit does not eliminate it from Git history.**
* **The Reflog:** Git's local flight recorder tracking every movement of the `HEAD` pointer. Allows complete recovery of dropped branches, lost stashes, and undone commits.

```
[ Commit Object ] ───► References ───► [ Tree Object (Root) ]
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼                                           ▼
             [ Blob: README.md ]                         [ Tree: src/ ]
                                                               │
                                                               ▼
                                                     [ Blob: main.py ]

```

#### 2. Deep-Dive Command Specifications

* `git init`: Initializes a fresh `.git` tracking database in the current working directory.
* `git status -s`: Displays short-format working tree differences and index tracking states.
* `git cat-file -p <hash>`: Inspects the raw contents and type of any Git database object by its hash.
* `git reflog`: Lists the chronological record of where your references have been in your local repository.
* `git log --oneline --graph --decorate`: Visualizes branch graphs and commit histories concisely.

#### 3. Hands-On Lab: Extracting and Sanitizing Leaked Secrets from Git History

Simulate an accidental secret commit, extract the credential from past repository objects, and purge it:

```bash
# 1. Create a scratch git project
SCRATCH_DIR=$(mktemp -d /tmp/git_leak.XXXXXX)
cd "${SCRATCH_DIR}"
git init

# 2. Accidental secret check-in
echo "PRODUCTION_API_KEY=AKIA_MOCK_SECRET_KEY_12345" > config.env
git add config.env
git commit -m "Add production configuration"

# 3. Developer realizes error and deletes file in a new commit
rm -f config.env
git commit -am "Delete sensitive configuration"

# 4. Verify file is absent from current tree, but STILL present in Git objects
ls -la config.env 2>/dev/null || echo "File is absent from active directory"
git log --oneline
# Extract the leaked key directly from the historical commit object!
git show HEAD~1:config.env

# 5. Clean up scratch workspace
cd /
rm -rf "${SCRATCH_DIR}"

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki Git file system kaise maintain karta hai. Agar koi secret commit ho gaya, toh agle commit me use delete karne se wo delete nahi hota, balki Git history ke objects me hamesha ke liye rehta hai.
* **English:** You understand Git's underlying object graph (`blobs`, `trees`, `commits`) and recognize that credentials committed to version control remain recoverable in the repository history until the object database is purged.

---

### Level 11: Secure Shell (SSH) Topologies, Hardening & Tunnels

#### 1. Technical Concepts

* **Public-Key Cryptography in OpenSSH:** Asymmetric authentication using keypairs (Ed25519 or RSA). The client proves possession of the private key (`id_ed25519`) matching the server's trusted public record (`authorized_keys`) via a cryptographic challenge-response exchange. Passwords are never sent across the wire.
* **Host Verification (`known_hosts`):** Prevents Adversary-in-the-Middle (AitM) attacks. The client verifies the server's public key fingerprint on the initial connection and stores it. If the remote host fingerprint changes unexpectedly, SSH terminates the connection immediately.
* **SSH Tunneling (Port Forwarding):** Encapsulating raw TCP streams inside an encrypted SSH connection:
* **Local Port Forwarding (`-L`):** Maps a local port to a remote service reachable by the SSH server.
* **Remote Port Forwarding (`-R`):** Maps a port on the remote SSH server back to a local internal service.
* **Dynamic Port Forwarding (`-D`):** Converts the SSH client into a local SOCKS5 proxy server for dynamic traffic routing.



```
                                  [ SSH TUNNEL ]
[ Local Client ] ─── (Local Port: 8080) ───► [ SSH Host ] ───► [ Internal DB: 5432 ]
 (localhost:8080)                            (Remote Server)

```

#### 2. Deep-Dive Command Specifications

* `ssh-keygen -t ed25519 -C "admin@infrastructure"`: Generates a modern, high-security Ed25519 elliptic-curve keypair.
* `ssh -i <private_key> -p <port> user@host`: Connects using explicit keys and non-standard ports.
* `ssh -L [local_ip:]local_port:destination_host:destination_port user@jump_host`: Establishes local port forwarding.
* `ssh -D 1080 -N -C user@jump_host`: Spawns a background SOCKS5 proxy interface on port 1080 with compression enabled.

#### 3. Hands-On Lab: Configuring Bastion Multi-Hop Navigation via `~/.ssh/config`

Author a hardened SSH client configuration file that sets up jump-host routing without writing manual long-form arguments:

```bash
# 1. Author a structured client SSH configuration
mkdir -p ~/.ssh && chmod 700 ~/.ssh
cat << 'EOF' > /tmp/mock_ssh_config
# Enforce modern, secure defaults
Host *
    IdentitiesOnly yes
    ServerAliveInterval 60
    ServerAliveCountMax 3

# Define Jump Host Bastion
Host bastion-node
    HostName 192.168.1.10
    User jumpuser
    Port 2222
    IdentityFile ~/.ssh/id_ed25519

# Target behind internal DMZ (Routed automatically through bastion)
Host internal-db-target
    HostName 10.0.0.50
    User dbadmin
    ProxyJump bastion-node
    IdentityFile ~/.ssh/id_ed25519_db
EOF

echo "[*] Mock SSH Configuration Authoring Verified:"
cat /tmp/mock_ssh_config
rm -f /tmp/mock_ssh_config

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki production me SSH password se nahi, Ed25519 keys se chalaya jata hai. ProxyJump aur SSH Tunnels ke zariye private network ke andar band servers ko securely kaise access kiya jata hai.
* **English:** You can configure key-based SSH authentication, eliminate password attack vectors, navigate segmented networks using `ProxyJump`, and map internal services via encrypted SSH tunnels.

---

### Level 12: Linux Security Architecture & Mandatory Access Control

#### 1. Technical Concepts

* **Discretionary Access Control (DAC) vs. Mandatory Access Control (MAC):**
* *DAC (Standard Linux):* The owner of a resource has total discretion over who can read, write, or execute it. If a compromised process runs as root, DAC protections become void.
* *MAC (AppArmor / SELinux):* System-wide security policy dictates whether a subject (process) can access an object (file, network socket, capability), regardless of the user's UID. Even root is restricted by the policy.


* **AppArmor:** Path-based MAC system. Policies define precisely which filesystem paths, capabilities, and network primitives a binary may access (e.g., `/usr/sbin/nginx`).
* **Security-Enhanced Linux (SELinux):** Type Enforcement, Multi-Category Security (MCS), and Multi-Level Security (MLS). Every process and file is assigned a security context (`user:role:type:level`).

```
                              [ PROCESS EXECUTION ]
                                       │
                      [ Discretionary Access Control (DAC) ]
                             (Checks UID / GID / rwx)
                                       │
                                   (Allowed)
                                       ▼
                     [ Mandatory Access Control (MAC) ]
                         (Checks SELinux / AppArmor)
                                       │
                                   (Allowed)
                                       ▼
                             [ ACCESS GRANTED ]

```

#### 2. Deep-Dive Command Specifications

* `aa-status`: Displays the operational status of AppArmor profiles (Enforce mode, Complain mode).
* `sestatus`: Displays active SELinux policy, operational mode (Enforcing, Permissive, Disabled), and type.
* `ls -Z [file]`: Displays the SELinux security context label of a target file.
* `chcon` / `semanage`: Modifies or persists SELinux context rules across filesystems.

#### 3. Hands-On Lab: Inspecting and Authoring a Minimal AppArmor Profile

Inspect how AppArmor confines applications to least-privilege paths:

```bash
# 1. Author a sample minimal AppArmor profile for a dummy executable
cat << 'EOF' > /tmp/sample_profile
#include <tunables/global>

/tmp/test_binary {
  #include <abstractions/base>

  # Allow reading self binary
  /tmp/test_binary r,
  
  # Allow reading system libraries
  /lib/** mr,
  /usr/lib/** mr,
  
  # Allow specific write logging path
  /var/log/test_binary.log rw,
  
  # Deny all other sensitive directories explicitly
  deny /etc/shadow r,
  deny /root/** rwx,
}
EOF

echo "[*] AppArmor profile layout successfully authored:"
cat /tmp/sample_profile
rm -f /tmp/sample_profile

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne samjha ki root user sabse powerful hone ke bawajood AppArmor aur SELinux (MAC) ke rules ko tod nahi sakta. Security policies se processes ko restricted box me rakha jata hai.
* **English:** You understand the difference between Discretionary and Mandatory Access Control, and how MAC implementations like AppArmor confine processes even if they run with root UID privileges.

---

### Level 13: Containers, Namespaces & Isolation Auditing

#### 1. Technical Concepts

* **What is a "Container"?** A container is **not** a virtual machine. There is no hypervisor or guest operating system. A container is simply a standard Linux process running directly on the host kernel, restricted by two kernel primitives:
* **Namespaces (Isolation - What it can SEE):**
* `pid`: Process IDs (Container PID 1 maps to a high PID on the host).
* `net`: Network devices, routing tables, and port allocations.
* `mnt`: Filesystem mount points.
* `ipc`: Inter-process communication and shared memory.
* `uts`: Hostname and domain name.
* `user`: Maps root in the container to a non-privileged UID on the host.


* **Control Groups / cgroups (Resource Constraints - What it can USE):** Restricts memory limits, CPU shares, disk I/O bandwidth, and maximum process counts.


* **The Container Breakout Surface:** Excessive capabilities (`--privileged`, `CAP_SYS_ADMIN`), mounted Docker sockets (`/var/run/docker.sock`), or unprotected `/proc` mounts allow containerized processes to escape into the host operating system.

```
+-------------------------------------------------------------------+
|                        HOST LINUX KERNEL                          |
|   Shared Memory Manager    Process Scheduler    Network Drivers   |
+-------------------------------------------------------------------+
           │                                         │
  [ cgroup: Max 512MB RAM ]                [ cgroup: Max 1 CPU Core ]
  [ Namespaces: pid, net, mnt ]            [ Namespaces: pid, net, mnt ]
           │                                         │
           ▼                                         ▼
   [ Container Alpha ]                       [ Container Beta ]
   (Isolated Process)                        (Isolated Process)

```

#### 2. Deep-Dive Command Specifications

* `unshare [options] [program]`: Runs a program with namespaces unshared from the parent process.
* `lsns`: Lists all active system namespaces, their types, owning PIDs, and users.
* `docker inspect <container>`: Dumps the complete JSON configuration, volume mounts, capabilities, and networking parameters of a container.

#### 3. Hands-On Lab: Building a Raw Namespace Sandbox Using `unshare`

Isolate a process namespace manually using native kernel system call utilities without Docker:

```bash
# 1. Spawn a shell inside a new PID and Mount namespace
# (Requires root permissions inside standard container/host)
if [ "$(id -u)" -eq 0 ]; then
    echo "[*] Creating an isolated PID namespace..."
    unshare --pid --mount --fork /bin/bash -c '
        mount -t proc proc /proc
        echo "Inside Namespace PID 1 View:"
        ps aux
    '
else
    echo "[-] Run this step as root/sudo on the host system to exercise unshare."
fi

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne jana ki Docker koi alag machine nahi hota, balki Linux kernel ke `Namespaces` (parde) aur `cgroups` (limits) ka use karke ek aam process ko isolated banata hai.
* **English:** You understand that containers are isolated Linux processes governed by kernel namespaces and cgroups, and can audit container configurations for dangerous privilege leaks.

---

### Level 14: Digital Forensics, Artifact Triage & Incident Response

#### 1. Technical Concepts

* **The Order of Volatility:** When a system is compromised, volatile evidence disappears first upon reboot. Evidence must be collected in order of decreasing volatility:
1. CPU registers and cache.
2. Routing tables, ARP cache, active network sockets, running processes (`/proc`).
3. Memory (RAM).
4. Temporary filesystems (`/tmp`, `/dev/shm`).
5. Disk storage metadata, logs, and persistent files.


* **Persistence Mechanisms:** Attackers maintain access via scheduled tasks (`cron`, `systemd.timers`), shell initialization files (`~/.bashrc`, `/etc/profile`), SSH keys (`~/.ssh/authorized_keys`), and rogue service units.
* **Log Tampering Indicators:** Irregular timestamp jumps, truncated log files, gaps in PID sequences, and missing log lines in `/var/log/auth.log` or `/var/log/secure`.

```
ORDER OF VOLATILITY (Collect Top to Bottom):
  [ 1. Network Sockets & Active Connections ]  <-- Lost immediately on disconnect
  [ 2. RAM & Volatile Memory State ]          <-- Lost on reboot / power-off
  [ 3. Process Execution Table & /proc ]       <-- Lost when processes terminate
  [ 4. Disk Storage, Inodes & System Logs ]   <-- Persistent across power cycles

```

#### 2. Deep-Dive Command Specifications

* `last` / `lastb`: Inspects the binary utmp/wtmp/btmp files to show successful and failed login attempts.
* `find / -mtime -2 -type f`: Locates all files modified within the last 48 hours.
* `debsums -c` (Debian/Ubuntu) or `rpm -Va` (RHEL): Verifies installed file MD5/SHA256 checksums against package vendor release signatures to detect tampered system binaries.

#### 3. Hands-On Lab: Forensic Triage of an Unauthorized System Modification

Trace an unknown file drop, find out when it arrived, inspect its inode, and discover which process wrote it:

```bash
# 1. Simulate an unauthorized dropped file
touch -d "2 days ago" /tmp/trojan.sh
chmod 777 /tmp/trojan.sh

# 2. Forensic Search: Identify anomalous executables in temporary spaces
find /tmp /var/tmp /dev/shm -type f -perm -111 -exec ls -la {} +

# 3. Perform detailed inode timeline inspection
stat /tmp/trojan.sh

# Clean up
rm -f /tmp/trojan.sh

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki jab koi system hack ya compromise hota hai, toh sabse pehle RAM aur network connections ka data kaise preserve kiya jata hai aur machine ke badle hue files ko kaise trace karte hain.
* **English:** You can triage a suspected system compromise using the Order of Volatility, extract forensic timestamps using `stat`, and audit system integrity against vendor binary checksums.

---

### Level 15: Bug Hunter Linux Flow & Structured Scope Recon

#### 1. Technical Concepts

* **Strict Scope Verification:** Professional security testing requires rigorous boundary control. Out-of-scope targets must never receive active traffic.
* **Data Normalization:** Raw tool outputs are messy. A terminal-based researcher normalizes data streams using Unix pipelines: convert to lowercase, strip trailing dots, clean protocols (`http://`), deduplicate, and sort.
* **Asset Storage Structure:**
```text
~/targets/
└── target-organization/
    ├── scope.txt               # Documented, confirmed CIDRs and domain wildcards
    ├── raw/                    # Untouched, timestamped outputs
    ├── normalized/             # Cleaned lists of IPs, hosts, endpoints
    └── evidence/               # Screenshots, response dumps, POC curl scripts

```



#### 2. Deep-Dive Command Specifications

* `anew`: Appends lines from stdin to a target file only if they don't already exist (in-stream deduplication).
* `sed -E 's#https?://##g'`: Strips protocol wrappers to isolate raw domain strings.
* `sort -u`: Sorts textual records and purges duplicate entries.

#### 3. Hands-On Lab: Building a Clean CLI Scope-Filtering Pipeline

Normalize an unformatted, duplicate-filled list of asset targets:

```bash
cat << 'EOF' > /tmp/raw_targets.txt
https://admin.example.local/
http://EXAMPLE.LOCAL:8080
admin.example.local
api.example.local/v1/test
http://api.example.local
http://example.local
EOF

# Pipeline: Strip protocols -> Remove trailing paths/slashes -> Lowercase -> Sort unique
cat /tmp/raw_targets.txt \
  | sed -E 's#https?://##' \
  | cut -d'/' -f1 \
  | cut -d':' -f1 \
  | tr '[:upper:]' '[:lower:]' \
  | sort -u

rm -f /tmp/raw_targets.txt

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki authorized bug bounty me scope kaise manage karte hain aur hazaron messy domains ko terminal pipelines ke zariye clean aur deduplicate kaise kiya jata hai.
* **English:** You can organize target scopes systematically, maintain reproducible directory trees, and construct data-cleaning pipelines that normalize target inputs across your testing workflow.

---

### Level 16: Resilient Recon Automation & Data Pipelines

#### 1. Technical Concepts

* **Rate-Limiting & Backoff:** Firing unbounded automated loops triggers target Denial-of-Service, crashes services, or results in immediate firewall IP bans. Automation must include configurable rate-limits and exponential backoff on errors.
* **Parallelization via `xargs`:** Scaling tasks safely across CPU cores without complex multithreading code:
`cat targets.txt | xargs -P 4 -n 1 ./audit_script.sh`
Runs up to 4 concurrent processes, passing 1 target per process.
* **Idempotency & State Tracking:** An automation pipeline must be safe to rerun without duplicating work or corrupting existing output files.

```
[ Input Targets ] ──► [ xargs -P 4 (Concurrency) ]
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
 [ Worker #1 ]           [ Worker #2 ]           [ Worker #3 ]
  (Target A)              (Target B)              (Target C)
       │                       │                       │
       └───────────────────────┼───────────────────────┘
                               ▼
            [ Thread-Safe Result Aggregation ]

```

#### 2. Deep-Dive Command Specifications

* `xargs -P <NUM> -I {} [cmd]`: Parallelizes CLI execution up to `NUM` concurrent worker forks.
* `timeout <DURATION> <cmd>`: Kills processes that hang past an allowable execution window, preventing pipeline deadlocks.

#### 3. Hands-On Lab: Building a Multi-Threaded HTTP Status Verifier

Write an idempotent pipeline that queries multiple local endpoints in parallel without hanging:

```bash
cat << 'EOF' > /tmp/targets.txt
127.0.0.1:80
127.0.0.1:443
127.0.0.1:3000
127.0.0.1:8080
EOF

# Process targets in parallel with a 2-second timeout per target
cat /tmp/targets.txt | xargs -P 2 -I {} bash -c '
    TARGET="{}"
    STATUS=$(curl -o /dev/null -s -w "%{http_code}" --connect-timeout 1 "http://${TARGET}" || echo "DOWN")
    echo "[PROBE] Target: ${TARGET} -> Response: ${STATUS}"
'

rm -f /tmp/targets.txt

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki bade automation scripts me parallel processing (`xargs -P`) kaise implement karte hain taaki pipeline hang na ho aur target servers par over-load na pade.
* **English:** You can design resilient automation pipelines that use controlled concurrency (`xargs`), enforce per-request timeouts, handle network errors gracefully, and maintain pipeline idempotency.

---

### Level 17: Kernel-to-Userspace Debugging Mastery

#### 1. Technical Concepts

* **The Debugging Methodology:**
1. **Symptom:** Observe the explicit failure (e.g., exit code 139, `Connection refused`, slow I/O).
2. **Evidence Collection:** Trace with `dmesg`, `strace`, `lsof`.
3. **Hypothesis:** Identify the failing subsystem (memory allocation, file access, network port).
4. **Isolation:** Re-test with a minimal reproduction command.
5. **Remediation & Validation:** Apply the fix and verify that the system returns to its normal baseline.


* **Kernel Ring Buffer (`dmesg`):** Stores low-level kernel log messages: Out-of-Memory (OOM) killer events, page faults, storage controller resets, and hardware link changes.
* **Tracing Tools:**
* `strace`: Intercepts system calls made to the kernel.
* `ltrace`: Intercepts calls made to userspace dynamic shared C libraries (`glibc`).
* `gdb`: The GNU Project Debugger. Inspects memory, registers, stack traces, and core dumps.



```
Application Crashes!
         │
         ▼
[ Step 1: dmesg -T | tail ] ──► Did OOM killer or Segfault occur?
         │
         ▼
[ Step 2: strace -f -e trace=file <binary> ] ──► Did an openat/access call return ENOENT or EACCES?
         │
         ▼
[ Step 3: lsof / ss ] ──► Are network sockets or file descriptors exhausted?

```

#### 2. Deep-Dive Command Specifications

* `strace -p <PID> -f`: Attaches dynamically to an already-running process and follows all child threads (`-f`).
* `dmesg -T --level=err,warn`: Displays timestamped, high-priority kernel warnings and error events.
* `gdb -batch -ex "bt" -c <core_file> <binary>`: Extracts an instant stack backtrace from a generated core dump file.

#### 3. Hands-On Lab: Diagnosing a Silent File Access Failure via `strace`

Trace an uncompiled script that fails silently to find out exactly which configuration file it cannot access:

```bash
# 1. Create a script that exits silently due to a missing dependency
cat << 'EOF' > /tmp/faulty_app.sh
#!/usr/bin/env bash
if [ ! -f /etc/secret_app.conf ]; then
    exit 1
fi
echo "Application running successfully"
EOF
chmod +x /tmp/faulty_app.sh

# 2. Execute directly (fails silently with exit code 1)
/tmp/faulty_app.sh || echo "Failed silently with code $?"

# 3. Intercept system calls to identify the root cause
strace -e trace=openat,access /tmp/faulty_app.sh 2>&1 | grep -i "secret_app"

# 4. Apply remediation and verify
touch /etc/secret_app.conf
/tmp/faulty_app.sh

# Clean up
rm -f /tmp/faulty_app.sh /etc/secret_app.conf

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Jab koi program bina error message diye band ho jata hai, tab andaza lagane ke bajay `strace` se trace karke 10 second me pata lagaya ja sakta hai ki konsi file gayab hai ya permission denied hai.
* **English:** You can debug crashing or silently failing applications systematically using `strace` to intercept failing system calls, and diagnose kernel-level issues via `dmesg`.

---

### Level 18: Binary Analysis, Dynamic Linking & ELF Internals

#### 1. Technical Concepts

* **The ELF (Executable and Linkable Format) Standard:** The standard binary file format for executables, object code, shared libraries, and core dumps in Linux.
* **ELF Header:** Identifies binary architecture (32/64-bit), endianness, entry point memory address, and target operating system ABI.
* **Program Headers:** Instruct the kernel's memory management subsystem how to map segments into virtual memory (`LOAD`, `DYNAMIC`, `GNU_STACK`).
* **Section Headers:** Internal organization for compilers and linkers (`.text` for machine code instructions, `.data` for initialized variables, `.rodata` for read-only strings, `.bss` for uninitialized data).


* **Dynamic Linking & The Dynamic Linker (`ld.so`):** Most programs do not bundle their own standard library code. When executed, `/lib64/ld-linux-x86-64.so.2` reads the binary's `DT_NEEDED` entries, loads required shared objects (`.so`) into memory, and resolves symbol addresses.

```
ELF BINARY STRUCTURE:
+-----------------------------------------------------------+
| ELF Header (Magic Bytes: 7f 45 4c 46, Arch, Entry Point)   |
+-----------------------------------------------------------+
| Program Headers (Segments: LOAD, DYNAMIC, GNU_STACK)      |
+-----------------------------------------------------------+
| Sections:                                                 |
|   .text   : Executable machine code instructions          |
|   .rodata : Hardcoded string constants ("Welcome", keys)  |
|   .data   : Global initialized variables                  |
+-----------------------------------------------------------+
| Section Header Table (Symbol Table references)            |
+-----------------------------------------------------------+

```

#### 2. Deep-Dive Command Specifications

* `file [binary]`: Reads magic bytes in the header to identify file architecture, linking type (static/dynamic), and whether debugging symbols have been stripped.
* `readelf -h -l -S [binary]`: Dumps ELF headers, program segment mappings, and internal section tables.
* `ldd [binary]`: Displays dynamic shared library dependencies resolved by the runtime dynamic linker.
* `strings -a [binary]`: Dumps all human-readable ASCII/Unicode strings embedded across both data and code sections.
* `nm -D [binary]`: Displays symbols exported or imported in the dynamic symbol table.

#### 3. Hands-On Lab: Reverse Engineering Hardcoded Tokens from an ELF Binary

Compile a simple C binary, extract its dynamic library dependencies, and uncover embedded secrets without compiling with debug symbols:

```bash
# 1. Author and compile a minimal native binary
cat << 'EOF' > /tmp/auth_gate.c
#include <stdio.h>
#include <string.h>

static const char* INTERNAL_SECRET = "SEC_TOKEN_4291_SUPER_SECRET";

int main(int argc, char** argv) {
    if (argc > 1 && strcmp(argv[1], INTERNAL_SECRET) == 0) {
        printf("[+] Access Granted.\n");
        return 0;
    }
    printf("[-] Access Denied.\n");
    return 1;
}
EOF

gcc -O2 -s /tmp/auth_gate.c -o /tmp/auth_gate # Stripped binary!

# 2. Inspect binary architecture and dynamic dependencies
file /tmp/auth_gate
ldd /tmp/auth_gate

# 3. Perform string extraction to uncover embedded tokens without running the binary
strings -a /tmp/auth_gate | grep "SEC_TOKEN"

# 4. Verify discovered secret against the binary
/tmp/auth_gate "SEC_TOKEN_4291_SUPER_SECRET"

# Clean up
rm -f /tmp/auth_gate.c /tmp/auth_gate

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki Linux binaries (ELF files) andar se kaise kaam karti hain. `strings`, `ldd`, aur `readelf` ka use karke binary run kiye bina uske hardcoded tokens aur dynamic libraries ko kaise extract karte hain.
* **English:** You understand the internal structure of ELF executables and can extract hardcoded secrets, dependencies, and dynamic symbols safely using static analysis utilities like `strings`, `ldd`, and `readelf`.

---

### Level 19: Secure Coding, Script Auditing & Privilege Safety

#### 1. Technical Concepts

* **Common Shell Injection Vulnerabilities:**
* **Unquoted Variables:** Passing unquoted arguments to commands triggers word-splitting and glob expansion, allowing users to pass unintended CLI flags or filenames containing spaces.
* **Command Injection via Eval / Backticks:** Executing shell evaluation directly on unvetted user input:
`eval "echo $USER_INPUT"` allows an input of `; rm -rf /` to execute arbitrary commands.
* **Path Hijacking:** Relying on relative binary calls (e.g., `system("service restart")` instead of `/usr/sbin/service`) allows an attacker with write access to a directory in `$PATH` to drop a malicious binary that executes with the caller's privileges.
* **Insecure Temporary File Creation:** Using fixed names like `/tmp/temp.txt` introduces symlink race-condition vulnerabilities.



```
VULNERABLE:
eval "cat /var/data/$1"
Attacker Input: "file.txt; id"
Result: Executes 'cat /var/data/file.txt' followed immediately by 'id'!

SECURE:
# Validate that the input contains ONLY alphanumeric characters
if [[ ! "$1" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    echo "Invalid input parameter" >&2
    exit 1
fi
cat -- "/var/data/$1"

```

#### 2. Deep-Dive Command Specifications

* `shellcheck [script.sh]`: High-performance static analysis tool for shell scripts. Identifies syntax errors, quoting bugs, race conditions, and security smells.
* `bash -n [script.sh]`: Validates syntax without executing the script.

#### 3. Hands-On Lab: Auditing, Exploiting, and Patching an Unsafe Bash Script

Review a vulnerable administrative script, demonstrate how it can be abused in a sandbox, and rewrite it securely:

```bash
# 1. Author an intentionally flawed administration script
cat << 'EOF' > /tmp/insecure_reader.sh
#!/usr/bin/env bash
# Vulnerable: Insecure quoting and path usage
cat /tmp/data/$1
EOF
chmod +x /tmp/insecure_reader.sh
mkdir -p /tmp/data && echo "Normal Data" > /tmp/data/report.txt

# 2. Demonstrate path traversal abuse
/tmp/insecure_reader.sh "../../etc/passwd" | head -n 3

# 3. Author the hardened version
cat << 'EOF' > /tmp/secure_reader.sh
#!/usr/bin/env bash
set -euo pipefail

# Whitelist validation: Restrict input strictly to safe alphanumeric filenames
INPUT_FILE="${1:?Error: Filename argument required}"
if [[ ! "${INPUT_FILE}" =~ ^[a-zA-Z0-9_.-]+$ ]]; then
    echo "[-] Security Violation: Illegal characters detected." >&2
    exit 1
fi

TARGET_PATH="/tmp/data/${INPUT_FILE}"
if [ ! -f "${TARGET_PATH}" ]; then
    echo "[-] File not found: ${TARGET_PATH}" >&2
    exit 1
fi

cat -- "${TARGET_PATH}"
EOF
chmod +x /tmp/secure_reader.sh

# 4. Verify that the traversal attack is blocked
/tmp/secure_reader.sh "../../etc/passwd" || echo "[+] Attack successfully blocked by input validation!"

# Clean up
rm -rf /tmp/data /tmp/insecure_reader.sh /tmp/secure_reader.sh

```

#### 4. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne seekha ki Bash scripts me security bugs (jaise Path Traversal aur Command Injection) kaise aate hain, unhe exploit karke proof-of-concept kaise banate hain, aur Regex validation se unhe patch kaise karte hain.
* **English:** You can identify common shell script security vulnerabilities (injection, unquoted expansions, path traversal), demonstrate their real-world exploitability, and refactor code to adhere to secure defensive standards.

---

### Level 20: Full-Spectrum Multi-Host Assessment Capstone

#### 1. Mission Overview

In this level, you combine everything you have learned: networking, permissions, processes, pipelines, debugging, and secure workflows. You are given access to the `mastery_auditor` workstation container and tasked with auditing the isolated target server (`mastery_target`) on the internal bridge network (`172.28.0.20`).

#### 2. Rules of Engagement & Boundaries

* **In-Scope:** The `172.28.0.0/16` subnet only.
* **Out-of-Scope:** Host physical interfaces, home Wi-Fi networks, default gateway routing to public IP addresses.
* **Objective:** Map services, isolate misconfigurations, verify operational stability, remediate identified weaknesses, and submit a reproducible engineering report.

```
                                  [ ASSESSMENT SCOPE ]
                     (Private Docker Bridge: 172.28.0.0/16)
                                        │
           ┌────────────────────────────┴────────────────────────────┐
           ▼                                                         ▼
┌──────────────────────┐                                  ┌──────────────────────┐
│   mastery_auditor    │                                  │    mastery_target    │
│    (172.28.0.10)     │ ───[ Map Ports & SUID Perms ]──► │    (172.28.0.20)     │
│ Workstation / Tester │ ◄──[ Return Forensic Audit ]──── │ Vulnerable Lab Node  │
└──────────────────────┘                                  └──────────────────────┘

```

#### 3. Step-by-Step Hands-On Execution

From inside the `mastery_auditor` container:

```bash
# 1. Discover active services on the target without external scanners
python3 -c '
import socket
target = "172.28.0.20"
for port in [21, 22, 80, 443, 3000, 8080]:
    s = socket.socket()
    s.settimeout(0.3)
    if s.connect_ex((target, port)) == 0:
        print(f"[DISCOVERY] Found open port {port} on {target}")
    s.close()
'

# 2. Connect to the target node via authorized SSH/exec and audit for SUID vulnerabilities
# (Simulated execution on the target node)
ssh user@172.28.0.20 "find / -perm -4000 -type f 2>/dev/null"

# 3. Identify failing services via journalctl logs
ssh user@172.28.0.20 "systemctl --failed --no-pager"

# 4. Generate structured incident report summarizing findings

```

#### 4. Deliverable Format (Professional Engineering Report)

Every finding must be documented using the following template:

```text
===================================================================
FINDING REPORT: MISCONFIGURED CAPABILITIES / UNNECESSARY PRIVILEGE
===================================================================
Target Node      : 172.28.0.20 (mastery_target)
Severity         : HIGH
Subsystem        : Local Filesystem Permissions / SUID

1. EXECUTIVE SUMMARY:
   A custom binary was found configured with the SetUID bit set to
   root UID 0, allowing unprivileged local users to perform arbitrary
   file overrides.

2. AFFECTED ASSETS:
   - File Path: /usr/local/bin/legacy_backup
   - Permissions: -rwsr-xr-x 1 root root

3. PROOF OF CONCEPT / MINIMAL REPRODUCTION:
   Executing '/usr/local/bin/legacy_backup' as user 'operator' allows
   arbitrary file reads from /etc/shadow without validation.

4. ROOT CAUSE ANALYSIS:
   The build pipeline applied octal mode 4755 instead of restricting
   capabilities via setcap.

5. REMEDIATION PLAN:
   Execute: chmod u-s /usr/local/bin/legacy_backup
   Apply granular capability if network access is required:
   setcap cap_net_bind_service=+ep /usr/local/bin/legacy_backup

6. POST-FIX VERIFICATION:
   Verified with 'getcap' and re-tested execution as unprivileged user.
===================================================================

```

#### 5. आपने क्या सीखा / What You Learned

* **Hindi:** Aapne single commands se nikal kar ek pure enterprise target ka comprehensive audit karna seekha: discovery se shuru karke, misconfiguration dhoondhna, fix verify karna aur professional security report likhna.
* **English:** You can execute end-to-end security and operational assessments across segmented systems, collect evidence without breaking environments, apply remediation, and author professional engineering reports.

---

### Level 21: The "Host-Ready" Operational Certification Standard

The final level is not a multiple-choice quiz or a command memorization exam. It is a **zero-guidance practical validation test**.

You are dropped onto a fresh, unfamiliar Linux system with no cheat sheets and no step-by-step instructions. You must complete **Seven Core Missions** independently using only native system tools, manual pages (`man`), `--help` flags, `/proc`, and your own systematic troubleshooting methodology.

```
THE 7 MISSIONS OF HOST-READY MASTERY:
  Mission 1: System Discovery & Architectural Fingerprinting
  Mission 2: Storage & Filesystem Forensics
  Mission 3: Process Topology & Resource Isolation
  Mission 4: Network Socket Forensics & Path Debugging
  Mission 5: Service Failure Root-Cause Analysis
  Mission 6: High-Volume Log Wrangling & Pipeline Synthesis
  Mission 7: Live Application Tracing & Patch Verification

```

---

#### Mission 1: System Discovery & Architectural Fingerprinting

**Challenge:** Without using a graphical interface or reading external tutorials, determine the exact state of the running operating system.

* What is the kernel release and CPU architecture?
* What Linux distribution and release version is installed?
* Is the kernel running in a virtualized container or on bare metal?
* What is the system hostname and system time synchronization status?

**Validation Commands:**

```bash
uname -srm
cat /etc/os-release
systemd-detect-virt || cat /proc/1/cgroup
timedatectl status || date

```

---

#### Mission 2: Storage & Filesystem Forensics

**Challenge:** A server alert warns that "Disk space is exhausted." Upon logging in, `df -h` shows the disk is only 40% full, but applications are crashing with `No space left on device` errors when trying to write files.

* Determine whether disk storage blocks or **inodes** are exhausted.
* Locate the directory holding millions of zero-byte files consuming the inode table.
* Clean up the directory without hanging the shell with `rm *` (which fails with `Argument list too long`).

**Validation Commands:**

```bash
# Check inode saturation
df -i /

# Locate directory consuming inodes
find / -xdev -printf '%h\n' | sort | uniq -c | sort -k1 -n | tail -n 5

# Safe deletion of millions of small files via xargs (avoids shell argument limits)
find /var/spool/bad_queue/ -type f -print0 | xargs -0 -P 4 rm -f

```

---

#### Mission 3: Process Topology & Resource Isolation

**Challenge:** An unknown process is consuming 100% of a CPU core, but when you run `top`, the process name appears as a disguised string (`kworker/0:1`).

* Trace the actual binary behind the disguised process name.
* Identify the parent process (`PPID`) that spawned it.
* Determine what network connections or open files this process currently maintains.
* Terminate the entire process tree cleanly.

**Validation Commands:**

```bash
# Locate PID of the high-CPU process
SUSPECT_PID=$(pgrep -f "kworker/0:1")

# Extract the real executable path from kernel descriptors
ls -l /proc/$SUSPECT_PID/exe
cat /proc/$SUSPECT_PID/cmdline | tr '\0' ' '; echo

# Identify parent and open resources
ps -o pid,ppid,user,cmd -p $SUSPECT_PID
lsof -p $SUSPECT_PID

# Terminate process and parent
kill -15 $SUSPECT_PID

```

---

#### Mission 4: Network Socket Forensics & Path Debugging

**Challenge:** The host can ping external IP addresses (e.g., `1.1.1.1`), but any command attempting to resolve domain names (`curl example.com`) fails with `Could not resolve host`.

* Is the problem physical interface down, routing table, or DNS resolution?
* Inspect `/etc/resolv.conf` and active systemd-resolved socket status.
* Fix the DNS resolution path and verify end-to-end connectivity.

**Validation Commands:**

```bash
# Isolate layer: Interface -> IP -> Gateway -> DNS
ip link show
ip route show
cat /etc/resolv.conf
resolvectl status 2>/dev/null || true

# Test explicit nameserver query directly bypassing local cache
dig @1.1.1.1 example.com +short

```

---

#### Mission 5: Service Failure Root-Cause Analysis

**Challenge:** A mission-critical background service (`database-sync.service`) is in a crash loop (`activating (auto-restart)`). No clear error was printed to the terminal.

* Extract the service unit configuration file location.
* Inspect the systemd journal for the exact exit code and stderr output from the last crash.
* Resolve the missing directory or permission misconfiguration and restore the service to an active, running state.

**Validation Commands:**

```bash
# Check unit status and crash cycle
systemctl status database-sync.service --no-pager

# Pull exact stderr output from journal buffer
journalctl -u database-sync.service -b -e --no-pager

# Fix root cause (e.g., missing permissions on target directory)
chown -R serviceuser:serviceuser /var/lib/database-sync
systemctl restart database-sync.service
systemctl is-active database-sync.service

```

---

#### Mission 6: High-Volume Log Wrangling & Pipeline Synthesis

**Challenge:** You are handed an unformatted, multi-gigabyte Apache/Nginx access log file (`access.log`). Without writing a Python or Perl script, construct a single terminal pipeline to extract the top 5 most attacked URL paths (requests returning HTTP 401 or 403 status codes).

**Validation Commands:**

```bash
cat /var/log/nginx/access.log \
  | awk '($9 ~ /401|403/) {print $7}' \
  | sort \
  | uniq -c \
  | sort -nr \
  | head -n 5

```

---

#### Mission 7: Live Application Tracing & Patch Verification

**Challenge:** An internally authored C binary crashes with `Segmentation fault (core dumped)` immediately upon execution on the host. You do not have the source code.

* Intercept the binary's system calls using `strace`.
* Identify whether the crash is caused by an environmental variable missing, an inaccessible library, or an invalid memory pointer dereference.
* Fix the environment and verify the binary executes to completion with exit code `0`.

**Validation Commands:**

```bash
# Run binary under system call tracing
strace -f -e trace=file,read,write ./mystery_binary

# Check memory fault details via kernel ring buffer
dmesg -T | tail -n 5

# Provide missing environment configuration indicated by failed openat call
export APP_CONFIG_PATH="/etc/app.conf"
./mystery_binary && echo "Execution succeeded cleanly!"

```

---

#### The Host-Ready Standard — Final Verification

You are considered **Host-Ready** when you no longer ask:

> *"What was that command again?"*

And instead approach any system with the engineer's mindset:

> *"I will inspect the system state, trace the system calls, read the documentation via `man` and `--help`, and isolate the root cause systematically."*

---

## 9. Automated Infrastructure Code (Docker Compose & Shell)

### Complete `lab-environment/docker-compose.yml`

This file builds and coordinates the air-gapped lab environment:

```yaml
version: '3.8'

networks:
  sandbox_net:
    name: sandbox_net
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.28.0.0/16
          gateway: 172.28.0.1

volumes:
  shared_workspace:
    name: mastery_shared_workspace

services:
  # -------------------------------------------------------------
  # 1. PRIMARY AUDITING & ANALYSIS WORKSTATION
  # -------------------------------------------------------------
  auditor:
    build:
      context: ./auditor
      dockerfile: Dockerfile
    container_name: mastery_auditor
    hostname: auditor-workstation
    networks:
      sandbox_net:
        ipv4_address: 172.28.0.10
    volumes:
      - shared_workspace:/workspace
    stdin_open: true
    tty: true
    cap_add:
      - SYS_PTRACE
      - NET_ADMIN
    security_opt:
      - seccomp:unconfined
    command: /bin/bash

  # -------------------------------------------------------------
  # 2. INTENTIONALLY MISCONFIGURED TARGET NODE (BREAK-FIX)
  # -------------------------------------------------------------
  target:
    build:
      context: ./target
      dockerfile: Dockerfile
    container_name: mastery_target
    hostname: vulnerable-server
    networks:
      sandbox_net:
        ipv4_address: 172.28.0.20
    volumes:
      - shared_workspace:/workspace
    privileged: false
    cap_add:
      - CHOWN
      - SETUID
      - SETGID
      - DAC_OVERRIDE
    command: /entrypoint.sh

  # -------------------------------------------------------------
  # 3. LOCAL MOCK APPLICATION SERVER (API & WEB TARGET)
  # -------------------------------------------------------------
  webapp:
    build:
      context: ./webapp
      dockerfile: Dockerfile
    container_name: mastery_webapp
    hostname: webapp-internal
    networks:
      sandbox_net:
        ipv4_address: 172.28.0.30
    ports:
      - "127.0.0.1:3000:3000"
    volumes:
      - shared_workspace:/workspace

```

---

### Auditing Station Image (`lab-environment/auditor/Dockerfile`)

```dockerfile
FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm-256color

# Install complete forensic, diagnostic, network, and automation tooling
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    iproute2 \
    iputils-ping \
    dnsutils \
    net-tools \
    curl \
    wget \
    tcpdump \
    tshark \
    lsof \
    strace \
    ltrace \
    procps \
    htop \
    mc \
    git \
    vim \
    nano \
    jq \
    python3 \
    python3-pip \
    bsdmainutils \
    ca-certificates \
    file \
    binutils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

CMD ["/bin/bash"]

```

---

### Target Server Image (`lab-environment/target/Dockerfile`)

```dockerfile
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    iproute2 \
    iputils-ping \
    net-tools \
    curl \
    python3 \
    openssh-server \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Inject intentionally vulnerable user accounts and configurations
RUN useradd -m -s /bin/bash operator && \
    echo "operator:operator123" | chpasswd && \
    useradd -m -s /bin/bash auditor && \
    echo "auditor:auditor123" | chpasswd

# Setup entrypoint orchestration script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 22 80

ENTRYPOINT ["/entrypoint.sh"]

```

---

### Target Server Orchestration Entrypoint (`lab-environment/target/entrypoint.sh`)

```bash
#!/usr/bin/env bash
set -e

echo "[*] Initializing Intentional Break-Fix Scenarios on Target..."

# 1. Setup intentional SUID vulnerability for Level 3 & Level 20 auditing
cp /bin/cp /usr/local/bin/backup_cp
chmod 4755 /usr/local/bin/backup_cp

# 2. Setup intentionally insecure world-writable file in /etc
echo "SYSTEM_FLAG_STATUS=UNLOCKED" > /etc/system_status.conf
chmod 666 /etc/system_status.conf

# 3. Create SSH daemon host keys and runtime directories
mkdir -p /var/run/sshd
ssh-keygen -A

# Start SSH service in background
/usr/sbin/sshd

echo "[+] Target Ready. Bound to sandbox network at 172.28.0.20."
# Keep container alive
exec tail -f /dev/null

```

---

### Application Target (`lab-environment/webapp/Dockerfile`)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN echo 'from http.server import HTTPServer, BaseHTTPRequestHandler\n\
import json\n\
class App(BaseHTTPRequestHandler):\n\
    def do_GET(self):\n\
        self.send_response(200)\n\
        self.send_header("Content-Type", "application/json")\n\
        self.end_headers()\n\
        self.wfile.write(json.dumps({"app":"Linux-Mastery-Lab","status":"healthy","endpoints":["/api/users","/api/audit"]}).encode())\n\
HTTPServer(("0.0.0.0", 3000), App).serve_forever()' > server.py

EXPOSE 3000

CMD ["python3", "server.py"]

```

---

## 10. Dual-Platform Deployment Engineering (GitHub Pages & Netlify)

This repository is designed to be hosted **100% free** as a static documentation and learning dashboard on either Netlify or GitHub Pages with zero build steps.

### Production Configuration: `netlify.toml`

Place this file in the root directory:

```toml
[build]
  publish = "."
  command = ""

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Content-Security-Policy = "default-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net;"

```

---

### Production Configuration: `.github/workflows/deploy.yml`

Place this file at `.github/workflows/deploy.yml` to automate GitHub Pages deployments on push:

```yaml
name: Deploy Static Documentation to GitHub Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup GitHub Pages Engine
        uses: actions/configure-pages@v4

      - name: Upload Static Artifacts
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4

```

---

### Zero-Framework Frontend: `index.html`

Place this complete, self-contained file in the repository root:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Production Linux Engineering & Security Mastery Curriculum">
  <title>Linux Mastery | Enterprise Security Engineering</title>
  <style>
    :root {
      --bg-primary: #0a0e14;
      --bg-surface: #111822;
      --border-color: #232d3d;
      --accent-green: #00e676;
      --accent-blue: #00b0ff;
      --text-main: #d1d5db;
      --text-muted: #8b949e;
      --text-heading: #f9fafb;
      --code-bg: #05080c;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.6;
      padding: 30px 20px;
    }
    .wrapper { max-width: 1100px; margin: 0 auto; }
    header {
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 25px;
      margin-bottom: 35px;
    }
    h1 { color: var(--text-heading); font-size: 2.2rem; margin-bottom: 10px; }
    .badge {
      display: inline-block;
      background: var(--accent-green);
      color: #000;
      font-weight: 700;
      font-size: 0.8rem;
      padding: 3px 10px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    .status-bar {
      display: flex;
      gap: 20px;
      margin-top: 15px;
      font-size: 0.9rem;
      color: var(--text-muted);
    }
    .level-block {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      margin-bottom: 18px;
      transition: border-color 0.2s;
    }
    .level-block:hover { border-color: var(--accent-blue); }
    .level-header {
      padding: 18px 22px;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
    }
    .level-header h3 { font-size: 1.15rem; color: var(--text-heading); }
    .level-content {
      display: none;
      padding: 0 22px 22px 22px;
      border-top: 1px solid var(--border-color);
      margin-top: 10px;
      padding-top: 15px;
    }
    .level-block.active .level-content { display: block; }
    pre {
      background: var(--code-bg);
      border: 1px solid var(--border-color);
      padding: 14px;
      border-radius: 4px;
      overflow-x: auto;
      margin: 12px 0;
      color: var(--accent-green);
      font-family: "Courier New", Courier, monospace;
      font-size: 0.9rem;
    }
    ul { padding-left: 20px; margin: 10px 0; }
    li { margin-bottom: 6px; }
  </style>
</head>
<body>
  <div class="wrapper">
    <header>
      <span class="badge">Air-Gapped Sandbox Architecture</span>
      <h1>Linux-Mastery Engineering Curriculum</h1>
      <p>From Visual Foundations to Enterprise Linux Security Engineering and Diagnostic Mastery.</p>
      <div class="status-bar">
        <span>Curriculum: 23 Levels Total</span>
        <span>Environment: 3 Isolated Local Nodes</span>
        <span>Build Dependency: Zero</span>
      </div>
    </header>

    <main id="levels-container">
      <!-- LEVEL -1 -->
      <div class="level-block active">
        <div class="level-header" onclick="this.parentElement.classList.toggle('active')">
          <h3>Level -1: Junior Explorer (Visual-First System Exploration)</h3>
          <span>▼</span>
        </div>
        <div class="level-content">
          <p>Learn the operating system through visual file managers and live process monitors before typing complex commands blind.</p>
          <pre><code># Launch visual terminal file manager
mc

# Launch visual interactive process monitor
htop</code></pre>
          <ul>
            <li><strong>Intuition:</strong> Directories are rooms, files are physical books, the kernel is the chief librarian.</li>
            <li><strong>Visual Data Flow:</strong> Use Midnight Commander (`mc`) to observe the Linux tree and `htop` to observe process execution states visually.</li>
          </ul>
        </div>
      </div>

      <!-- LEVEL 6 -->
      <div class="level-block">
        <div class="level-header" onclick="this.parentElement.classList.toggle('active')">
          <h3>Level 6: Core Networking, Packet Analysis & Sockets</h3>
          <span>▼</span>
        </div>
        <div class="level-content">
          <p>Inspect the TCP 3-way handshake and analyze raw network frames over the wire.</p>
          <pre><code># Inspect all listening numeric TCP/UDP sockets with process attribution
ss -tulpn

# Capture raw packets on the loopback interface without reverse DNS resolution
sudo tcpdump -i any -nn -vv "port 80 or port 3000"</code></pre>
        </div>
      </div>

      <!-- LEVEL 21 -->
      <div class="level-block">
        <div class="level-header" onclick="this.parentElement.classList.toggle('active')">
          <h3>Level 21: The "Host-Ready" Operational Certification Standard</h3>
          <span>▼</span>
        </div>
        <div class="level-content">
          <p>Execute the Seven Core Missions on an unfamiliar host without cheat sheets or step-by-step guides.</p>
          <pre><code># Mission 1: Host identification and virtualization check
uname -srm && cat /etc/os-release && systemd-detect-virt

# Mission 4: Verify complete DNS path resolution directly
dig @1.1.1.1 example.com +short</code></pre>
        </div>
      </div>
    </main>
  </div>
</body>
</html>

```

---

## 11. Verification Scripts & Automated Test Suite

### Host Sanity & Environment Checker (`scripts/test-sandbox.sh`)

Save this file as `scripts/test-sandbox.sh` and make it executable (`chmod +x scripts/test-sandbox.sh`):

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "========================================================="
echo "   Linux-Mastery: Host Environment Diagnostic Verifier   "
echo "========================================================="

MISSING_TOOLS=0
REQUIRED_BINARIES=(
    "git"
    "curl"
    "python3"
    "docker"
    "strace"
    "lsof"
    "tcpdump"
    "jq"
)

echo "[*] Checking host utility dependencies..."
for bin in "${REQUIRED_BINARIES[@]}"; do
    if command -v "$bin" &> /dev/null; then
        echo "  [✔] Found: $bin ($(command -v "$bin"))"
    else
        echo "  [✘] MISSING: $bin"
        MISSING_TOOLS=$((MISSING_TOOLS + 1))
    fi
done

echo "---------------------------------------------------------"
echo "[*] Checking container virtualization service..."
if command -v docker &> /dev/null; then
    if docker info &> /dev/null; then
        echo "  [✔] Docker daemon is running and accessible."
    else
        echo "  [✘] Docker is installed, but the daemon is not running or your user is not in the 'docker' group."
        MISSING_TOOLS=$((MISSING_TOOLS + 1))
    fi
else
    echo "  [✘] Docker binary not found."
    MISSING_TOOLS=$((MISSING_TOOLS + 1))
fi

echo "---------------------------------------------------------"
if [ "$MISSING_TOOLS" -eq 0 ]; then
    echo "[SUCCESS] Host system is fully qualified to run all 23 levels of Linux-Mastery!"
    exit 0
else
    echo "[FAILURE] $MISSING_TOOLS requirements are unfulfilled. Install the missing packages and re-run this check."
    exit 1
fi

```

---

### Automated Host Audit Script (`scripts/sysaudit.sh`)

Save this file as `scripts/sysaudit.sh` and make it executable (`chmod +x scripts/sysaudit.sh`):

```bash
#!/usr/bin/env bash
# ==============================================================================
# Script Name : sysaudit.sh
# Purpose     : Autonomous Linux Host Profiling & Incident Diagnostic Collector
# Standards   : POSIX Compliant, Defensive (set -euo pipefail), Zero External Dep
# ==============================================================================

set -euo pipefail

# Guarantee exclusive temporary execution workspace
AUDIT_RUN_ID=$(date +%Y%m%d_%H%M%S)
AUDIT_DIR=$(mktemp -d "/tmp/sysaudit_${AUDIT_RUN_ID}.XXXXXX")

# Register signal trap to bundle output into a tar archive and clean scratch data
cleanup() {
    local exit_code=$?
    if [ -d "${AUDIT_DIR}" ]; then
        if [ "$exit_code" -eq 0 ]; then
            TAR_FILE="/tmp/audit_report_${AUDIT_RUN_ID}.tar.gz"
            tar -czf "${TAR_FILE}" -C "${AUDIT_DIR}" .
            echo "[*] Audit completed successfully. Archive: ${TAR_FILE}"
        else
            echo "[!] Audit aborted unexpectedly with error code: ${exit_code}" >&2
        fi
        rm -rf "${AUDIT_DIR}"
    fi
    exit "${exit_code}"
}
trap cleanup EXIT INT TERM

echo "[*] Initiating System Audit. Staging in: ${AUDIT_DIR}"

# 1. Hardware & Operating System Architecture
mkdir -p "${AUDIT_DIR}/system"
uname -a > "${AUDIT_DIR}/system/kernel_uname.txt"
uptime > "${AUDIT_DIR}/system/uptime.txt"
[ -f /etc/os-release ] && cp /etc/os-release "${AUDIT_DIR}/system/os-release.txt"
cat /proc/cpuinfo > "${AUDIT_DIR}/system/cpuinfo.txt"
cat /proc/meminfo > "${AUDIT_DIR}/system/meminfo.txt"

# 2. Filesystem Mounts, Disks & Inode Health
mkdir -p "${AUDIT_DIR}/storage"
df -h > "${AUDIT_DIR}/storage/disk_space.txt"
df -i > "${AUDIT_DIR}/storage/disk_inodes.txt"
mount > "${AUDIT_DIR}/storage/mounts.txt"

# 3. Process Table & Execution Runtime
mkdir -p "${AUDIT_DIR}/processes"
ps aux > "${AUDIT_DIR}/processes/ps_aux.txt"

# 4. Networking, Active Sockets & Routing
mkdir -p "${AUDIT_DIR}/network"
ip a > "${AUDIT_DIR}/network/interfaces.txt"
ip r > "${AUDIT_DIR}/network/routing_table.txt"
if command -v ss &>/dev/null; then
    ss -tulpn > "${AUDIT_DIR}/network/listening_sockets.txt"
fi

# 5. Security & Privilege Boundaries
mkdir -p "${AUDIT_DIR}/security"
# Identify all SUID files across standard system paths safely
find / -xdev -perm -4000 -type f -exec ls -la {} + 2>/dev/null > "${AUDIT_DIR}/security/suid_files.txt" || true
# Identify world-writable files in /etc
find /etc -type f -perm -0002 -exec ls -la {} + 2>/dev/null > "${AUDIT_DIR}/security/world_writable_etc.txt" || true

echo "[+] Data collection complete. Finalizing archive package..."

```

---

## 12. Contribution Governance & Engineering Rigor

Contributions to the **Linux-Mastery** framework must meet the following technical standards:

1. **Deterministic Reproducibility:** Every lab, break-fix scenario, or exercise must run out-of-the-box using the standard `docker compose up` command. Mocks, simulated shells, and non-reproducible external web links are rejected.
2. **Strict Static Analysis Compliance:** All submitted shell scripts must pass `shellcheck` with zero warnings before merging.
3. **Bilingual Learning Artifacts:** Every new curriculum level or exercise update must conclude with a structured, bilingual **What You Learned / आपने क्या सीखा** summary.
4. **Defensive Rigor First:** Automation scripts must use defensive mechanisms: `set -euo pipefail`, explicit parameter boundaries, signal traps (`trap`), and input sanitization against shell injection.
5. **Ethical Scope Integrity:** Labs must remain 100% self-contained on the internal container bridge network. Code intended to target, scan, or probe external third-party infrastructure will not be accepted.
