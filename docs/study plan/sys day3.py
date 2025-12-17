Excellent.
These **two systems together** cover almost **every topic Google expects** at Senior/L5–L6:

* Strong consistency
* Distributed transactions
* Idempotency
* Async processing
* Saga
* Failure handling
* Scale & security

I’ll go **very deep**, exactly in **Google system-design interview style**.

---

# 🧱 SYSTEM DESIGN 1: PAYMENT SYSTEM (IN DEPTH)

---

## 1️⃣ REQUIREMENTS

### Functional

* Process payments (card / UPI / wallet)
* Support retries
* Prevent double charging
* Handle refunds
* Track payment status

### Non-Functional

* **Strong consistency**
* **High availability**
* **Low latency**
* **Idempotency**
* **Security (PCI, encryption)**

---

## 2️⃣ HIGH-LEVEL ARCHITECTURE

```
Client
  ↓
API Gateway
  ↓
Payment Service
  ↓
┌───────────────┐
│  Redis Cache  │ ← Idempotency keys
└───────────────┘
  ↓
Payment DB (SQL)
  ↓
Message Queue (Kafka / PubSub)
  ↓
Bank / PSP
```

---

## 3️⃣ CORE COMPONENTS

### 🔹 API Gateway

* Auth
* Rate limiting
* Request validation

---

### 🔹 Payment Service

Responsibilities:

* Validate request
* Generate payment ID
* Enforce idempotency
* Manage state transitions

---

### 🔹 Payment State Machine

```
INITIATED → AUTHORIZED → CAPTURED → SETTLED
                 ↓
              FAILED
```

---

## 4️⃣ IDEMPOTENCY (CRITICAL)

### Why?

* Network retries
* Client re-submission
* MQ redelivery

### Implementation

```
Idempotency-Key → Payment-ID
```

* Store key in Redis
* TTL = few hours
* Same request → same result

---

## 5️⃣ DATABASE DESIGN

### Payment Table

```sql
payment_id (PK)
order_id
amount
currency
status
idempotency_key
created_at
```

---

## 6️⃣ ASYNC PROCESSING

### Why Async?

* Bank calls are slow
* Avoid blocking user

### Flow

```
Payment Service → Kafka → PSP Worker → Bank
```

---

## 7️⃣ FAILURE HANDLING

| Failure           | Handling           |
| ----------------- | ------------------ |
| Bank timeout      | Retry              |
| Duplicate request | Idempotency        |
| Partial success   | Reconciliation job |
| MQ failure        | DLQ                |

---

## 8️⃣ CONSISTENCY MODEL

* **Strong consistency** for payment status
* Single writer per payment ID
* DB transactions

---

## 9️⃣ SECURITY

* Tokenization
* TLS
* Encryption at rest
* PCI DSS compliance

---

## 10️⃣ SCALING

* Shard by `payment_id`
* Stateless services
* Horizontal scaling

---

# 🧱 SYSTEM DESIGN 2: ORDER MANAGEMENT SYSTEM (OMS)

---

## 1️⃣ REQUIREMENTS

### Functional

* Create order
* Track order status
* Integrate payment
* Support cancellation

### Non-Functional

* Eventual consistency
* High throughput
* Fault tolerance

---

## 2️⃣ HIGH-LEVEL ARCHITECTURE

```
Client
  ↓
API Gateway
  ↓
Order Service
  ↓
Order DB
  ↓
Kafka / PubSub
  ↓
Payment | Inventory | Shipping
```

---

## 3️⃣ ORDER STATE MACHINE

```
CREATED → PAID → SHIPPED → DELIVERED
   ↓
CANCELLED
```

---

## 4️⃣ DATABASE DESIGN

```sql
order_id (PK)
user_id
total_amount
status
created_at
```

---

## 5️⃣ EVENT-DRIVEN FLOW

### Order Created Event

```
OrderCreated →
   Payment Service
   Inventory Service
   Notification Service
```

---

## 6️⃣ SAGA IMPLEMENTATION (CORE)

### Orchestration Saga

```
Order Saga Coordinator
   ↓
Payment → Inventory → Shipping
```

---

### Compensation Logic

| Step      | Compensation |
| --------- | ------------ |
| Payment   | Refund       |
| Inventory | Release      |
| Shipping  | Cancel       |

---

## 7️⃣ FAILURE SCENARIOS

| Scenario           | Action       |
| ------------------ | ------------ |
| Payment failed     | Cancel order |
| Inventory shortage | Refund       |
| Shipping failure   | Retry        |

---

## 8️⃣ CONSISTENCY

* **Eventual consistency**
* Saga ensures correctness
* No 2PC

---

## 9️⃣ SCALING OMS

* Partition by `order_id`
* Event streaming
* Cache order status

---

## 10️⃣ OBSERVABILITY

* Correlation IDs
* Distributed tracing
* Event logs

---

# 🔗 HOW PAYMENT + OMS WORK TOGETHER

```
Order Created
   ↓
Payment Initiated
   ↓
Payment Success → Order Paid
   ↓
Inventory Reserved
```

---

# 🎯 CROSS QUESTIONS & ANSWERS (INTERVIEW GOLD)

---

### Q1. Why Payment needs strong consistency but Order doesn’t?

**Answer:**
Money cannot be duplicated; orders can tolerate temporary inconsistency.

---

### Q2. How do you prevent double payment?

**Answer:**
Idempotency keys + unique constraints + state machine.

---

### Q3. What if payment succeeds but order update fails?

**Answer:**
Saga reconciliation → order update retry or refund.

---

### Q4. Why not use 2PC?

**Answer:**
Blocking, poor scalability, SPOF.

---

### Q5. How do you handle retries safely?

**Answer:**
Idempotent APIs and consumers.

---

### Q6. How to reconcile bank mismatches?

**Answer:**
Async reconciliation job comparing PSP and internal records.

---

### Q7. Kafka vs REST between Order & Payment?

**Answer:**
Kafka decouples services and improves resilience.

---

### Q8. What if Kafka is down?

**Answer:**
Persist events locally, retry publishing, or fallback to sync.

---

### Q9. How do you scale Payment Service?

**Answer:**
Shard DB, stateless service, async workers.

---

### Q10. How do you test failure scenarios?

**Answer:**
Chaos testing, fault injection, retries validation.

---

# 🧠 GOOGLE INTERVIEW EVALUATION CRITERIA

✔ Correct abstraction
✔ Trade-offs explained
✔ Failure handling
✔ Idempotency & Saga
✔ Security awareness

---

## 🚀 NEXT STEPS (FINAL PREP)

1️⃣ **Full Google System Design Mock (Live)**
2️⃣ **Behavioral + Googleyness (STAR)**
3️⃣ **Hiring committee level Q&A**

Say **“Mock System Design Interview”** and I’ll run it exactly like Google 🔥
