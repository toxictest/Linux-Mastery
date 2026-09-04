from pathlib import Path
from html import escape

repo = Path('/home/user/Linux-Mastery')
out = repo / 'notes.html'

page_labels = [
    ('मूल ढांचा', 'Foundation Blueprint', 'foundation'),
    ('वर्कफ़्लो', 'Workflow Map', 'workflow'),
    ('कमांड्स', 'Command Lens', 'commands'),
    ('गलतियाँ', 'Mistakes and Defense', 'pitfalls'),
    ('रिविज़न', 'Revision Sheet', 'revision'),
]

chapters = [
    ('foundation', 'Foundations', 'Foundations'),
    ('system-core', 'System Core', 'System Core'),
    ('network-web', 'Network and Web', 'Network and Web'),
    ('security-escalation', 'Security and Escalation', 'Security and Escalation'),
    ('advanced-ops', 'Advanced Operations', 'Advanced Operations'),
]

modules = [
    dict(slug='linux-mental-model', hi='Linux Mental Model', en='Linux Mental Model', chapter='foundation', tier='core',
         summary_hi='Linux ko command list ki jagah ek living system ki tarah samjho: kernel, userspace, files, memory, network, aur permissions deeply linked hote hain.',
         summary_en='Understand Linux as a living system rather than a command list: the kernel, user space, files, memory, networking, and permissions are deeply linked.',
         themes_hi=['kernel aur userspace boundary','system calls aur control flow','files, sockets, devices as interfaces','evidence-driven observation'],
         themes_en=['kernel and user-space boundary','system calls and control flow','files, sockets, and devices as interfaces','evidence-driven observation'],
         commands=['uname -a','whoami && id','cat /etc/os-release','ls -l /proc/self/fd'],
         pitfalls_hi=['output padhe bina next command chala dena','kernel aur userspace ko mix samajhna','everything is a file ko oversimplify kar dena','system ko static maan lena'],
         pitfalls_en=['running the next command without reading the output','mixing up kernel space and user space','oversimplifying the phrase everything is a file','assuming the system is static'],
         lab_hi='Ek host profile banao: OS, kernel, hostname, active user, top services, aur open sockets.',
         lab_en='Build a host profile: OS, kernel, hostname, active user, top services, and open sockets.'),
    dict(slug='terminal-mastery', hi='Terminal Mastery', en='Terminal Mastery', chapter='foundation', tier='core',
         summary_hi='Terminal tumhara control plane hai. Streams, quoting, redirection, aur pipelines samajh liye to tum text aur tools ko engineer ki tarah use karoge.',
         summary_en='The terminal is your control plane. Once you understand streams, quoting, redirection, and pipelines, you can use text and tools like an engineer.',
         themes_hi=['stdin stdout stderr','quoting aur expansion','pipes as dataflow','history aur repeatability'],
         themes_en=['stdin stdout and stderr','quoting and expansion','pipes as dataflow','history and repeatability'],
         commands=['echo $?','history | tail -20','cmd > out.txt 2> err.txt','cat file | grep key | sort | uniq -c'],
         pitfalls_hi=['stderr ko discard kar dena','unquoted variables use karna','pipeline ka meaning na samajhna','flashy one-liner ko goal bana lena'],
         pitfalls_en=['discarding stderr','using unquoted variables','not understanding the meaning of a pipeline','making flashy one-liners the goal'],
         lab_hi='Ek messy text file se top repeated lines nikaalo aur result ko file me save karo.',
         lab_en='Extract the top repeated lines from a messy text file and save the result to a file.'),
    dict(slug='filesystem-inodes', hi='Filesystem and Inodes', en='Filesystem and Inodes', chapter='foundation', tier='core',
         summary_hi='File ka asli structure naam se aage jaata hai: inode, metadata, links, mount points, aur open descriptors real story batate hain.',
         summary_en='The real structure of a file goes beyond its name: inodes, metadata, links, mount points, and open descriptors tell the real story.',
         themes_hi=['inode identity','hard links vs symlinks','mount points and storage context','deleted but open files'],
         themes_en=['inode identity','hard links versus symlinks','mount points and storage context','deleted but still open files'],
         commands=['stat file.txt','ls -li','find /path -name "*.log"','df -h && df -i'],
         pitfalls_hi=['filename ko file identity maan lena','inode exhaustion miss kar dena','symlink target verify na karna','timestamps ignore karna'],
         pitfalls_en=['treating the filename as file identity','missing inode exhaustion','failing to verify the symlink target','ignoring timestamps'],
         lab_hi='Hard link aur symlink banao, phir stat aur ls -li se compare karo.',
         lab_en='Create a hard link and a symlink, then compare them with stat and ls -li.'),
    dict(slug='permissions-identity', hi='Permissions and Identity', en='Permissions and Identity', chapter='foundation', tier='core',
         summary_hi='Linux access control ka center identity hai: user, group, sudo, ACLs, aur special bits milkar privilege boundaries banate hain.',
         summary_en='The center of Linux access control is identity: users, groups, sudo, ACLs, and special bits create privilege boundaries together.',
         themes_hi=['UID GID and groups','rwx in file vs directory context','sudo delegation','SUID SGID sticky bit'],
         themes_en=['UID GID and groups','rwx in file versus directory context','sudo delegation','SUID SGID and sticky bit'],
         commands=['id','ls -ld target','sudo -l','find / -perm -4000 2>/dev/null'],
         pitfalls_hi=['sirf file permission dekhna','chmod 777 ko fix samajhna','sudo rights ko harmless maan lena','ACLs aur capabilities ko skip karna'],
         pitfalls_en=['looking only at file permission','treating chmod 777 as a fix','assuming sudo rights are harmless','skipping ACLs and capabilities'],
         lab_hi='640, 750, 1777, aur 4755 modes ka practical meaning likho.',
         lab_en='Write the practical meaning of 640, 750, 1777, and 4755.'),
    dict(slug='processes-proc', hi='Processes and /proc', en='Processes and /proc', chapter='system-core', tier='core',
         summary_hi='Running process hi execution reality hai. PID, PPID, open files, environment, aur sockets current behavior ka snapshot dete hain.',
         summary_en='A running process is execution reality. PID, PPID, open files, environment, and sockets give you a snapshot of current behavior.',
         themes_hi=['process vs program','parent-child chain','/proc introspection','open descriptors and sockets'],
         themes_en=['process versus program','parent-child chain','proc introspection','open descriptors and sockets'],
         commands=['ps aux --sort=-%cpu | head','cat /proc/self/status','lsof -p PID','ss -tlnp'],
         pitfalls_hi=['process name par blind trust','zombie aur sleeping state confuse karna','environment leaks ignore karna','seedha kill -9 kar dena'],
         pitfalls_en=['blindly trusting the process name','confusing zombie and sleeping states','ignoring environment leaks','jumping straight to kill -9'],
         lab_hi='Ek long-running process launch karo aur uske proc aur lsof results note karo.',
         lab_en='Launch a long-running process and record its proc and lsof results.'),
    dict(slug='services-systemd', hi='Services and systemd', en='Services and systemd', chapter='system-core', tier='core',
         summary_hi='Production Linux me kaam services ke around hota hai: boot, dependencies, restart policy, unit files, aur journal-based diagnosis.',
         summary_en='In production Linux, work revolves around services: boot, dependencies, restart policy, unit files, and journal-based diagnosis.',
         themes_hi=['PID 1 and lifecycle','unit files as contracts','journalctl as source of truth','restart-loop analysis'],
         themes_en=['PID 1 and lifecycle','unit files as contracts','journalctl as source of truth','restart-loop analysis'],
         commands=['systemctl status nginx','journalctl -u nginx -n 50','systemctl list-timers','systemctl cat service.name'],
         pitfalls_hi=['status dekhkar journal skip karna','root cause ke bina restart karna','dependency chain ignore karna','hardening flags bina samjhe disable kar dena'],
         pitfalls_en=['reading status and skipping the journal','restarting without root-cause analysis','ignoring dependency chains','disabling hardening flags without understanding them'],
         lab_hi='Ek toy service banao jo timestamps likhe aur phir usme path error daal kar diagnose karo.',
         lab_en='Create a toy service that writes timestamps and then diagnose it after adding a path error.'),
    dict(slug='storage-layout', hi='Storage and Mount Layout', en='Storage and Mount Layout', chapter='system-core', tier='core',
         summary_hi='Storage diagnosis ke liye blocks, inodes, mount hierarchy, tmpfs, logs, aur growth patterns ko saath me dekhna padta hai.',
         summary_en='To diagnose storage properly, you need to view blocks, inodes, mount hierarchy, tmpfs, logs, and growth patterns together.',
         themes_hi=['blocks vs inodes','mount hierarchy','tmpfs and ephemeral paths','growth hot-spots'],
         themes_en=['blocks versus inodes','mount hierarchy','tmpfs and ephemeral paths','growth hot spots'],
         commands=['df -h','df -i','du -sh *','findmnt'],
         pitfalls_hi=['sirf df -h dekhna','inode issue miss karna','mounted path context ignore karna','rotated logs ko bhool jana'],
         pitfalls_en=['checking only df -h','missing inode issues','ignoring mounted-path context','forgetting rotated logs'],
         lab_hi='Ek disk-full scenario ki troubleshooting checklist banao.',
         lab_en='Create a troubleshooting checklist for a disk-full scenario.'),
    dict(slug='shell-scripting-discipline', hi='Shell Scripting Discipline', en='Shell Scripting Discipline', chapter='system-core', tier='core',
         summary_hi='Shell scripting tab useful hai jab intent clear ho, side effects controlled hon, aur har input safely handle kiya jaaye.',
         summary_en='Shell scripting becomes truly useful when intent is clear, side effects are controlled, and every input is handled safely.',
         themes_hi=['predictable inputs','small functions','logging discipline','safe cleanup'],
         themes_en=['predictable inputs','small functions','logging discipline','safe cleanup'],
         commands=['set -euo pipefail','trap cleanup EXIT','mktemp -d','bash -n script.sh'],
         pitfalls_hi=['debug output aur business output mix karna','unset variable ignore karna','cleanup na karna','unsafe temp files'],
         pitfalls_en=['mixing debug output with business output','ignoring unset variables','failing to clean up','using unsafe temporary files'],
         lab_hi='Ek script likho jo host summary banaye aur temporary folder clean kare.',
         lab_en='Write a script that builds a host summary and cleans up its temporary folder.'),
    dict(slug='python-for-systems', hi='Python for Systems', en='Python for Systems', chapter='system-core', tier='core',
         summary_hi='Jab parsing, state handling, testing, aur maintainability ki जरूरत badh jaye tab Python Bash se zyada controlled scale deta hai.',
         summary_en='When parsing, state handling, testing, and maintainability become more important, Python scales more cleanly than Bash.',
         themes_hi=['pathlib and structured IO','safe subprocess use','JSON and CSV handling','small testable functions'],
         themes_en=['pathlib and structured IO','safe subprocess use','JSON and CSV handling','small testable functions'],
         commands=['python3 -m venv .venv','python3 script.py --help','python3 -m json.tool file.json','pytest -q'],
         pitfalls_hi=['shell=True style thinking','timeouts na lagana','full file ko memory me load kar lena','exceptions swallow kar dena'],
         pitfalls_en=['thinking in shell equals true mode','forgetting timeouts','loading a full file into memory carelessly','swallowing exceptions'],
         lab_hi='Ek parser likho jo access log ka short JSON summary de.',
         lab_en='Write a parser that emits a short JSON summary of an access log.'),
    dict(slug='git-hygiene', hi='Git and Repo Hygiene', en='Git and Repo Hygiene', chapter='system-core', tier='core',
         summary_hi='Git evidence aur reversibility ka system hai. Security work me secret hygiene aur atomic commits central role play karte hain.',
         summary_en='Git is a system for evidence and reversibility. In security work, secret hygiene and atomic commits play a central role.',
         themes_hi=['atomic commit thinking','diff before commit','secret hygiene','rollback literacy'],
         themes_en=['atomic commit thinking','diff before commit','secret hygiene','rollback literacy'],
         commands=['git status --short','git diff --staged','git log --oneline --graph','git show COMMIT:path'],
         pitfalls_hi=['secret delete karke safe maan lena','mixed giant commits','README drift','reflog na samajhna'],
         pitfalls_en=['thinking a deleted secret is safe','creating giant mixed commits','README drift','not understanding reflog'],
         lab_hi='Ek scratch repo me teen tiny commits banao aur diff history compare karo.',
         lab_en='Create three tiny commits in a scratch repo and compare the diff history.'),
    dict(slug='networking-fundamentals', hi='Networking Fundamentals', en='Networking Fundamentals', chapter='network-web', tier='core',
         summary_hi='Network ko sirf IP aur port tak limit mat karo. Interface, route, DNS, transport state, aur packet path milkar connectivity define karte hain.',
         summary_en='Do not reduce networking to IPs and ports. Interfaces, routes, DNS, transport state, and packet paths define real connectivity together.',
         themes_hi=['layered troubleshooting','routing vs DNS vs service','socket states','packet-path visibility'],
         themes_en=['layered troubleshooting','routing versus DNS versus service','socket states','packet path visibility'],
         commands=['ip addr','ip route','dig domain +short','ss -tan'],
         pitfalls_hi=['ping successful ko complete success maan lena','DNS aur app issue mix karna','LISTEN aur ESTABLISHED confuse karna','packet evidence ke bina assume karna'],
         pitfalls_en=['treating a successful ping as total success','mixing DNS and app issues','confusing LISTEN and ESTABLISHED','assuming without packet evidence'],
         lab_hi='Ek local HTTP server chalao aur ip, ss, curl, tcpdump se flow dekho.',
         lab_en='Run a local HTTP server and inspect the flow with ip, ss, curl, and tcpdump.'),
    dict(slug='dns-and-routing', hi='DNS and Routing Paths', en='DNS and Routing Paths', chapter='network-web', tier='core',
         summary_hi='Kaafi outages me domain resolve nahi hota ya traffic wrong path le leta hai; isliye DNS aur routing ko separate failure domains ki tarah treat karo.',
         summary_en='Many outages happen because a domain does not resolve or traffic follows the wrong path, so DNS and routing should be treated as separate failure domains.',
         themes_hi=['resolver chain','default route and specific route','TTL and cache','layer isolation'],
         themes_en=['resolver chain','default route and specific route','TTL and cache','layer isolation'],
         commands=['cat /etc/resolv.conf','resolvectl status','ip route get 1.1.1.1','dig @1.1.1.1 example.com +short'],
         pitfalls_hi=['host down aur DNS down ko same samajhna','cached answer par overtrust','resolver order ignore karna','routing table na dekhna'],
         pitfalls_en=['treating host down and DNS down as the same thing','overtrusting cached answers','ignoring resolver order','failing to inspect the routing table'],
         lab_hi='Ek DNS-failure diagnosis flow chart banao.',
         lab_en='Create a diagnosis flow chart for DNS failure.'),
    dict(slug='http-apis', hi='HTTP and APIs', en='HTTP and APIs', chapter='network-web', tier='core',
         summary_hi='Browser sirf ek client hai; asli story HTTP request-response cycle me hoti hai: methods, headers, body, cookies, status codes, aur auth state.',
         summary_en='The browser is only one client; the real story lives in the HTTP request-response cycle: methods, headers, body, cookies, status codes, and auth state.',
         themes_hi=['request anatomy','status and body differences','cookies and tokens','JSON inspection'],
         themes_en=['request anatomy','status and body differences','cookies and tokens','JSON inspection'],
         commands=['curl -i URL','curl -s URL | jq .','curl -sI URL','grep -i set-cookie response.txt'],
         pitfalls_hi=['sirf status code dekhna','cookies ko noise samajhna','auth aur authz ko same maan lena','evidence save na karna'],
         pitfalls_en=['looking only at status codes','treating cookies as noise','treating auth and authz as the same','failing to save evidence'],
         lab_hi='Teen endpoints compare karo: public, authenticated, forbidden.',
         lab_en='Compare three endpoints: public, authenticated, and forbidden.'),
    dict(slug='traffic-analysis', hi='Traffic Analysis', en='Traffic Analysis', chapter='network-web', tier='core',
         summary_hi='Network troubleshooting aur web debugging dono me packet aur stream visibility bahut powerful hoti hai.',
         summary_en='Packet and stream visibility is powerful in both network troubleshooting and web debugging.',
         themes_hi=['packet capture purpose','filters and focus','protocol-layer reading','evidence capture'],
         themes_en=['packet-capture purpose','filters and focus','protocol-layer reading','evidence capture'],
         commands=['tcpdump -i any -nn port 80','tcpdump -r capture.pcap','ss -tulpn','curl -v URL'],
         pitfalls_hi=['too broad capture lena','DNS resolution on rakhkar noise badha dena','pcap save na karna','protocol layers ko mix karna'],
         pitfalls_en=['capturing too broadly','leaving DNS resolution on and adding noise','failing to save the pcap','mixing protocol layers'],
         lab_hi='Ek simple HTTP exchange capture karo aur SYN se response tak note banao.',
         lab_en='Capture a simple HTTP exchange and write notes from SYN to response.'),
    dict(slug='recon-enumeration', hi='Recon and Enumeration', en='Recon and Enumeration', chapter='network-web', tier='core',
         summary_hi='Authorized recon disciplined mapping hai: scope, collection, normalization, categorization, manual verification, aur note hygiene.',
         summary_en='Authorized recon is disciplined mapping: scope, collection, normalization, categorization, manual verification, and note hygiene.',
         themes_hi=['scope first','normalize and dedupe','service-specific depth','manual verification'],
         themes_en=['scope first','normalize and deduplicate','service-specific depth','manual verification'],
         commands=['sort -u','tr "A-Z" "a-z"','cut -d/ -f1','tee clean.txt'],
         pitfalls_hi=['tool output ko final truth maan lena','out-of-scope data mix kar dena','service-specific follow-up skip karna','notes structure na banana'],
         pitfalls_en=['treating tool output as final truth','mixing out-of-scope data','skipping service follow-up','failing to structure notes'],
         lab_hi='Messy asset list ko clean karke categories me split karo.',
         lab_en='Clean a messy asset list and split it into categories.'),
    dict(slug='web-pentest-methodology', hi='Web Pentest Methodology', en='Web Pentest Methodology', chapter='security-escalation', tier='advanced',
         summary_hi='Web testing payload bingo nahi; input, state, trust boundary, sink, response difference, aur impact reasoning ka process hai.',
         summary_en='Web testing is not payload bingo; it is a process of reasoning about input, state, trust boundaries, sinks, response differences, and impact.',
         themes_hi=['input to sink thinking','auth vs authorization','state transitions','repeatable proof'],
         themes_en=['input to sink thinking','authentication versus authorization','state transitions','repeatable proof'],
         commands=['curl -i URL','jq . response.json','grep -i content-type response.txt','diff resp1.txt resp2.txt'],
         pitfalls_hi=['payload yaad rakhkar context bhool jana','authorization bug ko login bug samajhna','single response se conclusion banana','fix language na dena'],
         pitfalls_en=['memorizing payloads while forgetting context','treating an authorization bug as a login bug','drawing conclusions from one response','failing to provide fix language'],
         lab_hi='Ek local demo app me role-based response differences ka table banao.',
         lab_en='Build a table of role-based response differences in a local demo app.'),
    dict(slug='linux-privesc', hi='Linux Privilege Escalation', en='Linux Privilege Escalation', chapter='security-escalation', tier='advanced',
         summary_hi='Mature privesc analysis trust edges par focus karti hai: sudo, SUID, caps, cron, services, writable paths, aur secrets.',
         summary_en='Mature privilege-escalation analysis focuses on trust edges: sudo, SUID, capabilities, cron, services, writable paths, and secrets.',
         themes_hi=['enumeration before exploitation','trust-edge mapping','impact beyond shell','remediation quality'],
         themes_en=['enumeration before exploitation','trust-edge mapping','impact beyond shell','remediation quality'],
         commands=['sudo -l','find / -perm -4000 2>/dev/null','getcap -r / 2>/dev/null','systemctl list-timers'],
         pitfalls_hi=['direct exploit pe jump karna','root shell ko hi sab kuch maan lena','trust chain document na karna','unsafe testing se system tod dena'],
         pitfalls_en=['jumping directly to exploits','treating a root shell as everything','not documenting the trust chain','breaking the system during unsafe testing'],
         lab_hi='Ek safe privesc checklist banao jisme sudo, SUID, caps, cron, services, secrets sections hon.',
         lab_en='Create a safe privesc checklist with sections for sudo, SUID, capabilities, cron, services, and secrets.'),
    dict(slug='ad-windows', hi='AD and Windows Thinking', en='AD and Windows Thinking', chapter='security-escalation', tier='advanced',
         summary_hi='AD ko command list nahi, identity graph ki tarah padhna chahiye: users, groups, sessions, services, ACLs, trusts, aur certificates linked hote hain.',
         summary_en='AD should be read not as a command list but as an identity graph: users, groups, sessions, services, ACLs, trusts, and certificates are linked.',
         themes_hi=['identity graph model','Kerberos awareness','ACL and delegation edges','enterprise-chain thinking'],
         themes_en=['identity graph model','Kerberos awareness','ACL and delegation edges','enterprise-chain thinking'],
         commands=['whoami /groups','klist','net user /domain','whoami /priv'],
         pitfalls_hi=['AD ko one-shot trick collection samajhna','isolated outputs par overfocus','service accounts underestimate karna','chain ko one-host problem banana'],
         pitfalls_en=['treating AD as a trick collection','overfocusing on isolated outputs','underestimating service accounts','reducing chains to one host'],
         lab_hi='Whiteboard par ek sample domain graph draw karo: user se admin path tak.',
         lab_en='Draw a sample domain graph from a user to an admin path.'),
    dict(slug='reporting-evidence', hi='Reporting and Evidence', en='Reporting and Evidence', chapter='security-escalation', tier='advanced',
         summary_hi='Finding ka final product report hota hai: precise title, affected scope, minimal proof, impact, remediation, aur verification.',
         summary_en='The final product of a finding is the report: precise title, affected scope, minimal proof, impact, remediation, and verification.',
         themes_hi=['minimal reproducible proof','technical plus business impact','clear remediation','post-fix validation'],
         themes_en=['minimal reproducible proof','technical plus business impact','clear remediation','post-fix validation'],
         commands=['curl -i URL > evidence.txt','script session.log','sha256sum file','date -Iseconds'],
         pitfalls_hi=['noisy screenshots par depend karna','impact exaggerate karna','fix omit karna','ambiguous steps likhna'],
         pitfalls_en=['depending on noisy screenshots','exaggerating impact','omitting the fix','writing ambiguous steps'],
         lab_hi='Ek sample finding likho using title, asset, proof, impact, fix, validation.',
         lab_en='Write a sample finding using title, asset, proof, impact, fix, and validation.'),
    dict(slug='linux-security-architecture', hi='Linux Security Architecture', en='Linux Security Architecture', chapter='security-escalation', tier='advanced',
         summary_hi='Security architecture tools se pehle boundaries ka design hai: least privilege, attack surface control, logging, aur recovery planning.',
         summary_en='Security architecture is the design of boundaries before it is a toolset: least privilege, attack-surface control, logging, and recovery planning.',
         themes_hi=['least privilege','attack-surface inventory','capabilities and MAC','visibility and recovery'],
         themes_en=['least privilege','attack-surface inventory','capabilities and MAC','visibility and recovery'],
         commands=['ss -tlnp','find / -perm -4000 2>/dev/null','getcap -r / 2>/dev/null','aa-status || sestatus'],
         pitfalls_hi=['security = tool purchase sochna','unused services ignore karna','hardening ke baad monitoring skip karna','documented exception na rakhna'],
         pitfalls_en=['thinking security equals buying a tool','ignoring unused services','skipping monitoring after hardening','failing to document exceptions'],
         lab_hi='Top attack surfaces aur quick controls ki hardening memo banao.',
         lab_en='Write a hardening memo with top attack surfaces and quick controls.'),
    dict(slug='containers-isolation', hi='Containers and Isolation', en='Containers and Isolation', chapter='security-escalation', tier='advanced',
         summary_hi='Container ek isolated process environment hai jo same kernel share karta hai; isliye namespaces, cgroups, mounts, aur capabilities samajhna zaroori hai.',
         summary_en='A container is an isolated process environment that still shares the same kernel, so namespaces, cgroups, mounts, and capabilities matter a lot.',
         themes_hi=['namespaces','cgroups','mount and socket risk','rootless vs privileged'],
         themes_en=['namespaces','cgroups','mount and socket risk','rootless versus privileged'],
         commands=['docker inspect CONTAINER','lsns','cat /proc/self/cgroup','id'],
         pitfalls_hi=['container ko VM samajhna','docker.sock risk ignore karna','privileged mode ko convenience maan lena','runtime config skip karna'],
         pitfalls_en=['treating a container like a VM','ignoring docker.sock risk','treating privileged mode as convenience','skipping runtime config review'],
         lab_hi='Ek container review checklist banao: user, mounts, net exposure, capabilities, secrets.',
         lab_en='Create a container review checklist for user, mounts, network exposure, capabilities, and secrets.'),
    dict(slug='debugging-methodology', hi='Debugging Methodology', en='Debugging Methodology', chapter='advanced-ops', tier='advanced',
         summary_hi='Debugging ka loop simple hai: symptom, baseline, hypothesis, minimal test, fix, validation. Guesswork ko discipline se replace karo.',
         summary_en='The debugging loop is simple: symptom, baseline, hypothesis, minimal test, fix, and validation. Replace guesswork with discipline.',
         themes_hi=['symptom clarity','baseline vs broken state','minimal experiments','post-fix regression'],
         themes_en=['symptom clarity','baseline versus broken state','minimal experiments','post-fix regression'],
         commands=['journalctl -u service -n 50','strace -f -e trace=file cmd','ss -tlnp','du -sh /var/log/*'],
         pitfalls_hi=['random fixes try karna','symptom ko root cause samajhna','before after state save na karna','validation skip karna'],
         pitfalls_en=['trying random fixes','treating the symptom as the root cause','not saving before and after state','skipping validation'],
         lab_hi='Ek broken script ya service lo aur structured debug journal maintain karo.',
         lab_en='Take a broken script or service and maintain a structured debug journal.'),
    dict(slug='memory-elf-binaries', hi='Memory, ELF, and Binaries', en='Memory, ELF, and Binaries', chapter='advanced-ops', tier='advanced',
         summary_hi='Binary ko blindly run karne se pehle uski type, strings, linked libraries, aur runtime memory model samajhna mature habit hai.',
         summary_en='A mature habit is to understand a binary’s type, strings, linked libraries, and runtime memory model before running it blindly.',
         themes_hi=['ELF structure basics','dynamic linking','strings and metadata clues','memory-layout awareness'],
         themes_en=['ELF structure basics','dynamic linking','strings and metadata clues','memory-layout awareness'],
         commands=['file /usr/bin/ls','strings /usr/bin/ls | head','ldd /usr/bin/ls','cat /proc/self/maps | head'],
         pitfalls_hi=['binary ko trust karke run kar dena','string clues ignore karna','library dependency miss karna','memory map ko abstract maan lena'],
         pitfalls_en=['blindly trusting and running a binary','ignoring string clues','missing library dependencies','treating the memory map as too abstract'],
         lab_hi='Ek system binary ka static review karo: file, strings, ldd, notes.',
         lab_en='Perform a static review of a system binary using file, strings, ldd, and notes.'),
    dict(slug='exam-roadmap', hi='Exam Roadmap and Study System', en='Exam Roadmap and Study System', chapter='advanced-ops', tier='advanced',
         summary_hi='Exam prep ka result structured loops se aata hai: topic compression, labs, revision, timed practice, weakness logs, aur writeup extraction.',
         summary_en='Exam progress comes from structured loops: topic compression, labs, revision, timed practice, weakness logs, and writeup extraction.',
         themes_hi=['active recall','daily output system','timed practice','weakness tracking'],
         themes_en=['active recall','daily output system','timed practice','weakness tracking'],
         commands=['browser find','local notes tracker','print to PDF','weekly review sheet'],
         pitfalls_hi=['sirf collect karna, output na banana','strong topics repeat karna','timed practice last me rakhna','progress track na karna'],
         pitfalls_en=['collecting without producing output','repeating only strong topics','leaving timed practice for the end','not tracking progress'],
         lab_hi='Apna 30-day plan banao jisme har din ka output aur weekly self-check ho.',
         lab_en='Build your own 30-day plan with a daily output and a weekly self-check.'),
    dict(slug='study-synthesis', hi='Study Synthesis and Note-Making', en='Study Synthesis and Note-Making', chapter='advanced-ops', tier='advanced',
         summary_hi='Strong notes sirf copy nahi hote. Unme compression, cross-links, mistakes, commands, aur next-action clarity hoti hai.',
         summary_en='Strong notes are not just copied text. They contain compression, cross-links, mistakes, commands, and clear next actions.',
         themes_hi=['compression over copying','command plus concept pairing','mistake logs','cross-linking modules'],
         themes_en=['compression over copying','command plus concept pairing','mistake logs','cross-linking modules'],
         commands=['markdown headings','tables and checklists','localStorage notes','print review sheets'],
         pitfalls_hi=['same to same copying','notes me next action na dena','commands without why likhna','weak areas hide karna'],
         pitfalls_en=['copying word for word','not adding a next action','listing commands without why they matter','hiding weak areas'],
         lab_hi='Ek topic ko 3 forms me compress karo: full note, 1-page revision, 10-line checklist.',
         lab_en='Compress one topic into three forms: full note, one-page revision, and a ten-line checklist.'),
    dict(slug='bug-bounty-prep', hi='Authorized Bug Bounty Prep', en='Authorized Bug Bounty Prep', chapter='advanced-ops', tier='advanced',
         summary_hi='Bug bounty prep ka right base legality, note hygiene, evidence discipline, scope reading, aur reproducible workflows hain.',
         summary_en='The right foundation for bug bounty prep is legality, note hygiene, evidence discipline, scope reading, and reproducible workflows.',
         themes_hi=['scope literacy','safe local practice','evidence-first workflow','future personal-note integration'],
         themes_en=['scope literacy','safe local practice','evidence-first workflow','future personal-note integration'],
         commands=['scope checklist','curl evidence saves','diff comparisons','note templates'],
         pitfalls_hi=['private ya paywalled material mirror karna','scope boundaries skip karna','raw notes organize na karna','finding reproduce na kar pana'],
         pitfalls_en=['mirroring private or paywalled material','skipping scope boundaries','not organizing raw notes','failing to reproduce a finding'],
         lab_hi='Ek dummy program scope padho aur in-scope vs out-of-scope table banao.',
         lab_en='Read a dummy program scope and create an in-scope versus out-of-scope table.'),
    dict(slug='api-security-deep-dive', hi='API Security Deep Dive', en='API Security Deep Dive', chapter='advanced-ops', tier='advanced',
         summary_hi='Modern targets me API surface first-class hota hai. Authentication, authorization, rate limits, object ownership, schema trust, aur replay behavior ko methodically test karna padta hai.',
         summary_en='In modern targets, the API surface is first class. Authentication, authorization, rate limits, object ownership, schema trust, and replay behavior must be tested methodically.',
         themes_hi=['token and session handling','object-level authorization','schema and parser trust','rate-limit and replay behavior'],
         themes_en=['token and session handling','object-level authorization','schema and parser trust','rate-limit and replay behavior'],
         commands=['curl -i -H "Authorization: Bearer TOKEN" URL','jq . response.json','diff object1.json object2.json','grep -i rate-limit headers.txt'],
         pitfalls_hi=['sirf happy-path endpoint dekhna','IDOR ko data mismatch samajhkar ignore karna','token scopes note na karna','schema validation assumptions bana lena'],
         pitfalls_en=['testing only the happy-path endpoint','ignoring IDOR as a data mismatch','not recording token scopes','assuming schema validation without proof'],
         lab_hi='Ek local API ke liye role-object matrix banao: kis role ko kaunsa object access milna chahiye.',
         lab_en='Create a role-object matrix for a local API showing which role should access which object.'),
    dict(slug='jwt-session-oauth', hi='JWT, Sessions, and OAuth Thinking', en='JWT, Sessions, and OAuth Thinking', chapter='advanced-ops', tier='advanced',
         summary_hi='Identity transport ko samjhe bina modern web testing adhuri hai. Session cookie, bearer token, refresh flow, aur delegated access alag-alag trust models rakhte hain.',
         summary_en='Modern web testing is incomplete without understanding identity transport. Session cookies, bearer tokens, refresh flows, and delegated access each use different trust models.',
         themes_hi=['session cookies vs bearer tokens','claims and scopes','refresh and expiry logic','delegated access boundaries'],
         themes_en=['session cookies versus bearer tokens','claims and scopes','refresh and expiry logic','delegated-access boundaries'],
         commands=['grep -i set-cookie response.txt','jq . header.payload.json','curl -H "Authorization: Bearer TOKEN" URL','diff unauth.txt auth.txt'],
         pitfalls_hi=['JWT ko encrypted token samajhna','scope aur role ko mix karna','expiry behavior ignore karna','token storage model note na karna'],
         pitfalls_en=['treating JWT as an encrypted token','mixing scope and role','ignoring expiry behavior','not recording the token storage model'],
         lab_hi='Ek session flow diagram banao: login, cookie set, refresh, logout, expiry.',
         lab_en='Draw a session-flow diagram: login, cookie set, refresh, logout, expiry.'),
    dict(slug='cloud-cicd-secrets', hi='Cloud, CI/CD, and Secrets Hygiene', en='Cloud, CI/CD, and Secrets Hygiene', chapter='advanced-ops', tier='advanced',
         summary_hi='Aaj ke projects me source code ke saath pipelines, environment files, deployments, aur secrets handling bhi attack surface ban jaate hain.',
         summary_en='In modern projects, pipelines, environment files, deployments, and secret handling become attack surfaces alongside source code.',
         themes_hi=['secret sprawl','build pipeline trust','artifact exposure','deployment metadata leaks'],
         themes_en=['secret sprawl','build-pipeline trust','artifact exposure','deployment metadata leaks'],
         commands=['git grep -i secret','find . -name ".env*"','grep -R "API_KEY" .','sed -n 1,120p .github/workflows/file.yml'],
         pitfalls_hi=['sample env aur real env ko mix kar dena','build logs me secret expose karna','artifact access control ignore karna','deploy metadata leak miss karna'],
         pitfalls_en=['mixing sample env files with real env files','exposing secrets in build logs','ignoring artifact access control','missing deployment-metadata leaks'],
         lab_hi='Ek repository ke liye secrets-hygiene checklist banao.',
         lab_en='Create a secrets-hygiene checklist for a repository.'),
    dict(slug='detection-engineering', hi='Detection Engineering and Validation', en='Detection Engineering and Validation', chapter='advanced-ops', tier='advanced',
         summary_hi='Security ka mature stage sirf bug dhoondhna nahi, balki detectability samajhna bhi hai: kaunsa event log hoga, kahan visible hoga, aur kya blind spot bachega.',
         summary_en='A mature security stage is not just finding bugs but understanding detectability: which event will be logged, where it will be visible, and what blind spots remain.',
         themes_hi=['telemetry source mapping','detection opportunity notes','signal-to-noise tradeoffs','validation after fix'],
         themes_en=['telemetry source mapping','detection-opportunity notes','signal-to-noise tradeoffs','validation after fix'],
         commands=['journalctl -n 100','grep -i failed /var/log/auth.log','awk patterns access.log','ss -tlnp'],
         pitfalls_hi=['finding likhkar detectability note na dena','false positive pressure ignore karna','logs aur controls ko separate worlds samajhna','fix ke baad validation na karna'],
         pitfalls_en=['writing a finding without detectability notes','ignoring false-positive pressure','treating logs and controls as separate worlds','failing to validate after the fix'],
         lab_hi='Ek finding ke saath detection opportunities aur validation steps likho.',
         lab_en='For one finding, write the detection opportunities and validation steps.'),
    dict(slug='severity-triage', hi='Severity, Triage, and Prioritization', en='Severity, Triage, and Prioritization', chapter='advanced-ops', tier='advanced',
         summary_hi='Har issue equal nahi hota. Severity ka sahi judgement exploitability, privilege, scope, recoverability, aur business impact ko balance karta hai.',
         summary_en='Not every issue is equal. Correct severity judgment balances exploitability, privilege, scope, recoverability, and business impact.',
         themes_hi=['technical vs business impact','likelihood vs severity','chaining effects','fix priority'],
         themes_en=['technical versus business impact','likelihood versus severity','chaining effects','fix priority'],
         commands=['CVSS worksheet','asset criticality note','reproduction summary','remediation timeline'],
         pitfalls_hi=['har cheez ko critical bol dena','impact aur exploitability ko mix kar dena','chain context ignore karna','fix priority language na dena'],
         pitfalls_en=['calling everything critical','mixing impact and exploitability','ignoring chain context','not providing fix-priority language'],
         lab_hi='Teen sample findings ko low, medium, high me justify karke rank karo.',
         lab_en='Rank three sample findings as low, medium, or high and justify each one.')
]

