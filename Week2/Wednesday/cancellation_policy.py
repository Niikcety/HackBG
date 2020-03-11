from datetime import datetime, timedelta


def validate_conditions(conditions):
	counter = 0
	for condition in conditions:
		if not condition.get('hours'):
			counter += 1
		elif condition.get('hours') > 24:
			raise ValueError("Hours cannot be > 24.")

	if counter != 1:
		raise ValueError("Invalid conditions.")


def ensure_conditions(conditions):
    # Ensure all condtions have hours
    for condition in conditions:
    	if not condition.get('hours'):
    		condition['hours'] = 0

    return conditions



def group_conditions(conditions):
# TODO
	hours = []
	group = []
	for condition in conditions:
		hours.append(condition.get('hours'))

	if hours != sorted(hours):
		hours.sort(reverse = True)

	for i in range(0,len(hours)-1):
		group.append((hours[i],hours[i+1]))

	return group


def get_current_condition(conditions, start, now):
    return conditions[0]


def get_cancellation_fee(price, percent):
    return price * (percent / 100)


def get_cancellation_policy(
    conditions,
    price,
    start,
    now
):
    assert start < now
    validate_conditions(conditions)

    ensure_conditions = ensure_conditions(conditions)
    grouped_conditions = group_conditions(conditions)

    current = get_current_condition(group_conditions)

    return get_cancellation_fee(current)


def main():
    now = datetime.now()
    booking_start = now + timedelta(hours=10)
    price = 1000
    conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'percent': 100}
    ]

    result = get_cancellation_policy(
        conditions,
        price,
        booking_start,
        now
    )
    print(result)


if __name__ == '__main__':
    main()