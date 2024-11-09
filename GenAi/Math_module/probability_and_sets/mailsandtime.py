import random
from datetime import datetime, timedelta

def generate_email_data(num_emails):
    emails = []
    send_time = datetime.now()
    for _ in range(num_emails):
        opened = random.random() < 0.4  # 40% chance of being opened
        if opened:
            minutes_to_open = random.randint(1, 60)
            open_time = send_time + timedelta(minutes=minutes_to_open)
            clicked = random.random() < 0.3  # 30% chance of click if opened
        else:
            open_time = None
            clicked = False
        emails.append((opened, open_time, clicked))
    return emails

# Generate email data
num_emails = 10
email_data = generate_email_data(num_emails)

# Set A: Emails opened in odd-numbered minutes
set_A = set(i for i, (opened, open_time, _) in enumerate(email_data) 
            if opened and open_time and (open_time.minute % 2 != 0))

# Set B: Emails that led to a click-through
set_B = set(i for i, (_, _, clicked) in enumerate(email_data) if clicked)

# Intersection: Emails opened in odd minutes and clicked
intersection = set_A.intersection(set_B)

# Calculate probability
p_b_given_a = len(intersection) / len(set_A) if set_A else 0

print(f"Total emails sent: {num_emails}")
print(f"Emails opened in odd-numbered minutes: {len(set_A)}")
print(f"Emails that led to click-throughs: {len(set_B)}")
print(f"Emails opened in odd minutes and clicked: {len(intersection)}")
print(f"P(Click | Opened in odd minute) = {p_b_given_a:.4f}")

# Additional analysis
total_opened = sum(1 for opened, _, _ in email_data if opened)
total_clicked = len(set_B)
print(f"\nOverall open rate: {total_opened / num_emails:.4f}")
print(f"Overall click-through rate: {total_clicked / num_emails:.4f}")
print(f"Click-through rate for opened emails: {total_clicked / total_opened:.4f}")