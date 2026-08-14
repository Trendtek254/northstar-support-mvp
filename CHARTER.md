# 📜 Team Charter: Northstar Sprint MVP

**Pod Name / Number:** Pod PLP Group 28  
**Repository:** https://github.com/Trendtek254/northstar-support-mvp  
**Date:** August 2026  

---

## 1. Project Objective & Scope

* **Core Goal:** Deliver a working, demoable Support Deflection MVP within 5 days that reduces manual ticket volume for Northstar Retail Co. across at least two ticket categories (**Order Status** and **Returns & Refunds**).
* **Deliverables:**
  1. Working Streamlit/Python prototype covering $\ge 2$ ticket categories.
  2. 1-Page Go-Live Readiness Note (`GO_LIVE_NOTE.md`).
  3. Verified commit and board task audit trail showing balanced team collaboration.

---

## 2. Working Agreements & Communication

* **Primary Communication Channel:** WhatsApp; daily 30-minute standup meeting at 6.00PM.
* **Core Collaboration Hours:** All team members available online between 8:00 PM – 1:00 AM.
* **Decision Making Process:** Majority vote wins. If tied after 15 minutes of technical discussion, the Task Lead/Owner makes the final call.

---

## 3. Git & Commit Message Policy (Anti-Black-Box Rules)

* **Commit Format:** Every commit message **must** strictly follow the pattern:  
  `<type>: <what changed> - <why it matters>`
  * *Valid Types:* `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.
  * *Prohibited Messages:* `wip`, `updates`, `fix bug`, `changes`, `latest code`.
* **Branching Rule:** Direct pushes to `main` are disabled. All work happens on feature branches named `feature/<task-id>-<description>`.
* **Peer Reviews:** Every Pull Request requires at least 1 teammate review approval before merging into `main`.

---

## 4. Project Board & Task Management Governance

* **Task Scope Constraint:** No board task may exceed **4 hours** of estimated effort. Larger tasks must be split immediately into sub-tasks.
* **Definition of Done (DoD):** Every task must have a single, verifiable sentence confirming completion (e.g., *"Function passes pytest unit test and handles missing Order IDs without crashing"*).
* **Same-Day Updates:** Board cards must be moved to **In Progress** when started and **Done** on the *same day* code is merged. Batched end-of-week updates are prohibited.

---

## 5. Escalation Path & Anti-Ghosting Protocol

* **24-Hour Inactivity:** If a teammate produces 0 visible activity or communication for 24 hours without prior notice, the Pod Lead sends a direct status ping.
* **48-Hour Escalation Trigger:** If a teammate shows **0 visible activity for 2+ consecutive days**:
  1. Pod Lead logs the timestamped inactivity in the project audit log.
  2. Unstarted tasks assigned to the inactive member are immediately re-assigned to active team members.
  3. Formal notification is submitted to course management per the non-negotiable sprint rules.

---

## 6. Team Roles & Task Allocation

| Team Member | Role Focus | Primary Task Responsibilities |
| :--- | :--- | :--- |
| **Morgan Nyanga'u(Lead)** | System Architecture & Repo Admin | Setup repo, GitHub board, stock lookup logic (`NS-01`, `NS-05`, `NS-09`) |
| **** | Data Architecture & Docs | Mock databases, Streamlit UI, Go-Live Note (`NS-02`, `NS-06`, `NS-10`) |
| **Member C** | Core Logic & API Integration | Order status backend, UI integration, audit log (`NS-03`, `NS-07`, `NS-11`) |
| **Member D** | Business Rules & QA | Return eligibility workflow, unit tests script (`NS-04`, `NS-08`) |# northstar-support-mvp

