# Bug Hunting Source Map

## Purpose
This companion note was created after a deep review of the public repository `https://github.com/toxictest/bug-hunting` and is meant to preserve the main themes, study directions, and public learning anchors that informed `bug-bounty-vault.html`.

## Reviewed-material summary
- Public repo reviewed locally before writing the vault.
- Review included text-heavy notes, DOCX files, PDF material, still images, and video snapshots.
- Local extraction artifact exists outside the repo as `/home/user/bug_hunting_repo_review.md`.

## Strong recurring vulnerability families noticed in the repo
1. Authentication and session-management weaknesses
   - weak registration flows
   - weak password reset flows
   - logout/session invalidation issues
   - token leakage
   - 2FA and OTP bypass/rate-limit weakness
2. Client-side and rendering issues
   - reflected XSS
   - stored XSS
   - blind XSS references
   - clickjacking
   - HTML/email injection
3. Authorization and access-control issues
   - IDOR
   - horizontal privilege escalation
   - vertical privilege escalation
   - request/response auth bypass patterns
4. Server-side and backend impact areas
   - SSRF
   - command injection
   - SSTI
   - XXE
   - LFI
   - file upload weakness
   - SQL injection
   - Log4J exposure notes
5. Recon and infrastructure surfaces
   - subdomain discovery
   - mail-security checks like SPF/DMARC
   - visible debug pages
   - origin/IP leakage
   - default credentials and forgotten asset behavior

## What this says about the study direction
The reviewed repo is rich in curiosity and breadth. The next maturity step is to convert raw examples into repeatable systems:
- state-transition maps for auth/session bugs
- authorization matrices for IDOR/role issues
- tool-selection checklists for recon and validation
- impact-first reporting language
- revision notes that compress one vulnerability family into one page

## Tools mapped from repo themes
| Theme | Good tools to learn | Why |
|---|---|---|
| Auth/session | Browser DevTools, Burp Suite, curl | request comparison, cookie/session tracing, clean reproduction |
| Recon | subfinder, Amass, assetfinder, crt.sh, httpx, Katana | asset discovery, live host filtering, route discovery |
| Historical URLs | waybackurls, gau | old endpoints and forgotten parameters |
| DNS / mail security | dig, dnsx, host | TXT/MX/CNAME/SPF/DMARC verification |
| Content discovery | ffuf, SecLists | route/file/parameter discovery in authorized scope |
| JSON/API testing | jq, curl, DevTools | API response interpretation and report-ready proof |
| Safe automation | Nuclei, Bash, Python | template-driven detection and structured evidence pipelines |

## Official and public source board
- PortSwigger Web Security Academy — https://portswigger.net/web-security
- PortSwigger XSS Cheat Sheet — https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
- OWASP Web Security Testing Guide — https://owasp.org/www-project-web-security-testing-guide/
- OWASP Top 10 — https://owasp.org/www-project-top-ten/
- Bugcrowd VRT — https://www.bugcrowd.com/vulnerability-rating-taxonomy/
- HackerOne Hacktivity — https://hackerone.com/hacktivity
- Intigriti Researcher Blog — https://www.intigriti.com/researchers/blog
- ProjectDiscovery docs — https://docs.projectdiscovery.io/
- PayloadsAllTheThings — https://github.com/swisskyrepo/PayloadsAllTheThings
- can-i-take-over-xyz — https://github.com/EdOverflow/can-i-take-over-xyz
- Default Credentials reference — https://github.com/netbiosX/Default-Credentials

## Best practice for using sources
- Use them for explanation, validation, and pattern recognition.
- Do not blindly paste payloads into live targets.
- Always check authorization and scope first.
- Build minimal reproducible evidence before reporting.

## Next personal-upload template
When adding your own lawful materials later, include:
- target/program name
- scope notes
- file list
- pasted raw notes
- screenshots/PDF references
- exact confusion points
- desired output format (Hindi notes, English translation, revision sheet, checklist, report summary)

## In-repo companions
- Main frontend: `index.html`
- Study hub: `study-hub.html`
- Notes vault: `notes.html`
- Bug bounty vault: `bug-bounty-vault.html`
- Personal intake template: `notes-import.html`
