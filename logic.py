"""
Core business logic for Northstar Support MVP.
Covers: order status lookup (NS-03), return eligibility (NS-04),
and inventory queries (NS-05).

Currently backed by in-memory sample data. Swap the data sources
below for a real database/API when available.
"""

from datetime import date, timedelta

# --- Sample data (replace with real DB/API calls later) ---

ORDERS = {
    "10234": {"status": "In Transit", "eta_days": 2},
    "10235": {"status": "Delivered", "eta_days": 0},
    "10236": {"status": "Processing", "eta_days": 5},
    "10237": {"status": "Delivered", "eta_days": 0},
}

PURCHASE_DATES = {
    "10234": date.today() - timedelta(days=5),
    "10235": date.today() - timedelta(days=10),
    "10236": date.today() - timedelta(days=1),
    "10237": date.today() - timedelta(days=45),  # outside return window
}

INVENTORY = {
    "blue t-shirt": 12,
    "running shoes": 0,
    "wireless mouse": 34,
    "coffee mug": 5,
}

RETURN_WINDOW_DAYS = 30


# --- Public functions ---

def get_order_status(order_number: str) -> str:
    """Look up the status of an order by its order number."""
    order = ORDERS.get(order_number.strip())
    if not order:
        return f"I couldn't find an order matching **{order_number}**. Please double-check the order number."

    status = order["status"]
    if status == "Delivered":
        return f"Order **{order_number}** has already been **Delivered**."
    return (
        f"Order **{order_number}** is currently **{status}** "
        f"and expected to arrive in {order['eta_days']} day(s)."
    )


def evaluate_return(question: str, order_number: str = None) -> str:
    """
    Evaluate return eligibility. If an order number is provided (or found
    in the question text), checks against the purchase date and return window.
    """
    if not order_number:
        for token in question.split():
            cleaned = token.strip("?.,!#")
            if cleaned in PURCHASE_DATES:
                order_number = cleaned
                break

    if not order_number or order_number not in PURCHASE_DATES:
        return (
            "To check return eligibility, please provide your order number "
            f"(items are eligible for return within {RETURN_WINDOW_DAYS} days of purchase)."
        )

    purchased_on = PURCHASE_DATES[order_number]
    days_since = (date.today() - purchased_on).days

    if days_since <= RETURN_WINDOW_DAYS:
        remaining = RETURN_WINDOW_DAYS - days_since
        return (
            f"Order **{order_number}** is **eligible** for return "
            f"({remaining} day(s) remaining in the return window)."
        )
    return (
        f"Order **{order_number}** is **not eligible** for return — "
        f"it was purchased {days_since} days ago, which exceeds the "
        f"{RETURN_WINDOW_DAYS}-day return window."
    )


def query_inventory(item_name: str) -> str:
    """Check current stock level for an item by name (case-insensitive match)."""
    key = item_name.strip().lower()

    if key in INVENTORY:
        count = INVENTORY[key]
        if count == 0:
            return f"**{item_name}** is currently **out of stock**."
        return f"**{item_name}** currently has **{count} unit(s)** in stock."

    matches = [name for name in INVENTORY if key in name or name in key]
    if matches:
        best = matches[0]
        count = INVENTORY[best]
        return f"Did you mean **{best}**? It has **{count} unit(s)** in stock."

    return f"I couldn't find **{item_name}** in our inventory system."