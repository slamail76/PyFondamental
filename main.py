import asyncio
import pandas
import pandas_datareader
import yahoo_fin.stock_info as si

async def get_fundamental_indicators_for_company(config, company):
    company.fundamental_indicators = {}

    # Statistics Valuation
    keys = {
        'Market Cap (intraday) 5': 'MarketCap',
        'Price/Sales (ttm)': 'PS',
        'Trailing P/E': 'PE',
        'PEG Ratio (5 yr expected) 1': 'PEG',
        'Price/Book (mrq)': 'PB'
     }
    data = si.get_stats_valuation(company.symbol)
    get_data_item(company.fundamental_indicators, data, keys)

    # Income statement and Balance sheet
    data = get_statatistics(company.symbol)

    get_data_item(company.fundamental_indicators, data,
                  {
                      'Profit Margin': 'ProfitMargin',
                      'Operating Margin (ttm)': 'OperMargin',
                      'Current Ratio (mrq)': 'CurrentRatio',
                      'Payout Ratio 4': 'DivPayoutRatio'
                  })

    get_last_data_item(company.fundamental_indicators, data,
               {
                   'Return on assets': 'ROA',
                   'Return on equity': 'ROE',
                   'Total cash per share': 'Cash/Share',
                   'Book value per share': 'Book/Share',
                   'Total debt/equity': 'Debt/Equity'
               })
