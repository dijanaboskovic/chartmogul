import chartmogul
config = chartmogul.Config('7106bc21bea6d37151fade3a7f6a6454', 'e27de4134adda316b8c929d84779076a')

try:
    # Total MRR for Q1 2019
    req = chartmogul.Metrics.mrr(config,
                                 start_date='2019-01-01',
                                 end_date='2019-03-31',
                                 interval='quarter')
    total_q1_mrr = req.get()

    # January 2019 MRR
    req = chartmogul.Metrics.mrr(config,
                                 start_date='2019-01-01',
                                 end_date='2019-01-31')
    jan_mrr = req.get()

    # February 2019 MRR
    req = chartmogul.Metrics.mrr(config,
                                 start_date='2019-02-01',
                                 end_date='2019-02-28')
    feb_mrr = req.get()

    # March 2019 MRR
    req = chartmogul.Metrics.mrr(config,
                                 start_date='2019-03-01',
                                 end_date='2019-03-31')
    mar_mrr = req.get()

    # April 2019 MRR
    req = chartmogul.Metrics.mrr(config,
                                 start_date='2019-04-01',
                                 end_date='2019-04-30')
    apr_mrr = req.get()

    print("\u0332".join("Total MRR for Q1 2019: ") + str(total_q1_mrr.entries[0].mrr/100))
    print()
    print("January: " + str(jan_mrr.entries[0].mrr/100))
    print("February: " + str(feb_mrr.entries[0].mrr / 100))
    print("March: " + str(mar_mrr.entries[0].mrr / 100))
    print("April: " + str(apr_mrr.entries[0].mrr / 100))
except Exception as ex:
    print(ex)