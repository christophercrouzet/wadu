Wadu
====

Wadu implements recurrence rules for calendar events.


## Features

* **sane**: the implementation is fairly linear and straightforward, making it
  easy enough to follow the code paths and make sense of them.
* **compliant**: implements the [RFC 5545 specification][rfc-5545] but also
  with the unambiguous [JSCalendar draft][jscalendar] from IETF.


## Usage

```py
# The 1st Friday of each month, for 10 occurrences.
rule = RecurrenceRule(MONTHLY,
                      on_week_days=(FRIDAY(1),),
                      count=10)
for dttm in rule:
    print(dttm)


# Every other year on January and February, starting on a given date.
rule = RecurrenceRule(YEARLY,
                      interval=2,
                      on_months=(JANUARY, FEBRUARY),
                      count=10)
start = datetime(1997, 3, 10, hour=9)
for dttm in rule.iterate_from(start):
    print(dttm)
```


## Repository

<https://github.com/christophercrouzet/wadu>


## License

[Unlicense][unlicense].


[jscalendar]: https://datatracker.ietf.org/doc/html/draft-ietf-calext-jscalendar
[rfc-5545]: https://tools.ietf.org/html/rfc5545
[unlicense]: https://unlicense.org
