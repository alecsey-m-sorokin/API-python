import random
from datetime import datetime
import uuid
from config import settings
import pytest

from partner.pages.transferwallet_page import APITransferWallet
from locators import APIPartnerData

A = APIPartnerData
api = APITransferWallet

partner_transaction_id_uuid = uuid.uuid4().hex
transactions_types = {'deposit': 1, 'withdrawing': 2, 'debit': 3, 'credit': 4}
test_data = [(str(random.randint(10000000, 20000000)), 'TRY', '20', '10')]


# test_data = [('666666', 'FUN', 200, 15)]


@pytest.mark.parametrize("partner_user_id, currency, deposit, withdraw", test_data)
class TestTransferWallet:

    def test_01_partner_add_transfer_wallet(self, partner_user_id, currency, deposit, withdraw):
        add_transfer_wallet = api.add_transfer_wallet(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id, currency=currency,
                                                      apiKey=settings.node_ApiKey)

    def test_02_partner_deposit_in_transfer_wallet(self, partner_user_id, currency, deposit, withdraw):
        partner_transaction_id = 'deposit_' + datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        deposit_in_transfer_wallet = api.deposit_in_transfer_wallet(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id, currency=currency,
                                                                    partnerTransactionId=partner_transaction_id, amount=deposit, apiKey=settings.node_ApiKey)

    def test_03_partner_get_balance_transfer_wallet(self, partner_user_id, currency, deposit, withdraw):
        get_balance_transfer_wallet = api.get_balance_transfer_wallet(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id, currency=currency,
                                                                      apiKey=settings.node_ApiKey)

    def test_04_partner_get_transaction_history(self, partner_user_id, currency, deposit, withdraw):
        get_transaction_history = api.get_transaction_history(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id, currency=currency,
                                                              apiKey=settings.node_ApiKey, periodStart=0, periodEnd=0, type=0)

    def test_05_partner_withdraw_in_transfer_wallet(self, partner_user_id, currency, deposit, withdraw):
        partner_transaction_id = 'withdraw_' + datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        withdraw_in_transfer_wallet = api.withdraw_in_transfer_wallet(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id, currency=currency,
                                                                      partnerTransactionId=partner_transaction_id, amount=withdraw, apiKey=settings.node_ApiKey)