cmd_desc = {
    'uname -a': ('Kernel aur architecture baseline.', 'Kernel and architecture baseline.'),
    'whoami && id': ('Effective user aur group context.', 'Effective user and group context.'),
    'cat /etc/os-release': ('Distribution identity aur version.', 'Distribution identity and version.'),
    'ls -l /proc/self/fd': ('Open descriptors ka view.', 'A view of open descriptors.'),
    'echo $?': ('Last command ka exit status.', 'The exit status of the last command.'),
    'history | tail -20': ('Recent command trail review.', 'Review your recent command history.'),
    'cmd > out.txt 2> err.txt': ('Stdout aur stderr ko alag rakhne ka pattern.', 'A pattern for separating stdout and stderr.'),
    'cat file | grep key | sort | uniq -c': ('Classic text-pipeline pattern.', 'A classic text-pipeline pattern.'),
    'stat file.txt': ('Metadata aur inode details.', 'Metadata and inode details.'),
    'ls -li': ('Names ke saath inode numbers.', 'Inode numbers beside names.'),
    'find /path -name "*.log"': ('Targeted filesystem search.', 'Targeted filesystem search.'),
    'df -h && df -i': ('Block aur inode usage compare karo.', 'Compare block and inode usage.'),
    'id': ('Identity snapshot.', 'Identity snapshot.'),
    'ls -ld target': ('Directory permission context.', 'Directory permission context.'),
    'sudo -l': ('Delegated privilege surface.', 'Delegated privilege surface.'),
    'find / -perm -4000 2>/dev/null': ('SUID audit baseline.', 'A baseline SUID audit.'),
    'ps aux --sort=-%cpu | head': ('Top CPU consumers.', 'Top CPU consumers.'),
    'cat /proc/self/status': ('Runtime process status.', 'Runtime process status.'),
    'lsof -p PID': ('Open files aur sockets.', 'Open files and sockets.'),
    'ss -tlnp': ('Listening sockets with owning process.', 'Listening sockets with the owning process.'),
    'systemctl status nginx': ('Service health snapshot.', 'A service-health snapshot.'),
    'journalctl -u nginx -n 50': ('Recent service timeline.', 'The recent service timeline.'),
    'systemctl list-timers': ('Scheduled task map.', 'A scheduled-task map.'),
    'systemctl cat service.name': ('Effective unit definition.', 'The effective unit definition.'),
    'df -h': ('Disk usage by mounted filesystem.', 'Disk usage by mounted filesystem.'),
    'df -i': ('Inode usage by mounted filesystem.', 'Inode usage by mounted filesystem.'),
    'du -sh *': ('Top-level size estimate.', 'Top-level size estimate.'),
    'findmnt': ('Mount relationship view.', 'Mount relationship view.'),
    'set -euo pipefail': ('Defensive Bash baseline.', 'A defensive Bash baseline.'),
    'trap cleanup EXIT': ('Cleanup guarantee.', 'A cleanup guarantee.'),
    'mktemp -d': ('Safe temporary workspace.', 'A safe temporary workspace.'),
    'bash -n script.sh': ('Shell syntax validation.', 'Shell syntax validation.'),
    'python3 -m venv .venv': ('Isolated Python environment.', 'An isolated Python environment.'),
    'python3 script.py --help': ('CLI shape validation.', 'CLI-shape validation.'),
    'python3 -m json.tool file.json': ('Quick JSON validation.', 'Quick JSON validation.'),
    'pytest -q': ('Repeatable test signal.', 'A repeatable test signal.'),
    'git status --short': ('Working-tree summary.', 'A working-tree summary.'),
    'git diff --staged': ('Exactly what will be committed.', 'Exactly what will be committed.'),
    'git log --oneline --graph': ('History shape and relationships.', 'History shape and relationships.'),
    'git show COMMIT:path': ('Historical file review.', 'Historical file review.'),
    'ip addr': ('Interface aur address inventory.', 'Interface and address inventory.'),
    'ip route': ('Routing table baseline.', 'A routing-table baseline.'),
    'dig domain +short': ('Quick DNS answer.', 'A quick DNS answer.'),
    'ss -tan': ('TCP state view.', 'A TCP state view.'),
    'cat /etc/resolv.conf': ('Resolver configuration.', 'Resolver configuration.'),
    'resolvectl status': ('Resolver runtime state.', 'Resolver runtime state.'),
    'ip route get 1.1.1.1': ('Specific route decision.', 'A specific route decision.'),
    'dig @1.1.1.1 example.com +short': ('Resolver bypass check.', 'A resolver-bypass check.'),
    'curl -i URL': ('Headers ke saath response dekho.', 'Inspect the response with headers.'),
    'curl -s URL | jq .': ('Structured API inspection.', 'Structured API inspection.'),
    'curl -sI URL': ('Header-only behavior check.', 'A header-only behavior check.'),
    'grep -i set-cookie response.txt': ('Session-state clues.', 'Session-state clues.'),
    'tcpdump -i any -nn port 80': ('Packet capture without DNS noise.', 'Packet capture without DNS noise.'),
    'tcpdump -r capture.pcap': ('Saved traffic review.', 'Review saved traffic.'),
    'ss -tulpn': ('Socket inventory by protocol.', 'Socket inventory by protocol.'),
    'curl -v URL': ('Verbose HTTP exchange.', 'A verbose HTTP exchange.'),
    'sort -u': ('Deduplication step.', 'A deduplication step.'),
    'tr "A-Z" "a-z"': ('Normalization step.', 'A normalization step.'),
    'cut -d/ -f1': ('Path or host cleanup.', 'Path or host cleanup.'),
    'tee clean.txt': ('Intermediate output preservation.', 'Intermediate output preservation.'),
    'jq . response.json': ('Readable JSON analysis.', 'Readable JSON analysis.'),
    'grep -i content-type response.txt': ('Response-format clue.', 'A response-format clue.'),
    'diff resp1.txt resp2.txt': ('Behavior comparison.', 'A behavior comparison.'),
    'curl -i URL > evidence.txt': ('Repeatable web evidence capture.', 'Repeatable web evidence capture.'),
    'script session.log': ('Terminal transcript capture.', 'Terminal transcript capture.'),
    'sha256sum file': ('Artifact integrity note.', 'An artifact integrity note.'),
    'date -Iseconds': ('Precise evidence timestamp.', 'A precise evidence timestamp.'),
    'getcap -r / 2>/dev/null': ('Capability audit.', 'A capability audit.'),
    'aa-status || sestatus': ('MAC state check.', 'MAC state check.'),
    'docker inspect CONTAINER': ('Runtime container config.', 'Runtime container configuration.'),
    'lsns': ('Active namespace view.', 'The active namespace view.'),
    'cat /proc/self/cgroup': ('Cgroup context.', 'Cgroup context.'),
    'journalctl -u service -n 50': ('Service failure evidence.', 'Service-failure evidence.'),
    'strace -f -e trace=file cmd': ('File or syscall tracing.', 'File or syscall tracing.'),
    'du -sh /var/log/*': ('Disk-pressure context.', 'Disk-pressure context.'),
    'file /usr/bin/ls': ('Binary type identification.', 'Binary-type identification.'),
    'strings /usr/bin/ls | head': ('Static string clues.', 'Static string clues.'),
    'ldd /usr/bin/ls': ('Dynamic library dependencies.', 'Dynamic library dependencies.'),
    'cat /proc/self/maps | head': ('Process memory-map preview.', 'Process memory-map preview.'),
    'browser find': ('Fast on-page revision.', 'Fast on-page revision.'),
    'local notes tracker': ('Micro-progress retention.', 'Micro-progress retention.'),
    'print to PDF': ('Offline printable bundle.', 'An offline printable bundle.'),
    'weekly review sheet': ('Regular feedback loop.', 'A regular feedback loop.'),
    'markdown headings': ('Structured notes layout.', 'A structured notes layout.'),
    'tables and checklists': ('Compression and recall aid.', 'Compression and recall aid.'),
    'localStorage notes': ('Browser-side personal note storage.', 'Browser-side personal note storage.'),
    'print review sheets': ('Revision artifact creation.', 'Revision-artifact creation.'),
    'scope checklist': ('Scope clarity before testing.', 'Scope clarity before testing.'),
    'curl evidence saves': ('Preserve repeatable request proofs.', 'Preserve repeatable request proofs.'),
    'diff comparisons': ('Behavior-difference tracking.', 'Behavior-difference tracking.'),
    'note templates': ('Consistent finding capture.', 'Consistent finding capture.'),
    'curl -i -H "Authorization: Bearer TOKEN" URL': ('Authenticated request validation.', 'Authenticated-request validation.'),
    'grep -i rate-limit headers.txt': ('Rate-limit signal review.', 'Rate-limit signal review.'),
    'grep -i content-type response.txt': ('Response parser hint.', 'A response-parser hint.'),
    'grep -i set-cookie response.txt': ('Cookie issue inspection.', 'Cookie-issue inspection.'),
    'jq . header.payload.json': ('JWT claim visibility.', 'JWT claim visibility.'),
    'curl -H "Authorization: Bearer TOKEN" URL': ('Token-based API access check.', 'Token-based API access check.'),
    'diff unauth.txt auth.txt': ('Auth-state comparison.', 'Auth-state comparison.'),
    'git grep -i secret': ('Repo-level secret search.', 'Repository-level secret search.'),
    'find . -name ".env*"': ('Environment-file discovery.', 'Environment-file discovery.'),
    'grep -R "API_KEY" .': ('Hardcoded key discovery.', 'Hardcoded-key discovery.'),
    'sed -n 1,120p .github/workflows/file.yml': ('Pipeline config review.', 'Pipeline-configuration review.'),
    'journalctl -n 100': ('Recent log slice.', 'A recent log slice.'),
    'grep -i failed /var/log/auth.log': ('Auth-failure pattern review.', 'Auth-failure pattern review.'),
    'awk patterns access.log': ('Structured web-log extraction.', 'Structured web-log extraction.'),
    'CVSS worksheet': ('Severity reasoning aid.', 'A severity-reasoning aid.'),
    'asset criticality note': ('Business impact context.', 'Business-impact context.'),
    'reproduction summary': ('Condensed proof structure.', 'Condensed proof structure.'),
    'remediation timeline': ('Fix priority planning.', 'Fix-priority planning.')
}

