# build_part3.py — hub data (levels 22-33 + resources + tools + misc)

HUB = {
"levels": [
{"id":22,"t":"Advanced Free Resource Hub","ph":4,
 "intro":"Resource Hub ka purpose sirf links dena nahi — har resource ke saath: What is it? · Why use it? · Prerequisite · Free status · Official source · Difficulty · Recommended level · Hands-on lab? · Related commands · Related security concepts · Next resource.",
 "body":"resources",
 "tasks":[
  {"t":"Official source verify karo: man dig (lab mein DNS tool ka official doc)","checks":[{"k":"cmd","re":"^man (dig|curl|nmap)"}]},
  {"t":"DNS resource practice: dig lab.local +short","checks":[{"k":"cmd","re":"dig lab\\.local"}]}
 ]},
{"id":23,"t":"Tool Mastery Directory","ph":4,
 "intro":"Tool page 'Tool List' nahi, 'Tool Mastery' format hai. Har tool card: Name · Category · Free Status · Open Source? · Official Docs · Installation · Basic Usage · Important Options · Input · Output · Common Errors · Linux Integration · Security Use Case · Safe Lab · Related Tools · Difficulty.",
 "body":"tools",
 "tasks":[
  {"t":"Tool mastery: man grep padho, phir use karo: grep -n ERROR /var/log/app.log","checks":[{"k":"cmd","re":"^man grep"},{"k":"cmd","re":"grep -n ERROR /var/log/app\\.log"}]},
  {"t":"Tool operate: find /etc -name 'motd' -type f","checks":[{"k":"cmd","re":"find /etc"}]},
  {"t":"Tool combine: cat /home/learner/lab/data/dupes.txt | sort | uniq -c","checks":[{"k":"cmd","re":"sort \\| uniq"}]}
 ]},
{"id":24,"t":"Browser-Based Free Tools Hub","ph":4,
 "intro":"Browser par free utilities — Encoding/Decoding, Data (JSON), Regex, Web, Security references. SAKTAM: har online tool par privacy warning — neeche. Sensitive data ke liye LOCAL CLI alternatives hamesha pehla choice.",
 "body":"browsertools",
 "tasks":[
  {"t":"Local alternative practice: jq . /srv/lab/api_users.json (browser JSON formatter ki jagah)","checks":[{"k":"cmd","re":"jq . /srv/lab/api_users\\.json"}]},
  {"t":"Privacy mindset: secret ko browser tool mein paste NAHI — local dekho: cat /srv/lab/.env","checks":[{"k":"cmd","re":"cat /srv/lab/\\.env"}]}
 ]},
{"id":25,"t":"Web Tool vs Local Tool","ph":4,
 "intro":"Advanced feature: har task ke liye browser tool aur Linux tool dono dekho. Learning objective: browser tools convenient hain, lekin professional workflow ke liye local tools + reproducibility zaroori.",
 "body":"compare",
 "tasks":[
  {"t":"Compare practice: DNS lookup LOCAL se — dig lab.local (browser DNS tool ki jagah)","checks":[{"k":"cmd","re":"dig lab\\.local"}]},
  {"t":"HTTP request LOCAL se: curl -sI http://lab.local/ | head -3","checks":[{"k":"cmd","re":"curl -sI http://lab\\.local"}]}
 ]},
{"id":26,"t":"Resource Verification System","ph":4,
 "intro":"Har resource par 'Verified' badges — taaki aap ko pata ho resource kaunsa hai: official? open source? sach mein free? free tier? community edition? ya paid?",
 "body":"verify",
 "tasks":[
  {"t":"Verification habit: apne lab OS ka official info — cat /etc/os-release","checks":[{"k":"cmd","re":"cat /etc/os-release"}]},
  {"t":"Free status check: free -h (lab ka memory 'report' — tool output ki tarah read karo)","checks":[{"k":"cmd","re":"^free -h"}]}
 ]},
{"id":27,"t":"Resource Quality Score","ph":4,
 "intro":"Har resource ko internal scoring — Authenticity 25% · Free Access 20% · Maintenance 15% · Hands-on 15% · Documentation 10% · Community 10% · Beginner Value 5%. Score se resource rank banta hai.",
 "body":"quality",
 "tasks":[
  {"t":"Score your lab: disk + memory + uptime collect karo (df -h, free -h, uptime)","checks":[{"k":"cmd","re":"^df -h"},{"k":"cmd","re":"^free -h"},{"k":"cmd","re":"^uptime"}]}
 ]},
{"id":28,"t":"Learning Path From Resource Hub","ph":4,
 "intro":"Resource page overwhelm NAHI karega. 4 structured paths: Beginner → Intermediate → Advanced → Bug Hunter. Apna path dhundo, usi ko follow karo.",
 "body":"paths",
 "tasks":[
  {"t":"Beginner path step 1: file system explore — ls -a /home/learner","checks":[{"k":"cmd","re":"ls -a /home/learner"}]},
  {"t":"Beginner path step 2: logs padho — tail -5 /var/log/sys.log","checks":[{"k":"cmd","re":"tail -5 /var/log/sys\\.log"}]}
 ]},
{"id":29,"t":"Don't Learn This Yet","ph":4,
 "intro":"Beginner ko advanced tools ki 100-item list dekar confuse NAHI karna. Rule: Prerequisite complete → unlock advanced resource. Isse learning structured rehti hai.",
 "body":"dly",
 "tasks":[
  {"t":"Structure maintain karo: history dekho — aapne ab tak kya kiya (audit trail)","checks":[{"k":"cmd","re":"^history$"}]}
 ]},
{"id":30,"t":"Tool Dependency Map","ph":4,
 "intro":"Visual dependency graph — tool tab unlock hoga jab prerequisites complete hon. Linux → Bash/Networking/Web Security/Python ka tree.",
 "body":"depmap",
 "tasks":[
  {"t":"Dependency check: which bash (Bash Linux ki dependency hai)","checks":[{"k":"cmd","re":"^which bash"}]},
  {"t":"Which tools available: which curl dig nmap","checks":[{"k":"cmd","re":"^which (curl|dig|nmap)"}]}
 ]},
{"id":31,"t":"Tool Challenge System","ph":4,
 "intro":"Har tool ke liye 5 stages: Identify (kya hai?) → Operate (basic) → Interpret (output samjho) → Combine (doosre tools ke saath) → Troubleshoot (fail ho to diagnose).",
 "body":"stages",
 "tasks":[
  {"t":"Stage 2 Operate: echo 'stage2 done' > /tmp/stage2.txt && cat /tmp/stage2.txt","checks":[{"k":"fs","p":"/tmp/stage2.txt","c":"stage2"}]},
  {"t":"Stage 4 Combine: cat /var/log/app.log | grep ERROR | wc -l","checks":[{"k":"cmd","re":"grep ERROR \\| wc"}]}
 ]},
{"id":32,"t":"Can I Use This Tool? (Safety Gate)","ph":4,
 "intro":"Security tools ke liye context gate — har tool use se pehle platform batata hai: kahan use kar sakte ho. Ye platform ki default safety architecture ka part hai. Terminal mein bhi Red Line enforced hai — external target try karo, block hoga.",
 "body":"gate",
 "tasks":[
  {"t":"Safe target: ping -c 2 lab.local (allowed zone)","checks":[{"k":"cmd","re":"ping .*lab\\.local"}]},
  {"t":"RED LINE TEST: ping -c 2 8.8.8.8 try karo — dekho block kyun hua (safety gate demo)","checks":[{"k":"cmd","re":"ping .*8\\.8\\.8\\.8"}]}
 ]},
{"id":33,"t":"Final 100% Ready Checklist + HOST READY Certification","ph":4,
 "intro":"Learner dashboard — 5 domains ka checklist. Sab complete karo → HOST READY certification unlock. Golden Rule: 'Tool mastery ≠ command memorization.'",
 "body":"final",
 "tasks":[
  {"t":"Final profile: uname -a > /tmp/hostready.txt && ip addr >> /tmp/hostready.txt && ss -tlnp >> /tmp/hostready.txt && df -h >> /tmp/hostready.txt","checks":[{"k":"fs","p":"/tmp/hostready.txt","c":"Linux"}]}
 ]}
],
"resourceCategories":[
 {"icon":"🐧","name":"Linux","items":["Linux fundamentals","Bash","GNU Coreutils","Filesystems","Permissions","Processes","systemd","Networking","Linux internals","Linux security","Containers"]},
 {"icon":"🌐","name":"Networking","items":["TCP/IP","DNS","HTTP","TLS","Routing","Packet analysis","Network troubleshooting"]},
 {"icon":"🔐","name":"Web Security","items":["OWASP","PortSwigger Academy","Hacker101","API security","Authentication","Authorization","Session security","Input validation","Business logic"]},
 {"icon":"🧪","name":"Labs","items":["Web labs","Linux labs","CTFs","Network labs","Defensive labs","Local vulnerable applications"]},
 {"icon":"🛠️","name":"Tools","items":["CLI tools","Web-testing tools","Network tools","Packet-analysis tools","DNS tools","Content-analysis tools","Automation tools"]},
 {"icon":"📚","name":"References","items":["CVE","CWE","CVSS","RFCs","vendor documentation","security advisories"]}
],
"resources":[
 {"name":"OverTheWire Bandit","cat":"Linux","what":"25 progressive levels — har level par SSH box par password hunt. Linux commands ka gamified course.","why":"Pipes, redirection, permissions, SUID — sab naturally aate hain, boring lecture ke bina. Phase 1 (Levels 1-3) ka perfect companion.","prereq":"Level 0-1 complete (basic terminal: ls, cat, cd)","free":"100% Free","source":"overthewire.org/wargames/bandit","difficulty":"Beginner","level":"Levels 1-3","handsOn":"Yes — SSH lab, live machine","commands":["ssh","cat","grep","find","sudo","su","chmod"],"concepts":["permissions","SUID/SGID","users & groups","command substitution"],"next":"OverTheWire Natas (Web) → Level 7 ke baad","badges":["official","free"],"stars":5},
 {"name":"The Odin Project","cat":"Linux","what":"Full-stack web development + Linux fundamentals ka free structured path.","why":"Terminal se lekar web tak — Linux ke 'Builder Phase' ke liye solid foundation. Hands-on exercises har section mein.","prereq":"Level 0 complete (mental model)","free":"100% Free","source":"theodinproject.com","difficulty":"Beginner","level":"Levels 0-2","handsOn":"Yes — local terminal exercises","commands":["ls","cd","mkdir","touch","man","grep"],"concepts":["filesystem","shell basics","web basics"],"next":"Level 1 Terminal Mastery → Level 2","badges":["official","free"],"stars":5},
 {"name":"Linux Journey","cat":"Linux","what":"Interactive Linux tutorial — 100+ short lessons, beginner-friendly.","why":"Zero base ke liye best start. Har topic chhota, focused, example ke saath. Bina pressure ke foundation banta hai.","prereq":"None — absolute beginner OK","free":"100% Free","source":"linuxjourney.com","difficulty":"Beginner","level":"Level 0","handsOn":"Partial — terminal examples","commands":["ls","pwd","whoami","echo","man"],"concepts":["kernel","filesystem","shell"],"next":"OverTheWire Bandit","badges":["official","free"],"stars":4},
 {"name":"GNU Manuals (Coreutils + Bash)","cat":"Linux","what":"Official documentation — GNU coreutils (ls, grep, find...) aur bash reference manual.","why":"Documentation mastery (Level 21.22) ka asli source. 'man command' ke peeche jo content hai, wahi asli reference hai.","prereq":"Level 1 complete (terminal basic)","free":"100% Free + Open Source","source":"gnu.org/manuals","difficulty":"All levels (reference)","level":"Level 21.22","handsOn":"No — reference manual","commands":["man","info","grep"],"concepts":["reference skills","documentation mastery"],"next":"Har level ke man pages","badges":["official","opensource","free"],"stars":5},
 {"name":"Nmap (Official + Book)","cat":"Tools","what":"Nmap Reference Guide + 'Nmap Network Scanning' book (free PDF, official site par).","why":"Authorized network discovery ka gold standard. Tool card (Level 23) ke saath padho — usage se theory tak.","prereq":"Level 6 complete (networking fundamentals)","free":"100% Free + Open Source","source":"nmap.org/book","difficulty":"Intermediate","level":"Level 23.2","handsOn":"Yes — lab.local par safe scan","commands":["nmap","ip","ss"],"concepts":["port scanning","service detection","attack surface"],"next":"Wireshark (packet level)","badges":["official","opensource","free"],"stars":5},
 {"name":"Wireshark (Official User's Guide)","cat":"Tools","what":"Packet analyzer ka official guide + live lab captures.","why":"'Packet capture ko READ karna' sikhata hai — filters copy nahi. Level 6/17 ka core skill. tcpdump ka visual version.","prereq":"Level 6 complete (TCP/IP, protocols)","free":"100% Free + Open Source","source":"wireshark.org/docs","difficulty":"Intermediate","level":"Level 23.2","handsOn":"Yes — lab traffic capture","commands":["tcpdump","ss","dig"],"concepts":["packet analysis","protocol hierarchy","streams"],"next":"Level 17 Debugging Mastery","badges":["official","opensource","free"],"stars":5},
 {"name":"PortSwigger Web Security Academy","cat":"Web Security","what":"Burp Suite makers ka free web security academy — 60+ interactive labs (AppSec).","why":"Web security ka most structured FREE resource. Har topic: read → lab → solve. Level 7/15 ka perfect practice ground.","prereq":"Level 7 complete (HTTP basics) + burp community edition","free":"100% Free (labs + content)","source":"portswigger.net/web-security","difficulty":"Intermediate → Advanced","level":"Levels 12, 15-20","handsOn":"Yes — 60+ guided labs","commands":["curl","grep","jq"],"concepts":["injection","auth flaws","business logic","OWASP Top 10"],"next":"OWASP Juice Shop (local lab)","badges":["official","free"],"stars":5},
 {"name":"OWASP (Top 10 + Juice Shop + SAM)","cat":"Web Security","what":"Web security ka standard: OWASP Top 10, Juice Shop (intentionally vulnerable app), SAM (Security Assessment Methodology).","why":"Juice Shop = LOCAL vulnerable app — Red Line ke andar full practice. Top 10 = bug hunting ki checklist. SAM = methodology.","prereq":"Level 7 + basic HTTP","free":"100% Free + Open Source","source":"owasp.org","difficulty":"Intermediate","level":"Levels 12, 15-20","handsOn":"Yes — Juice Shop local Docker lab","commands":["curl","docker","grep"],"concepts":["OWASP Top 10","vulnerability classes","assessment methodology"],"next":"TryHackMe Web paths","badges":["official","opensource","free"],"stars":5},
 {"name":"TryHackMe","cat":"Labs","what":"Gamified guided hacking rooms + learning paths (Beginner → Bug Hunter).","why":"Guided labs mein step-by-step progress. Free tier beginner ke liye kaafi hai. 'Build before break' philosophy ke saath match karta hai.","prereq":"Level 0-1 (basics) — rooms khud guide karti hain","free":"Free tier (guided paths limited) — paid: all rooms","source":"tryhackme.com","difficulty":"Beginner → Advanced","level":"Levels 1-15","handsOn":"Yes — browser-based labs","commands":["nmap","grep","python3"],"concepts":["CTF methodology","recon","exploitation basics"],"next":"Hack The Box (unguided)","badges":["freetier"],"stars":4},
 {"name":"Hack The Box","cat":"Labs","what":"Realistic CTF machines + Academy (structured courses). Free: limited machines + academy.","why":"TryHackMe ke baad 'unguided' practice — khud exploit dhundo. Bug hunter mindset isi se banta hai (scope ke andar).","prereq":"TryHackMe basics + Linux comfort","free":"Free tier (machines limited, academy free)","source":"hackthebox.com","difficulty":"Intermediate → Advanced","level":"Levels 15-21","handsOn":"Yes — full machines","commands":["nmap","ssh","grep","python3"],"concepts":["CTF methodology","privilege escalation","recon at scale"],"next":"Authorized bug bounty programs","badges":["freetier"],"stars":4},
 {"name":"Cybrary","cat":"References","what":"Security training platform — free courses + labs (Security+, network, cloud).","why":"Video + labs combo. Security+ prep + hands-on labs free tier mein. Professor Messer ke saath pair karo.","prereq":"Level 12+ (security basics)","free":"Free tier (courses limited, labs included)","source":"cybrary.io","difficulty":"Intermediate","level":"Level 12-17","handsOn":"Yes — virtual labs","commands":["—"],"concepts":["security+ topics","risk management","incident response"],"next":"Security+ exam prep","badges":["freetier"],"stars":4},
 {"name":"Professor Messer (Security+)","cat":"References","what":"CompTIA Security+ ka complete free video course + flashcards + practice exams.","why":"Security fundamentals ka most structured free video course. Level 12 (Security Architecture) ka perfect backup. Practice exams free hain.","prereq":"Level 12 (security basics)","free":"100% Free","source":"professormesser.com","difficulty":"Intermediate","level":"Level 12-17","handsOn":"Partial — labs par focus kam","commands":["—"],"concepts":["security+ domains","risk","cryptography basics"],"next":"Cybrary labs + PortSwigger","badges":["official","free"],"stars":5},
 {"name":"RFC Editor","cat":"Networking","what":"Internet Standards ki official documents (RFCs) — TCP, DNS, HTTP sab yahan defined hain.","why":"Networking 'deep dive' ka source of truth. RFC 791 (IP), RFC 768 (UDP), RFC 9110 (HTTP). 'Why' samajhne ke liye.","prereq":"Level 6 (networking fundamentals)","free":"100% Free","source":"rfc-editor.org","difficulty":"Advanced (reference)","level":"Level 18-19","handsOn":"No — reference","commands":["curl","dig"],"concepts":["protocol standards","RFC reading","networking theory"],"next":"Level 18 Internals","badges":["official","free"],"stars":5},
 {"name":"MITRE CWE","cat":"References","what":"Common Weakness Enumeration — vulnerability classes ka standard (CWE-79 XSS, CWE-89 SQLi, ...).","why":"Bug hunting mein findings ko classify karo + responsible reporting mein standard language. Har finding ka CWE ID.","prereq":"Level 15 (web security basics)","free":"100% Free","source":"cwe.mitre.org","difficulty":"All levels (reference)","level":"Levels 15-20","handsOn":"No — reference","commands":["—"],"concepts":["vulnerability taxonomy","CWE mapping","reporting standards"],"next":"CVSS (severity scoring)","badges":["official","free"],"stars":5},
 {"name":"FIRST CVSS","cat":"References","what":"Common Vulnerability Scoring System — vulnerability severity ka standard (0-10).","why":"Report mein severity justify karo: CVSS vector (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N = 9.8). Professional reporting ka core.","prereq":"Level 20 (reporting basics)","free":"100% Free","source":"first.org/cvss","difficulty":"Intermediate (reference)","level":"Level 20","handsOn":"No — calculator + reference","commands":["—"],"concepts":["severity scoring","impact analysis","reporting"],"next":"NVD (CVE lookup)","badges":["official","free"],"stars":5},
 {"name":"NVD (National Vulnerability Database)","cat":"References","what":"CVE (Common Vulnerabilities and Exposures) ka official database — NIST maintain karta hai.","why":"Known vulnerabilities lookup + CVSS scores. Bug hunting mein 'kya known hai' verify karo. Patch tracking ke liye.","prereq":"Level 15+ (vulnerability basics)","free":"100% Free","source":"nvd.nist.gov","difficulty":"All levels (reference)","level":"Levels 15-20","handsOn":"No — lookup tool","commands":["—"],"concepts":["CVE lookup","patch management","known vulns"],"next":"Vendor security advisories","badges":["official","free"],"stars":5}
],
"toolCategories":{
 "title":"23.1 Linux Native Toolkit — built-in tools sabse pehle master karo",
 "essential":["pwd","ls","cd","cp","mv","rm","mkdir","touch","cat","less","head","tail","grep","find","sort","uniq","cut","tr","sed","awk","xargs","tee"],
 "system":["ps","top","htop","free","df","du","uptime","uname","hostname","lsblk"],
 "networking":["ip","ss","ping","dig","host","curl","wget","tcpdump"],
 "security":["sudo","chmod","chown","find","lsof","ss","journalctl","systemctl","strace","file"],
 "note":"Mastery target: in commands ka PURPOSE aur COMBINATION samajhna chahiye — not necessarily every obscure flag memorize karna."
},
"tools":[
 {"name":"grep","cat":"Text Processing","free":"Free + Open Source","os":"Yes (GNU)","docs":"man grep + gnu.org","install":"Preinstalled (GNU coreutils)","basic":"grep -i 'error' /var/log/app.log","options":"-i (case-insensitive) · -n (line number) · -c (count) · -v (invert) · -r (recursive) · -E (extended regex)","input":"File ya stdin","output":"Matching lines (stdout)","errors":"'No such file' → path check; 'Binary file matches' → -a add karo","integration":"Pipelines ka core: cat f | grep x | wc -l; -o + cut + sort se structured output","securityUse":"Logs mein suspicious patterns, config audit, secret scan (grep -r 'password' .)","lab":"grep -c 'Failed password' /var/log/auth.log","related":["awk","sed","ripgrep"],"difficulty":"Beginner"},
 {"name":"find","cat":"Filesystem Search","free":"Free + Open Source","os":"Yes (GNU)","docs":"man find","install":"Preinstalled (findutils)","basic":"find /home -name '*.txt' -type f","options":"-name (pattern) · -type f/d/l · -perm (permissions) · -mtime (time) · -size · -user · -exec","input":"Start path + filters","output":"Matching paths (one per line)","errors":"'Permission denied' → sudo ya 2>/dev/null; broad search slow → -maxdepth limit","integration":"find | xargs rm (careful!); find -exec stat {} ; metadata batch","securityUse":"Hidden files (find . -name '.*'), SUID binaries (find / -perm -4000), world-writable (find / -perm -o+w)","lab":"find /home -name '.secret_note' -type f","related":["locate","grep","stat"],"difficulty":"Beginner"},
 {"name":"sed","cat":"Text Processing","free":"Free + Open Source","os":"Yes (GNU)","docs":"man sed","install":"Preinstalled (GNU sed)","basic":"sed 's/old/new/' file","options":"s/pattern/replacement/ (substitute) · -n (quiet) · -i (in-place) · d (delete line) · p (print) · -E (extended)","input":"File ya stdin","output":"Modified stream","errors":"'unescaped newline' → escaping check; -i bina backup ke destructive","integration":"cat f | sed 's/://g' | sort -u; log parsing pipelines mein","securityUse":"Log sanitization (secrets redact karo), config normalize, pattern replace in reports","lab":"sed 's/lab-01/LAB/g' /etc/hostname","related":["awk","grep","perl"],"difficulty":"Intermediate"},
 {"name":"awk","cat":"Text Processing","free":"Free + Open Source","os":"Yes (gawk)","docs":"man awk","install":"Preinstalled (gawk)","basic":"awk '{print $1, $3}' file","options":"{print $N} (field) · NR (line no) · /pattern/ (match) · -F (delimiter) · BEGIN/END blocks","input":"File ya stdin (whitespace/comma delimited)","output":"Processed lines","errors":"'syntax error' → quotes check; -F galat → field positions shift","integration":"grep x f | awk '{print $5}' | sort | uniq -c — classic report pipeline","securityUse":"Log correlation (IP + timestamp + action extract), CSV → report, dedup with seen[]","lab":"awk '{print $(NF-3)}' /var/log/auth.log | sort -u (attacker IPs)","related":["cut","sed","grep"],"difficulty":"Intermediate"},
 {"name":"jq","cat":"JSON Processing","free":"Free + Open Source","os":"Yes","docs":"stedolan.github.io/jq","install":"apt install jq","basic":"jq . file.json","options":". (pretty) · .key (path) · .[] (array) · length · keys · map() · select() · -r (raw output)","input":"JSON (file ya stdin)","output":"Formatted/extracted JSON","errors":"'parse error' → input valid JSON nahi; path miss → keys se structure dekho","integration":"curl -s url | jq .data — API work ka core; > file se save","securityUse":"API response analysis, user enumeration data clean, JSON logs parse, token structures inspect","lab":"jq . /srv/lab/api_users.json","related":["python3 -m json.tool","yq"],"difficulty":"Beginner"},
 {"name":"ss","cat":"Networking (sockets)","free":"Free + Open Source","os":"Yes (iproute2)","docs":"man ss","install":"Preinstalled (iproute2)","basic":"ss -tlnp","options":"-t (TCP) · -u (UDP) · -l (listening) · -n (no resolve) · -p (process) · -tan (all + states) · state <state>","input":"Kernel socket state","output":"Socket list: state, local/peer addr, process","errors":"Empty → filter check; process column empty → sudo chahiye","integration":"ss -tlnp | grep :8080; ss -tan state time-wait | wc -l (leak detect)","securityUse":"Exposed services inventory (attack surface), connection states analyze, suspicious listeners","lab":"ss -tlnp (lab services: 22, 80, 8080)","related":["netstat","lsof","ip"],"difficulty":"Beginner"},
 {"name":"ip","cat":"Networking","free":"Free + Open Source","os":"Yes (iproute2)","docs":"man ip","install":"Preinstalled (iproute2)","basic":"ip addr","options":"addr (interfaces) · route (routes) · neigh (ARP) · link (state) · -s (stats) · -j (JSON)","input":"Kernel network state","output":"Interface/route/neighbor details","errors":"Permission → sudo (changes ke liye); empty route table → gateway check","integration":"ip addr | grep inet; ip route get <ip> (path trace); ip -j addr | jq (structured)","securityUse":"Interface audit, IP config verify, neighbor table (ARP anomalies), attack surface base","lab":"ip addr + ip route (lab-01: 10.8.0.5/24)","related":["ifconfig","ss","ping"],"difficulty":"Beginner"},
 {"name":"curl","cat":"HTTP/HTTPS","free":"Free + Open Source","os":"Yes","docs":"curl.se/docs","install":"Preinstalled","basic":"curl -i http://lab.local/","options":"-i (headers) · -v (verbose) · -X (method) · -H (header) · -d (data) · -L (follow redirect) · -c/-b (cookies) · -o (output) · --max-time","input":"URL (+ headers/data)","output":"Response (headers + body)","errors":"'(7) Failed to connect' → service down/DNS; '(6) Could not resolve' → DNS; '(35) SSL error' → cert","integration":"curl -s url | jq . (API); curl -o file url (download); loops se batch","securityUse":"Endpoint enumeration, auth testing (Bearer/Basic), redirect chains, cookie flags, error handling inspect","lab":"curl -i http://lab.local/ + /api/users + /admin","related":["wget","httpie","Burp"],"difficulty":"Beginner"},
 {"name":"dig","cat":"DNS","free":"Free + Open Source","os":"Yes (bind-utils)","docs":"man dig","install":"Preinstalled (bind9-dnsutils)","basic":"dig lab.local A","options":"+short · +trace (full journey) · +noall +answer · @server · -t (type: A/AAAA/MX/TXT/NS)","input":"Domain + type","output":"DNS answer (IP, TTL, server)","errors":"'SERVFAIL' → server issue; 'NXDOMAIN' → domain exist nahi; timeout → resolver","integration":"dig +short domain; dig +trace domain (resolution journey); loops se subdomain check","securityUse":"Subdomain recon, TXT records (SPF/DMARC), DNS enumeration, stale records dhundo","lab":"dig lab.local +short (10.8.0.5)","related":["host","nslookup","resolvectl"],"difficulty":"Beginner"},
 {"name":"tcpdump","cat":"Packet Analysis","free":"Free + Open Source","os":"Yes","docs":"tcpdump.org/manpages","install":"Preinstalled (tcpdump)","basic":"tcpdump -i any host lab.local -n","options":"-i (interface) · -n (no resolve) · -c (count) · -A (ASCII) · -w (save pcap) · -r (read pcap) · filter expressions","input":"Live traffic (kernel tap)","output":"Packet details (headers + optional payload)","errors":"'no permission' → sudo; 'no such device' → interface name; chup → filter galat","integration":"tcpdump -w cap.pcap & (background); baad mein Wireshark mein open; -A se HTTP payload","securityUse":"Packet forensics, protocol behavior verify, handshake/redirect observe, evidence capture (lab)","lab":"tcpdump -i any host lab.local -c 10 -n","related":["wireshark","tshark","ss"],"difficulty":"Intermediate"},
 {"name":"nmap","cat":"Network Discovery","free":"Free + Open Source","os":"Yes","docs":"nmap.org/book (free book)","install":"Preinstalled / apt install nmap","basic":"nmap -sT -p 22,80,8080 lab.local","options":"-sT (TCP connect) · -sU (UDP) · -sV (versions) · -p (ports) · -oN (output) · -sC (default scripts) · --max-rate","input":"Target (IP/domain) + options","output":"Open/closed ports + services","errors":"'Permission denied (UDP)' → sudo; timeout → target down; rate limit → --max-rate","integration":"nmap -oN scan.txt lab.local; grep open scan.txt; report mein use","securityUse":"AUTHORIZED targets only: service discovery, attack surface inventory, lab enumeration. External = RED LINE.","lab":"nmap -sT -p 22,80,8080 lab.local","related":["masscan","rustscan","ss"],"difficulty":"Intermediate"},
 {"name":"strace","cat":"Debugging (syscalls)","free":"Free + Open Source","os":"Yes","docs":"man strace","install":"apt install strace","basic":"strace -c ls","options":"-p (attach pid) · -c (summary) · -e trace=openat (filter) · -f (follow forks) · -s (string len) · -o (output file)","input":"Process (live ya new command)","output":"Syscall sequence + results","errors":"'Operation not permitted' → sudo (other users' processes); 'attach: ptrace' → kernel restriction","integration":"strace -c cmd (performance); strace -e trace=network cmd (network syscalls); logs ke saath correlate","securityUse":"Permission errors root cause, network behavior trace, malware behavior (lab), crash diagnosis","lab":"strace -c ls (lab host)","related":["ltrace","gdb","lsof"],"difficulty":"Advanced"},
 {"name":"journalctl","cat":"Logs","free":"Free + Open Source","os":"Yes (systemd)","docs":"man journalctl","install":"Preinstalled (systemd)","basic":"journalctl -u sshd -n 50","options":"-u (unit) · -n (last N) · --since '10 min ago' · -p (priority: err/warn) · -f (follow) · -b (last boot) · _COMM= (process)","input":"systemd journal (binary logs)","output":"Formatted log lines","errors":"'No journal files' → systemd journal enabled nahi; empty → filter too specific","integration":"journalctl -u X -p err --since '1 hour ago' | grep pattern; > file se evidence","securityUse":"Service failure diagnosis, auth events timeline, failure correlation, incident response","lab":"journalctl -n 20 (lab snapshot)","related":["systemctl","dmesg","grep","awk"],"difficulty":"Beginner"}
],
"progressions":[
 {"tool":"Nmap","label":"Learning Progression","steps":["Basic discovery","Ports","Services","Versions","Output analysis","Automation"],"note":"Authorized targets only. Lab: nmap -sT lab.local se shuru, phir -sV, phir -oN + grep."},
 {"tool":"Wireshark","label":"Learning Progression","steps":["Capture","Packet","Protocol","Stream","Filter","Analyze"],"note":"Packet capture ko READ karna sikhaya jayega — not simply filters copy karna. tcpdump se pcap banao, Wireshark mein open karo."},
 {"tool":"tcpdump","label":"Goal","steps":["CLI capture","Filters","Pcap save/read","ASCII payload","Analysis"],"note":"'GUI available na ho tab bhi network traffic investigate kar sako.' — yahi tcpdump ka mission hai."},
 {"tool":"Burp Suite (Community)","label":"Learning Progression","steps":["Proxy","HTTP History","Repeater","Request Analysis","Response Analysis","Testing Workflow"],"note":"Free/community capabilities clearly identify kiye jaate hain (Community: proxy, repeater, history, scanner limited; Pro: automated scanner, intruder, collaborator)."},
 {"tool":"Browser Developer Tools","label":"Mandatory Category","steps":["Network tab","Headers","Cookies","Storage","Console","Sources","Application data"],"note":"Bug hunter ko browser aur terminal DONO environments understand karne chahiye. Network tab = curl ka visual version."},
 {"tool":"ProjectDiscovery Ecosystem","label":"Pipeline Concept","steps":["Input","Discovery","HTTP identification","Normalization","Analysis","Validation"],"note":"Tools ko individual commands ki tarah nahi, PIPELINE ke roop mein teach kiya jayega. Important rule: ONLY AUTHORIZED TARGETS. Rate limits, scope aur safe automation bhi sikhaya jayega."}
],
"dataToolkit":{
 "title":"23.5 Content & Data Processing — 'Security Data Processing Toolkit'",
 "note":"Bug hunting mein raw output HUGE ho sakta hai. Isliye ye 9 tools ek toolkit ke roop mein: filter → transform → dedupe → report.",
 "tools":["grep","sed","awk","cut","sort","uniq","tr","jq","xargs"],
 "miniProject":{"title":"Mini Project: 1000 → Report","desc":"Raw authorized lab output (1000 lines) convert karo: clean → normalized → deduplicated → categorized → into a report.","steps":["cat raw.txt | grep -v '^$' (clean)","tr 'A-Z' 'a-z' | sort (normalize + sort)","uniq -c (dedupe + count)","awk / cut se categories","report.txt mein save + wc -l verify"]}
},
"browserTools":{
 "categories":[
  {"icon":"🔤","name":"Encoding / Decoding","items":["Base64","URL encoding","Hex","HTML entities"]},
  {"icon":"📦","name":"Data","items":["JSON formatter","JSON validator","JSON diff","XML formatter"]},
  {"icon":"🔎","name":"Regex","items":["Regex tester","Regex debugger","Regex visualizer"]},
  {"icon":"🌐","name":"Web","items":["HTTP status reference","HTTP header reference","MIME type reference","URL parser","JWT structure viewer"]},
  {"icon":"🔐","name":"Security","items":["CVSS calculator","CWE lookup","CVE lookup","Hash identification/reference"]}
 ],
 "privacyWarning":"NEVER paste passwords, session cookies, private API keys, authentication tokens, proprietary source code, personal information, ya koi bhi sensitive data into an untrusted third-party web tool. Sensitive data ke liye LOCAL CLI alternatives use karo (lab mein har browser tool ka local equivalent available hai)."
},
"compare":{
 "title":"25 — Web Tool vs Local Tool (side-by-side)",
 "rows":[
  ["Task","Browser (convenience)","Linux (professional)"],
  ["JSON format","Online formatter","jq ."],
  ["Regex test","Regex web tool","grep -E 'pattern'"],
  ["DNS lookup","DNS web tool","dig +short"],
  ["HTTP request","Web utility","curl -i"],
  ["Packet analysis","Online reference","tcpdump / Wireshark"],
  ["Encoding","Online tool","CLI utilities (base64, hexdump)"]
 ],
 "objectiveHi":"Learner ko samajhna hai ki convenience ke liye browser tools useful hain, lekin professional workflow ke liye local tools aur reproducibility important hain.",
 "objectiveEn":"Learners should understand that browser tools are convenient, while local tooling provides better privacy, reproducibility, automation, and control."
},
"verifyBadges":[
 {"icon":"🟢","name":"Official","desc":"Resource project/organization ki OFFICIAL website. Fake lookalikes se bachav."},
 {"icon":"🔵","name":"Open Source","desc":"Source code publicly available — audit kar sakte ho, fork kar sakte ho."},
 {"icon":"🟣","name":"Free","desc":"Learning/resource access GENUINELY free — no hidden paywall."},
 {"icon":"🟡","name":"Free Tier","desc":"Kuch functionality free, advanced functionality paid. Clear limit samjho."},
 {"icon":"🟠","name":"Community Edition","desc":"Free edition exists but commercial editions bhi hain (Burp Community vs Pro)."},
 {"icon":"🔴","name":"Paid","desc":"Resource ko 'free' section mein NAHI rakhna — is badge se mark hoga."}
],
"qualityScore":{
 "weights":[["Authenticity","25%"],["Free Access","20%"],["Maintenance","15%"],["Hands-on","15%"],["Documentation","10%"],["Community","10%"],["Beginner Value","5%"]],
 "exampleBadge":{"stars":"★★★★★","authenticity":"Official","access":"Free","handsOn":"Yes","maintenance":"Active","level":"Beginner → Advanced"}
},
"paths":[
 {"name":"Beginner","icon":"🟢","steps":["Linux Basics","Terminal","Filesystem","Permissions","Networking","HTTP"]},
 {"name":"Intermediate","icon":"🔵","steps":["Bash","Git","SSH","Web Security","Burp","OWASP"]},
 {"name":"Advanced","icon":"🟣","steps":["Linux Internals","Networking Deep Dive","Python","Automation","Containers","Debugging","Security Architecture"]},
 {"name":"Bug Hunter","icon":"🔴","steps":["Web Security","Labs","HTTP Analysis","Recon Concepts","Automation","Validation","Reporting"]}
],
"dontLearnYet":{
 "items":[
  "Abhi Kubernetes ki zarurat nahi. (Level 13 containers complete hone ke baad)",
  "Abhi kernel development ki zarurat nahi. (Level 18 internals complete hone ke baad)",
  "Abhi advanced reverse engineering ki zarurat nahi. (Level 17-18 debugging + binaries complete hone ke baad)",
  "Abhi cloud infra (AWS/GCP) ki zarurat nahi. (Level 5 sysadmin solid hone ke baad)",
  "Abhi mobile security ki zarurat nahi. (Web + Linux workflow complete hone ke baad)"
 ],
 "rule":"Prerequisite complete → unlock advanced resource. Isse learning structured rahegi — confusion nahi."
},
"dependencyMap":{
 "root":"Linux",
 "children":[
  {"name":"Bash","children":[{"name":"Automation"}]},
  {"name":"Networking","children":[{"name":"DNS"},{"name":"TCP/IP"},{"name":"HTTP"}]},
  {"name":"Web Security","children":[{"name":"Browser DevTools"},{"name":"Burp"},{"name":"OWASP"}]},
  {"name":"Python","children":[{"name":"Security Automation"}]}
 ]
},
"challengeStages":[
 {"stage":1,"name":"Identify","desc":"What is this tool? Purpose, category, input/output. 2 minute mein samjho."},
 {"stage":2,"name":"Operate","desc":"Basic operation. Lab mein 3-4 basic commands successfully chalaao."},
 {"stage":3,"name":"Interpret","desc":"Output samjho. Har column/field ka meaning pata ho. Garbage output par panic nahi."},
 {"stage":4,"name":"Combine","desc":"Doosre tools ke saath use karo. Pipeline mein fit ho. Real workflow mein lage."},
 {"stage":5,"name":"Troubleshoot","desc":"Tool fail hone par diagnose karo. Error message se root cause nikalo."}
],
"safetyGate":[
 {"icon":"🟢","name":"Safe Local Lab","desc":"Use freely. Aapka lab-01 + lab.local — fully authorized, isolated environment."},
 {"icon":"🟢","name":"CTF","desc":"Follow CTF rules. Challenge scope ke andar, rules read karo pehle."},
 {"icon":"🟡","name":"Authorized Program","desc":"ONLY within written scope. Scope document bina koi tool nahi. Bug bounty = program ki rules."},
 {"icon":"🔴","name":"Random Public Target","desc":"DO NOT test without authorization. Ye RED LINE hai — illegal + unethical."}
],
"checklist":{
 "domains":[
  {"icon":"🐧","name":"Linux","items":["Terminal","Filesystem","Permissions","Users","Processes","Services","Logs","Storage","Packages","SSH"]},
  {"icon":"🌐","name":"Networking","items":["IP","Subnet","Routing","DNS","TCP","UDP","Ports","Sockets","HTTP","TLS","Packet analysis"]},
  {"icon":"💻","name":"Programming","items":["Bash","Regex","Text processing","JSON","Python","Git","Automation"]},
  {"icon":"🔐","name":"Security","items":["Authentication","Authorization","Permissions","Least privilege","Linux hardening","Web security","API security","Logging","Vulnerability research","Responsible reporting"]},
  {"icon":"🛠️","name":"Tools","items":["Linux native tools","Nmap","Wireshark","tcpdump","Burp Suite","Browser DevTools","DNS tools","HTTP tools","Security automation tools"]}
 ]
},
"certification":{
 "title":"HOST READY — Linux Security & Bug Hunting",
 "hi":"Aapko ek unfamiliar Linux host diya ja sakta hai. Aap system ko systematically understand, troubleshoot, automate aur authorized security lab ke context mein investigate kar sakte hain. Aap unfamiliar commands ke liye documentation use kar sakte hain aur bina blind copy-paste ke problem solve kar sakte hain.",
 "en":"You can work on an unfamiliar Linux host, systematically understand and troubleshoot the system, automate routine tasks, and investigate authorized security-lab environments. You can use documentation to learn unfamiliar commands and solve problems without blindly relying on copy-paste instructions."
},
"goldenRule":{
 "quote":"Tool mastery ≠ command memorization.",
 "hi":"Mastery tab hai jab learner ko pata ho problem kya hai, evidence kaha milega, kaunsa tool choose karna hai, output ka meaning kya hai, aur result ko independently verify kaise karna hai.",
 "en":"Mastery means knowing what the problem is, where to find evidence, which tool to choose, how to interpret its output, and how to independently verify the result."
}
}
