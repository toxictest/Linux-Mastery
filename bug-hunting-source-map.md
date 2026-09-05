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


## Extra modern technique lanes added after additional research
- OAuth / OIDC review
  - redirect trust
  - state binding
  - scope and audience checks
  - refresh-token handling and replay resistance
- JWT review
  - claim trust
  - signature validation path
  - key lookup behavior
  - revocation/session-lifecycle thinking
- GraphQL review
  - introspection exposure
  - batching abuse
  - query depth / cost
  - broken authorization in nested objects
- Race-condition review
  - temporary sub-states
  - single-use logic collisions
  - concurrent request edge cases
- Cache / CDN review
  - cache key confusion
  - personalized/public response mixing
  - variation inputs
- Upload pipeline review
  - upload -> transform -> preview -> download chain
  - filename, content-type, size, and storage controls
- Webhook / integration review
  - outbound requests
  - destination validation
  - metadata/internal reach thinking

## Extra official/public links added after research
- PortSwigger OAuth — https://portswigger.net/web-security/oauth
- PortSwigger JWT — https://portswigger.net/web-security/jwt
- PortSwigger GraphQL API vulnerabilities — https://portswigger.net/web-security/graphql
- PortSwigger Race Conditions — https://portswigger.net/web-security/race-conditions
- PortSwigger Web Cache Poisoning — https://portswigger.net/web-security/web-cache-poisoning
- PortSwigger Web Cache Deception — https://portswigger.net/web-security/web-cache-deception
- PortSwigger API Testing — https://portswigger.net/web-security/api-testing
- PortSwigger Request Smuggling — https://portswigger.net/web-security/request-smuggling
- PortSwigger WebSockets — https://portswigger.net/web-security/websockets
- PortSwigger CORS — https://portswigger.net/web-security/cors
- OWASP Authentication Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- OWASP Session Management Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- OWASP Forgot Password Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html
- OWASP OAuth 2.0 Protocol Cheatsheet — https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html
- OWASP JSON Web Token Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html
- OWASP GraphQL Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html
- OWASP File Upload Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
- OWASP SSRF Prevention Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
- Chrome DevTools Network — https://developer.chrome.com/docs/devtools/network
- Chrome DevTools Security — https://developer.chrome.com/docs/devtools/security

- Bug bounty 170-day series: `bug-bounty-series.html`
