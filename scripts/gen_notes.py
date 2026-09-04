from pathlib import Path
from html import escape

repo = Path('/home/user/Linux-Mastery')
out = repo / 'notes.html'

modules = [
    dict(slug='linux-mental-model', hi='Linux Mental Model', en='Linux Mental Model',
         summary_hi='Linux ko command list ki jagah ek living system ki tarah samjho: kernel, userspace, files, memory, network, aur permissions ek doosre se jude hote hain.',
         summary_en='Understand Linux as a living system rather than a command list: kernel, user space, files, memory, networking, and permissions are deeply connected.',
         themes_hi=['kernel aur userspace boundary','system calls aur control flow','files, sockets, devices as interfaces','evidence-driven observation'],
         themes_en=['kernel and user-space boundary','system calls and control flow','files, sockets, and devices as interfaces','evidence-driven observation'],
         commands=['uname -a','whoami && id','cat /etc/os-release','ls -l /proc/self/fd'],
         pitfalls_hi=['output padhe bina next command chala dena','kernel aur userspace ko mix samajhna','"everything is a file" ko oversimplify kar dena','system ko static maan lena'],
         pitfalls_en=['running the next command without reading the current output','mixing up kernel space and user space','oversimplifying the phrase everything is a file','assuming the system is static'],
         lab_hi='Ek host profile banao: OS, kernel, hostname, active user, top 3 services, aur open sockets.',
         lab_en='Build a host profile: OS, kernel, hostname, active user, top three services, and open sockets.'),
    dict(slug='terminal-mastery', hi='Terminal Mastery', en='Terminal Mastery',
         summary_hi='Terminal tumhara control plane hai. Streams, quoting, redirection, aur pipelines samajh liye to tum text aur tools ko engineer ki tarah use karoge.',
         summary_en='The terminal is your control plane. Once you understand streams, quoting, redirection, and pipelines, you can use text and tools like an engineer.',
         themes_hi=['stdin stdout stderr','quoting aur expansion','pipes as dataflow','history aur repeatability'],
         themes_en=['stdin stdout and stderr','quoting and expansion','pipes as dataflow','history and repeatability'],
         commands=['echo $?','history | tail -20','cmd > out.txt 2> err.txt','cat file | grep key | sort | uniq -c'],
         pitfalls_hi=['stderr ko discard kar dena','unquoted variables use karna','pipeline ka meaning na samajhna','one-liners ko goal bana lena'],
         pitfalls_en=['discarding stderr','using unquoted variables','not understanding the meaning of a pipeline','making flashy one-liners the goal'],
         lab_hi='Ek messy text file se top repeated lines निकालो aur result ko file me save karo.',
         lab_en='Extract the top repeated lines from a messy text file and save the result to a file.'),
    dict(slug='filesystem-inodes', hi='Filesystem and Inodes', en='Filesystem and Inodes',
         summary_hi='File ka asli structure naam se aage jaata hai: inode, metadata, links, mount points, aur open descriptors real story batate hain.',
         summary_en='The real structure of a file goes beyond its name: inodes, metadata, links, mount points, and open descriptors tell the real story.',
         themes_hi=['inode identity','hard links vs symlinks','mount points and storage context','deleted but open files'],
         themes_en=['inode identity','hard links versus symlinks','mount points and storage context','deleted but still open files'],
         commands=['stat file.txt','ls -li','find /path -name "*.log"','df -h && df -i'],
         pitfalls_hi=['filename ko file identity maan lena','inode exhaustion miss kar dena','symlink target verify na karna','timestamps ignore karna'],
         pitfalls_en=['treating the filename as the file identity','missing inode exhaustion','failing to verify the symlink target','ignoring timestamps'],
         lab_hi='Hard link aur symlink banao, phir stat aur ls -li se compare karo.',
         lab_en='Create a hard link and a symlink, then compare them with stat and ls -li.'),
    dict(slug='permissions-identity', hi='Permissions and Identity', en='Permissions and Identity',
         summary_hi='Linux access control ka center identity hai: user, group, sudo, ACLs, aur special bits milkar privilege boundaries banate hain.',
         summary_en='The center of Linux access control is identity: users, groups, sudo, ACLs, and special bits create privilege boundaries together.',
         themes_hi=['UID GID and groups','rwx in file vs directory context','sudo delegation','SUID SGID sticky bit'],
         themes_en=['UID GID and groups','rwx in file versus directory context','sudo delegation','SUID SGID and sticky bit'],
         commands=['id','ls -ld target','sudo -l','find / -perm -4000 2>/dev/null'],
         pitfalls_hi=['sirf file permission dekhna','chmod 777 ko fix samajhna','sudo rights ko harmless maan lena','ACLs/capabilities ko skip karna'],
         pitfalls_en=['looking only at file permission','treating chmod 777 as a fix','assuming sudo rights are harmless','skipping ACLs or capabilities'],
         lab_hi='640, 750, 1777, aur 4755 modes ka practical meaning likho.',
         lab_en='Write the practical meaning of the modes 640, 750, 1777, and 4755.'),
    dict(slug='processes-proc', hi='Processes and /proc', en='Processes and /proc',
         summary_hi='Running process hi execution reality hai. PID, PPID, open files, environment, aur sockets current behavior ka snapshot dete hain.',
         summary_en='A running process is execution reality. PID, PPID, open files, environment, and sockets give you a snapshot of current behavior.',
         themes_hi=['process vs program','parent-child chain','/proc introspection','open descriptors and sockets'],
         themes_en=['process versus program','parent-child chains','/proc introspection','open descriptors and sockets'],
         commands=['ps aux --sort=-%cpu | head','cat /proc/self/status','lsof -p PID','ss -tlnp'],
         pitfalls_hi=['process name par blind trust','zombie aur sleeping state confuse karna','environment leaks ignore karna','seedha kill -9 kar dena'],
         pitfalls_en=['blindly trusting the process name','confusing zombie and sleeping states','ignoring environment leaks','jumping straight to kill -9'],
         lab_hi='Ek long-running process launch karo aur uske /proc aur lsof results note karo.',
         lab_en='Launch a long-running process and record its /proc and lsof results.'),
    dict(slug='services-systemd', hi='Services and systemd', en='Services and systemd',
         summary_hi='Production Linux me kaam aksar services ke around hota hai: boot, dependencies, restart policy, unit files, aur journal-based diagnosis.',
         summary_en='In production Linux, work often revolves around services: boot order, dependencies, restart policy, unit files, and journal-based diagnosis.',
         themes_hi=['PID 1 and lifecycle','unit files as contracts','journalctl as source of truth','restart loop analysis'],
         themes_en=['PID 1 and lifecycle','unit files as contracts','journalctl as a source of truth','restart-loop analysis'],
         commands=['systemctl status nginx','journalctl -u nginx -n 50','systemctl list-timers','systemctl cat service.name'],
         pitfalls_hi=['status dekhkar journal skip karna','root cause ke bina restart karna','dependency chain ignore karna','hardening flags bina samjhe disable kar dena'],
         pitfalls_en=['reading status and skipping the journal','restarting without root-cause analysis','ignoring dependency chains','disabling hardening flags without understanding them'],
         lab_hi='Ek toy service banao jo file me timestamps likhe aur phir usme path error daal kar diagnose karo.',
         lab_en='Create a toy service that writes timestamps to a file and then diagnose it after adding a path error.'),
    dict(slug='networking-fundamentals', hi='Networking Fundamentals', en='Networking Fundamentals',
         summary_hi='Network ko sirf IP aur port tak limit mat karo. Interface, route, DNS, transport state, aur packet path milkar connectivity define karte hain.',
         summary_en='Do not reduce networking to IPs and ports. Interfaces, routes, DNS, transport states, and packet paths define real connectivity together.',
         themes_hi=['layered troubleshooting','routing vs DNS vs service','socket states','packet path visibility'],
         themes_en=['layered troubleshooting','routing versus DNS versus service','socket states','packet-path visibility'],
         commands=['ip addr','ip route','dig domain +short','ss -tan'],
         pitfalls_hi=['ping successful = sab theek samajhna','DNS aur app issue mix karna','LISTEN aur ESTABLISHED confuse karna','packet evidence ke bina assume karna'],
         pitfalls_en=['assuming everything is fine because ping works','mixing DNS and application issues','confusing LISTEN and ESTABLISHED','assuming without packet evidence'],
         lab_hi='Ek local HTTP server chalao aur ip, ss, curl, tcpdump se same flow ko different layers par dekho.',
         lab_en='Run a local HTTP server and observe the same flow at different layers with ip, ss, curl, and tcpdump.'),
    dict(slug='http-apis', hi='HTTP and APIs', en='HTTP and APIs',
         summary_hi='Browser sirf ek client hai; asli story HTTP request-response cycle me hoti hai: methods, headers, body, cookies, status codes, aur auth state.',
         summary_en='The browser is just one client; the real story lives in the HTTP request-response cycle: methods, headers, bodies, cookies, status codes, and authentication state.',
         themes_hi=['request anatomy','status and body differences','cookies and tokens','JSON inspection'],
         themes_en=['request anatomy','status and body differences','cookies and tokens','JSON inspection'],
         commands=['curl -i URL','curl -s URL | jq .','curl -sI URL','grep -i set-cookie response.txt'],
         pitfalls_hi=['sirf status code dekhna','cookies ko noise samajhna','auth aur authz ko same maan lena','evidence save na karna'],
         pitfalls_en=['looking only at the status code','treating cookies as noise','treating authentication and authorization as the same thing','failing to save evidence'],
         lab_hi='Teen endpoints compare karo: public, authenticated, forbidden.',
         lab_en='Compare three endpoints: public, authenticated, and forbidden.'),
    dict(slug='bash-automation', hi='Bash Automation', en='Bash Automation',
         summary_hi='Bash best tab hota hai jab script disciplined ho: set -euo pipefail, clean inputs, clear outputs, aur cleanup traps.',
         summary_en='Bash is at its best when the script is disciplined: set -euo pipefail, clean inputs, clear outputs, and cleanup traps.',
         themes_hi=['defensive shell style','functions and reuse','input validation','logging and cleanup'],
         themes_en=['defensive shell style','functions and reuse','input validation','logging and cleanup'],
         commands=['set -euo pipefail','trap cleanup EXIT','mktemp -d','shellcheck script.sh'],
         pitfalls_hi=['unquoted variables','fixed temp filenames','silent failures','error handling skip karna'],
         pitfalls_en=['unquoted variables','fixed temporary filenames','silent failures','skipping error handling'],
         lab_hi='Ek mini audit script likho jo uname, uptime, df, ss ka summary de.',
         lab_en='Write a mini-audit script that summarizes uname, uptime, df, and ss.'),
    dict(slug='python-automation', hi='Python Security Automation', en='Python Security Automation',
         summary_hi='Jab structured parsing, concurrency, testing, aur maintainability chahiye ho tab Python Bash se better scaling deta hai.',
         summary_en='When you need structured parsing, concurrency, testing, and maintainability, Python scales better than Bash.',
         themes_hi=['safe subprocess use','JSON CSV regex parsing','timeouts and retries','readable tooling'],
         themes_en=['safe subprocess use','JSON CSV and regex parsing','timeouts and retries','readable tooling'],
         commands=['python3 -m venv .venv','python3 script.py --help','python3 -m json.tool file.json','pytest -q'],
         pitfalls_hi=['shell=True style thinking','timeouts na lagana','large file ko ek saath load karna','errors swallow kar dena'],
         pitfalls_en=['thinking in shell=True mode','forgetting timeouts','loading large files all at once','swallowing errors'],
         lab_hi='Ek script likho jo access log padhe aur top 4xx paths ki report de.',
         lab_en='Write a script that reads an access log and reports the top 4xx paths.'),
    dict(slug='git-hygiene', hi='Git and Repo Hygiene', en='Git and Repo Hygiene',
         summary_hi='Git evidence aur reversibility ka system hai. Security context me secret hygiene aur atomic commits bahut important hote hain.',
         summary_en='Git is a system for evidence and reversibility. In security work, secret hygiene and atomic commits matter a lot.',
         themes_hi=['atomic commit thinking','diff before commit','secret hygiene','rollback literacy'],
         themes_en=['atomic commit thinking','diff before commit','secret hygiene','rollback literacy'],
         commands=['git status --short','git diff --staged','git log --oneline --graph','git show COMMIT:path'],
         pitfalls_hi=['secret delete karke safe maan lena','mixed giant commits','README drift','reflog na samajhna'],
         pitfalls_en=['thinking a deleted secret is now safe','giant mixed commits','README drift','not understanding reflog'],
         lab_hi='Ek scratch repo me teen tiny commits banao aur diff history compare karo.',
         lab_en='Create three tiny commits in a scratch repo and compare the diff history.'),
    dict(slug='ssh-tunneling', hi='SSH and Tunneling', en='SSH and Tunneling',
         summary_hi='SSH remote shell se aage jaata hai: key trust, host verification, bastions, aur tunnels secure access fabric banate hain.',
         summary_en='SSH goes far beyond a remote shell: key trust, host verification, bastions, and tunnels form a secure access fabric.',
         themes_hi=['public-key auth','known_hosts trust','jump hosts','local and dynamic forwarding'],
         themes_en=['public-key authentication','known_hosts trust','jump hosts','local and dynamic forwarding'],
         commands=['ssh-keygen -t ed25519','ssh -L 8080:localhost:80 host','ssh -J bastion target','cat ~/.ssh/config'],
         pitfalls_hi=['password auth ko normal maan lena','host key warning ignore karna','tunnel endpoint bhool jana','private key perms loose rakhna'],
         pitfalls_en=['treating password auth as normal','ignoring host-key warnings','forgetting the real tunnel endpoint','leaving private-key permissions too loose'],
         lab_hi='Ek local-forwarding diagram banao aur explain karo browser request kaha ja rahi hai.',
         lab_en='Draw a local-forwarding diagram and explain where the browser request actually goes.'),
    dict(slug='logging-forensics', hi='Logging and Forensics', en='Logging and Forensics',
         summary_hi='Logs hindsight nahi, evidence hote hain. Auth, app, web, aur file metadata ko jodkar timeline banti hai.',
         summary_en='Logs are not just hindsight; they are evidence. A timeline emerges when you connect auth, app, web, and file metadata.',
         themes_hi=['time-window narrowing','cross-source correlation','signal vs noise','evidence preservation'],
         themes_en=['time-window narrowing','cross-source correlation','signal versus noise','evidence preservation'],
         commands=['journalctl -n 100','grep -i "Failed password" /var/log/auth.log','awk ... access.log | sort | uniq -c','stat file'],
         pitfalls_hi=['single log ko final truth maan lena','timezone confuse karna','evidence wipe kar dena','timeline note na banana'],
         pitfalls_en=['treating one log as final truth','confusing time zones','wiping evidence','failing to build a timeline'],
         lab_hi='Auth aur access logs se ek short incident summary banao.',
         lab_en='Create a short incident summary from auth and access logs.'),
    dict(slug='linux-security-architecture', hi='Linux Security Architecture', en='Linux Security Architecture',
         summary_hi='Security architecture tools se pehle boundaries ka design hai: least privilege, attack surface control, logging, aur recovery planning.',
         summary_en='Security architecture is the design of boundaries before it is a toolset: least privilege, attack-surface control, logging, and recovery planning.',
         themes_hi=['least privilege','attack surface inventory','capabilities and MAC','visibility and recovery'],
         themes_en=['least privilege','attack-surface inventory','capabilities and MAC','visibility and recovery'],
         commands=['ss -tlnp','find / -perm -4000 2>/dev/null','getcap -r / 2>/dev/null','aa-status || sestatus'],
         pitfalls_hi=['security = tool purchase sochna','unused services ignore karna','hardening ke baad monitoring skip karna','documented exception na rakhna'],
         pitfalls_en=['thinking security equals buying a tool','ignoring unused services','skipping monitoring after hardening','failing to document exceptions'],
         lab_hi='Top 5 attack surfaces aur top 5 quick controls ki hardening memo banao.',
         lab_en='Write a hardening memo listing the top five attack surfaces and the top five quick controls.'),
    dict(slug='containers-isolation', hi='Containers and Isolation', en='Containers and Isolation',
         summary_hi='Container ek isolated process environment hai jo same kernel share karta hai; isliye namespaces, cgroups, mounts, aur capabilities ko samajhna जरूरी hai.',
         summary_en='A container is an isolated process environment that still shares the same kernel, so namespaces, cgroups, mounts, and capabilities are essential concepts.',
         themes_hi=['namespaces','cgroups','mount and socket risk','rootless vs privileged'],
         themes_en=['namespaces','cgroups','mount and socket risk','rootless versus privileged'],
         commands=['docker inspect CONTAINER','lsns','cat /proc/self/cgroup','id'],
         pitfalls_hi=['container ko VM samajhna','docker.sock risk ignore karna','--privileged ko convenience maan lena','runtime config skip karna'],
         pitfalls_en=['treating a container like a VM','ignoring docker.sock risk','treating --privileged as harmless convenience','skipping runtime config review'],
         lab_hi='Ek container review checklist banao: user, mounts, net exposure, capabilities, secrets.',
         lab_en='Create a container review checklist covering user, mounts, network exposure, capabilities, and secrets.'),
    dict(slug='debugging-methodology', hi='Debugging Methodology', en='Debugging Methodology',
         summary_hi='Debugging ka loop simple hai: symptom, baseline, hypothesis, minimal test, fix, validation. Guesswork ko discipline se replace karo.',
         summary_en='The debugging loop is simple: symptom, baseline, hypothesis, minimal test, fix, and validation. Replace guesswork with discipline.',
         themes_hi=['symptom clarity','baseline vs broken state','minimal experiments','post-fix regression'],
         themes_en=['symptom clarity','baseline versus broken state','minimal experiments','post-fix regression'],
         commands=['journalctl -u service -n 50','strace -f -e trace=file cmd','ss -tlnp','du -sh /var/log/*'],
         pitfalls_hi=['random fixes try karna','symptom ko root cause samajhna','before/after state save na karna','validation skip karna'],
         pitfalls_en=['trying random fixes','treating the symptom as the root cause','not saving before and after state','skipping validation'],
         lab_hi='Ek broken script ya service lo aur structured debug journal maintain karo.',
         lab_en='Take a broken script or service and maintain a structured debug journal.'),
    dict(slug='recon-enumeration', hi='Recon and Enumeration', en='Recon and Enumeration',
         summary_hi='Authorized recon ka center disciplined mapping hai: scope, collection, normalization, categorization, manual verification, aur note hygiene.',
         summary_en='The center of authorized recon is disciplined mapping: scope, collection, normalization, categorization, manual verification, and note hygiene.',
         themes_hi=['scope first','normalize and dedupe','service-specific depth','manual verification'],
         themes_en=['scope first','normalize and deduplicate','service-specific depth','manual verification'],
         commands=['sort -u','tr "A-Z" "a-z"','cut -d/ -f1','tee clean.txt'],
         pitfalls_hi=['tool output ko final truth maan lena','out-of-scope data mix kar dena','service-specific follow-up skip karna','notes structure na banana'],
         pitfalls_en=['treating tool output as final truth','mixing out-of-scope data','skipping service-specific follow-up','failing to structure notes'],
         lab_hi='Messy asset list ko clean करके categories me split karo.',
         lab_en='Clean a messy asset list and split it into categories.'),
    dict(slug='web-pentest-methodology', hi='Web Pentest Methodology', en='Web Pentest Methodology',
         summary_hi='Web testing payload bingo nahi; input, state, trust boundary, sink, response difference, aur impact reasoning ka process hai.',
         summary_en='Web testing is not payload bingo; it is a process of reasoning about input, state, trust boundaries, sinks, response differences, and impact.',
         themes_hi=['input to sink thinking','auth vs authorization','state transitions','repeatable proof'],
         themes_en=['input-to-sink thinking','authentication versus authorization','state transitions','repeatable proof'],
         commands=['curl -i URL','jq . response.json','grep -i "content-type" response.txt','diff resp1.txt resp2.txt'],
         pitfalls_hi=['payload yaad rakhkar context bhool jana','authorization bug ko login bug samajhna','single response se conclusion banana','fix language na dena'],
         pitfalls_en=['memorizing payloads while forgetting context','treating an authorization issue like a login issue','drawing conclusions from a single response','failing to provide fix language'],
         lab_hi='Ek local demo app me role-based response differences ka table banao.',
         lab_en='Build a table of role-based response differences in a local demo app.'),
    dict(slug='linux-privesc', hi='Linux Privilege Escalation', en='Linux Privilege Escalation',
         summary_hi='Mature privesc analysis trust edges par focus karti hai: sudo, SUID, caps, cron, services, writable paths, aur secrets.',
         summary_en='Mature privilege-escalation analysis focuses on trust edges: sudo, SUID, capabilities, cron, services, writable paths, and secrets.',
         themes_hi=['enumeration before exploitation','trust edge mapping','impact beyond shell','remediation quality'],
         themes_en=['enumeration before exploitation','trust-edge mapping','impact beyond a shell','remediation quality'],
         commands=['sudo -l','find / -perm -4000 2>/dev/null','getcap -r / 2>/dev/null','systemctl list-timers'],
         pitfalls_hi=['direct exploit pe jump karna','root shell ko hi sab kuch maan lena','trust chain document na karna','unsafe testing se system tod dena'],
         pitfalls_en=['jumping directly to exploitation','treating a root shell as the only meaningful outcome','failing to document the trust chain','breaking the system during unsafe testing'],
         lab_hi='Ek safe privesc checklist banao jisme sudo, SUID, caps, cron, services, secrets sections hon.',
         lab_en='Create a safe privesc checklist with sections for sudo, SUID, capabilities, cron, services, and secrets.'),
    dict(slug='ad-windows', hi='AD and Windows Thinking', en='AD and Windows Thinking',
         summary_hi='AD ko command list nahi, identity graph ki tarah padhna chahiye: users, groups, sessions, services, ACLs, trusts, aur certificates related hote hain.',
         summary_en='AD should be read not as a command list but as an identity graph: users, groups, sessions, services, ACLs, trusts, and certificates are all related.',
         themes_hi=['identity graph model','Kerberos awareness','ACL and delegation edges','enterprise chain thinking'],
         themes_en=['identity graph model','Kerberos awareness','ACL and delegation edges','enterprise-chain thinking'],
         commands=['whoami /groups','klist','net user /domain','whoami /priv'],
         pitfalls_hi=['AD ko one-shot trick collection samajhna','isolated outputs par overfocus','service accounts underestimate karna','chain ko one-host problem banana'],
         pitfalls_en=['treating AD as a bag of tricks','overfocusing on isolated outputs','underestimating service accounts','reducing the chain to one host'],
         lab_hi='Whiteboard par ek sample domain graph draw karo: user -> group -> server -> service account -> admin.',
         lab_en='Draw a sample domain graph on a whiteboard: user -> group -> server -> service account -> admin.'),
    dict(slug='memory-elf-binaries', hi='Memory, ELF, and Binaries', en='Memory, ELF, and Binaries',
         summary_hi='Binary ko blindly run karne se pehle uski type, strings, linked libraries, aur runtime memory model samajhna mature habit hai.',
         summary_en='A mature habit is to understand a binary’s type, strings, linked libraries, and runtime memory model before you run it blindly.',
         themes_hi=['ELF structure basics','dynamic linking','strings and metadata clues','memory layout awareness'],
         themes_en=['ELF structure basics','dynamic linking','strings and metadata clues','memory-layout awareness'],
         commands=['file /usr/bin/ls','strings /usr/bin/ls | head','ldd /usr/bin/ls','cat /proc/self/maps | head'],
         pitfalls_hi=['binary ko trust karke run kar dena','string clues ignore karna','library dependency miss karna','memory map ko abstract maan lena'],
         pitfalls_en=['trusting and running a binary blindly','ignoring string clues','missing library dependencies','treating memory maps as too abstract'],
         lab_hi='Ek system binary ka static review karo: file, strings, ldd, notes.',
         lab_en='Perform a static review of a system binary using file, strings, ldd, and notes.'),
    dict(slug='web-auth-business-logic', hi='Web Auth and Business Logic', en='Web Auth and Business Logic',
         summary_hi='Real web bugs aksar input sanitization se nahi balki auth state aur business rule mismatches se milte hain.',
         summary_en='Real web bugs often emerge not from simple input sanitization errors but from mismatches in auth state and business rules.',
         themes_hi=['login vs session vs role','workflow transitions','object ownership checks','business constraint testing'],
         themes_en=['login versus session versus role','workflow transitions','object ownership checks','business-constraint testing'],
         commands=['curl -i -b cookie.txt URL','diff before.txt after.txt','grep -i authorization request.txt','jq . response.json'],
         pitfalls_hi=['sirf payload classes dekhna','role matrix na banana','session transitions ignore karna','object ownership verify na karna'],
         pitfalls_en=['looking only at payload classes','failing to create a role matrix','ignoring session transitions','not verifying object ownership'],
         lab_hi='Ek feature ka role matrix banao: guest, user, manager, admin.',
         lab_en='Create a role matrix for one feature: guest, user, manager, and admin.'),
    dict(slug='reporting-evidence', hi='Reporting and Evidence', en='Reporting and Evidence',
         summary_hi='Finding ka final product report hota hai: precise title, affected scope, minimal proof, impact, remediation, aur verification.',
         summary_en='The final product of a finding is the report: precise title, affected scope, minimal proof, impact, remediation, and verification.',
         themes_hi=['minimal reproducible proof','technical plus business impact','clear remediation','post-fix validation'],
         themes_en=['minimal reproducible proof','technical plus business impact','clear remediation','post-fix validation'],
         commands=['curl -i URL > evidence.txt','script session.log','sha256sum file','date -Iseconds'],
         pitfalls_hi=['noisy screenshots par depend karna','impact exaggerate karna','fix omit karna','ambiguous steps likhna'],
         pitfalls_en=['depending on noisy screenshots','exaggerating impact','omitting the fix','writing ambiguous steps'],
         lab_hi='Ek sample finding likho using title, asset, proof, impact, fix, validation.',
         lab_en='Write a sample finding using title, asset, proof, impact, fix, and validation.'),
    dict(slug='exam-roadmap', hi='Exam Roadmap and Study System', en='Exam Roadmap and Study System',
         summary_hi='Exam prep ka result structured loops se aata hai: topic compression, labs, revision, timed practice, weakness logs, aur writeup extraction.',
         summary_en='Exam progress comes from structured loops: topic compression, labs, revision, timed practice, weakness logs, and writeup extraction.',
         themes_hi=['active recall','daily output system','timed practice','weakness tracking'],
         themes_en=['active recall','daily output system','timed practice','weakness tracking'],
         commands=['browser find','local notes tracker','print to PDF','weekly review sheet'],
         pitfalls_hi=['sirf collect karna, output na banana','strong topics repeat karna','timed practice last me rakhna','progress track na karna'],
         pitfalls_en=['collecting but not producing output','repeating only strong topics','leaving timed practice for the end','not tracking progress'],
         lab_hi='Apna 30-day plan banao jisme har din ka output aur har hafte ka self-check ho.',
         lab_en='Build your own 30-day plan with a daily output and a weekly self-check.'),
    dict(slug='study-synthesis', hi='Study Synthesis and Note-Making', en='Study Synthesis and Note-Making',
         summary_hi='Strong notes sirf copy nahi hote. Unme compression, cross-links, mistakes, commands, and next-action clarity hoti hai.',
         summary_en='Strong notes are not just copied text. They contain compression, cross-links, mistakes, commands, and clear next actions.',
         themes_hi=['compression over copying','command plus concept pairing','mistake logs','cross-linking modules'],
         themes_en=['compression over copying','pairing commands with concepts','mistake logs','cross-linking modules'],
         commands=['markdown headings','tables and checklists','localStorage notes','print review sheets'],
         pitfalls_hi=['same-to-same copying','notes me next action na dena','commands without why likhna','weak areas hide karna'],
         pitfalls_en=['copying material word for word','omitting the next action in notes','listing commands without why they matter','hiding weak areas'],
         lab_hi='Ek topic ko 3 forms me compress karo: full note, 1-page revision, 10-line checklist.',
         lab_en='Compress one topic into three forms: full note, one-page revision, and a ten-line checklist.'),
    dict(slug='bug-bounty-prep', hi='Authorized Bug Bounty Prep', en='Authorized Bug Bounty Prep',
         summary_hi='Bug bounty prep ka right base legality, note hygiene, evidence discipline, scope reading, aur reproducible workflows hain.',
         summary_en='The right foundation for bug bounty prep is legality, note hygiene, evidence discipline, scope reading, and reproducible workflows.',
         themes_hi=['scope literacy','safe local practice','evidence-first workflow','future personal note integration'],
         themes_en=['scope literacy','safe local practice','evidence-first workflow','future personal-note integration'],
         commands=['scope checklist','curl evidence saves','diff comparisons','note templates'],
         pitfalls_hi=['private/paywalled material mirror karna','scope boundaries skip karna','raw notes ko organize na karna','finding reproduce na kar pana'],
         pitfalls_en=['mirroring private or paywalled material','skipping scope boundaries','failing to organize raw notes','failing to reproduce a finding'],
         lab_hi='Ek dummy program scope padho aur in-scope/out-of-scope table banao.',
         lab_en='Read a dummy program scope and create an in-scope versus out-of-scope table.')
]

