# Source Code Disclosure via Backup Files — Hunting Sensitive Data Left in the Wild 🔍🗃️

**By Aditya Bhatt**

## Introduction

Information disclosure vulnerabilities remain a frequent and critical issue in web security. One surprisingly common mistake developers make is unintentionally exposing sensitive files—like source code backups or configuration files—in publicly accessible directories. These exposures can leak hard-coded credentials, API keys, or other secrets, instantly turning a simple app into an easy target 🎯.

In this write-up, I walk through a practical example from a recent BurpSuite lab focused on **Source Code Disclosure via Backup Files** — a classic yet often overlooked vulnerability that can yield high-impact rewards in bug bounty programs 💰.

![Cover](https://github.com/user-attachments/assets/79777647-0f89-46f6-a4bd-fa71517e0c2f) <br/>

---

## Lab Overview: Source Code Disclosure via Backup Files

The lab simulates a real-world scenario where a web application leaks its source code through backup files stored in a hidden directory. The goal is to discover and retrieve a hard-coded database password embedded inside the leaked source code 🔐.

---

## Step-by-Step Walkthrough

### 1. Access the Lab

Navigate to the lab URL: [https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files) 🌐.

![1](https://github.com/user-attachments/assets/db503da8-6ba8-46fe-ac7b-a1cc937e85e0) <br/>

### 2. Check robots.txt for Clues

Open `/robots.txt` to see if any disallowed paths might hint at hidden directories. The file reveals a `/backup` directory—a potential goldmine for leftover files 🗂️.

![2](https://github.com/user-attachments/assets/d69b5ed4-6230-4d0f-b2e1-87d8874fe905) <br/>

### 3. Explore the `/backup` Directory

Browsing to `/backup` lists available files, including `ProductTemplate.java.bak`. This is clearly a backup file, potentially containing sensitive source code 🧾.

![3](https://github.com/user-attachments/assets/dead20b8-4c21-445c-9dc1-9356c3953832) <br/>

### 4. Inspect the Backup Source Code

Opening `/backup/ProductTemplate.java.bak` reveals the entire Java source file. Scanning through the code, we spot a connection builder with a hard-coded Postgres database password. This careless developer left the keys to the kingdom right in the code—likely a result of rushed work or overlooked cleanup 🔑.

> *"Click on weird links to get weird bounties" — Aditya Bhatt 🗿*
> Just kidding, but sometimes it really is that simple 😅.

![4](https://github.com/user-attachments/assets/a5b2786d-fa27-48b9-a0ab-112aeb50425e) <br/>

### 5. Submit the Extracted Password

Copy the discovered password and submit it via the lab’s solution interface ✅.

![5](https://github.com/user-attachments/assets/e2f66c50-7b67-4d41-b983-566edcfc8117) <br/>

### 6. Lab Solved!

Success! 🎉 The lab confirms the vulnerability exploitation, demonstrating the risks of leaving backup files accessible in production environments.

![6](https://github.com/user-attachments/assets/b9e61bc3-55fd-45d3-8f22-022ba5e69707) <br/>

---

## Lessons Learned

* **Backup files are dangerous:** Developers often forget to remove backup or temporary files before deployment. These files can expose entire source code or secrets 🛑.
* **robots.txt can leak info:** While intended to instruct web crawlers, `robots.txt` can unintentionally disclose sensitive paths 🕵️‍♂️.
* **Source code leaks = instant root access:** Hard-coded credentials in source code can compromise entire systems 🚨.
* **Content discovery is essential:** Automated directory fuzzing and content discovery tools help reveal hidden files and directories 🔎.

---

## Real-World Implications

In live environments, the exposure of backup or configuration files containing sensitive data is a common vector for attackers to gain foothold, escalate privileges, or dump databases. Many bug bounty programs reward such findings generously because of their critical impact 💸.

As bug hunters, we must always:

* Check `/robots.txt` for sensitive paths 📜.
* Perform thorough content discovery to find hidden directories and files 🔍.
* Analyze backup, temp, and config files for secrets 🗝️.
* Report responsibly with remediation advice: restrict access, remove backups, and avoid hard-coded credentials 🛡️.

---

## Conclusion

This BurpSuite lab highlights a fundamental security lapse: leaving backup files accessible on public servers. Despite being a simple misconfiguration, it can lead to serious data breaches. For bug bounty hunters, mastering this technique can unlock critical vulnerabilities quickly and effectively ⚡.

Happy hunting, and remember — sometimes the “weird links” are the keys to the bounty! 🕵️‍♀️💥

---

If you found this write-up helpful, follow me for more bug bounty tips and real-world InfoSec insights 🔐✨.

— **Aditya Bhatt**
Cybersecurity Researcher & Bug Bounty Hunter

---
