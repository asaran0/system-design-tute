# Google Senior Software Engineer Interview Preparation

This document consolidates the complete preparation roadmap discussed in our chat. It is structured as a **21-day Google-style interview plan**, covering **DSA, System Design, Distributed Systems, and Large-Scale Architecture**, exactly aligned with **Google L5/L6 expectations**.

---

## OVERALL GOAL

* Crack **Google Senior Software Engineer (L5/L6)** interviews
* Master **problem solving + system design + distributed systems**
* Think and communicate like a Google engineer

---

# DAY 1–4: CORE DATA STRUCTURES

## Topics

* Arrays
* Strings
* HashMaps / HashSets
* Linked Lists
* Stack & Queue

## Focus Areas

* Time & space complexity analysis
* Edge cases
* In-place operations
* Pointer techniques

## Key Patterns

* Two pointers
* Sliding window
* Prefix sums
* Hashing

## Practice Level

* Medium + Hard
* Google-style constraints

---

# DAY 5–6: TREES & RECURSION

## Topics

* Binary Trees
* Binary Search Trees
* DFS / BFS
* Recursion vs Iteration

## Core Concepts

* Tree traversals
* Height / Diameter
* Lowest Common Ancestor
* Balanced trees

## Expectations

* Recursive thinking
* Stack space awareness
* Bottom-up vs Top-down DP on trees

---

# DAY 7–8: GRAPHS

## Topics

* BFS / DFS
* Topological Sort
* Union-Find (Disjoint Set)
* Cycle detection

## Graph Types

* Directed / Undirected
* Weighted / Unweighted

## Patterns

* Multi-source BFS
* Graph coloring
* Connected components

---

# DAY 9–12: DYNAMIC PROGRAMMING

## Day 9–10: DP (Medium)

* 1D DP (Fibonacci, Climbing Stairs)
* 2D DP (Grid paths)
* Knapsack basics

## Day 11–12: DP (Hard)

* State compression
* DP + Binary Search
* DP on graphs
* DP optimization

## Key Skill

* State definition
* Transition clarity
* Memoization vs Tabulation

---

# DAY 13–14: ADVANCED GRAPHS + DP MIX

## Topics

* Graph + DP combinations
* DAG DP
* Shortest path with state
* Topological DP

## Example Problems

* Longest Increasing Path in Matrix
* Course Schedule with constraints

---

# DAY 15–16: SYSTEM DESIGN BASICS

## Load Balancers

* L4 vs L7
* Algorithms: Round Robin, Least Connections
* Global & regional load balancing

## Caching

* Redis vs Memcached
* Cache-aside pattern
* TTL & invalidation strategies

## Sharding & Partitioning

* Range-based
* Hash-based
* Consistent hashing

## CAP Theorem

* CP vs AP systems
* Trade-offs in real systems

## Consistency Models

* Strong consistency
* Eventual consistency
* Read-your-writes

---

# DAY 17–18: DISTRIBUTED SYSTEMS

## Message Queues

* Kafka internals
* Pub/Sub concepts
* Delivery semantics

## Async Processing

* Background jobs
* Retry & backoff
* Dead Letter Queues

## Event-Driven Architecture

* Events vs commands
* Loose coupling
* Schema evolution

## Saga Pattern

* Orchestration vs Choreography
* Compensation transactions
* Failure handling

---

# DAY 19–20: GOOGLE-STYLE LARGE SYSTEMS

## Scalability to Billions

* Horizontal scaling
* Stateless services
* Caching layers
* Hot key mitigation

## Multi-Region Systems

* Active-Active vs Active-Passive
* Data replication strategies
* Failover design

## Observability

* Metrics, logs, traces
* Golden signals
* SRE mindset

## Data Pipelines

* Batch vs streaming
* Pub/Sub → Dataflow → Storage
* Handling late & duplicate data

---

# SYSTEM DESIGN CASE STUDIES

## Payment System

* Strong consistency
* Idempotency
* Async bank calls
* Security & PCI compliance

## Order Management System

* Event-driven architecture
* Saga-based workflow
* Eventual consistency
* Failure recovery

---

# DAY 21: FINAL GOOGLE PREP

## Mock Interviews

* Coding + Explanation
* Full System Design

## Behavioral (Googleyness)

* STAR format
* Ownership
* Conflict resolution
* Failure stories

---

# GOOGLE INTERVIEW EXPECTATIONS

✔ Clear communication
✔ Trade-off analysis
✔ Failure-first thinking
✔ Scalability awareness
✔ Production realism

---

## HOW TO USE THIS DOC

1. Follow days sequentially
2. Practice coding daily
3. Speak solutions aloud
4. Revise system design diagrams
5. Do mock interviews

---

**You are now following a Google-hiring-committee-level preparation plan.**
