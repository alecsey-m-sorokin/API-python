import hashlib
import json
from datetime import datetime
from loguru import logger
import requests
from config import settings
from locators import APIPartnerData, TransferWallet


class APITransferWallet:

    @staticmethod
    def add_transfer_wallet(**data):
        """
        Add transfer wallet
        :param data:
        :return: response
        """
        if settings.stand_url_branch != "":
            stand_url = settings.stand_url_branch
        else:
            stand_url = settings.stand_url

        _hash = hashlib.md5(('AddTransferWallet/' + data['clientGuid'] + data['partnerUserId'] + data['currency'] + data['apiKey']).encode('utf-8')).hexdigest()
        logger.info(f'hash_AddTransferWallet = {_hash}')
        params_add_transfer_wallet = {
            'Hash': _hash,
            'ClientGuid': data['clientGuid'],
            'PartnerUserId': data['partnerUserId'],
            'Currency': data['currency']
        }
        logger.info(f'params_add_transfer_wallet = {json.dumps(params_add_transfer_wallet, indent=2)}')
        response = requests.post(stand_url + TransferWallet.addTransferWallet_Url, json=params_add_transfer_wallet, headers={'Connection': 'close'})
        logger.info(response.url)
        assert response.status_code == 200, f'error getting data for AddTransferWallet, status code = {response.status_code}'
        logger.info(f'response_add_transfer_wallet = {json.dumps(response.json(), indent=2)}')
        logger.info(f'response_add_transfer_wallet_status_code = {response.status_code}')
        return response

    @staticmethod
    def deposit_in_transfer_wallet(**data):
        """
         Deposit in transfer wallet
        :param data:
        :return: response
       """
        if settings.stand_url_branch != "":
            stand_url = settings.stand_url_branch
        else:
            stand_url = settings.stand_url

        _hash = hashlib.md5(
            ('DepositInTransferWallet/' + data['clientGuid'] + data['partnerUserId'] + data['currency'] + data['partnerTransactionId'] + data['amount'] + data['apiKey']).encode(
                'utf-8')).hexdigest()
        logger.info(f'hash_DepositInTransferWallet = {_hash}')
        params_deposit_in_transfer_wallet = {
            'Hash': _hash,
            'ClientGuid': data['clientGuid'],
            'PartnerUserId': data['partnerUserId'],
            'Currency': data['currency'],
            'PartnerTransactionId': data['partnerTransactionId'],
            'Amount': data['amount']
        }
        logger.info(f'params_deposit_in_transfer_wallet = {json.dumps(params_deposit_in_transfer_wallet, indent=2)}')
        response = requests.post(stand_url + TransferWallet.depositInTransferWallet_Url, json=params_deposit_in_transfer_wallet, headers={'Connection': 'close'})
        logger.info(response.url)
        assert response.status_code == 200, f'error getting data for DepositInTransferWallet, status code = {response.status_code}'
        logger.info(f'response_deposit_in_transfer_wallet = {json.dumps(response.json(), indent=2)}')
        logger.info(f'response_deposit_in_transfer_wallet_status_code = {response.status_code}')
        return response

    @staticmethod
    def get_balance_transfer_wallet(**data):
        """
        Get balance transfer wallet
        :param data:
        :return: response
        """
        if settings.stand_url_branch != "":
            stand_url = settings.stand_url_branch
        else:
            stand_url = settings.stand_url

        _hash = hashlib.md5(('GetBalanceTransferWallet/' + data['clientGuid'] + data['partnerUserId'] + data['currency'] + data['apiKey']).encode('utf-8')).hexdigest()
        logger.info(f'hash_GetBalanceTransferWallet = {_hash}')
        params_get_balance_transfer_wallet = {
            'Hash': _hash,
            'ClientGuid': data['clientGuid'],
            'PartnerUserId': data['partnerUserId'],
            'Currency': data['currency']
        }
        logger.info(f'params_get_balance_transfer_wallet = {json.dumps(params_get_balance_transfer_wallet, indent=2)}')
        response = requests.post(stand_url + TransferWallet.getBalanceTransferWallet_Url, json=params_get_balance_transfer_wallet, headers={'Connection': 'close'}, verify=False)
        logger.info(response.url)
        assert response.status_code == 200, f'error getting data for GetBalanceTransferWallet, status code = {response.status_code} '
        logger.info(f'response_get_balance_transfer_wallet = {json.dumps(response.json(), indent=2)}')
        logger.info(f'response_get_balance_transfer_wallet = {response.status_code}')
        return response

    @staticmethod
    def get_transaction_history(**data):
        """
        Get transaction history
        :param data:
        :return: response
        """
        if settings.stand_url_branch != "":
            stand_url = settings.stand_url_branch
        else:
            stand_url = settings.stand_url

        _hash = hashlib.md5(('GetTransactionHistory/' + data['clientGuid'] + data['partnerUserId'] + data['currency'] + data['apiKey']).encode('utf-8')).hexdigest()
        logger.info(f'hash_GetTransactionHistory = {_hash}')
        params_get_transaction_history = {
            'Hash': _hash,
            'ClientGuid': data['clientGuid'],
            'PartnerUserId': data['partnerUserId'],
            'Currency': data['currency'],
            'PeriodStart': data['periodStart'],
            'PeriodEnd': data['periodEnd'],
            'Type': data['type']
        }
        logger.info(f'params_get_transaction_history = {json.dumps(params_get_transaction_history, indent=2)}')
        response = requests.post(stand_url + TransferWallet.getTransactionHistory_Url, json=params_get_transaction_history, headers={'Connection': 'close'}, verify=False)
        logger.info(response.url)
        assert response.status_code == 200, f'error getting data for GetTransactionHistory, status code = {response.status_code}'
        logger.info(f'response_get_transaction_history = {json.dumps(response.json(), indent=2)}')
        logger.info(f'response_get_transaction_history_status_code = {response.status_code}')
        return response

    @staticmethod
    def withdraw_in_transfer_wallet(**data):
        """
        Withdraw in transfer wallet
        :param data:
        :return: response
        """
        if settings.stand_url_branch != "":
            stand_url = settings.stand_url_branch
        else:
            stand_url = settings.stand_url

        _hash = hashlib.md5(
            ('WithdrawInTransferWallet/' + data['clientGuid'] + data['partnerUserId'] + data['currency'] + data['partnerTransactionId'] + data['amount'] + data['apiKey']).encode(
                'utf-8')).hexdigest()
        logger.info(f'hash_WithdrawInTransferWallet = {_hash}')
        params_withdraw_in_transfer_wallet = {
            'Hash': _hash,
            'ClientGuid': data['clientGuid'],
            'PartnerUserId': data['partnerUserId'],
            'Currency': data['currency'],
            'PartnerTransactionId': data['partnerTransactionId'],
            'Amount': data['amount']
        }
        logger.info(f'params_withdraw_in_transfer_wallet = {json.dumps(params_withdraw_in_transfer_wallet, indent=2)}')
        response = requests.post(stand_url + TransferWallet.withdrawInTransferWallet_Url, json=params_withdraw_in_transfer_wallet, headers={'Connection': 'close'})
        logger.info(response.url)
        assert response.status_code == 200, f'error getting data for WithdrawInTransferWallet, status code = {response.status_code}'
        logger.info(f'response_withdraw_in_transfer_wallet = {json.dumps(response.json(), indent=2)}')
        logger.info(f'response_response_withdraw_in_transfer_wallet_status_code = {response.status_code}')
        return response


