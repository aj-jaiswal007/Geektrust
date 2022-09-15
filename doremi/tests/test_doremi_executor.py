from unittest import TestCase

from src.doremi_executor import DoremiExecutor


class TestDoremiExecutor(TestCase):
    def test_all_free_subscription(self):
        ip = [
            "START_SUBSCRIPTION 05-02-2022",
            "ADD_SUBSCRIPTION MUSIC FREE",
            "ADD_SUBSCRIPTION VIDEO FREE",
            "ADD_SUBSCRIPTION PODCAST FREE",
            "PRINT_RENEWAL_DETAILS",
        ]
        expected_result = [
            "RENEWAL_REMINDER MUSIC 23-02-2022",
            "RENEWAL_REMINDER VIDEO 23-02-2022",
            "RENEWAL_REMINDER PODCAST 23-02-2022",
            "RENEWAL_AMOUNT 0"
        ]
        executor = DoremiExecutor()
        executor.execute(command_lines=ip)
        self.assertEqual(executor.context.results, expected_result)

    def test_all_free_subscription_and_topup(self):
        ip = [
            "START_SUBSCRIPTION 05-02-2022",
            "ADD_SUBSCRIPTION MUSIC FREE",
            "ADD_SUBSCRIPTION VIDEO FREE",
            "ADD_SUBSCRIPTION PODCAST FREE",
            "ADD_TOPUP FOUR_DEVICE 2",
            "PRINT_RENEWAL_DETAILS",
        ]
        expected_result = [
            "RENEWAL_REMINDER MUSIC 23-02-2022",
            "RENEWAL_REMINDER VIDEO 23-02-2022",
            "RENEWAL_REMINDER PODCAST 23-02-2022",
            "RENEWAL_AMOUNT 100"
        ]
        executor = DoremiExecutor()
        executor.execute(command_lines=ip)
        self.assertEqual(executor.context.results, expected_result)

    def test_invalid_date(self):
        ip = [
            "START_SUBSCRIPTION 05-13-2022",
            "ADD_SUBSCRIPTION MUSIC FREE",
            "ADD_TOPUP FOUR_DEVICE 2",
            "PRINT_RENEWAL_DETAILS",
        ]
        expected_result = [
            'INVALID_DATE',
            'ADD_SUBSCRIPTION_FAILED INVALID_DATE',
            'ADD_TOPUP_FAILED INVALID_DATE',
            'SUBSCRIPTIONS_NOT_FOUND'
        ]
        executor = DoremiExecutor()
        executor.execute(command_lines=ip)
        self.assertEqual(executor.context.results, expected_result)

    def test_duplicate_subscription(self):
        ip = [
            "START_SUBSCRIPTION 05-12-2022",
            "ADD_SUBSCRIPTION MUSIC PERSONAL",
            "ADD_SUBSCRIPTION MUSIC PREMIUM",
            "PRINT_RENEWAL_DETAILS",
        ]
        expected_result = [
            "ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY",
            "RENEWAL_REMINDER MUSIC 26-12-2022",
            "RENEWAL_AMOUNT 100"
        ]
        executor = DoremiExecutor()
        executor.execute(command_lines=ip)
        self.assertEqual(executor.context.results, expected_result)

    def test_duplicate_topup(self):
        ip = [
            "START_SUBSCRIPTION 05-12-2022",
            "ADD_SUBSCRIPTION MUSIC PREMIUM",
            "ADD_TOPUP FOUR_DEVICE 2",
            "ADD_TOPUP TEN_DEVICE 2",
            "PRINT_RENEWAL_DETAILS",
        ]
        expected_result = [
            "ADD_TOPUP_FAILED DUPLICATE_TOPUP",
            "RENEWAL_REMINDER MUSIC 23-02-2023",
            "RENEWAL_AMOUNT 350"
        ]
        executor = DoremiExecutor()
        executor.execute(command_lines=ip)
        self.assertEqual(executor.context.results, expected_result)

    def test_subscription_not_found(self):
        ip = [
            "START_SUBSCRIPTION 05-12-2022",
            "ADD_TOPUP FOUR_DEVICE 2",
            "PRINT_RENEWAL_DETAILS",
        ]
        expected_result = [
            "ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND",
            "SUBSCRIPTIONS_NOT_FOUND"
        ]
        executor = DoremiExecutor()
        executor.execute(command_lines=ip)
        self.assertEqual(executor.context.results, expected_result)