page_total = len(modules) * len(page_labels)
chapter_map = {key: {'hi': hi, 'en': en, 'mods': []} for key, hi, en in chapters}
for idx, mod in enumerate(modules, start=1):
    mod['index'] = idx
    start = (idx - 1) * len(page_labels) + 1
    mod['start_page'] = start
    mod['end_page'] = start + len(page_labels) - 1
    chapter_map[mod['chapter']]['mods'].append(mod)


def htext(hi, en):
    return f'<span class="hi">{escape(hi)}</span><span class="en">{escape(en)}</span>'


def command_rows(cmds):
    rows = []
    for c in cmds:
        hi, en = cmd_desc.get(c, (f'{c} ko module context me inspect ya verify karne ke liye use karo.', f'Use {c} to inspect or verify this module context.'))
        rows.append(
            '<tr>'
            f'<td><code>{escape(c)}</code></td>'
            f'<td>{htext(hi, en)}</td>'
            '</tr>'
        )
    return ''.join(rows)


def list_block(hi_items, en_items, ordered=False):
    tag = 'ol' if ordered else 'ul'
    body = ''.join(f'<li>{htext(h, e)}</li>' for h, e in zip(hi_items, en_items))
    return f'<{tag}>{body}</{tag}>'


def workflow_points(mod):
    hi = [
        f'Question ko {mod["hi"]} context me classify karo.',
        'Current state collect karo aur assumptions alag rakho.',
        'Observed signal ko command output ya artifact se verify karo.',
        'Risk, impact, ya learning point ko short note me compress karo.',
        'Next action define karo: inspect, compare, fix, ya revise.'
    ]
    en = [
        f'Classify the question in the context of {mod["en"]}.',
        'Collect the current state and keep assumptions separate.',
        'Verify the observed signal with a command output or artifact.',
        'Compress the risk, impact, or learning point into a short note.',
        'Define the next action: inspect, compare, fix, or revise.'
    ]
    return hi, en