cmd_desc = {
    'uname -a': ('Kernel aur architecture baseline.', 'Kernel and architecture baseline.'),
    'whoami && id': ('Effective user aur group context.', 'Effective user and group context.'),
    'cat /etc/os-release': ('Distribution identity aur version.', 'Distribution identity and version.'),
    'ls -l /proc/self/fd': ('Open descriptors ka view.', 'A view of open descriptors.'),
    'echo $?': ('Last command ka exit status.', 'The exit status of the last command.'),
    'history | tail -20': ('Recent command trail review.', 'Review of recent command history.'),
    'cmd > out.txt 2> err.txt': ('Stdout/stderr separation pattern.', 'A pattern for separating stdout and stderr.'),
    'cat file | grep key | sort | uniq -c': ('Text pipeline pattern.', 'A text-pipeline pattern.'),
    'stat file.txt': ('Metadata aur inode details.', 'Metadata and inode details.'),
    'ls -li': ('Names ke saath inode numbers.', 'Inode numbers beside names.'),
    'find /path -name "*.log"': ('Targeted filesystem search.', 'Targeted filesystem search.'),
    'df -h && df -i': ('Block aur inode usage compare karo.', 'Compare block and inode usage.'),
    'id': ('Identity snapshot.', 'Identity snapshot.'),
    'ls -ld target': ('Directory permissions context.', 'Directory-permission context.'),
    'sudo -l': ('Delegated privilege surface.', 'Delegated privilege surface.'),
    'find / -perm -4000 2>/dev/null': ('SUID audit baseline.', 'A baseline SUID audit.'),
    'ps aux --sort=-%cpu | head': ('Top CPU consumers.', 'Top CPU consumers.'),
    'cat /proc/self/status': ('Runtime process status.', 'Runtime process status.'),
    'lsof -p PID': ('Open files aur sockets.', 'Open files and sockets.'),
    'ss -tlnp': ('Listening sockets with owning process.', 'Listening sockets with the owning process.'),
    'systemctl status nginx': ('Service health snapshot.', 'Service health snapshot.'),
    'journalctl -u nginx -n 50': ('Recent service timeline.', 'Recent service timeline.'),
    'systemctl list-timers': ('Scheduled tasks map.', 'Scheduled-task map.'),
    'systemctl cat service.name': ('Effective unit definition.', 'Effective unit definition.'),
    'ip addr': ('Interface aur address inventory.', 'Interface and address inventory.'),
    'ip route': ('Routing table baseline.', 'Routing-table baseline.'),
    'dig domain +short': ('Quick DNS answer.', 'Quick DNS answer.'),
    'ss -tan': ('TCP state view.', 'TCP state view.'),
    'curl -i URL': ('Request + response with headers.', 'Request and response with headers.'),
    'curl -s URL | jq .': ('Structured API inspection.', 'Structured API inspection.'),
    'curl -sI URL': ('Header-only behavior check.', 'Header-only behavior check.'),
    'grep -i set-cookie response.txt': ('Session-state clues.', 'Session-state clues.'),
    'set -euo pipefail': ('Defensive Bash baseline.', 'Defensive Bash baseline.'),
    'trap cleanup EXIT': ('Cleanup guarantee.', 'Cleanup guarantee.'),
    'mktemp -d': ('Safe temporary workspace.', 'Safe temporary workspace.'),
    'shellcheck script.sh': ('Static shell review.', 'Static shell review.'),
    'python3 -m venv .venv': ('Isolated Python environment.', 'Isolated Python environment.'),
    'python3 script.py --help': ('CLI shape validation.', 'CLI shape validation.'),
    'python3 -m json.tool file.json': ('Quick JSON validation.', 'Quick JSON validation.'),
    'pytest -q': ('Repeatable test signal.', 'Repeatable test signal.'),
    'git status --short': ('Working-tree summary.', 'Working-tree summary.'),
    'git diff --staged': ('Exactly what will be committed.', 'Exactly what will be committed.'),
    'git log --oneline --graph': ('History shape and relationships.', 'History shape and relationships.'),
    'git show COMMIT:path': ('Historical file review.', 'Historical file review.'),
    'ssh-keygen -t ed25519': ('Modern keypair generation.', 'Modern keypair generation.'),
    'ssh -L 8080:localhost:80 host': ('Local forwarding concept.', 'Local forwarding concept.'),
    'ssh -J bastion target': ('Jump-host path.', 'Jump-host path.'),
    'cat ~/.ssh/config': ('Client config review.', 'Client configuration review.'),
    'journalctl -n 100': ('Recent log slice.', 'Recent log slice.'),
    'grep -i "Failed password" /var/log/auth.log': ('Auth failure review.', 'Authentication-failure review.'),
    'awk ... access.log | sort | uniq -c': ('Top-path or top-IP summary.', 'Top-path or top-IP summary.'),
    'stat file': ('Timeline-friendly metadata.', 'Timeline-friendly metadata.'),
    'getcap -r / 2>/dev/null': ('Capability audit.', 'Capability audit.'),
    'aa-status || sestatus': ('MAC/AppArmor/SELinux state.', 'MAC/AppArmor/SELinux state.'),
    'docker inspect CONTAINER': ('Runtime container config.', 'Runtime container config.'),
    'lsns': ('Active namespaces.', 'Active namespaces.'),
    'cat /proc/self/cgroup': ('Cgroup context.', 'Cgroup context.'),
    'journalctl -u service -n 50': ('Service failure evidence.', 'Service failure evidence.'),
    'strace -f -e trace=file cmd': ('File/syscall failure tracing.', 'File or syscall failure tracing.'),
    'du -sh /var/log/*': ('Disk pressure context.', 'Disk-pressure context.'),
    'sort -u': ('Deduplication step.', 'Deduplication step.'),
    'tr "A-Z" "a-z"': ('Normalization step.', 'Normalization step.'),
    'cut -d/ -f1': ('Path or host cleanup step.', 'A path or host cleanup step.'),
    'tee clean.txt': ('Intermediate output preservation.', 'Intermediate output preservation.'),
    'jq . response.json': ('Readable JSON analysis.', 'Readable JSON analysis.'),
    'grep -i "content-type" response.txt': ('Response-format clue.', 'Response-format clue.'),
    'diff resp1.txt resp2.txt': ('Behavior comparison.', 'Behavior comparison.'),
    'whoami /groups': ('Windows group context.', 'Windows group context.'),
    'klist': ('Ticket visibility.', 'Ticket visibility.'),
    'net user /domain': ('Domain-user view.', 'Domain-user view.'),
    'whoami /priv': ('Local Windows privileges.', 'Local Windows privileges.'),
    'file /usr/bin/ls': ('Binary type identification.', 'Binary type identification.'),
    'strings /usr/bin/ls | head': ('Static string clues.', 'Static string clues.'),
    'ldd /usr/bin/ls': ('Dynamic library dependencies.', 'Dynamic library dependencies.'),
    'cat /proc/self/maps | head': ('Process memory map preview.', 'Process memory-map preview.'),
    'curl -i -b cookie.txt URL': ('Authenticated request replay.', 'Authenticated request replay.'),
    'diff before.txt after.txt': ('State-change comparison.', 'State-change comparison.'),
    'grep -i authorization request.txt': ('Authorization-header review.', 'Authorization-header review.'),
    'curl -i URL > evidence.txt': ('Repeatable web evidence capture.', 'Repeatable web evidence capture.'),
    'script session.log': ('Terminal transcript capture.', 'Terminal transcript capture.'),
    'sha256sum file': ('Artifact integrity note.', 'Artifact integrity note.'),
    'date -Iseconds': ('Precise evidence timestamps.', 'Precise evidence timestamps.'),
    'browser find': ('Fast on-page revision.', 'Fast on-page revision.'),
    'local notes tracker': ('Small progress retention.', 'Small progress retention.'),
    'print to PDF': ('Offline printable bundle.', 'Offline printable bundle.'),
    'weekly review sheet': ('Regular feedback loop.', 'A regular feedback loop.'),
    'markdown headings': ('Structured notes layout.', 'Structured notes layout.'),
    'tables and checklists': ('Compression and recall aid.', 'Compression and recall aid.'),
    'localStorage notes': ('Browser-side personal note storage.', 'Browser-side personal note storage.'),
    'print review sheets': ('Revision artifact creation.', 'Revision artifact creation.'),
    'scope checklist': ('Scope clarity before testing.', 'Scope clarity before testing.'),
    'curl evidence saves': ('Preserve repeatable request proofs.', 'Preserve repeatable request proofs.'),
    'diff comparisons': ('Behavior-difference tracking.', 'Behavior-difference tracking.'),
    'note templates': ('Consistent finding capture.', 'Consistent finding capture.')
}

