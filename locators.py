from datetime import datetime


class APIPartnerData:
    DateFrom = 1632949200
    DateTo = 1633035599
    DateFromToday = datetime.timestamp(datetime(datetime.now().date().year, datetime.now().date().month, datetime.now().date().day, 0, 0, 0))
    DateToToday = datetime.timestamp(datetime(datetime.now().date().year, datetime.now().date().month, datetime.now().date().day, 23, 59, 0))
    StartDate = str(datetime(datetime.now().date().year, datetime.now().date().month, datetime.now().date().day, 0, 0, 0))
    EndDate = str(datetime(datetime.now().date().year, datetime.now().date().month, datetime.now().date().day, 23, 59, 0))


class TransferWallet:
    addTransferWallet_Url = 'transferwallet/AddTransferWallet'
    depositInTransferWallet_Url = 'transferwallet/DepositInTransferWallet'
    getBalanceTransferWallet_Url = 'transferwallet/GetBalanceTransferWallet'
    getTransactionHistory_Url = 'transferwallet/GetTransactionHistory'
    withdrawInTransferWallet_Url = 'transferwallet/WithdrawInTransferWallet'
