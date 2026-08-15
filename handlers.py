"""
Handlers for NS-07 (UI <-> backend integration).
Now wired to real business logic in logic.py (NS-03/04/05).
"""

import re
from logic import get_order_status, evaluate_return, query_inventory


def route_message(user_message: str) -> str:
    """
    Simple intent router: decides which handler to call based on
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