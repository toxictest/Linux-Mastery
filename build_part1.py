# build_part1.py — meta, vfs, man, levels 0-10
def V(s): return s.strip("\n")

META = {
  "title": "Linux-Mastery",
  "version": "2.0",
  "updated": "2026-09-04",
  "_editGuide": "YE FILE FRONTEND + TERMINAL + ANSWERS KA SINGLE SOURCE OF TRUTH HAI. Edit karo: build scripts (build_part1.py, build_part2.py, build_part3.py) ko badlo, phir 'python3 build.py' chalao — index.html + terminal + answers sab auto-update. Ya seedha content.json edit karo (valid JSON rakhna)."
}

VFS = {
  "home": "/home/learner", "user": "learner", "hostname": "lab-01",
  "dirs": ["/bin","/etc","/home","/home/learner","/home/learner/lab","/home/learner/lab/data","/tmp","/usr","/usr/bin","/var","/var/log","/proc","/dev","/run","/srv","/srv/lab","/opt","/root"],
  "files": {
    "/etc/motd": V("""Linux-Mastery LAB — authorized sandbox
Red Line active: sirf lab.local aur localhost targets allowed.
Terminal mein 'help' type karo."""),
    "/etc/hostname": V("lab-01"),
    "/etc/os-release": V("""PRETTY_NAME="Linux-Mastery Lab (Debian 12)"
VERSION_ID="12"
ID=debian"""),
    "/etc/passwd": V("""root:x:0:0:root:/root:/bin/bash
learner:x:1000:1000:Learner:/home/learner:/bin/bash
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin"""),
    "/etc/hosts": V("""127.0.0.1 localhost
10.8.0.5 lab.local lab-01"""),
    "/home/learner/welcome.txt": V("""Welcome to the Linux-Mastery lab, learner.

This is a SAFE, authorized sandbox. Red Line: no external targets.
Start with: ls, cat notes.txt, then do the Level tasks.
Tip: terminal (bottom-right) mein 'help' type karo."""),
    "/home/learner/notes.txt": V("""Study notes — Level 2 (Filesystem):
1. ls by default sirf visible files dikhata hai.
2. Hidden files dot '.' se start hote hain.
3. Try: ls -a
4. Lab task: /home/learner mein hidden file dhundo."""),
    "/home/learner/.secret_note": V("""Flag: hidden_file_found

Hidden files dot se start hoti hain. ls -a ya find . -name '.*'
Level 2 core done: files, hidden files, directories samajh aa gaye."""),
    "/home/learner/.bash_history": V("""ls
cd /var/log
cat auth.log
sudo journalctl -u sshd
grep -i failed /var/log/auth.log
ssh learner@lab.local
curl -i http://lab.local/
find /home -name '.*' -type f
chmod 640 lab/permfile.txt
ps aux | grep nginx"""),
    "/home/learner/lab/permfile.txt": V("""INSECURE: is file ke permissions world-writable hain (mode 666).
Level 3 task: 'chmod 640 /home/learner/lab/permfile.txt' se fix karo.
[mode:666]"""),
    "/home/learner/lab/data/dupes.txt": V("""nginx
postgres
redis
nginx
sshd
redis
nginx
mysql
sshd
nginx"""),
    "/home/learner/lab/data/servers.csv": V("""ip,host,os,port
10.8.0.5,web-01,debian,80
10.8.0.6,db-01,ubuntu,5432
10.8.0.7,cache-01,alpine,6379
10.8.0.8,api-01,debian,8080
10.8.0.9,log-01,fedora,9200
10.8.0.10,auth-01,debian,443"""),
    "/home/learner/lab/recon/raw_output.txt": V("""WEB-01.LAB.LOCAL
web-01.lab.local
API-01.lab.local
web-01.lab.local
api-01.LAB.local
db-01.lab.local
WEB-01.lab.local
api-01.lab.local
DB-01.LAB.LOCAL
web-01.lab.local
log-01.lab.local
api-01.lab.local"""),
    "/var/log/sys.log": V("""Sep 04 07:00:01 lab-01 systemd[1]: Started Daily apt upgrade.
Sep 04 07:02:11 lab-01 kernel: [  120.4] eth0: link up
Sep 04 07:10:45 lab-01 systemd[1]: Started nginx - high performance web server.
Sep 04 07:11:02 lab-01 sshd[1834]: Server listening on 0.0.0.0 port 22.
Sep 04 07:15:30 lab-01 systemd[1]: memory pressure detected on /
Sep 04 07:18:00 lab-01 CRON[2210]: (root) CMD (debian-sa1 1)
Sep 04 07:22:14 lab-01 kernel: [ 1100.7] out of memory: Killed process 2455 (stress-ng)
Sep 04 07:25:00 lab-01 systemd[1]: Stopping lab service..."""),
    "/var/log/auth.log": V("""Sep 04 07:05:12 lab-01 sshd[1834]: Failed password for root from 203.0.113.15 port 51234 ssh2
Sep 04 07:05:19 lab-01 sshd[1834]: Failed password for root from 203.0.113.15 port 51235 ssh2
Sep 04 07:05:26 lab-01 sshd[1834]: Failed password for root from 203.0.113.15 port 51236 ssh2
Sep 04 07:05:33 lab-01 sshd[1834]: Failed password for root from 203.0.113.15 port 51237 ssh2
Sep 04 07:06:01 lab-01 sshd[1834]: Connection closed by 203.0.113.15 port 51237 [preauth]
Sep 04 07:12:40 lab-01 sshd[1901]: Accepted publickey for learner from 10.8.0.10 port 40122 ssh2: ED25519
Sep 04 07:12:40 lab-01 sshd[1901]: pam_unix(sshd:session): session opened for user learner(uid=1000)
Sep 04 07:30:00 lab-01 sudo[2010]: learner : TTY=pts/0 ; PWD=/home/learner ; USER=root ; COMMAND=/usr/bin/journalctl -u sshd
Sep 04 07:41:22 lab-01 sshd[1901]: pam_unix(sshd:session): session closed for user learner
Sep 04 07:50:10 lab-01 sshd[2100]: Failed password for invalid user admin from 198.51.100.7 port 33012 ssh2"""),
    "/var/log/app.log": V("""2026-09-04T07:00:12Z INFO  Starting lab-service v1.4.2
2026-09-04T07:00:13Z INFO  Listening on 127.0.0.1:8080
2026-09-04T07:05:00Z WARN  Slow query: 2.3s (users table)
2026-09-04T07:10:45Z ERROR Connection refused: db-01:5432
2026-09-04T07:11:02Z INFO  Reconnected to db-01:5432
2026-09-04T07:20:30Z ERROR Disk quota exceeded for /var/log/app
2026-09-04T07:25:00Z INFO  Log rotated: app.log.1.gz
2026-09-04T07:30:00Z WARN  Memory usage 87% (limit 100%)"""),
    "/var/log/nginx/access.log": V("""10.8.0.10 - - [04/Sep/2026:07:01:22 +0000] "GET / HTTP/1.1" 200 512
10.8.0.10 - - [04/Sep/2026:07:02:10 +0000] "GET /index.html HTTP/1.1" 200 512
203.0.113.42 - - [04/Sep/2026:07:05:33 +0000] "GET /admin HTTP/1.1" 403 152
203.0.113.42 - - [04/Sep/2026:07:05:41 +0000] "GET /wp-login.php HTTP/1.1" 404 175
203.0.113.42 - - [04/Sep/2026:07:06:02 +0000] "GET /.env HTTP/1.1" 403 152
10.8.0.10 - - [04/Sep/2026:07:12:40 +0000] "GET /api/users HTTP/1.1" 200 128
198.51.100.7 - - [04/Sep/2026:07:20:15 +0000] "POST /login HTTP/1.1" 401 88
198.51.100.7 - - [04/Sep/2026:07:20:22 +0000] "POST /login HTTP/1.1" 401 88
10.8.0.10 - - [04/Sep/2026:07:30:00 +0000] "GET /healthz HTTP/1.1" 200 2
10.8.0.10 - - [04/Sep/2026:07:45:11 +0000] "GET /favicon.ico HTTP/1.1" 404 175"""),
    "/proc/version": V("Linux version 6.1.0-21-lm (build@lab) (gcc 12.2.0) #1 SMP Linux-Mastery Lab"),
    "/srv/lab/index.html": V("<!doctype html><html><body><h1>Lab Service v1.4</h1><p>Authorized lab endpoint.</p></body></html>"),
    "/srv/lab/.env": V("""DB_HOST=db-01
DB_PASSWORD=sup3rS3cret-LabOnly
API_KEY=lm-lab-0001
SECRET=do-not-put-in-git"""),
    "/srv/lab/api_users.json": V("""[
  {"user": "alice", "role": "admin", "last_seen": "2026-09-03"},
  {"user": "bob", "role": "user", "last_seen": "2026-09-04"}
]"""),
  }
}

