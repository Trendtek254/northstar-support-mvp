# Northstar Retail Support MVP
## Go-Live Readiness Note

**Project:** Northstar Retail Support Deflection MVP  
**Version:** MVP  
**Status:** Ready for demonstration and controlled internal use

---

## 1. What Works

The Northstar Retail Support MVP is a Streamlit-based support application designed to reduce repetitive customer support tickets.

The MVP currently supports three common support categories:

### Order Status
- Customers can enter their Order ID.
- The system checks the mock order database.
- Customers receive the current order status and available tracking information.
- Invalid or unknown Order IDs return a clear error message.

### Returns & Refunds
- Customers can enter an Order ID to check return eligibility.
- Delivered orders are identified as eligible for return.
- Orders that have not been delivered are identified as ineligible at the current stage.
- The application provides the general Northstar return policy.
- Eligible returns provide instructions for initiating the return and downloading a return label.

### Stock Availability
- Customers can select a product from the available inventory.
- Customers can select or enter the required size.
- The system checks the mock inventory database.
- The application reports whether the requested item is in stock.
- When a requested size is unavailable, the application displays other available sizes where applicable.

### Data
The MVP uses mock JSON data stored in the `/data` directory:
- `orders.json` — mock customer order information.
- `inventory.json` — mock product and stock information.

The application can be launched locally using Streamlit.

---

## 2. Known Limitations / Broken Edge Cases

This is an MVP and does not connect to Northstar's real production systems.

Known limitations include:

- Order and inventory information is based on mock JSON data and is not real-time.
- The application does not connect to a real order management, inventory, payment, or shipping system.
- Tracking URLs and return labels are demonstration links/files and are not connected to real carrier or Northstar systems.
- Customer authentication is not implemented.
- The application does not verify that the person entering an Order ID is the actual customer.
- Refund processing is not performed automatically; the application only provides return/refund information.
- The return eligibility logic is simplified for the MVP and primarily relies on the order delivery status.
- Invalid product names, sizes, and Order IDs may return an error or unavailable message rather than providing a human support escalation.
- Mock data must be manually updated when testing different orders or inventory scenarios.
- No production database or persistent customer conversation history is currently implemented.

---

## 3. Internal Pickup Instructions

### Running the application

1. Clone or download the project repository.
2. Open a terminal in the project root.
3. Create and activate a Python virtual environment if required.
4. Install the required Python packages.
5. Run the application using:

```bash
streamlit run app.py