def self_checks(mod):
    hi = [
        f'Kya tum {mod["themes_hi"][0]} ko simple language me samjha sakte ho?',
        f'Kya tum {mod["themes_hi"][1]} ke liye ek relevant command ya observation de sakte ho?',
        f'Kya tum {mod["themes_hi"][2]} aur {mod["themes_hi"][3]} ko ek workflow me jod sakte ho?'
    ]
    en = [
        f'Can you explain {mod["themes_en"][0]} in simple language?',
        f'Can you name one relevant command or observation for {mod["themes_en"][1]}?',
        f'Can you connect {mod["themes_en"][2]} and {mod["themes_en"][3]} into one workflow?'
    ]
    return hi, en


def page_body(mod, variant_key):
    wf_hi, wf_en = workflow_points(mod)
    chk_hi, chk_en = self_checks(mod)
    tier_note_hi = 'Advanced module' if mod['tier'] == 'advanced' else 'Core module'
    tier_note_en = 'Advanced module' if mod['tier'] == 'advanced' else 'Core module'
    if variant_key == 'foundation':
        return f'''
        <div class="grid two">
          <section class="card">
            <h3>{htext('Focus', 'Focus')}</h3>
            <p>{htext(mod['summary_hi'], mod['summary_en'])}</p>
            <div class="note"><p>{htext('Rule: command se pehle context samjho, context ke baad command chuno.', 'Rule: understand the context before the command, then choose the command.')}</p></div>
          </section>
          <section class="card">
            <h3>{htext('Themes', 'Themes')}</h3>
            {list_block(mod['themes_hi'], mod['themes_en'])}
            <div class="ok"><p>{htext(tier_note_hi, tier_note_en)}</p></div>
          </section>
        </div>
        <section class="card wide"><h3>{htext('Why this matters', 'Why this matters')}</h3><p>{htext(f'{mod["hi"]} strong hone ka matlab hai ki tum related tools aur errors ko faster interpret kar paoge.', f'When you are strong in {mod["en"]}, you can interpret related tools and errors much faster.')}</p></section>
        '''
    if variant_key == 'workflow':
        return f'''
        <div class="grid two">
          <section class="card"><h3>{htext('Workflow steps', 'Workflow steps')}</h3>{list_block(wf_hi, wf_en, ordered=True)}</section>
          <section class="card"><h3>{htext('Signals to watch', 'Signals to watch')}</h3>{list_block(mod['themes_hi'], mod['themes_en'])}</section>
        </div>
        <section class="card wide"><h3>{htext('Compression sentence', 'Compression sentence')}</h3><p>{htext(f'{mod["hi"]} me strong learner output ko classify karke next step justify kar sakta hai.', f'A strong learner in {mod["en"]} can classify output quickly and justify the next step.')}</p></section>
        '''
    if variant_key == 'commands':
        return f'''
        <section class="card wide"><h3>{htext('Core commands', 'Core commands')}</h3><table class="table"><tr><th>Command</th><th>Use case</th></tr>{command_rows(mod['commands'])}</table></section>
        <section class="card wide"><h3>{htext('Command discipline', 'Command discipline')}</h3><p>{htext('Har command ka purpose, expected output, aur failure mode note karo.', 'Record the purpose, expected output, and failure mode of every command.')}</p></section>
        '''
    if variant_key == 'pitfalls':
        return f'''
        <div class="grid two">
          <section class="card"><h3>{htext('Common mistakes', 'Common mistakes')}</h3>{list_block(mod['pitfalls_hi'], mod['pitfalls_en'])}</section>
          <section class="card"><h3>{htext('Defensive correction', 'Defensive correction')}</h3><p>{htext('Is module me speed se zyada clarity matter karti hai. Notes, evidence, aur comparison ko habit banao.', 'In this module, clarity matters more than speed. Make notes, evidence, and comparison part of your habit.')}</p><div class="warn"><p>{htext('Unauthorized ya private/paywalled material ko mirror karna study shortcut nahi, risk hai.', 'Mirroring unauthorized or private/paywalled material is not a study shortcut; it is a risk.')}</p></div></section>
        </div>
        '''
    return f'''
    <div class="grid two">
      <section class="card"><h3>{htext('Mini lab', 'Mini lab')}</h3><p>{htext(mod['lab_hi'], mod['lab_en'])}</p><div class="ok"><p>{htext('Best output forms: short summary, commands list, mistakes list, aur next-action checklist.', 'Best output forms: short summary, command list, mistake list, and next-action checklist.')}</p></div></section>
      <section class="card"><h3>{htext('Self-check', 'Self-check')}</h3>{list_block(chk_hi, chk_en, ordered=True)}</section>
    </div>
    <section class="card wide"><h3>{htext('What you learned', 'What you learned')}</h3><p>{htext(f'{mod["hi"]} ka goal ratta nahi, repeatable understanding hai.', f'The goal of {mod["en"]} is not memorization but repeatable understanding.')}</p></section>
    '''


