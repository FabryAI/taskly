# src/core/calendar_link.py

from urllib.parse import quote
from datetime import datetime, timedelta

def generate_gcal_link(description: str, start_iso: str) -> str:
    """
    Generate a Google Calendar event creation link.
    """
    try:
        start = datetime.fromisoformat(start_iso)
    except ValueError:
        return "❌ Invalid date format"

    end = start + timedelta(hours=1)  # default 1-hour event
    fmt = "%Y%m%dT%H%M%SZ"
    start_str = start.strftime(fmt)
    end_str = end.strftime(fmt)

    base_url = "https://calendar.google.com/calendar/render?action=TEMPLATE"
    title = quote(description)
    details = quote("Event created by Taskly AI")

    return f"{base_url}&text={title}&dates={start_str}/{end_str}&details={details}"
