from datetime import datetime, timedelta


def get_next_two_weeks():
        today = datetime.today()
        # Calculate the start of the current week (Sunday)
        start_of_week = today - timedelta(days=today.weekday() + 1) if today.weekday() != 6 else today
        # Calculate the start of the next two weeks
        next_week_start = start_of_week + timedelta(weeks=1)
        two_weeks_start = start_of_week + timedelta(weeks=2)
        return (
            next_week_start.strftime("%m/%d"),
            two_weeks_start.strftime("%m/%d"),
        )
