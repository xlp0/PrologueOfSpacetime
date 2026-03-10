# SpacetimeDB Overview

## Introduction
SpacetimeDB is a unique backend platform that integrates a relational database with an application server, allowing application logic to run directly within the database itself. This architecture aims to simplify development and deployment, particularly for real-time applications such as multiplayer games, chat applications, and collaboration tools.

## Key Architectural Features

### 1. Unified Database and Server
SpacetimeDB acts as both a database and a server, eliminating the need for separate web or game servers, API layers, or message brokers. Clients connect directly to the database.

### 2. Modules for Business Logic
Application logic and schema are defined within "modules" that run inside the database. These modules can be written in languages such as C#, C++, Rust, or TypeScript, and are compiled into WebAssembly (Wasm) or JavaScript bundles.

### 3. Tables, Reducers, Procedures, and Views
*   **Tables**: The database uses SQL-like tables for data storage.
*   **Reducers**: Functions clients call to make requests, similar to stored procedures or RPC endpoints, and can also schedule other reducers.
*   **Procedures**: Functions exported by the database.
*   **Views**: Read-only functions for computing and returning results from tables.

### 4. Real-time Client Synchronization
SpacetimeDB automatically pushes real-time updates to subscribed clients when data in the database changes. Clients subscribe to specific data through queries, and the system sends incremental updates. Client-side SDKs maintain a local cache that mirrors the server state.

### 5. In-Memory State with Durability
To achieve high performance and low latency, all application state is held in memory. Data persistence and crash recovery are managed through a commit log on disk, ensuring durability while maintaining speed.

### 6. ACID Guarantees
SpacetimeDB provides all the ACID (Atomicity, Consistency, Isolation, Durability) guarantees of a traditional relational database management system.

### 7. Simplified Deployment ("Serverless" Approach)
The architecture significantly simplifies deployment by consolidating the backend into a single deployable unit, removing the need for managing separate web servers, containers, or Kubernetes. It's described as a "serverless" platform because the game logic runs within the database, abstracting away the underlying physical server infrastructure.

### 8. Built-in Access Control and Authorization
Authorization and permission logic can be implemented directly within the modules, allowing for integrated security.

### 9. Scalability and Concurrency
It is designed to handle a large number of concurrent users and data updates, employing database research principles to run functions in parallel and simplify multithreading for developers.

### 10. Client SDKs and APIs
SpacetimeDB offers official client SDKs for various languages and provides both HTTP and WebSocket APIs served on a single port.
