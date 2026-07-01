The **Personal Knowledge Container (PKC)** is a self-hosted, **unified interface layer** to provide a standardized platform for managing various AI projects and data. Rather than building a unique interface for every individual project—such as coal mining, energy, or shopper analytics—PKC acts as a single framework that can be deployed across different sectors.

The following details outline the core components and functionalities of PKC based on the sources:

### **1. Technical Architecture and Deployment**
*   **Hardware:** PKC is designed to run on **local hardware**, specifically mini-computers like the **Raspberry Pi**.
*   **Self-Hosting:** It is a **self-hosted system**, allowing clients to keep their data local for better privacy, lower storage costs, and easier backups.
*   **Portal Access:** Users can access their local PKC instance from anywhere via a browser or phone through a portal (such as **pkc.pub**). The system includes a **server registry** where users can register their local server to a public domain and connect to it as a path.
*   **Multiple Nodes:** For large-scale operations, such as a supermarket chain, PKC can support **multiple nodes** that send data to various locations or a centralized cloud.

### **2. Core Functionalities**
*   **Browser-Based IDE:** PKC functions as a **"browser IDE,"** allowing users to edit server-side files, manage code, and open files directly within the browser.
*   **Remote Monitoring:** It provides a **dashboard** for real-time monitoring of activities, such as tracking shopper maps or viewing analytics graphs (e.g., via integration with Graphana).
*   **Authentication Levels:** The system supports **multi-level authentication**, providing different access rights for developers (who can edit code), analysts, and shop owners (who may only need to monitor the dashboard).

### **3. AI and "Open Claw" Integration**
PKC is designed to be deeply integrated with AI assistants to make data more accessible:
*   **AI Assistants:** It can utilize models like **Llama, Claude (referred to as Cloudbot), or Gemini**.
*   **Natural Language Queries:** By integrating with services like **Open Claw**, users can query their data through a terminal or chat interface (even via external services like WhatsApp).
*   **System Memory:** The AI within PKC has **terminal access** and can memorize system data, allowing it to execute commands or answer specific questions about the data stored in the local file system (e.g., "How many customers were in the shop today?").

### **4. Strategic Purpose**
The primary goal of PKC is to serve as a **universal interface** that simplifies the deployment of AI solutions. By using this unified layer, the team avoids the "bottleneck" of developing new websites and interfaces for every project. It also serves as a consistent portal framework, ensuring that regardless of the specific service—be it energy management or retail analytics—the user interacts with a unified interface.