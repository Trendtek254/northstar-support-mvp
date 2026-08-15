"""
Mock backend handlers for NS-07 (UI <-> backend integration).
These will be replaced by real implementations from NS-03 (order lookup),
NS-04 (return eligibility), and NS-05 (inventory query) once pushed.
"""

import re

def get_order_status(order_number: str) -> str:
    """Mock order status lookup. Replace with NS-03 import when available."""
    return (
        f"Order **{order_number}** is currently *In Transit* and expected "
        f"to arrive in 2-3 business days. (mock response)"
    )

def evaluate_return(question: str) -> str:
    """Mock return eligibility check. Replace with NS-04 import when available."""
    return (
        f"Based on your question, this item appears *eligible* for return "
        f"within 30 days of purchase. (mock response)"
    )

def query_inventory(item_name: str) -> str:
    """Mock inventory lookup. Replace with NS-05 import when available."""
    return f"**{item_name}** currently shows *12 units* in stock. (mock response)"


def route_message(user_message: str) -> str:
    """
    Very simple intent router: decides which handler to call based on
    keywords/patterns in the user's chat input.
    """
    text = user_message.lower()

    order_match = re.search(r"\b(order\s*#?\s*)?(\d{4,})\b", text)
    if order_match and ("order" in text or order_match.group(2)):
        order_number = order_match.group(2)
        return get_order_status(order_number)

    if "return" in text or "refund" in text:
        return evaluate_return(user_message)

    if "stock" in text or "inventory" in text or "available" in text:
        return query_inventory(user_message)

    return (
        "I can help with order status, returns/refunds, or stock questions. "
        "Try asking something like 'Where is order 10234?' or "
        "'Can I return this item?'"
    )