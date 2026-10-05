from credit_services_refresh import fetch_statement, statement_rows

targets = [("4546","長亨"),("3659","百辰"),("6618","永虹先進")]
for ticker, company in targets:
    raw = fetch_statement(ticker, company, "20261")
    rows = statement_rows(raw)
    print("==", ticker, company, "==")
    for k, v in rows.items():
        print(repr(k), v)
