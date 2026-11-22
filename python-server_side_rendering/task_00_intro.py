#!/usr/bin/env python3
"""Module for generating invitation files from a template."""

import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def generate_invitations(template, attendees):
    """Generate invitation from a template str and a list of attendee dicts.
    """
    # Validate input types
    if not isinstance(template, str):
        logging.error(
            "Invalid input type for template: expected str, got %s.",
            type(template).__name__,
        )
        return

    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        logging.error(
            "Invalid input type for attendees: expected list of dicts, got %s.",
            type(attendees).__name__,
        )
        return

    # Empty inputs
    if template == "":
        logging.error("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None or value == "":
                replacement = "N/A"
            else:
                replacement = str(value)
            content = content.replace(f"{{{key}}}", replacement)

        filename = f"output_{index}.txt"
        try:
            if os.path.exists(filename):
                logging.warning(
                    "File %s already exists and will be overwritten.", filename
                )
            with open(filename, "w", encoding="utf-8") as out_file:
                out_file.write(content)
        except OSError as err:
            logging.error("Failed to write %s: %s", filename, err)