page_labels = [
    ('मूल ढांचा', 'Foundation Blueprint'),
    ('वर्कफ़्लो', 'Workflow Map'),
    ('कमांड्स', 'Command Lens'),
    ('गलतियाँ', 'Mistakes and Defense'),
    ('रिविज़न', 'Revision Sheet')
]

def hblock(hi, en, tag='p', cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c}><span class="hi">{escape(hi)}</span><span class="en">{escape(en)}</span></{tag}>'

def list_block(hi_items, en_items):
    rows = []
    for hi, en in zip(hi_items, en_items):
        rows.append(f'<li><span class="hi">{escape(hi)}</span><span class="en">{escape(en)}</span></li>')
    return '<ul>' + ''.join(rows) + '</ul>'

def command_rows(cmds):
    rows = []
    for c in cmds:
        hi, en = cmd_desc.get(c, (f'{c} ko module context me validate, inspect, ya summarize karne ke liye use karo.', f'Use {c} to validate, inspect, or summarize this module context.'))
        rows.append(
            '<tr>'
            f'<td><code>{escape(c)}</code></td>'
            f'<td><span class="hi">{escape(hi)}</span><span class="en">{escape(en)}</span></td>'
            '</tr>'
        )
    return ''.join(rows)

def self_checks(module):
    hi = [
        f'Kya tum {module["themes_hi"][0]} ko simple language me samjha sakte ho?',
        f'Kya tum {module["themes_hi"][1]} ke liye ek relevant command ya observation de sakte ho?',
        f'Kya tum {module["themes_hi"][2]} aur {module["themes_hi"][3]} ko ek workflow me jod sakte ho?'
    ]
    en = [
        f'Can you explain {module["themes_en"][0]} in simple language?',
        f'Can you name one relevant command or observation for {module["themes_en"][1]}?',
        f'Can you connect {module["themes_en"][2]} and {module["themes_en"][3]} into one workflow?'
    ]
    return hi, en

