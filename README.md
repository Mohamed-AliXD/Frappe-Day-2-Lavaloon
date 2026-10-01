# Day 2 – Flights, Web Pages & Automation

Adds the **Airplane Flight** DocType, a public booking flow, and ticket business logic.

- **Airplane Flight** – submittable, published to the web at `/flights`; becomes *Completed* on submit (`airplane_flight.py`).
- **Web templates** – flight detail page and list row (`airplane_flight.html`, `airplane_flight_row.html`) with a "Book Flight" button; `show-me.html` is a small colour demo.
- **Book Flight web form** – `/book-flight` creates an Airplane Ticket (`book_flight_ticket_web_form.json`).
- **Airplane Ticket logic** – random seat on insert, duplicate add-ons removed, total = flight price + add-ons, submit only when *Boarded* (`airplane_ticket.py`).
- **Flight Passenger** – builds `full_name` on save (`flight_passenger.py`).
- **Patch** – `populate_seats.py` backfills seats on existing tickets.
- **Notification** – emails System Managers 1 day before a scheduled flight departs.

`web_form.json` and `notification.json` are Frappe's built-in DocType definitions, included for reference.