def render_pages():
    pages = []
    page_no = 1
    for mod in modules:
        for hi_label, en_label, variant_key in page_labels:
            pages.append(f'''
            <article class="page" id="page-{page_no}" data-page="{page_no}" data-module="{mod['index']}" data-chapter="{mod['chapter']}" data-tier="{mod['tier']}" data-variant="{variant_key}">
              <div class="page-top">
                <div class="meta-left">
                  <span class="badge">Page {page_no:03d}</span>
                  <span class="badge alt">Module {mod['index']:02d}</span>
                  <span class="badge {'adv' if mod['tier'] == 'advanced' else 'core'}">{escape(mod['tier'].upper())}</span>
                </div>
                <div class="meta-right">{htext(f'{page_total}+ printable pages', f'{page_total}+ printable pages')}</div>
              </div>
              <div class="eyebrow">Linux-Mastery Notes Vault</div>
              <h2>{htext(f'{mod["hi"]} — {hi_label}', f'{mod["en"]} — {en_label}')}</h2>
              {page_body(mod, variant_key)}
              <div class="page-foot">{htext('Original Hindi notes · English toggle · Search · Revision mode · Authorized learning only', 'Original Hindi notes · English toggle · Search · Revision mode · Authorized learning only')}</div>
            </article>
            ''')
            page_no += 1
    return ''.join(pages)


