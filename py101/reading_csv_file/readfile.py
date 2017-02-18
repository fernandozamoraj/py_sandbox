

FILE_IO_CAPABLE = True

STOCK_SYMBOL_FIELD = 'stock_symbol'
COMPANY_NAME_FIELD = 'company_name'
EXCHANGE_COUNTRY_FIELD = 'exchange_country'
STOCK_PRICE_FIELD = 'stock_price'
EXCHANGE_RATE_FIELD = 'exchange_rate'
SHARES_OUTSTANDING_FIELD = 'shares_outstanding'
NET_INCOME_FIELD = 'net_income'
MARKET_VALUE_FIELD = 'marketvalue'

stockFieldNames = [
  STOCK_SYMBOL_FIELD, 
  COMPANY_NAME_FIELD, 
  EXCHANGE_COUNTRY_FIELD, 
  STOCK_PRICE_FIELD, 
  EXCHANGE_RATE_FIELD, 
  SHARES_OUTSTANDING_FIELD, 
  NET_INCOME_FIELD, 
  MARKET_VALUE_FIELD]

def getFile(fileName):

    if(FILE_IO_CAPABLE == True):
        file = open(fileName, 'r')
        return file
        
    else:
        #use alternate method of getting data when FILE IO IS NOT POSSIBLE
        file = [  
            "msft,Microsoft Corp,USA,45.99,1.2,30000,120000,30000", 
            "google,Microsoft Corp,USA,45.99,1.2,30000,0,30000", 
            ",Berkshire,USA,45000.00,1.2,30000,120000,30000", 
            "fb,USA,45.99,1.2,30000,120000,30000", 
            "fb,facebook,USA,45.99,1.2,30000,120000,30000", 
            "ua,under armour,USA,45.99,1.2,30000,120000,30000", 
        ]

        
        return file

class BadDataException(Exception):
    pass

class AbstractRecord:

    def __init__(self, name):
        self.name = name

class StockStatRecord(AbstractRecord):
        
    def rowToRecord(self, stockRecDict):

        try:

            if not stockRecDict[STOCK_SYMBOL_FIELD]:
                raise BadDataException('Stock Symbol is Empty')

            record = StockStatRecord(stockRecDict[STOCK_SYMBOL_FIELD])              
            record.company = stockRecDict[COMPANY_NAME_FIELD]
            record.exchangeCountry = stockRecDict[EXCHANGE_COUNTRY_FIELD]
            record.stockPrice = float(stockRecDict[STOCK_PRICE_FIELD])
            record.exchangeRate = float(stockRecDict[EXCHANGE_RATE_FIELD])
            record.sharesOutstanding = float(stockRecDict[SHARES_OUTSTANDING_FIELD])
            record.netIncome = float(stockRecDict[NET_INCOME_FIELD])
            
            if record.netIncome == 0:
                raise BadDataException('Net Income is 0')

            record.marketValue = record.stockPrice * record.exchangeRate * record.sharesOutstanding
            record.peRatio = (record.stockPrice * record.sharesOutstanding) / record.netIncome

            
            record.marketValue = float(stockRecDict[MARKET_VALUE_FIELD])
        except Exception as e:
            raise BadDataException('BadDataException: {0}'.format(e))

        return record

    def __str__(self):
        return 'StockStatRecord ({} {} {} {} {:06.2f} {:06.2f} {:06.2f} {:06.2f})'.format( 
        self.name, self.company, self.exchangeCountry, 
        self.exchangeRate, self.sharesOutstanding, 
        self.netIncome, self.marketValue, self.peRatio)


    
class CsvReader:

    def __init__(self, filename, fieldNames):
        self.filename = filename
        self.fieldNames = fieldNames
        self.records = []

    def load(self, recordTranslator):
        file = getFile(self.filename)

        '''
         read the records from 
         linr in file works with a file as well
        ''' 
        for line in file:
            try:
                if not line:
                    raise BadDataException("Empty line in file")

                values = line.split(',')

                #if record does not have the correct number of fields
                if(len(values) != len(self.fieldNames)):
                    raise BadDataException('BadDataException: Values has ' \
                           ' different length than fieldNames.\nLine: ' + \
                           line )

                
                #create dictionary of values
                rec = dict(zip(self.fieldNames, line.split(',')))

                #debugging code
                #print(rec)
                try:
                    candidateRecord = recordTranslator.rowToRecord(rec)
                except BadDataException as e1:
                    raise BadDataException('{} \nLine: {}'.format(e1, line))    
                
                self.records.append(candidateRecord)
            
            except BadDataException as bde:
                print(bde)
                print('...skipping record...')
            except Exception as e:
                print(e)
                print('...skipping record...')

        if(FILE_IO_CAPABLE):
            file.close()
        
        return self.records

    def getRecords(self):
        return self.records
        
reader = CsvReader("stocks.dat", stockFieldNames)

records = reader.load(StockStatRecord(""))

print('\n*********Valid Records*****')
for record in records:
    print(record)