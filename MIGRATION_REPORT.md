# MIGRATION REPORT

## Student Information
- Course: CPE0049L - Software Design
- Project: Final Examination

---

## 1. Legacy System Analysis

The provided project is intended to be migrated from a monolithic architecture into a microservice-based architecture.

### Identified Code Smells
1. God Object - One class handles too many responsibilities.
2. Tight Coupling - Components depend directly on each other.
3. Hardcoded Values - Configuration values are written directly in the source code.

---

## 2. Migration Plan

The system will be divided into smaller services.

Example services:
- Authentication Service
- Data Processing Service
- Client Service

---

## 3. Design Patterns

### Factory Pattern

Purpose:
- Create service objects without directly specifying their classes.

Benefit:
- Easier to add new services in the future.

---

### Strategy Pattern

Dataset:

```
[78, 82, 91, 65, 40, 99, 88]
```

Strategies:

- Strategy A
  - Encryption
  - Key: 0x4F

- Strategy B
  - Compression
  - Factor: 0.85

---

## 4. JWT Authentication

JWT (JSON Web Token) is used to authenticate users.

Authentication Flow:

1. User enters username and password.
2. Server verifies the credentials.
3. If valid, the server creates a signed JWT.
4. The JWT is returned to the client.
5. The client includes the JWT in future requests.
6. The server verifies the JWT before allowing access.

Benefits:
- Stateless authentication
- Secure token verification
- Easy integration with APIs

---

## 5. Manual Verification of AI Output

AI-assisted outputs were reviewed manually before use.

Corrections made:
- Verified Markdown formatting.
- Verified GitHub workflow filenames.
- Verified command syntax.