def render_toc():
    blocks = []
    for key, hi, en in chapters:
        mods = chapter_map[key]['mods']
        start = mods[0]['start_page']
        end = mods[-1]['end_page']
        items = ''.join(
            f'<a href="#page-{m["start_page"]}" data-chapter-link="{key}" data-tier-link="{m["tier"]}"><b>{m["index"]:02d}.</b> {htext(m["hi"], m["en"])} <small>{m["start_page"]:03d}-{m["end_page"]:03d}</small></a>'
            for m in mods
        )
        blocks.append(f'''
        <section class="toc-block">
          <div class="toc-head">
            <div><b>{htext(hi, en)}</b></div>
            <div class="muted">{start:03d}-{end:03d}</div>
          </div>
          <div class="toc">{items}</div>
        </section>
        ''')
    return ''.join(blocks)


def render_chapter_cards():
    cards = []
    for key, hi, en in chapters:
        mods = chapter_map[key]['mods']
        start = mods[0]['start_page']
        end = mods[-1]['end_page']
        cards.append(f'''
        <button class="chapter-card filter-btn" type="button" data-chapter-filter="{key}">
          <span class="c-tag">{htext(hi, en)}</span>
          <span class="c-meta">{len(mods)} modules · {start:03d}-{end:03d}</span>
        </button>
        ''')
    return ''.join(cards)