def workflow_points(module):
    hi = [
        f'Question ko {module["hi"]} context me classify karo.',
        'Current state collect karo aur assumptions alag rakho.',
        'Observed signal ko command output ya artifact se verify karo.',
        'Risk, impact, ya learning point ko short note me compress karo.',
        'Next action define karo: inspect, compare, fix, ya revise.'
    ]
    en = [
        f'Classify the question in the context of {module["en"]}.',
        'Collect the current state and keep assumptions separate.',
        'Verify the observed signal with a command output or artifact.',
        'Compress the risk, impact, or learning point into a short note.',
        'Define the next action: inspect, compare, fix, or revise.'
    ]
    return hi, en

def page_html(page_no, module, variant_index):
    label_hi, label_en = page_labels[variant_index]
    title = f'{module["hi"]} — {label_hi}'
    title_en = f'{module["en"]} — {label_en}'
    wf_hi, wf_en = workflow_points(module)
    chk_hi, chk_en = self_checks(module)

    if variant_index == 0:
        body = f'''
        <div class="grid two">
          <section class="card">
            <h3>{hblock('Focus', 'Focus', 'span')}</h3>
            {hblock(module['summary_hi'], module['summary_en'])}
            <div class="note">{hblock('Rule: command se pehle context samjho, context ke baad command chuno.', 'Rule: understand the context before the command, then choose the command.')}</div>
          </section>
          <section class="card">
            <h3>{hblock('Themes', 'Themes', 'span')}</h3>
            {list_block(module['themes_hi'], module['themes_en'])}
          </section>
        </div>
        <section class="card wide">
          <h3>{hblock('Why this matters', 'Why this matters', 'span')}</h3>
          {hblock(f'{module["hi"]} strong hone ka matlab hai ki tum related tools aur errors ko faster interpret kar paoge.', f'When you are strong in {module["en"]}, you can interpret related tools and errors much faster.')}
        </section>
        '''
    elif variant_index == 1:
        body = f'''
        <div class="grid two">
          <section class="card">
            <h3>{hblock('Workflow steps', 'Workflow steps', 'span')}</h3>
            <ol>{''.join(f'<li><span class="hi">{escape(h)}</span><span class="en">{escape(e)}</span></li>' for h, e in zip(wf_hi, wf_en))}</ol>
          </section>
          <section class="card">
            <h3>{hblock('Signals to watch', 'Signals to watch', 'span')}</h3>
            {list_block(module['themes_hi'], module['themes_en'])}
          </section>
        </div>
        <section class="card wide">
          <h3>{hblock('Compression sentence', 'Compression sentence', 'span')}</h3>
          {hblock(f'{module["hi"]} me strong learner वही hai jo output ko quickly classify karke next step justify kar सके.', f'A strong learner in {module["en"]} can classify output quickly and justify the next step.')}
        </section>
        '''
    elif variant_index == 2:
        body = f'''
        <section class="card wide">
          <h3>{hblock('Core commands', 'Core commands', 'span')}</h3>
          <table class="table"><tr><th>Command</th><th>{escape('Use case')}</th></tr>{command_rows(module['commands'])}</table>
        </section>
        <section class="card wide">
          <h3>{hblock('Command discipline', 'Command discipline', 'span')}</h3>
          {hblock('Har command ka purpose, expected output, aur failure mode note karo.', 'Record the purpose, expected output, and failure mode of every command.')}
        </section>
        '''
    elif variant_index == 3:
        body = f'''
        <div class="grid two">
          <section class="card">
            <h3>{hblock('Common mistakes', 'Common mistakes', 'span')}</h3>
            {list_block(module['pitfalls_hi'], module['pitfalls_en'])}
          </section>
          <section class="card">
            <h3>{hblock('Defensive correction', 'Defensive correction', 'span')}</h3>
            {hblock(f'Is module me speed se zyada clarity matter karti hai. Notes, evidence, aur comparison ko habit banao.', f'In this module, clarity matters more than speed. Make notes, evidence, and comparison part of your habit.')}
            <div class="warn">{hblock('Unauthorized ya private/paywalled material ko mirror karna study shortcut nahi, risk hai.', 'Mirroring unauthorized or private/paywalled material is not a study shortcut; it is a risk.')}</div>
          </section>
        </div>
        '''
    else:
        body = f'''
        <div class="grid two">
          <section class="card">
            <h3>{hblock('Mini lab', 'Mini lab', 'span')}</h3>
            {hblock(module['lab_hi'], module['lab_en'])}
            <div class="ok">{hblock('Best output forms: short summary, commands list, mistakes list, aur next-action checklist.', 'Best output forms: short summary, command list, mistake list, and next-action checklist.')}</div>
          </section>
          <section class="card">
            <h3>{hblock('Self-check', 'Self-check', 'span')}</h3>
            <ol>{''.join(f'<li><span class="hi">{escape(h)}</span><span class="en">{escape(e)}</span></li>' for h, e in zip(chk_hi, chk_en))}</ol>
          </section>
        </div>
        <section class="card wide">
          <h3>{hblock('What you learned', 'What you learned', 'span')}</h3>
          {hblock(f'{module["hi"]} ka goal ratta nahi, repeatable understanding hai.', f'The goal of {module["en"]} is not memorization but repeatable understanding.')}
        </section>
        '''

    return f'''
    <article class="page" id="page-{page_no}">
      <div class="page-top">
        <div class="meta-left">
          <span class="badge">Page {page_no:03d}</span>
          <span class="badge alt">Module {((page_no - 1) // 5) + 1:02d}</span>
        </div>
        <div class="meta-right">
          <span class="hi">{page_total}+ printable pages</span>
          <span class="en">{page_total}+ printable pages</span>
        </div>
      </div>
      <div class="eyebrow">Linux-Mastery Notes Vault</div>
      <h2><span class="hi">{escape(title)}</span><span class="en">{escape(title_en)}</span></h2>
      {body}
      <div class="page-foot">
        <span class="hi">Original Hindi notes · English toggle available · Authorized learning only</span>
        <span class="en">Original Hindi notes · English toggle available · Authorized learning only</span>
      </div>
    </article>
    '''

