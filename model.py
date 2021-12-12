import requests

class Model():

    def __init__(self):
        self.baseCurrency = "EUR"
        self.amount = 0
        self.targetCurrency = None

    def req(self, currencies):
        payload = {'access_key': 'latest'}
        r = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key=f9f271f121e28cbe28ffbc52b2bfa215&symbols={currencies}")
        if r.status_code != 200:
            print(r.status_code)
            print(r.json())
            raise Exception(r.json()['error']['message'])
        return r.json()

    def convertCurrency(self):
        result = []
        try:
            target = self.req(self.targetCurrency)
            base = self.req(self.baseCurrency)['rates']
            base = 1/base[next(iter(base.keys()))]
            print(base)
            print(type(base))
            for key, value in target["rates"].items():
                result.append(f"{(value*base*self.amount)} {key}")
            return result
        except Exception as e:
            raise e

    def getRates(self):
        result = []
        base = self.req(self.baseCurrency)['rates']
        base = 1/base[next(iter(base.keys()))]
        try:
            for item in self.req(self.targetCurrency)["rates"].items():
                result.append(item[1]*base)
            return result
        except Exception as e:
            raise e

    def getDate(self):
        try:
            return self.req(self.targetCurrency)['date']
        except Exception as e:
            raise e

    def reset(self):
        self.baseCurrency = ""
        self.amount = 0
        self.targetCurrency = None


    def setTargetCurrency(self, tG):
        self.targetCurrency = tG

    def setBaseCurrency(self, bC):
        self.baseCurrency = bC

    def setAmount(self, a):
        self.amount = a


if __name__ == "__main__":
    m = Model()
    m.setTargetCurrency("USD, EUR, CHF, AED")
    try:
        m.setBaseCurrency("PLN++")
        print(m.baseCurrency)
        print(m.req(m.baseCurrency))
        print(m.convertCurrency())
        #print(m.getDate())
        #print(m.getRates())
    except Exception as e:
        print(e)