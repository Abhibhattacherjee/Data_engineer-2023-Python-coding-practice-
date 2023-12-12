import re
import pandas  as pd
import numpy as np
import scipy as sc


repetitive_phrases = ['issue with login', 'reset password']

def is_repetitive_ticket(ticket_description):
    for phrase in repetitive_phrases:
        if re.search(phrase, ticket_description, re.IGNORECASE):
            return True
    return False

def handle_repetitive_ticket(ticket_id):
    # Implement actions to handle the repetitive ticket
    print(f"Handling repetitive ticket {ticket_id}")

# Simulated ticket information
ticket_id = 123
ticket_description = "I'm having an issue with login."

# Check if the ticket is repetitive
if is_repetitive_ticket(ticket_description):
    handle_repetitive_ticket(ticket_id)
else:
    print(f"Ticket {ticket_id} is not repetitive.")