page_total = len(modules) * 5

toc = []
for i, module in enumerate(modules, start=1):
    start = (i - 1) * 5 + 1
    end = start + 4
    toc.append(f'<a href="#page-{start}"><b>{i:02d}.</b> <span class="hi">{escape(module["hi"])}</span><span class="en">{escape(module["en"])}</span> <small>{start:03d}-{end:03d}</small></a>')

pages = []
page_no = 1
for module in modules:
    for idx in range(5):
        pages.append(page_html(page_no, module, idx))
        page_no += 1

html = f'''<!DOCTYPE html>
<html lang="hi" data-lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Linux-Mastery Notes Vault — {page_total}+ Printable Hindi Pages</title>
<meta name="description" content="Linux-Mastery notes vault with {page_total}+ printable Hindi pages and an English translation toggle.">
<style>
:root{{
  --bg:#061008; --bg2:#09150d; --panel:#0d1c13; --panel2:#11261a; --line:#1d3c2d; --line2:#2b5d46;
  --text:#dbf3e5; --muted:#8bb19d; --green:#39f6a5; --amber:#ffcb74; --red:#ff8585; --cyan:#7fdcff;
  --mono:"JetBrains Mono","Fira Code","Cascadia Code",Consolas,monospace;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:var(--mono);background:var(--bg);color:var(--text);line-height:1.68;padding:22px;background-image:radial-gradient(1000px 500px at 85% -10%, rgba(57,246,165,.08), transparent 60%),linear-gradient(rgba(57,246,165,.03) 1px, transparent 1px),linear-gradient(90deg, rgba(57,246,165,.03) 1px, transparent 1px);background-size:auto,28px 28px,28px 28px}}
a{{color:var(--green);text-decoration:none}} a:hover{{text-decoration:underline}}
html[data-lang="hi"] .en{{display:none!important}}
html[data-lang="en"] .hi{{display:none!important}}
.wrap{{max-width:1260px;margin:0 auto}}
.toolbar{{position:sticky;top:0;z-index:20;border:1px solid var(--line2);background:rgba(6,16,8,.95);backdrop-filter:blur(8px);border-radius:16px;padding:16px 18px;margin-bottom:18px;box-shadow:0 16px 40px rgba(0,0,0,.28)}}
.toolbar h1{{font-size:clamp(28px,4vw,40px);line-height:1.12;color:#edfff5;margin:8px 0}}
.toolbar .sub{{color:var(--muted);max-width:90ch;font-size:13.5px}}
.badges,.actions,.links,.toc{{display:flex;gap:8px;flex-wrap:wrap}}
.badge,.btn,.toc a{{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line2);border-radius:999px;padding:7px 12px;font-size:12px;background:rgba(57,246,165,.06);color:var(--text)}}
.badge.alt{{background:rgba(127,220,255,.06);border-color:rgba(127,220,255,.26);color:var(--cyan)}}
.btn{{cursor:pointer;font-family:var(--mono);background:var(--panel)}}
.btn.primary{{background:var(--green);color:#032012;border-color:var(--green);font-weight:800}}
.btn.warn{{border-color:rgba(255,203,116,.35);color:var(--amber)}}
.links{{margin-top:12px}}
.links a{{font-size:12px}}
.grid{{display:grid;gap:16px;margin-top:14px}}
.grid.two{{grid-template-columns:repeat(2,1fr)}}
@media(max-width:880px){{.grid.two{{grid-template-columns:1fr}}}}
.card{{border:1px solid var(--line);background:var(--panel);border-radius:16px;padding:18px}}
.card h3{{font-size:14px;color:#effff6;margin-bottom:10px}}
.card p,.card li,.card ol{{font-size:13.5px;color:var(--muted)}}
.card ul,.card ol{{padding-left:20px}}
.card li{{margin-bottom:8px}}
.note,.warn,.ok{{margin-top:12px;border-left:3px solid var(--amber);padding:10px 0 10px 12px;background:rgba(255,203,116,.06);font-size:13px;color:#ffe4b5}}
.warn{{border-left-color:var(--red);background:rgba(255,133,133,.06);color:#ffd7d7}}
.ok{{border-left-color:var(--green);background:rgba(57,246,165,.06);color:#d1fbe6}}
.table{{width:100%;border-collapse:collapse;font-size:12.5px}}
.table th,.table td{{padding:10px;border-bottom:1px dashed var(--line);text-align:left;vertical-align:top}}
.table th{{color:var(--green);font-size:11px;letter-spacing:1px;text-transform:uppercase}}
.table td{{color:var(--muted)}}
code{{font-family:var(--mono);background:var(--bg2);border:1px solid var(--line2);border-radius:8px;padding:2px 6px;color:var(--cyan)}}
.toc-shell{{border:1px solid var(--line);background:var(--panel);border-radius:18px;padding:18px;margin-bottom:18px}}
.toc-shell h2{{font-size:18px;color:#effff6;margin-bottom:10px}}
.toc a{{font-size:12px}} .toc small{{color:var(--amber)}}
.page{{border:1px solid var(--line);background:linear-gradient(180deg, rgba(255,255,255,.015), transparent), var(--panel2);border-radius:20px;padding:22px;margin:0 auto 18px;box-shadow:0 20px 50px rgba(0,0,0,.24);break-inside:avoid}}
.page-top{{display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:10px}}
.meta-left,.meta-right{{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:12px}}
.eyebrow{{color:var(--green);font-size:11px;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px}}
.page h2{{font-size:clamp(22px,3vw,32px);line-height:1.2;margin-bottom:12px;color:#effff6}}
.page-foot{{margin-top:16px;padding-top:10px;border-top:1px dashed var(--line);font-size:12px;color:var(--muted)}}
.wide{{margin-top:14px}}
.screen-note{{margin-top:12px;color:var(--muted);font-size:12px}}
@media print{{
  body{{background:#fff;color:#000;padding:0}}
  .toolbar,.toc-shell{{display:none!important}}
  .page{{margin:0;border:none;border-radius:0;box-shadow:none;min-height:276mm;padding:12mm 14mm;break-after:page;background:#fff}}
  .card{{border:1px solid #d7d7d7;background:#fff}}
  .page h2,.card h3{{color:#000}}
  .card p,.card li,.table td,.page-foot,.screen-note{{color:#222}}
  .table th{{color:#000}}
  code{{background:#f6f6f6;border-color:#ddd;color:#111}}
}}
</style>
</head>
<body>
<div class="wrap">
  <header class="toolbar">
    <div class="badges">
      <span class="badge">{page_total} content pages</span>
      <span class="badge alt">Hindi default</span>
      <span class="badge alt">English translation toggle</span>
      <span class="badge warn">Original notes only</span>
    </div>
    <h1><span class="hi">Linux-Mastery Notes Vault</span><span class="en">Linux-Mastery Notes Vault</span></h1>
    <p class="sub"><span class="hi">Yeh <b>notes.html</b> file {page_total} printable content pages ke saath ek bada Hindi notes vault hai. Upar ka button use karke English translation mode on/off kar sakte ho. Isse direct open bhi kar sakte ho aur main index page me embedded bhi hai.</span><span class="en">This <b>notes.html</b> file is a large Hindi notes vault with {page_total} printable content pages. Use the button above to turn English translation mode on or off. It can be opened directly and is also embedded inside the main index page.</span></p>
    <div class="actions" style="margin-top:14px">
      <button class="btn primary" id="langToggle">English Translation</button>
      <button class="btn" id="printBtn">Print / Save PDF</button>
      <a class="btn" href="index.html">Main Index</a>
      <a class="btn" href="study-hub.html">Study Hub</a>
      <a class="btn" href="linux-privesc-hindi.html">Linux PrivEsc</a>
      <a class="btn" href="web-pentest-hindi.html">Web Pentest</a>
    </div>
    <div class="links">
      <a class="btn" href="ad-windows-hindi.html">AD / Windows</a>
      <a class="btn" href="exam-roadmap-hindi.html">Exam Roadmap</a>
    </div>
    <div class="screen-note"><span class="hi">Tip: browser Find (Ctrl/Cmd+F) aur Print to PDF dono ka use karo. Print mode me har page alag printable sheet banega.</span><span class="en">Tip: use both browser Find (Ctrl/Cmd+F) and Print to PDF. In print mode, each card becomes a separate printable sheet.</span></div>
  </header>

  <section class="toc-shell">
    <h2><span class="hi">Quick Table of Contents</span><span class="en">Quick Table of Contents</span></h2>
    <div class="toc">{''.join(toc)}</div>
  </section>

  {''.join(pages)}
</div>
<script>
(() => {{
  const root = document.documentElement;
  const btn = document.getElementById('langToggle');
  const printBtn = document.getElementById('printBtn');
  const key = 'lm_notes_lang_v1';
  function setLang(lang) {{
    root.setAttribute('data-lang', lang);
    root.setAttribute('lang', lang === 'en' ? 'en' : 'hi');
    if (btn) btn.textContent = lang === 'en' ? 'हिंदी मोड' : 'English Translation';
    try {{ localStorage.setItem(key, lang); }} catch {{}}
  }}
  let stored = 'hi';
  try {{ stored = localStorage.getItem(key) || 'hi'; }} catch {{}}
  setLang(stored === 'en' ? 'en' : 'hi');
  btn?.addEventListener('click', () => setLang(root.getAttribute('data-lang') === 'en' ? 'hi' : 'en'));
  printBtn?.addEventListener('click', () => window.print());
}})();
</script>
</body>
</html>
'''

out.write_text(html, encoding='utf-8')
print(f'Wrote {out} with {page_total} pages')