if __name__ == "__main__":
    partner_user_id = '665544332211'
    currency = 'TRY'
    deposit = '5'
    withdraw = '6'

    # add_transfer_wallet = APITransferWallet.add_transfer_wallet(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id,
    #                                                             currency=currency, apiKey=settings.node_ApiKey)
    #
    # partner_transaction_id = 'deposit_' + datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    # deposit_in_transfer_wallet = APITransferWallet.deposit_in_transfer_wallet(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id,
    #                                                                           currency=currency, partnerTransactionId=partner_transaction_id, amount=deposit,
    #                                                                           apiKey=settings.node_ApiKey)
    #
    get_balance_transfer_wallet = APITransferWallet.get_balance_transfer_wallet(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id,
                                                                                currency=currency, apiKey=settings.node_ApiKey)
    #
    # get_transaction_history = APITransferWallet.get_transaction_history(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id, currency=currency,
    #                                                                     apiKey=settings.node_ApiKey, periodStart=0, periodEnd=0, type=0)
    #
    # partner_transaction_id = 'withdraw_' + datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    # withdraw_in_transfer_wallet = APITransferWallet.withdraw_in_transfer_wallet(clientGuid=settings.node_transfer_wallet_ClientGuid, partnerUserId=partner_user_id,
    #                                                                             currency=currency, partnerTransactionId=partner_transaction_id,
    #                                                                             amount=withdraw, apiKey=settings.node_ApiKey)
