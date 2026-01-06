🧠 Mental model to lock this in
Think of it like this:
| Frontend   | Backend      |
| ---------- | ------------ |
| JavaScript | NodeJS       |
| React      | Express      |
| Hooks      | Middleware   |
| Events     | Requests     |
| Props      | Request Body |

Backend concepts have hidden prerequisites that frontend doesn’t.

Example:

Routing doesn’t make sense unless you know HTTP

Middleware doesn’t make sense unless you know routing

Request bodies don’t make sense unless you know POST

---

# NodeJS (Server-Side JavaScript)

This folder contains **concept-based notes and examples** for learning backend
development using **Node.js** and **Express.js**.

The goal of this folder is **understanding**, not building full applications.
Each subfolder focuses on **one idea at a time**, with heavily commented files
that explain *what happens, when it happens, and why it happens*.

This mirrors how the frontend folders (HTML, CSS, React) are organized in this
repository.

---

## What is Node.js?

**Node.js** allows JavaScript to run **outside the browser**.

Instead of responding to user clicks and UI events (frontend),
Node.js code typically:

- waits for requests
- processes data
- returns responses
- interacts with files, databases, or APIs

In other words:

> Frontend JavaScript **reacts to users**  
> Backend JavaScript **waits for clients**

---

## Where does Express.js fit?

**Express.js** is a lightweight framework that runs **on top of Node.js**.

Node.js provides the engine.  
Express provides convenience.

Express helps with:
- creating servers
- defining routes (URLs)
- reading requests
- sending responses
- handling middleware and errors

Because Express depends on Node, it is **not separated into its own top-level
folder**. Instead, Express concepts are introduced gradually *inside* this
NodeJS learning path.

---

## Folder Philosophy

This folder is **concept-driven**, not project-driven.

That means:
- No “real app” pressure
- No MVC / controllers / services yet
- No databases or auth at the start
- No hidden magic

Each file should be readable **top-to-bottom** and answer:
- When does this code run?
- What triggers it?
- What problem does it solve?

---

## Learning Order (Recommended)

The folders are designed to be read in this general order:

1. **node-basics**
   - what Node is
   - how Node runs JavaScript
   - modules and files

2. **http-basics**
   - what HTTP is
   - requests vs responses
   - status codes and methods

3. **express-basics**
   - creating a server
   - listening on a port
   - sending text and JSON

4. **routing**
   - GET vs POST
   - URL paths
   - route matching

5. **requests**
   - params
   - query strings
   - request bodies

6. **middleware**
   - what middleware is
   - how `next()` works
   - logging and request flow

7. **errors**
   - 404 handling
   - error middleware
   - graceful failures

These folders are **logically ordered**, but each one is still **self-contained**.

---

## How to Use These Files

Recommended workflow:

1. Open a single file
2. Read the comments first
3. Run the file (if applicable)
4. Observe console output
5. Modify one line and re-run
6. Re-read the comments

Treat each file like **executable notes**.

---

## Important Mental Model

Backend code does **not** run immediately.

Most backend code:
- starts once
- then waits
- then reacts to requests

If something feels confusing, the first question to ask is:

> “When does this code actually run?”

---

## Status

This folder is intentionally minimal at the start.
Complexity will be added **only after fundamentals are clear**.

Clarity > speed  
Understanding > buzzwords  
Notes > projects (for now)

---

## Related Frontend Concepts

| Frontend Concept | Backend Equivalent |
|------------------|-------------------|
| Events           | Requests          |
| Props            | Request body      |
| State            | Server memory / DB|
| Hooks            | Middleware        |
| Routes (React)   | Routes (Express)  |

---

End of README.
