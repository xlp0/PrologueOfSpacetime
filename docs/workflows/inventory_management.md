# Duwi's Workshop: Inventory Management Workflow

## Objective
To capture, document, and manage all existing and incoming equipment, tools, and projects across the 5 zones of Duwi's Workshop using an Agentic Workflow aligned with SSoT (Single Source of Truth) principles.

## The Problem
- A large amount of existing equipment is currently undocumented.
- Items in the Warehouse/Storage have suffered damage due to humidity and lack of tracking.
- We need a low-friction way for Duwi to document items without interrupting his physical work.

## Proposed Agentic Workflow

### 1. Data Capture (The "Perception" Path)
Instead of forcing Duwi to manually type out spreadsheets, we rely on voice and visual capture:
- **Action**: Duwi takes a quick photo of an item or a box of items.
- **Action**: Duwi records a short voice memo dictating what the item is, where he found it, and its current condition (e.g., "This is a broken laser cutter lens from the warehouse, it looks humid").
- **Ingestion**: These multimodal inputs are sent to the **Inventory Agent**.

### 2. Processing & Categorization (The "Algorithm")
The Inventory Agent uses LLM vision and audio transcription to structure the data based on the MCard schema (Homotopy Type Theory ADTs):
- **Sum Type (Identity/Who)**: What is this object? (e.g., Tool, Prototype, Broken Equipment). Generates a unique ID/Handle.
- **Product Type (Evolution/When)**: Where is this located currently? What is its condition? (Location × Condition × Timestamp).
- **Exponent Type (Reality/What)**: The raw photo, the audio transcript, and any extracted technical manuals or specifications linked to the item.

### 3. SSoT Integration (The "Card")
- The structured data is automatically compiled into an **MCard** directly within the PKC (Personal Knowledge Container).
- A corresponding physical QR code or NFC tag can be printed to stick onto the physical bin or machine.

### 4. Alerting & Maintenance (The "Reasoning" Path)
The Agent continuously audits the MCard database:
- **Humidity Alerts**: If items categorized under "Warehouse" are flagged with "rust" or "water damage" keywords, the Agent creates an urgent task to inspect the room's dehumidifier.
- **Maintenance Schedules**: If an item is a 3D printer in the Main Workshop, the agent sets a recurring reminder to lubricate the z-axis rods every 3 months.

## Implementation Steps
1. **Set up the Ingestion Channel**: A simple WhatsApp/Telegram bot or an iOS Shortcut that Duwi can use to send photos and voice notes directly to the Agent.
2. **Define the MCard Template**: Standardize the database fields specifically for Workshop Inventory.
3. **Database Selection**: Use the project's existing SSoT database to log these entries.
4. **Dashboard**: Create a simple Grafana or Next.js dashboard view showing inventory distribution across the 5 zones.