def render_revision_grid():
    cards = []
    for mod in modules:
        cards.append(f'''
        <a class="rev-card" href="#page-{mod['end_page']}" data-chapter-link="{mod['chapter']}">
          <div class="rev-top"><span class="badge alt">Module {mod['index']:02d}</span><span class="badge {'adv' if mod['tier'] == 'advanced' else 'core'}">{escape(mod['tier'].upper())}</span></div>
          <h3>{htext(mod['hi'], mod['en'])}</h3>
          <p>{htext(mod['summary_hi'], mod['summary_en'])}</p>
          <div class="rev-foot">{htext('Revision pages', 'Revision pages')} {mod['end_page'] - 4:03d}-{mod['end_page']:03d}</div>
        </a>
        ''')
    return ''.join(cards)


html = f'''<!DOCTYPE html>
<html lang="hi" data-lang="hi" data-view="all" data-chapter="all">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Linux-Mastery Notes Vault — {page_total}+ Printable Hindi Pages</title>
<meta name="description" content="Linux-Mastery notes vault with {page_total}+ printable Hindi pages, search, revision mode, advanced filters, and an English translation toggle.">
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
button{{font-family:var(--mono)}}
html[data-lang="hi"] .en{{display:none!important}}
html[data-lang="en"] .hi{{display:none!important}}
.wrap{{max-width:1280px;margin:0 auto}}
.toolbar{{position:sticky;top:0;z-index:20;border:1px solid var(--line2);background:rgba(6,16,8,.95);backdrop-filter:blur(8px);border-radius:16px;padding:16px 18px;margin-bottom:18px;box-shadow:0 16px 40px rgba(0,0,0,.28)}}
.toolbar h1{{font-size:clamp(28px,4vw,40px);line-height:1.12;color:#edfff5;margin:8px 0}}
.toolbar .sub{{color:var(--muted);max-width:92ch;font-size:13.5px}}
.badges,.actions,.links,.toc,.filter-row,.chapter-grid,.rev-grid{{display:flex;gap:8px;flex-wrap:wrap}}
.badge,.btn,.toc a,.filter-btn{{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line2);border-radius:999px;padding:7px 12px;font-size:12px;background:rgba(57,246,165,.06);color:var(--text)}}
.badge.alt{{background:rgba(127,220,255,.06);border-color:rgba(127,220,255,.26);color:var(--cyan)}}
.badge.adv{{background:rgba(255,203,116,.07);border-color:rgba(255,203,116,.28);color:var(--amber)}}
.badge.core{{background:rgba(57,246,165,.07);border-color:rgba(57,246,165,.28);color:var(--green)}}
.btn{{cursor:pointer;font-family:var(--mono);background:var(--panel)}}
.btn.primary{{background:var(--green);color:#032012;border-color:var(--green);font-weight:800}}
.btn.warn{{border-color:rgba(255,203,116,.35);color:var(--amber)}}
.links{{margin-top:12px}}
.links a{{font-size:12px}}
.search-shell{{display:grid;grid-template-columns:1.2fr .8fr;gap:12px;margin-top:14px}}
@media(max-width:900px){{.search-shell{{grid-template-columns:1fr}}}}
.search-box,.status-box{{border:1px solid var(--line);background:var(--panel);border-radius:16px;padding:14px}}
.search-box input{{width:100%;background:var(--bg2);border:1px solid var(--line2);border-radius:12px;padding:12px 14px;color:var(--text);font-size:13px;outline:none}}
.search-box input:focus{{border-color:var(--green)}}
.status-box{{display:flex;flex-direction:column;justify-content:center;gap:8px}}
.status-box .big{{color:#effff6;font-size:16px;font-weight:800}}
.status-box .small{{color:var(--muted);font-size:12px}}
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
.toc-shell,.chapter-shell,.revision-shell{{border:1px solid var(--line);background:var(--panel);border-radius:18px;padding:18px;margin-bottom:18px}}
.toc-shell h2,.chapter-shell h2,.revision-shell h2{{font-size:18px;color:#effff6;margin-bottom:10px}}
.toc-block + .toc-block{{margin-top:14px}}
.toc-head{{display:flex;justify-content:space-between;gap:10px;align-items:center;margin-bottom:8px}}
.toc a{{font-size:12px}}
.toc small{{color:var(--amber)}}
.muted{{color:var(--muted);font-size:12px}}
.chapter-grid{{margin-top:12px}}
.chapter-card{{cursor:pointer;border-radius:16px;padding:14px 16px;background:var(--panel2);border:1px solid var(--line);min-width:220px;text-align:left}}
.chapter-card .c-tag{{display:block;color:#effff6;font-weight:800}}
.chapter-card .c-meta{{display:block;color:var(--muted);font-size:12px;margin-top:6px}}
.filter-row{{margin-top:12px}}
.filter-btn.active{{border-color:var(--green);color:var(--green);background:rgba(57,246,165,.12)}}
.rev-grid{{margin-top:12px}}
.rev-card{{display:block;flex:1 1 280px;min-width:260px;border:1px solid var(--line);background:var(--panel2);border-radius:16px;padding:16px;color:inherit}}
.rev-card:hover{{border-color:var(--green);text-decoration:none}}
.rev-card h3{{font-size:15px;color:#effff6;margin:10px 0 8px}}
.rev-card p{{font-size:13px;color:var(--muted)}}
.rev-top{{display:flex;gap:8px;flex-wrap:wrap}}
.rev-foot{{margin-top:12px;color:var(--amber);font-size:12px}}
.page{{border:1px solid var(--line);background:linear-gradient(180deg, rgba(255,255,255,.015), transparent), var(--panel2);border-radius:20px;padding:22px;margin:0 auto 18px;box-shadow:0 20px 50px rgba(0,0,0,.24);break-inside:avoid}}
.page.hidden{{display:none!important}}
.page-top{{display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:10px}}
.meta-left,.meta-right{{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:12px}}
.eyebrow{{color:var(--green);font-size:11px;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px}}
.page h2{{font-size:clamp(22px,3vw,32px);line-height:1.2;margin-bottom:12px;color:#effff6}}
.page-foot{{margin-top:16px;padding-top:10px;border-top:1px dashed var(--line);font-size:12px;color:var(--muted)}}
.wide{{margin-top:14px}}
.screen-note{{margin-top:12px;color:var(--muted);font-size:12px}}
.empty{{display:none;border:1px dashed var(--line2);background:var(--panel);border-radius:16px;padding:22px;color:var(--muted);margin-bottom:18px;text-align:center}}
.empty.show{{display:block}}
@media print{{
  body{{background:#fff;color:#000;padding:0}}
  .toolbar,.toc-shell,.chapter-shell,.revision-shell,.empty{{display:none!important}}
  .page{{display:block!important;margin:0;border:none;border-radius:0;box-shadow:none;min-height:276mm;padding:12mm 14mm;break-after:page;background:#fff}}
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
      <span class="badge adv">Advanced filters</span>
      <span class="badge warn">Original notes only</span>
    </div>
    <h1>{htext('Linux-Mastery Notes Vault', 'Linux-Mastery Notes Vault')}</h1>
    <p class="sub">{htext(f'Yeh notes.html file {page_total} printable content pages ke saath ek bada Hindi notes vault hai. Isme search, chapter filtering, quick revision mode, advanced-only mode, print-friendly layout, aur English translation toggle diya gaya hai. Yeh direct open bhi hoti hai aur main index page me embedded bhi hai.', f'This notes.html file is a large Hindi notes vault with {page_total} printable content pages. It includes search, chapter filtering, a quick revision mode, an advanced-only mode, a print-friendly layout, and an English translation toggle. It can be opened directly and is also embedded in the main index page.')}</p>
    <div class="actions" style="margin-top:14px">
      <button class="btn primary" id="langToggle">English Translation</button>
      <button class="btn" id="printBtn">Print / Save PDF</button>
      <button class="btn" id="revisionBtn">Quick Revision Mode</button>
      <button class="btn" id="advancedBtn">Advanced Only</button>
      <button class="btn" id="showAllBtn">Show All</button>
      <a class="btn" href="index.html">Main Index</a>
      <a class="btn" href="study-hub.html">Study Hub</a>
    </div>
    <div class="links">
      <a class="btn" href="linux-privesc-hindi.html">Linux PrivEsc</a>
      <a class="btn" href="web-pentest-hindi.html">Web Pentest</a>
      <a class="btn" href="ad-windows-hindi.html">AD / Windows</a>
      <a class="btn" href="exam-roadmap-hindi.html">Exam Roadmap</a>
    </div>
    <div class="search-shell">
      <section class="search-box">
        <div class="muted" style="margin-bottom:8px">{htext('Search pages, modules, commands, mistakes, ya revision prompts', 'Search pages, modules, commands, mistakes, or revision prompts')}</div>
        <input id="searchInput" type="text" placeholder="search: privesc, jwt, systemd, reporting, docker, auth, routing..." autocomplete="off">
      </section>
      <section class="status-box">
        <div class="big" id="resultCount">{page_total} / {page_total} pages visible</div>
        <div class="small">{htext('Tip: revision mode me sirf revision sheets dikhenge. Advanced mode me sirf advanced modules dikhenge.', 'Tip: revision mode shows only revision sheets. Advanced mode shows only advanced modules.')}</div>
      </section>
    </div>
    <div class="screen-note">{htext('Tip: browser Find, page search, chapter filters, aur Print to PDF ko combine karo. Print mode me har page separate printable sheet banega.', 'Tip: combine browser Find, page search, chapter filters, and Print to PDF. In print mode, every page becomes a separate printable sheet.')}</div>
  </header>

  <section class="chapter-shell">
    <h2>{htext('Chapter Packs', 'Chapter Packs')}</h2>
    <div class="chapter-grid">{render_chapter_cards()}</div>
    <div class="filter-row">
      <button class="filter-btn active" type="button" data-mode="all">{htext('All Pages', 'All Pages')}</button>
      <button class="filter-btn" type="button" data-mode="revision">{htext('Revision Sheets', 'Revision Sheets')}</button>
      <button class="filter-btn" type="button" data-mode="advanced">{htext('Advanced Only', 'Advanced Only')}</button>
      <button class="filter-btn" type="button" data-mode="core">{htext('Core Only', 'Core Only')}</button>
      <button class="filter-btn" type="button" data-chapter-filter="all">{htext('All Chapters', 'All Chapters')}</button>
    </div>
  </section>

  <section class="revision-shell">
    <h2>{htext('Quick Revision Deck', 'Quick Revision Deck')}</h2>
    <p class="muted">{htext('Har module ka compressed jump-card. Fast revision ke liye is deck ko use karo.', 'A compressed jump card for every module. Use this deck for fast revision.')}</p>
    <div class="rev-grid">{render_revision_grid()}</div>
  </section>

  <section class="toc-shell">
    <h2>{htext('Chapter Table of Contents', 'Chapter Table of Contents')}</h2>
    {render_toc()}
  </section>

  <div class="empty" id="emptyState">{htext('Search/filter ke hisaab se koi page visible nahi hai. Doosra keyword ya mode try karo.', 'No pages are visible for this search/filter. Try another keyword or mode.')}</div>

  {render_pages()}
</div>
<script>
(() => {{
  const root = document.documentElement;
  const keyLang = 'lm_notes_lang_v2';
  const keyView = 'lm_notes_view_v2';
  const keyChapter = 'lm_notes_chapter_v2';
  const keySearch = 'lm_notes_search_v2';
  const searchInput = document.getElementById('searchInput');
  const resultCount = document.getElementById('resultCount');
  const emptyState = document.getElementById('emptyState');
  const pages = Array.from(document.querySelectorAll('.page'));
  const chapterButtons = Array.from(document.querySelectorAll('[data-chapter-filter]'));
  const modeButtons = Array.from(document.querySelectorAll('[data-mode]'));

  function setLang(lang) {{
    root.setAttribute('data-lang', lang);
    root.setAttribute('lang', lang === 'en' ? 'en' : 'hi');
    const btn = document.getElementById('langToggle');
    if (btn) btn.textContent = lang === 'en' ? 'हिंदी मोड' : 'English Translation';
    try {{ localStorage.setItem(keyLang, lang); }} catch {{}}
  }}

  function setMode(mode) {{
    root.setAttribute('data-view', mode);
    modeButtons.forEach(btn => btn.classList.toggle('active', btn.dataset.mode === mode));
    document.getElementById('revisionBtn')?.classList.toggle('primary', mode === 'revision');
    document.getElementById('advancedBtn')?.classList.toggle('primary', mode === 'advanced');
    try {{ localStorage.setItem(keyView, mode); }} catch {{}}
    applyFilters();
  }}

  function setChapter(chapter) {{
    root.setAttribute('data-chapter', chapter);
    chapterButtons.forEach(btn => btn.classList.toggle('active', btn.dataset.chapterFilter === chapter));
    try {{ localStorage.setItem(keyChapter, chapter); }} catch {{}}
    applyFilters();
  }}

  function matchMode(page, mode) {{
    if (mode === 'revision') return page.dataset.variant === 'revision';
    if (mode === 'advanced') return page.dataset.tier === 'advanced';
    if (mode === 'core') return page.dataset.tier === 'core';
    return true;
  }}

  function applyFilters() {{
    const mode = root.getAttribute('data-view') || 'all';
    const chapter = root.getAttribute('data-chapter') || 'all';
    const query = (searchInput?.value || '').trim().toLowerCase();
    let visible = 0;
    pages.forEach(page => {{
      const text = page.textContent.toLowerCase();
      const match = matchMode(page, mode) && (chapter === 'all' || page.dataset.chapter === chapter) && (!query || text.includes(query));
      page.classList.toggle('hidden', !match);
      if (match) visible += 1;
    }});
    const tocLinks = Array.from(document.querySelectorAll('.toc a'));
    tocLinks.forEach(link => {{
      const chapterOk = chapter === 'all' || link.dataset.chapterLink === chapter;
      const tierOk = mode === 'all' || mode === 'revision' ? true : (mode === 'advanced' ? link.dataset.tierLink === 'advanced' : link.dataset.tierLink === 'core');
      const textOk = !query || link.textContent.toLowerCase().includes(query);
      link.style.display = chapterOk && tierOk && textOk ? '' : 'none';
    }});
    const revCards = Array.from(document.querySelectorAll('.rev-card'));
    revCards.forEach(card => {{
      const chapterOk = chapter === 'all' || card.dataset.chapterLink === chapter;
      const textOk = !query || card.textContent.toLowerCase().includes(query);
      card.style.display = chapterOk && textOk ? '' : 'none';
    }});
    if (resultCount) resultCount.textContent = `${{visible}} / {page_total} pages visible`;
    if (emptyState) emptyState.classList.toggle('show', visible === 0);
    try {{ localStorage.setItem(keySearch, searchInput?.value || ''); }} catch {{}}
  }}

  let lang = 'hi';
  let mode = 'all';
  let chapter = 'all';
  let search = '';
  try {{ lang = localStorage.getItem(keyLang) || 'hi'; }} catch {{}}
  try {{ mode = localStorage.getItem(keyView) || 'all'; }} catch {{}}
  try {{ chapter = localStorage.getItem(keyChapter) || 'all'; }} catch {{}}
  try {{ search = localStorage.getItem(keySearch) || ''; }} catch {{}}
  setLang(lang === 'en' ? 'en' : 'hi');
  if (searchInput) searchInput.value = search;
  setChapter(chapter);
  setMode(mode);
  applyFilters();

  document.getElementById('langToggle')?.addEventListener('click', () => setLang(root.getAttribute('data-lang') === 'en' ? 'hi' : 'en'));
  document.getElementById('printBtn')?.addEventListener('click', () => window.print());
  document.getElementById('revisionBtn')?.addEventListener('click', () => setMode(root.getAttribute('data-view') === 'revision' ? 'all' : 'revision'));
  document.getElementById('advancedBtn')?.addEventListener('click', () => setMode(root.getAttribute('data-view') === 'advanced' ? 'all' : 'advanced'));
  document.getElementById('showAllBtn')?.addEventListener('click', () => {{ if (searchInput) searchInput.value = ''; setChapter('all'); setMode('all'); applyFilters(); }});
  searchInput?.addEventListener('input', applyFilters);
  chapterButtons.forEach(btn => btn.addEventListener('click', () => setChapter(btn.dataset.chapterFilter || 'all')));
  modeButtons.forEach(btn => btn.addEventListener('click', () => setMode(btn.dataset.mode || 'all')));
}})();
</script>
</body>
</html>
'''

out.write_text(html, encoding='utf-8')
print(f'Wrote {out} with {page_total} pages')
