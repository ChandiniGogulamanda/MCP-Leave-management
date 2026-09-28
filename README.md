# MCP Leave Management

A simple **Model Context Protocol (MCP)** server built with **Python** for managing employee leave operations.

## 🚀 Features

* Check employee leave balance
* Apply for leave
* Validate employee ID
* Validate leave type and requested days
* Check available leave balance
* Test MCP tools using **MCP Inspector**

## 🏗️ Architecture

```text
User / AI Assistant
        ↓
    MCP Client
        ↓
   MCP Server
        ↓
 ┌───────────────┐
 │  MCP Tools    │
 │               │
 │ • Get Balance │
 │ • Apply Leave │
 └───────┬───────┘
         ↓
   Employee Data
```

## 🛠️ Tech Stack

* **Python**
* **MCP Python SDK**
* **uv**
* **MCP Inspector**
* **STDIO**

## 🔧 MCP Tools

### `get_leave_balance`

Checks an employee's available leave.

**Input:**

```text
employee_id: EMP001
```

**Response:**

```json
{
  "success": true,
  "employee_id": "EMP001",
  "employee_name": "Chandini",
  "leave_balance": {
    "casual_leave": 8,
    "sick_leave": 5,
    "earned_leave": 12
  }
}
```

### `apply_leave`

Applies for leave after checking the available balance.

**Input:**

```text
employee_id: EMP001
leave_type: casual_leave
days: 2
```

**Response:**

```json
{
  "success": true,
  "message": "Leave applied successfully.",
  "employee_id": "EMP001",
  "employee_name": "Chandini",
  "leave_type": "casual_leave",
  "days_applied": 2,
  "remaining_balance": 6
}
```

## ▶️ Run the Project

### Install Dependencies

```bash
uv add "mcp[cli]"
```

### Run the MCP Server

```bash
uv run mcp run main.py
```

### Run MCP Inspector

```bash
uv run mcp dev main.py
```

## 📁 Project Structure

```text
MCP Leave management/
├── main.py
├── README.md
├── pyproject.toml
├── uv.lock
└── .venv/
```

## ⚠️ Current Limitation

Employee data is currently stored **in memory**, so changes are not persistent after the application stops.

## 🔮 Future Improvements

* **SQLite/PostgreSQL** database
* **Leave history**
* **Leave cancellation**
* **Employee authentication**
* **Leave approval workflow**   

## 👩‍💻 Author

**Chandini Gogulamanda**

**AI/ML Engineer | Generative AI | LLM Systems | RAG | Agentic AI**
"# MCP-Leave-management" 
