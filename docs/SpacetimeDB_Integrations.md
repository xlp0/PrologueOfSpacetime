# SpacetimeDB Integrations

## Supported Languages

SpacetimeDB supports multiple languages for defining both server-side business logic (modules) and connecting via client-side libraries.

### Server-Side (Modules)
When writing backend logic that runs directly inside the database, developers can use:
- **Rust**: The core language for building robust systems in SpacetimeDB, compiling highly efficient WebAssembly modules.
- **C#**: A leading option, particularly useful for teams building games with Unity, so they can share code and use a consistent language across the stack.
- **TypeScript**: An excellent choice for full-stack web developers building multiplayer browser experiences using web standards, executing via V8.
- **C++**: Supported for performance-critical projects and developers deeply entrenched in existing C++ codebases.

### Client-Side SDKs
To connect applications to the database and establish real-time socket connections, SpacetimeDB offers SDKs in:
- **Rust**
- **C#**
- **TypeScript** 

The TypeScript SDK provides seamless integrations with major modern web frameworks such as **React**, **Vue**, **Angular**, and **Svelte**. These integrations provide reactive hooks (like React's standard `useEffect`, `useState`) and composables to automate syncing UI components directly with the ongoing database state changes.

## Engine Integrations

Because SpacetimeDB is built to support massively multiplayer games (originally developed to run games like *BitCraft*), its strongest integrations are directly tied to standard game engines.

### 1. Unity
- The C# Client SDK seamlessly integrates with Unity. 
- Unity developers can generate C# code directly from their database schema. It creates type-safe classes that perfectly mirror the backend database, allowing them to subscribe to tables directly within standard Unity scripts.

### 2. Unreal Engine
- SpacetimeDB offers first-party integration support for Unreal Engine.
- This encompasses both C++ SDK connectivity for performance-critical systems and full support for traditional Unreal Engine **Blueprints**, giving designers visual access to networking layers.

## General Systems & LLM Integrations

Because SpacetimeDB operates as an application server itself, its database "procedures" can execute external network requests. Developers can author modules that query third-party APIs from inside the database:
- **Large Language Models (LLMs)**: Connecting the database backend to LLMs (OpenAI, Anthropic, or local open-source models).
- traditional REST API connections to auxiliary web services.
