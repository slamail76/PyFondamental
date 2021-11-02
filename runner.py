import asyncio
import fundamental_indicators_provider
from fundamental_indicators_provider import Company
config = {}
lista = ['AAPL', 'FB']

for azienda in lista:
    company = Company(azienda)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fundamental_indicators_provider.get_fundamental_indicators_for_company(config, company))
    print(company.fundamental_indicators)