MAN = {
  "ls": "ls [-a] [-l] [-h] [path] — directory listing. -a: hidden files dikhao, -l: long format (perms/owner/size), -h: human-readable sizes.",
  "cd": "cd [path] — directory change. cd .. parent, cd ~ home, cd - last dir.",
  "cat": "cat <file...> — file print karo. Multiple files join ho jaate hain. Bade files ke liye less/head/tail use karo.",
  "grep": "grep [-i] [-n] [-c] [-v] [-r] <pattern> [file] — text search. -i: case-insensitive, -n: line number, -c: count, -v: invert. File na do to stdin padhta hai.",
  "find": "find [path] [-name pattern] [-type f|d] [-perm nnn] — filesystem tree search. Example: find /home -name '*.txt' -type f",
  "head": "head [-n N] [file] — pehle N lines (default 10).",
  "tail": "tail [-n N] [file] — aakhri N lines (default 10). Live: tail -f file.",
  "sort": "sort [-r] [-n] [-u] [file] — lines sort. -r reverse, -n numeric, -u unique. uniq se pehle hamesha sort.",
  "uniq": "uniq [-c] [file] — adjacent duplicate lines collapse. Pehle sort karo warna kaam nahi karega!",
  "cut": "cut -d<delim> -f<N> [file] — fields extract. Example: cut -d, -f2 servers.csv",
  "tr": "tr <set1> <set2> — characters translate. tr 'A-Z' 'a-z' lowercase. 'tr -d' delete set.",
  "wc": "wc [-l] [-w] [-c] [file] — lines / words / bytes count.",
  "sed": "sed 's/pattern/replacement/' [file] — stream editor. Line-by-line transform. -e multiple scripts.",
  "awk": "awk '{print $1, $3}' [file] — field processor. $0 = full line, $N = field, NR = line number. BEGIN/END blocks.",
  "jq": "jq [filter] [file] — JSON processor. jq . = pretty print, jq .user[0].role = path extract. Security data processing ka core.",
  "ps": "ps aux — all processes (PID, USER, %CPU, CMD). Custom: ps -o pid,ppid,user,cmd ax",
  "top": "top — live process monitor. CPU/MEM sorted. q to quit (lab mein snapshot milta hai).",
  "free": "free [-h] — memory: total/used/free/buff-cache. -h human readable.",
  "df": "df [-h] — filesystem space usage per mount.",
  "du": "du [-sh] [path] — actual directory/file sizes. du -sh * = top-level sizes.",
  "ip": "ip addr | ip route | ip neigh | ip link — interfaces, routes, neighbors. ifconfig/route ka modern replacement.",
  "ss": "ss -tlnp — listening TCP sockets + owning process. ss -tan — all TCP connections + states.",
  "ping": "ping [-c N] <host> — ICMP reachability test. LAB RULE: sirf lab.local / localhost allowed (Red Line).",
  "dig": "dig <host> [A|MX|TXT] — DNS query. +short = concise, +trace = full resolution journey.",
  "host": "host <name> — simple DNS lookup. host -t MX example.com = mail records.",
  "curl": "curl [-i] [-v] [-X METHOD] [-H header] [-d data] <url> — HTTP client. -i: headers dikhao. LAB RULE: sirf http://lab.local/* aur localhost:8080.",
  "nmap": "nmap [opts] <target> — network discovery (ports/services). LAB RULE: sirf lab.local. External target = RED LINE violation.",
  "tcpdump": "tcpdump [-i any] <filter> — packet capture. -n: no DNS resolve, -c N: N packets. LAB RULE: lab traffic only.",
  "strace": "strace [-p <pid>] [cmd] — system calls trace. -c: summary, -e trace=openat: filter. Permission/network debugging ka weapon.",
  "lsof": "lsof [-i :port] [-p <pid>] [-u user] — list open files. lsof -i :8080 = kaun us port pe hai. lsof +L1 = deleted-but-open files.",
  "journalctl": "journalctl [-u unit] [-n N] [--since '10 min ago'] [-p err] — systemd journal logs. Log investigation ka core tool.",
  "systemctl": "systemctl start|stop|restart|status|enable <unit> — services manage. daemon-reload config change ke baad.",
  "chmod": "chmod <octal|symbolic> <file> — permissions. Octal: 755=rwxr-xr-x, 640=rw-r-----. -R recursive. SUID: +4000.",
  "chown": "chown [user][:group] <file> — ownership change (root). -R recursive.",
  "ssh": "ssh [-i key] user@host — encrypted remote shell. ssh-keygen -t ed25519 keys banata hai.",
  "man": "man <topic> — manual pages padho. Available: ls cd cat grep find head tail sort uniq cut tr wc sed awk jq ps top free df du ip ss ping dig host curl nmap tcpdump strace lsof journalctl systemctl chmod chown ssh man",
}

