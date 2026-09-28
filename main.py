from mcp.server import MCPServer


mcp = MCPServer("Leave Management")


@mcp.tool()
def get_leave_balance(employee_id: str) -> dict:
    """Get the available leave balance for an employee."""

    employees = {
        "EMP001": {
            "name": "Chandini",
            "casual_leave": 8,
            "sick_leave": 5,
            "earned_leave": 12,
        },
        "EMP002": {
            "name": "Rahul",
            "casual_leave": 6,
            "sick_leave": 4,
            "earned_leave": 10,
        },
    }

    employee = employees.get(employee_id)

    if not employee:
        return {
            "success": False,
            "message": f"Employee {employee_id} not found."
        }

    return {
        "success": True,
        "employee_id": employee_id,
        "employee_name": employee["name"],
        "leave_balance": {
            "casual_leave": employee["casual_leave"],
            "sick_leave": employee["sick_leave"],
            "earned_leave": employee["earned_leave"],
        },
    }

@mcp.tool()
def apply_leave(employee_id: str, leave_type: str, days: int) -> dict:
    """Apply for leave for an employee after checking available balance."""

    employees = {
        "EMP001": {
            "name": "Chandini",
            "casual_leave": 8,
            "sick_leave": 5,
            "earned_leave": 12,
        },
        "EMP002": {
            "name": "Rahul",
            "casual_leave": 6,
            "sick_leave": 4,
            "earned_leave": 10,
        },
    }

    employee = employees.get(employee_id)

    if not employee:
        return {
            "success": False,
            "message": f"Employee {employee_id} not found."
        }

    if leave_type not in ["casual_leave", "sick_leave", "earned_leave"]:
        return {
            "success": False,
            "message": "Invalid leave type."
        }

    if days <= 0:
        return {
            "success": False,
            "message": "Number of leave days must be greater than 0."
        }

    available_days = employee[leave_type]

    if days > available_days:
        return {
            "success": False,
            "message": (
                f"Insufficient {leave_type}. "
                f"Available: {available_days}, Requested: {days}."
            )
        }

    employee[leave_type] -= days

    return {
        "success": True,
        "message": "Leave applied successfully.",
        "employee_id": employee_id,
        "employee_name": employee["name"],
        "leave_type": leave_type,
        "days_applied": days,
        "remaining_balance": employee[leave_type],
    }

if __name__ == "__main__":
    mcp.run()