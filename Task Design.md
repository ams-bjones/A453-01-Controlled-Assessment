Creating a Currency Converter.
====

That...
a) Has exchange rates that can be regularly changed by the user.
b) User should be able to enter an amount, select chosen currency, and the currency to convert it into.
c) Figure shown should be to two decimal places.

Currencys required: GBP (£) Euro (€) USD ($) and JPY (¥)

Tests
====

Import symbols        (GBP, EUR, USD, JPY)
import exchange rates   (1, 1.2, 1.6, 200)

GBP - EUR = GBP * EUR
GBP - USD = GBP * USD
GBP - JPY = GBP * JPY

EUR - GBP = EUR * EUR
EUR - USD = EUR * USD
EUR - JPY = EUR * JPY