def G(h, *items): return {"h": h, "i": list(items)}
def T(t, *checks): return {"t": t, "checks": list(checks)}
def C(re_): return {"k": "cmd", "re": re_}
def F(p, c=""): return {"k": "fs", "p": p, "c": c}
def L(i, t, ph, g, lab=None, tasks=None, lx=None, **kw):
    d = {"id": i, "t": t, "ph": ph, "g": g}
    if lab: d["lab"] = lab
    if tasks: d["tasks"] = tasks
    if lx: d["lx"] = lx
    d.update(kw)
    return d

LEVELS_A = [
L(0, "Linux Mental Model", 1,
  [G("सीखेंगे / You Will Learn",
    ("Linux kya hai?", "Linux ek open-source monolithic kernel hai jo hardware ko manage karta hai — processes, memory, files, network sab iske through. GNU tools + Linux kernel milkar GNU/Linux OS banta hai."),
    ("Kernel kya karta hai?", "Kernel hardware ke saath user-space ke beech ka bridge hai: process scheduling, memory management, device drivers, system calls. uname -r se version milta hai."),
    ("Distribution kya hoti hai?", "Distribution = kernel + packages + package manager + default configs ka bundle. Ubuntu (apt), Fedora (dnf), Arch (pacman) — sab alag distros, same kernel family."),
    ("GNU/Linux relationship", "Kernel (Linus Torvalds) + user tools jaise bash, grep, coreutils (GNU project) milkar poora OS banta hai. Isliye technically sahi naam 'GNU/Linux' hai."),
    ("User space vs kernel space", "Kernel space (ring 0) mein direct hardware access hai; user space (ring 3) mein aapke apps chalte hain. Isolation isliye taaki app crash se system na toote. strace -c ls se dono ka interaction dekho."),
    ("Processes", "Process = running program ka instance. Har process ka apna PID, address space, file descriptors. ps aux se live dekho."),
    ("Files", "Linux mein 'everything is a file' — disk, network socket, terminal, USB device, sab file interface se access hote hain (regular, device, FIFO, socket nodes)."),
    ("File descriptors", "Har process ke open resources ko numbers milte hain: 0=stdin, 1=stdout, 2=stderr. ls -l /proc/self/fd se apne shell ke FDs dekho."),
    ("System calls", "Apps kernel se directly nahi baat kar sakte — syscalls (read, write, open, execve) ka use karte hain. strace -c ls se live syscall traffic dekho."),
    ("Shell", "Shell (bash/zsh) aapke commands ko parse karke processes start karta hai. Ye OS nahi, ek user-space program hai. echo $SHELL se verify karo."),
    ("Terminal", "Terminal = interface jisse shell tak input/output hota hai (TTY/PTY). Purane CRT ka digital version; aaj Ctrl+Alt+T ya tmux/zellij."),
    ("Environment", "Environment variables (PATH, HOME, USER...) har process ko config dete hain. env se dekho, export VAR=val se set karo — child processes tak jaate hain."),
    ("/proc aur /sys ka purpose", "/proc = running kernel ka live view virtual files mein (processes, memory, network). /sys = devices/drivers ka view. cat /proc/cpuinfo, ls /sys/class/net try karo."),
    ("Linux architecture", "Layers: Hardware → kernel (drivers, scheduler, VFS, network stack) → system services (systemd, dbus) → user apps. Yahi layering Linux ke stable hone ki wajah hai."))],
  lab={"n":"Host Profiling (terminal practice)","d":"Virtual lab host ka profile banao: uname, whoami, ip addr, ss -tlnp. Ye 'Mission 1 — Identify' ka chhota version hai."},
  tasks=[
    T("Host profile karo: uname -a, whoami, hostname run karo", C(r"^uname( -a)?$"), C(r"^whoami$"), C(r"^hostname")),
    T("Network dekho: ip addr aur ip route", C(r"^ip addr"), C(r"^ip route")),
    T("Listening services inventory: ss -tlnp", C(r"^ss.*-tlnp"))],
  lx={"hi":"Aapko Linux sirf commands ka collection nahi, balki ek complete operating-system architecture ke roop mein samajh aa gaya.","en":"You now understand Linux as an operating-system architecture rather than just a collection of commands."}),

L(1, "Terminal Mastery", 1,
  [G("Topics",
    ("Bash fundamentals", "Bash commands line-by-line parse aur execute karta hai. #!/bin/bash shebang se scripts bante hain; bash script.sh ya ./script.sh se chalte hain."),
    ("shell parsing", "Shell line ko tokens karta hai, phir operators se split: pipe, redirect, background, keyword expansion. Debug ke liye set -x (xtrace) use karo."),
    ("quoting", "Single quotes = literal (koi expansion nahi), double quotes = variables expand, $(...) = command substitution. echo '$HOME' vs echo \"$HOME\" difference dekho."),
    ("escaping", "Backslash agle character ko literal banata hai: \\, \" aur ' — sab backslash se escape hote hain. echo \"a\\nb\" se real line break milta hai."),
    ("globbing", "Patterns: * (kuch bhi), ? (ek char), [abc] (character set). ls *.txt, ls [a-c]* try karo. Glob fail ho to output khali — nullglob se control hota hai."),
    ("command expansion", "Expansion ka order: brace {a,b} → tilde ~ → variables → command substitution. ls -l {/etc,/home} try karo."),
    ("command substitution", "$(cmd) — command run karke uska output text mein replace karo. echo $(date); nested bhi chalta hai: $(cat notes.txt | wc -l)."),
    ("environment variables", "Shell se processes tak jaane wale key=value pairs. export MY_VAR=hi — child processes ko bhi dikhega. env | grep PATH se dekho."),
    ("aliases", "alias ll='ls -la' se shortcut. Dhyaan: non-interactive scripts mein aliases expand nahi hote — uske liye functions use karo."),
    ("functions", "myfunc() { echo \"hi $1\"; } — reusable blocks with parameters. Scripts mein maintainability isi se aati hai."),
    ("history", "Commands ki list: history, Ctrl+R se search, !123 se re-run. HISTSIZE/HISTFILE se control hota hai."),
    ("readline", "Terminal editing shortcuts: Ctrl+A (start), Ctrl+E (end), Ctrl+W (word delete), Ctrl+U (line delete), Ctrl+K (end tak delete)."),
    ("terminal control", "stty size, clear, colors (escape sequences), tput. stty -a se poore terminal settings dekho.")),
   G("Advanced",
    ("stdin", "Program ko input ka source (keyboard ya pipe). cat bina args ke stdin se padhta hai. grep x < file se file stdin ban jaati hai."),
    ("stdout", "Default output stream (fd 1). command > out.txt ise file mein bhejta hai. Programs apna normal output isi par dete hain."),
    ("stderr", "Error stream (fd 2) — stdout se alag taaki errors clean output se mix na hon. cmd 2> err.log chala kar dekho."),
    ("file descriptors", "0/1/2 ke alawa extra FDs bhi: exec 3> log.txt se naya FD kholo. lsof -p $$ se process ke saare FDs dekho."),
    ("pipelines", "cmd1 | cmd2 — cmd1 ka stdout, cmd2 ko stdin. ps aux | grep ssh classic. set -o pipefail se har stage ka exit status matter kare."),
    ("process substitution", "<(cmd) / >(cmd) — process ko file jaisa treat karo. diff <(ls /) <(ls /tmp) — bina temp files ke compare."),
    ("here-documents", "cat <<EOF ... EOF — multi-line stdin. Scripts mein config/templates inline likhne ke liye perfect. <<-EOF leading tabs ignore karta hai."),
    ("here-strings", "cmd <<< \"text\" — single-line stdin. grep x <<< \"abc axd\" — quick inline test."),
    ("redirection", "> overwrite, >> append, 2>&1 errors ko stdout mein merge. cmd > out.txt 2> err.log — classic split pattern."),
    ("exit status", "$? = last command ka exit code (0=success, non-zero=fail). cmd1 && cmd2 (sirf success par) aur cmd1 || fallback."))],
  lab={"n":"Gamified Milestone","d":"OverTheWire Bandit (Levels 0→10) — har level ek password hunt. Terminal practice: redirection + pipes yahan naturally aate hain."},
  tasks=[
    T("Redirection: echo se /tmp/l1.txt banao, phir cat se padho", C(r"^echo .*>"), F("/tmp/l1.txt")),
    T("Pipeline: ls /usr/bin | head -5 (pipe + head combine karo)", C(r"\| head")),
    T("Exit status: $? check karo — jo bhi command chala ho, phir echo $?", C(r"^echo \$\?"))],
  lx={"hi":"Aap terminal mein confidently kaam kar sakte hain aur shell command ko Linux ke internal data flow ke saath samajh sakte hain.","en":"You can confidently operate the terminal and understand how shell commands interact through Linux data streams and processes."}),

L(2, "Filesystem Deep Dive", 1,
  [G("Core",
    ("absolute/relative paths", "Absolute /etc/passwd root se shuru; relative notes.txt current directory se. pwd + realpath file se verify karo."),
    ("directories", "Directory bhi file hai — sirf name→inode entries ki list. ls -l mein pehla character d hota hai."),
    ("hidden files", "Dot . se shuru hote files hidden hain. ls -a se dikhao. .bashrc, .ssh, .secret_note aise hi files hain."),
    ("links", "Hard link = same inode ka doosra naam; symlink = target path point karne wala chhota file. ls -li se inodes compare karo."),
    ("permissions", "rwx × user/group/others. chmod 750 file, ls -l se dekho. Ye access control ki first line of defense hai."),
    ("metadata", "File ki info — size, owner, timestamps (atime/mtime/ctime), inode number. stat file se sab milta hai.")),
   G("Advanced",
    ("inode", "Filesystem ka unique number jo content + metadata point karta hai. Rename ho to inode wahi. ls -i, inode usage: df -i."),
    ("directory entries", "Directory ke andar name → inode number ki mapping hoti hai. find . -maxdepth 1 entries dikhata hai."),
    ("hard links", "Same inode ke multiple names (same filesystem mein). ln file link banata hai. Data tab tak rehta hai jab tak koi link na ho."),
    ("symbolic links", "ln -s target link — path store karta hai, target alag file. Broken symlink possible hai. readlink -f se resolve karo."),
    ("mount points", "Directory jahan doosra filesystem attach hota hai. mount, findmnt, df -h se dekho. /boot, /home, USB sab mounts."),
    ("filesystem types", "ext4, xfs, btrfs, tmpfs, procfs, sysfs. blkid + findmnt -o TARGET,FSTYPE se identify karo."),
    ("/proc", "Running kernel ka live view — processes, memory, network stats. cat /proc/uptime try karo."),
    ("/sys", "Devices aur drivers ka view — network interfaces, USB. cat /sys/class/net/eth0/address MAC dega."),
    ("/dev", "Device nodes — hardware access ke file interfaces. ls -l /dev | head dekho."),
    ("/run", "Runtime state — PID files, sockets, boot-time info. Reboot par empty ho jaata hai. ls /run.")),
   G("Commands",
    ("ls", "List files; -a hidden, -l long, -h human, -R recursive. ls -lah /etc."),
    ("stat", "Metadata: size, owner, perms, timestamps, inode. stat /etc/passwd."),
    ("find", "Tree search + filters: find /home -name '*.txt' -type f. -mtime, -size +10M, -perm bhi."),
    ("file", "File type guess: file /bin/ls → 'ELF 64-bit executable'."),
    ("mount", "Filesystems attach/detach. mount | grep /home current mounts."),
    ("df", "Disk space per mount: df -h (space), df -i (inodes)."),
    ("du", "Actual sizes: du -sh * top-level, du -ah | sort -h | tail largest files."),
    ("lsblk", "Block devices tree: lsblk -f (fstype + mounts)."),
    ("blkid", "Device ki fs type + UUID: blkid /dev/sda1."))],
  lab={"n":"Filesystem Forensics Lab","d":"Investigate: unusual files, links, mounts. Pehla goal — /home/learner mein hidden file dhundo."},
  tasks=[
    T("Hidden file dhundo: ls -a /home/learner (ya find se)", C(r"(ls -a /home/learner|find /home/learner)")),
    T("Us hidden file ko padho: cat /home/learner/.secret_note", C(r"cat /home/learner/\.secret_note")),
    T("Metadata dekho: stat /home/learner/notes.txt", C(r"^stat /home/learner/notes.txt")),
    T("Forensics: find se /home mein saare .txt files dhundo", C(r"find /home .*\.txt"))],
  lx={"hi":"Aap Linux filesystem ko surface level par nahi, balki inode, metadata, links aur mounts ke level par samajhte hain.","en":"You understand Linux filesystems beyond basic navigation, including inodes, metadata, links, mounts, and virtual filesystems."}),

L(3, "Permissions & Linux Access Control", 2,
  [G("Topics",
    ("UID/GID", "User/Group identity numbers — files inhi numbers se verify hoti hain, usernames sirf display ke liye. id se apna dekho."),
    ("ownership", "Har file ka ek owner + group. chown user:group file (root chahiye). ls -l mein dikhta hai."),
    ("rwx", "Read (content), Write (modify), Execute (run / enter directory). Directory ke liye x = andar ja sakte ho."),
    ("octal permissions", "r=4, w=2, x=1 → sum: 755 = rwxr-xr-x, 640 = rw-r-----. chmod 755 script.sh."),
    ("chmod", "Permissions change — symbolic (chmod u+x f) ya octal (chmod 640 f). -R recursive."),
    ("chown", "Owner/group change (root only). chown -R user:group dir."),
    ("umask", "Naye files/dirs par default permissions ka mask. umask 022 → files 644, dirs 755. umask -S readable format."),
    ("sudo", "Doosre user (default root) se commands. sudoers policy check hoti hai. sudo -l se apni allowed commands dekho.")),
   G("Advanced",
    ("SUID", "File execute hone par owner ki privileges le leti hai (e.g. /usr/bin/passwd). SUID binaries = attack surface. find / -perm -4000 2>/dev/null."),
    ("SGID", "File: group owner ki permissions; Directory: naye files usi group ke. find / -perm -2000."),
    ("sticky bit", "Directory mein sirf apni file delete kar sakte ho (jaise /tmp). find / -perm -1000."),
    ("ACL", "Standard permissions ke upar per-user/per-group access. setfacl -m u:bob:rwx file, getfacl file."),
    ("extended attributes", "Files par metadata keys (security contexts etc.). getfattr -d file."),
    ("Linux capabilities", "Root ke powers ko 38 chhote capabilities mein split (CAP_NET_ADMIN...). getcap /usr/bin/capsh — precise privilege control."),
    ("privilege boundaries", "Ownership + permissions + capabilities + LSM (AppArmor/SELinux) — sab milkar decide karte hain kaun kya kar sakta hai. Misconfigured system lab se seekho."))],
  lab={"n":"Security Lab — Intentionally Misconfigured System","d":"/home/learner/lab/permfile.txt world-writable (666) hai — Fix: chmod 640. Phir explain karo KYUN dangerous tha."},
  tasks=[
    T("Insecure file inspect karo: stat /home/learner/lab/permfile.txt", C(r"stat /home/learner/lab/permfile")),
    T("FIX: chmod 640 se permissions theek karo", C(r"chmod 640 .*permfile"), F("/home/learner/lab/permfile.txt", "[mode:640]")),
    T("Audit: /home mein hidden files dhundo (find -name '.*')", C(r"find /home.*\..*"))],
  lx={"hi":"Aap samajhte hain ki Linux mein \"kaun kya access kar sakta hai\" kaise decide hota hai.","en":"You understand how Linux determines who can access, execute, modify, or administer resources."}),

L(4, "Processes & Internals", 2,
  [G("Topics",
    ("PID", "Process ID — running process ka unique number. echo $$ se apne shell ka PID."),
    ("PPID", "Parent Process ID — kaun is process ko start kiya. ps -o pid,ppid,cmd -p $$."),
    ("process tree", "Parent-child hierarchy. ps axjf se tree view."),
    ("foreground/background", "FG = terminal block; cmd & se BG start, Ctrl+Z hold, bg resume, fg wapas."),
    ("jobs", "Current shell ki jobs: jobs list, %1 se job reference."),
    ("signals", "Process events: SIGTERM (15) graceful kill, SIGKILL (9) force, SIGINT (2) = Ctrl+C. kill -15 <pid>."),
    ("process states", "R running, S sleeping, D uninterruptible (disk wait), Z zombie, T stopped. ps -o stat,comm ax.")),
   G("Advanced",
    ("/proc/<pid>", "Har process ka virtual dir: cmdline, status, fd/, environ. cat /proc/self/status try karo."),
    ("process namespaces", "Isolated PID views — containers isi se kaam karte hain. lsns se dekho (root)."),
    ("file descriptors (process)", "Process ke open files/sockets: ls -l /proc/self/fd, lsof -p $$."),
    ("environment inspection", "Process ki env: cat /proc/self/environ (null-separated) — tr se readable banao."),
    ("zombie processes", "Exit ho gaya par parent ne wait() nahi kiya — entry rehti hai. ps aux | awk '$8 ~ /Z/'. Cleanup = parent ka exit."),
    ("orphan processes", "Parent mar gaya → systemd (PID 1) adopt kar leta hai. Problem nahi, but awareness chahiye."),
    ("scheduling basics", "CFS scheduler, nice values (-20..19). nice -n 10 cmd, renice se priority."),
    ("resource limits", "Per-process limits: memory, files, CPU. ulimit -a dekho.")),
   G("Tools",
    ("ps", "Process snapshot: ps aux (everything), ps -ef, ps -o pid,ppid,user,cmd ax."),
    ("top", "Live monitor — CPU/mem sorted. -u user filter."),
    ("htop", "Interactive colorized top — filters, kill, search."),
    ("pgrep", "Name se PID: pgrep -af python (full cmd), pgrep -x sshd exact."),
    ("strace", "Syscalls trace: strace -p <pid>, strace -c ls. Permission issues ka weapon."),
    ("lsof", "Open files: lsof -i :8080 (port), lsof -p <pid>."),
    ("fuser", "Kaun file/port use kar raha: fuser 8080/tcp."))],
  lab={"n":"Process Investigation","d":"Unknown process identify karo: kaun, parent kaun, kya kar raha. Port 8080 ke process ko dhundo."},
  tasks=[
    T("Saare processes dekho: ps aux (ya ps ax)", C(r"^ps (aux|ax|ef)")),
    T("Port 8080 kaun use kar raha? ss -tlnp (ya lsof -i :8080)", C(r"(ss.*tlnp|lsof -i :8080)")),
    T("Apne shell ka /proc inspect karo: cat /proc/self/status", C(r"/proc/self"))],
  lx={"hi":"Aap Linux system ke andar chal rahe processes ko inspect aur troubleshoot kar sakte hain.","en":"You can inspect, understand, and troubleshoot running Linux processes and their relationships."}),

L(5, "System Administration", 2,
  [G("Topics",
    ("services", "Background daemons (sshd, nginx...). systemctl list-units --type=service se inventory."),
    ("systemd", "Init system (PID 1) — services, mounts, sockets, timers units ke roop mein. systemctl status sshd."),
    ("boot process", "BIOS/UEFI → bootloader (GRUB) → kernel → initramfs → systemd → default target. systemd-analyze blame se slow boot."),
    ("targets", "Units ke groups — multi-user.target (servers), graphical.target (desktop). systemctl get-default."),
    ("timers", "systemd ka cron-like scheduling. systemctl list-timers."),
    ("logs", "journal + /var/log files. journalctl -u sshd -n 50 — recent unit logs."),
    ("service dependencies", "Kaun kisse depend karti hai: systemctl list-dependencies sshd.")),
   G("Advanced",
    ("unit files", "/etc/systemd/system/*.service — ExecStart, After=, WantedBy=. systemctl cat sshd se padho."),
    ("service hardening", "Unit mein: ProtectSystem=strict, NoNewPrivileges=yes, User=nobody. systemd-analyze security sshd score dega."),
    ("startup dependencies", "After=/Wants=/Requires= — order aur auto-start. Circular deps = boot issues."),
    ("system recovery", "Emergency mode: systemctl rescue ya systemd.unit=emergency boot arg. Root password reset isi se."),
    ("resource limits (systemd)", "Unit level: MemoryMax=, CPUQuota=. systemctl show sshd -p MemoryMax."),
    ("scheduled tasks", "cron (crontab -e) ya systemd timers. * * * * * cmd syntax.")),
   G("Tools",
    ("systemctl", "start/stop/restart/enable/disable/status. daemon-reload config change ke baad."),
    ("journalctl", "-u unit, -n N, --since '10 min ago', -p err. Log investigation ka core."),
    ("systemd-analyze", "blame (slow units), critical-chain, verify (unit files)."),
    ("crontab", "User scheduled tasks: crontab -e edit, crontab -l view."))],
  lab={"n":"Broken Linux Server","d":"Observe → Diagnose → Root cause → Fix → Verify → Document. Lab host ke logs mein OOM kill + failed service dhundo."},
  tasks=[
    T("Service logs dekho: journalctl (lab snapshot)", C(r"^journalctl")),
    T("Failed logins timeline: cat /var/log/auth.log | grep Failed", C(r"grep.*[Ff]ailed")),
    T("Disk status: df -h", C(r"^df -h"))],
  lx={"hi":"Aap Linux server ko operate, diagnose aur recover kar sakte hain.","en":"You can operate, diagnose, repair, and document Linux server environments."}),

L(6, "Networking Deep Dive", 2,
  [G("Fundamentals",
    ("OSI model", "7-layer reference: Physical→DataLink→Network→Transport→Session→Presentation→Application. Troubleshooting mein layer-by-layer approach seekhoge."),
    ("TCP/IP model", "Practical 4-layer: Network Access→Internet→Transport→Application. Real protocols isi ke upar chalte hain."),
    ("IPv4", "32-bit address (dotted quad). Private ranges: 10/8, 172.16/12, 192.168/16. ip addr se apna dekho."),
    ("IPv6", "128-bit address — IPv4 exhaustion ki wajah se. ip -6 addr, typical prefix /64."),
    ("subnetting", "Network ko CIDR se chhote networks mein divide: /24 = 256 addresses. ip route show se apne subnets dekho."),
    ("routing", "Packet ka path — next-hop gateway decide karna. ip route get <ip> se path test karo (lab mein lab.local)."),
    ("ARP", "IP → MAC resolution local network mein. ip neigh cache dikhata hai. ARP spoofing = attack vector (sirf theory mein)."),
    ("ICMP", "Control/error messages — ping isi par. Ping ka reply ICMP echo-request/reply hai."),
    ("TCP", "Reliable, ordered, connection-oriented. Retransmissions + ACKs. Web traffic mostly TCP."),
    ("UDP", "Fast, unreliable, connectionless — DNS, VoIP. ss -uap se UDP sockets dekho.")),
   G("Advanced",
    ("TCP handshake", "SYN → SYN-ACK → ACK (3-way). tcpdump -i any 'tcp[tcpflags] & (tcp-syn) != 0' se dekho (lab traffic)."),
    ("connection states", "LISTEN, ESTABLISHED, TIME_WAIT, CLOSE_WAIT... ss -tan se dekho. TIME_WAIT bahut ho to server issue."),
    ("ephemeral ports", "Client side ka temporary port (32768–60999). Har naye outbound connection ke liye naya port."),
    ("sockets", "Network communication ka endpoint (IP:port + protocol). ss -tlnp — kaunsa process kaunse port pe."),
    ("routing tables", "Destination → interface/gateway mapping. ip route show, ip route get <ip>."),
    ("MTU", "Max packet size per hop. Chhota MTU + DF flag = timeout issues. ping -M do -s 1472 se test."),
    ("fragmentation", "Bade packet ko chhote pieces mein (IP level). tcpdump mein 'frag offset != 0' filter."),
    ("DNS resolution", "Domain → IP: resolver → root → TLD → authoritative. dig +trace se full journey dekho."),
    ("caching", "DNS results cache hote hain (OS + resolver), TTL expire par fresh query. resolvectl flush-caches."),
    ("TLS fundamentals", "Encrypted channel: handshake (certs, key exchange) → symmetric session. curl -v https:// se steps dekho.")),
   G("Tools",
    ("ip", "ip addr, ip route, ip neigh, ip link — modern networking CLI (ifconfig/route ka replacement)."),
    ("ss", "Sockets: ss -tlnp (listening + process), ss -tan (connections). netstat se faster."),
    ("ping", "ICMP reachability: ping -c 4 lab.local. Block ho to aage ki layers check karo."),
    ("traceroute", "Hop-by-hop path (TTL expiry). traceroute lab.local; ICMP block par -T (TCP mode)."),
    ("dig", "DNS power tool: dig lab.local A, +short, +trace, dig @server."),
    ("host", "dig ka simple wrapper: host -t MX example.com."),
    ("tcpdump", "Raw packet capture: tcpdump -i any port 80 -n. Packet forensics ka core tool."))],
  lab={"n":"Packet Analysis + Network Diagnosis","d":"Lab host ki connectivity verify karo: ping, dig, traceroute, ss, tcpdump — sab sirf lab.local par (Red Line)."},
  tasks=[
    T("Reachability: ping -c 3 lab.local", C(r"ping .*lab\.local")),
    T("DNS: dig lab.local (ya host lab.local)", C(r"^(dig|host) lab\.local")),
    T("Connections: ss -tan", C(r"^ss -tan")),
    T("Packet capture (lab only): tcpdump -i any host lab.local", C(r"^tcpdump"))],
  lx={"hi":"Aap network ko sirf IP aur port ke level par nahi, packet aur connection behavior ke level par samajh sakte hain.","en":"You can analyze networking at the packet and connection level rather than merely thinking in terms of IP addresses and ports."}),

L(7, "HTTP & Web From Linux", 2,
  [G("Topics",
    ("HTTP request", "Method + URL + Headers + optional body. curl -i http://lab.local/ se raw request/response dekho."),
    ("HTTP response", "Status line + headers + body. Status code (200/404/500) turant batata hai kya hua."),
    ("methods", "GET (read), POST (send/create), PUT (update), DELETE (remove), HEAD (headers only), OPTIONS (capabilities)."),
    ("headers", "Metadata: Host, User-Agent, Accept, Cookie, Authorization... curl -vI se dekho. Security headers (HSTS, CSP) yahi se check hote hain."),
    ("cookies", "Server → client ka state (Set-Cookie). Sessions isi se track hote hain. curl -c jar -b jar se manage karo."),
    ("redirects", "301 permanent, 302 temporary, 307/308. curl -L follow karta hai. Open redirects = security issue."),
    ("status codes", "2xx success, 3xx redirect, 4xx client error (401/403/404), 5xx server error. Bug hunting mein 403/404 patterns dhundo."),
    ("HTTPS", "HTTP + TLS — encrypted. curl -v https:// se handshake dekho. Cert errors, mixed content dhundo."),
    ("TLS basics", "Cert chain, CAs, expiration. echo | openssl s_client -connect host:443 se inspect (theory + lab).")),
   G("Linux Workflow",
    ("curl", "Swiss-army HTTP: -i headers, -v verbose, -X POST -d data, -H header, -o file. Lab ka #1 tool."),
    ("wget", "Downloads + recursion: wget -r -l 1 url. Bada content save karne ke liye."),
    ("grep/sed/awk/jq", "Response dump → grep filter → sed clean → awk columns → jq JSON. curl -s url | jq .user.")),
   G("Advanced",
    ("request/response debugging", "curl -v + --trace-ascii file — wire-level log. Headers order, redirects, TLS sab dikhta hai."),
    ("proxy concepts", "Requests third-party se pass hote hain (forward/reverse). curl -x http://proxy:8080 url. Burp isi principle par."),
    ("authentication headers", "Authorization: Basic (base64 — encrypted NAHI!), Bearer tokens, API keys. curl -u user:pass, curl -H 'Authorization: Bearer t'."),
    ("content negotiation", "Accept headers se client preference, server Content-Type se reply. curl -H 'Accept: application/json'."),
    ("JSON APIs", "REST endpoints jo JSON dete hain. curl -s url | jq '.[0]' — auth, rate limits, error shapes samjho."),
    ("WebSockets concepts", "Full-duplex persistent connection (HTTP upgrade). Browser devtools wscat view. Realtime apps isi par."),
    ("HTTP/2 concepts", "Multiplexing, header compression. curl --http2 -v. HTTP/3 = QUIC (UDP)."))],
  lab={"n":"HTTP Investigation Lab","d":"lab.local service par: root, /api/users, /admin fetch karo — status codes compare karo. Phir hidden /srv/lab/.env ko HTTP se dhoondo (path traversal mindset, sirf lab par)."},
  tasks=[
    T("Root fetch karo: curl -i http://lab.local/", C(r"curl.*lab\.local/?$")),
    T("API test: curl http://lab.local/api/users | jq .", C(r"curl.*api/users")),
    T("403 verify: curl -sI http://lab.local/admin | head -1", C(r"curl.*admin"))],
  lx={"hi":"Aap browser ke peeche hone wale HTTP communication ko terminal se inspect aur analyze kar sakte hain.","en":"You can inspect and analyze browser-style HTTP communication directly from the Linux terminal."}),

L(8, "Bash Programming", 2,
  [G("Topics",
    ("variables", "NAME=value set; $NAME expand; ${NAME:-default} fallback. Scripts mein set -u se unset use fail ho jaata hai."),
    ("conditions", "if [ condition ]; then ... fi; [[ ]] bash-extended (regex, &&). [ -f file ] file checks."),
    ("loops", "for x in ...; do ...; done, while [ cond], until. Range: for i in {1..5}."),
    ("functions", "Reusable + parameters + return. local variables mat bhulo."),
    ("arrays", "arr=(a b c), ${arr[0]}, ${#arr[@]} length. Associative: declare -A."),
    ("arguments", "$1..$9, $@ saare, $# count, shift. getopts se -flags parse karo."),
    ("exit codes", "0 success; 1+ failure. Custom: exit 2 bad args. Professional scripts isi se padhe jaate hain.")),
   G("Advanced",
    ("robust quoting", "Har variable double-quote: \"$var\" — spaces/newlines safe. Script top: set -euo pipefail (holy trinity)."),
    ("error handling", "set -e (fail-fast), set -o pipefail (pipe mein bhi), || fallback, if ! cmd; then. Silent failures = prod pain."),
    ("traps", "trap 'cleanup' EXIT — exit/signal par run. Temp files delete, locks release."),
    ("temp files", "tmp=$(mktemp); trap mein delete. Predictable /tmp names = symlink attack risk."),
    ("parallel execution", "cmd & + wait; xargs -P4 parallel. CPU-heavy jobs fast — resource limits dhyan mein."),
    ("logging", "log(){ echo \"[$(date -Iseconds)] $*\"; } — timestamped output, >> log file 2>&1. Debugging ki bread & butter."),
    ("input validation", "Numbers: [[ $x =~ ^[0-9]+$ ]]; paths: realpath -e. Untrusted input = injection risk — hamesha validate."),
    ("script portability", "#!/usr/bin/env bash, POSIX-safe syntax. Alpine/Debian dono par chalna chahiye.")),
   G("Tools",
    ("grep/sed/awk", "Filter → transform → fields. Text processing ki backbone."),
    ("cut/sort/uniq", "Fields extract → sort → dedupe. Report pipelines mein daily use."),
    ("xargs", "List ko batch commands mein convert: ls | xargs -I{} wc -l {}."),
    ("jq", "JSON processing — API output ka clean handling."))],
  lab={"n":"Project — Linux Investigation Toolkit","d":"/tmp/profile.sh script banao jo uname, ip addr, ss -tlnp, df -h, ps aux ka summary chhapaye. Echo + > se shuru karo."},
  tasks=[
    T("Script banao: echo '#!/bin/bash' > /tmp/profile.sh (phir aur lines >> se add karo)", C(r"echo.*> /tmp/profile\.sh"), F("/tmp/profile.sh", "#!/bin/bash")),
    T("Processing practice: cat /home/learner/lab/data/dupes.txt | sort | uniq -c | sort -rn", C(r"uniq -c")),
    T("head/tail combo: cat /var/log/app.log | head -3", C(r"head -"))],
  lx={"hi":"Aap repetitive Linux tasks ko Bash scripts ke through automate kar sakte hain.","en":"You can automate repetitive Linux operations using reliable Bash scripts."}),

L(9, "Python for Linux & Security Automation", 2,
  [G("Topics",
    ("Python basics", "Indentation-based, dynamically typed. python3 script.py. Bash se zyada structured — complex logic ke liye."),
    ("variables", "Dynamic types: x = 5, s = 'hi'. f-strings: f'User {user}'. Naming: snake_case."),
    ("functions", "def f(a, b=1): return a+b — defaults, *args, **kwargs. Docstrings likho."),
    ("modules", "import os, json, subprocess, requests. Standard library + pip. pip install -r requirements.txt."),
    ("exceptions", "try/except/finally — specific exceptions catch karo (except FileNotFoundError). Bare except = debugging death."),
    ("files", "open('f') as f: f.read() — context manager (auto close). pathlib.Path modern way."),
    ("JSON", "json.load(f), json.dumps(obj, indent=2). API work ka 90% isi se."),
    ("regex", "re.findall, re.search, re.sub — patterns se dhundo (emails, IPs, tokens)."),
    ("subprocess", "subprocess.run(['ip','addr'], capture_output=True). shell=True avoid karo (injection risk)."),
    ("HTTP clients", "requests.get(url) — status, json(), timeouts hamesha set karo. Web automation ka core.")),
   G("Advanced",
    ("sockets", "Raw TCP/UDP: socket.socket(), bind/connect/send/recv. Custom protocols, scanners isi se."),
    ("concurrent requests", "concurrent.futures.ThreadPoolExecutor — parallel HTTP without raw threads ka complexity. Rate limit dhyan rakh kar."),
    ("structured logging", "logging module: levels (DEBUG..ERROR), formatters, file handlers. Ad-hoc print() se hamesha better."),
    ("CLI applications", "argparse/typer — flags, subcommands, auto --help. Professional tooling."),
    ("API integration", "Auth (tokens), pagination, retries (exponential backoff), error handling — real APIs isi se handle hote hain."),
    ("parsing large datasets", "Chunked/line-by-line reading, generators — 10GB logs bhi process hote hain bina RAM exhaust kiye."))],
  lab={"n":"Project — CLI Security Data Analyzer","d":"Lab logs (duplicates wale) ko clean → normalize → dedupe → report. Pehle Bash pipeline se, phir Python script se same kaam."},
  tasks=[
    T("Data dhundo: cat /home/learner/lab/data/servers.csv", C(r"cat .*servers\.csv")),
    T("Count ERROR lines: grep -c ERROR /var/log/app.log", C(r"grep -c ERROR /var/log/app\.log")),
    T("Normalize: cat /home/learner/lab/recon/raw_output.txt | tr 'A-Z' 'a-z' | sort -u", C(r"tr 'A-Z' 'a-z'"))],
  lx={"hi":"Aap Bash ke saath Python ka use karke sophisticated Linux/security automation tools bana sakte hain.","en":"You can combine Bash and Python to build sophisticated Linux and security automation tools."}),

L(10, "Git & Engineering Workflow", 2,
  [G("Topics",
    ("Git fundamentals", "Version control — snapshots. git init, git status, git add, git commit."),
    ("branches", "Cheap pointers to commits. git branch dev, git switch -c feature. Parallel work ka foundation."),
    ("commits", "Atomic, descriptive (imperative: 'Add login validation'). Har commit = working state."),
    ("diffs", "git diff (unstaged), git diff --staged, git diff HEAD~1. Code review culture isi par."),
    ("merges", "git merge — fast-forward ya merge commit. Conflicts manually resolve. Rebase = linear history (team convention follow karo)."),
    ("tags", "Release markers: git tag v1.0.0. SemVer: MAJOR.MINOR.PATCH."),
    ("remotes", "git remote -v, git push origin main, git pull. GitHub/GitLab connection.")),
   G("Advanced",
    (".gitignore", "Push NAHI karna: *.log, .env, __pycache__/. Secrets protect karne ka first step."),
    ("clean commit history", "WIP commits squash karo, rebase se linear. Future-you ko thank you."),
    ("debugging with git", "git bisect — bad commit binary search. git log -p changes trace. git stash current work park karo."),
    ("rollback", "git checkout -- file (discard), git revert <sha> (safe inverse commit). Force push se bacho."),
    ("collaboration", "Fork/PR flow, code review, conventional commits. Team workflow."),
    ("documentation", "README + docs ko code ke saath update karo. Doc drift = project death.")),
   G("Security",
    ("secrets commit NA karna", "API keys/passwords repo mein NAHI. Accidentally push hua? git filter-repo + secret ROTATE karo — history delete se safe nahi hota."),
    ("configuration separation", "Code = repo, secrets = env vars / secret manager. .env.example provide karo, .env ignore."),
    ("safe credential handling", "CI/CD: encrypted secrets; local: credential helpers, keychain. Hardcoded = compromised."))],
  lab={"n":"Workflow Practice","d":"Apne lab environment ki 'audit trail' banao: .bash_history inspect karo aur interesting commands filter karo."},
  tasks=[
    T("History dekho: history", C(r"^history$")),
    T("Audit: grep se .bash_history mein ssh commands dhundo: grep ssh /home/learner/.bash_history", C(r"grep.*bash_history")),
    T("Version control mindset: cat /home/learner/.bash_history | wc -l", C(r"bash_history.*wc|wc.*bash_history"))],
  lx={"hi":"Aap apne scripts, tools aur projects ko professional software-engineering workflow mein manage kar sakte hain.","en":"You can manage Linux/security projects using a professional software-engineering workflow."}),
]
