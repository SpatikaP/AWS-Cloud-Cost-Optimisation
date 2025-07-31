# AWS Compute Optimization  
**Automate. Save. Sleep Better.**  

Welcome to a lightweight, serverless toolkit that helps you **cut cloud waste** and **run smarter AWS infrastructure** — all using **AWS Lambda** and **Amazon EventBridge**.

---

## Why This Exists

Imagine leaving the lights on in every room of your house — all night, every night. That’s what happens when cloud resources like **EC2 instances**, **EBS snapshots**, or **EKS nodes** run 24/7 — even when no one's using them.

This repo helps you **flip those lights off** automatically with a few simple scripts.

---

## What’s Inside?

This project includes Lambda functions (think: tiny cloud robots 🛠️) that handle common cleanup and automation tasks:

- **EBS Snapshot Cleaner** – Deletes old or unused snapshots you forgot existed.
- **EC2 Scheduler** – Turns dev/test instances on in the morning and off at night.
- **EKS Node Scaler** – Scales your Kubernetes nodegroups up or down on demand.

And all of it runs on **autopilot**, thanks to **EventBridge**.

---

## Meet the Heroes

### AWS Lambda  
Think of it as a robot that waits for a signal, does its job (like deleting old stuff or turning things off), and goes back to sleep. You don’t need to feed it, patch it, or scale it.

### Amazon EventBridge  
This is the clock, calendar, and alert system. It tells Lambda what to do and *when* to do it — like,  
⏰ “Hey, it’s 7 PM, time to shut down those test servers!”

---

## Why Should You Care?

- **Save money**: Stop paying for idle resources.
- **Stay clean**: Keep your environment clutter-free.
- **Automate the boring stuff**: Focus on building, not babysitting infra.
- **Scale smart**: Match your resources to real demand.

---

## How to Use

Just plug in the scripts to your AWS Lambda functions, set up a few EventBridge rules (cron or event-based), and let your infrastructure manage itself.

No huge frameworks. No complexity. Just **simple, serverless automation** that works.
