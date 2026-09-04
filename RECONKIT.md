# ReconKit — single-file client-side recon suite 🔧

Ek hi HTML file. Zero backend. Zero API keys. Zero dependencies.
Poora recon + pentest toolkit apni website me embed karo — sab kuch **client-side** chalta hai.

## 📦 Files

| File | Kaam |
|---|---|
| `reconkit.html` | Poora tool — isko apni site pe rakhna hai (bas ek file) |
| `README.md` | Yeh file |

## 🔗 Apni website me integrate karna (2 lines)

`reconkit.html` apne server pe rakho (jahan bhi ho), phir apni site me:

```html
<iframe src="/reconkit.html" style="width:100%;height:900px;border:0"
        allow="microphone; fullscreen"></iframe>
```

Bas. Koi JS/CSS import nahi, koi build nahi, koi server-side code nahi.

## ⚡ Features

### 🌐 Recon 360 (domain daalo, sab chalta hai)
- DNS (A/AAAA/MX/NS/TXT/CAA/SOA) — dns.google + cloudflare DoH
- SPF / DMARC / DKIM checks + email security score
- WHOIS via **RDAP** (rdap.org + IANA bootstrap — free, no key)
- Certificate Transparency subdomains (crt.sh)
- ASN + GeoIP (Cymru DNS + ip-api/ipinfo/ipapi fallback)
- Wayback Machine history

### 🔎 Subdomain brute force
- 300+ wordlist built-in (ya apna paste karo)
- DoH se live-check, CSV export

### 🕸 Site Scan
- Headers + security checks (HSTS, CSP, nosniff, clickjacking... + score)
- Tech/WAF detection
- 80+ secret paths fuzz (.env, .git, backups, API endpoints...)
- Source se **secret extraction** (AWS keys, API keys, tokens)
- **Google Maps API key** detection + verification
- robots.txt + sitemap parse

### 🔑 JWT Lab
- Decode + claim audit (exp/iss/aud/kid/jku flags)
- `alg:none` token generator
- ~250 weak-secret dictionary brute (HS256)
- Verify mode (custom key)

### 💣 Payloads
- XSS / SQLi / LFI / SSRF / Command Injection / SSTI — copy button ke saath

### 🛠 Tools
- CIDR calculator
- Encoders: Base64, Base32, Hex, URL, Unicode, Reverse
- **MD5 + SHA-1 built-in** (offline, RFC-verified — kisi bhi context me chalega)
- SHA-256/384/512 (WebCrypto — https chahiye)
- **Phone/Network recon** — WebRTC se local IP leak check

### ⌨ TERMINAL (naya — data yahan direct dikhta hai, koi redirect nahi)

Type `help` ke baad yeh sab available hai:

```
help                 yeh list
clear                terminal saaf
recon <dom>          full recon (DNS+WHOIS+CT) — in-terminal
scan <url>           quick site scan (headers/tech/WAF/checks)
dns <dom>            A/AAAA/MX/NS/TXT/CAA/SOA + DMARC
whois <dom>          RDAP whois
asn <ip|dom>         ASN + origin + geo
geoip <ip|dom>       geolocation
crt <dom>            certificate transparency subs
wayback <dom>        archive snapshots
subs <dom>           quick subdomain brute (top 80)
jwt <tok>            JWT decode + audit
none <tok>           alg:none token generate
md5 <str>            MD5 hash (offline)
sha1 <str>           SHA-1 hash (offline)
sha256 <str>         SHA-256
crackmd5 <hash>      MD5 dictionary crack (~10k entries)
cracksha1 <hash>     SHA-1 dictionary crack
b64e/b64d <str>      base64
b32e/b32d <str>      base32
hexe/hexd <str>      hex
urle/urld <str>      URL encode/decode
rot13 <str>          ROT13
atbash <str>         Atbash cipher
morse <str>          Morse (auto encode/decode)
bin <n>              decimal → binary
int <n>              binary → decimal/hex
cidr <net>           CIDR calculator
gtfo <bin>           GTFOBins data — live fetch, in-terminal render
gtfo-list            curated GTFO bins list
trophy               NetSecFocus Trophy Room — PWK/OSCP box list (live)
ctfs                 CTF site list (ctf-practice, live)
thm                  TryHackMe free rooms 390+ (live)
caesar <n> <text>    Caesar cipher
xor <hexkey> <text>  XOR cipher (CyberChef-style)
wiki <topic>         cheatsheets: oscp, linux-privesc, windows-privesc,
                     web, recon, gmap, jwt, lfi, ssrf, ctf, writeups,
                     hashcat, stego, kali
payload <cat>        payload categories
hist                 history
report               full report download (.md)
links                reference links
```

**GTFOBins integration:** `gtfo find` → poora GTFOBins page (file-read/file-write/shell,
code + comments) terminal me render hota hai — data GitHub se live fetch hota hai
(ya internet na ho to `gtfo-list` + `wiki linux-privesc` offline available hai).

**Writeups/cheatsheets:** `wiki oscp`, `wiki linux-privesc`, `wiki windows-privesc`,
`wiki jwt`, `wiki lfi`, `wiki ssrf`, `wiki ctf`, `wiki writeups`, `wiki hashcat`,
`wiki stego`, `wiki kali`, `wiki gmap` — bookmark batch ke best sources ka distilled
data in-terminal. `wiki writeups` me **HTB TwoMillion (0xdf) ka poora exploit chain**
distilled hai (invite challenge → ROT13/base64 → broken access control → command
injection → .env pivot → CVE-2023-0386 root). `wiki gmap` me Chirag Soni ke GMap API
key writeup ka flow (keyhacks ke saath saare endpoints test karna).

**CTF batch live data:** `trophy` (NetSecFocus PWK box list), `ctfs` (CTF site list),
`thm` (390+ free rooms) — sab live fetch hota hai aur terminal me render hota hai,
koi redirect nahi.

### 📁 History & Reports
- LocalStorage me history (60 entries)
- Full report download — Markdown + JSON

## 🔒 Privacy / Notes

- Sab processing **browser me** hoti hai — koi data kisi server pe nahi jaata
  (sirf public DNS/DoH/crt.sh/RDAP jaise public endpoints se lookup hota hai,
  waise bhi woh public data hai)
- CORS-blocked pages ke liye public CORS proxies ka fallback hai (ya apna proxy
  Site Scan me daal sakte ho: `https://yoursite.com/proxy/?url={url}`)
- SHA-256/384/512 ke liye WebCrypto chahiye → **https (ya localhost)** pe chalao.
  MD5/SHA-1 built-in hai, wahi bhi chalega
- Phone recon = WebRTC ICE check → `allow="microphone"` iframe attribute zaroori nahi,
  par permission prompt ho sakta hai

## ✅ Verified

- MD5 + SHA-1: 13 test vectors node:crypto se verify (RFC 1321 / RFC 3174)
- Terminal: 33 command smoke tests + GTFOBins live fetch (YAML parse) verified
- Single `<script>` block, zero external JS/CSS dependencies

## 📄 License

MIT — use karo, modify karo, distribute karo.
