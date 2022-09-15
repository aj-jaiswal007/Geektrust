from typing import List

from src.dtos import SubscriptionContext
from src.enums import InputCommand, PlanCategory, PlanType, TopUpType
from src.exceptions import InvalidCommandError
from src.handlers import (AddSubscriptionHandler, AddTopUpHandler,
                          PrintRenewalDetailsHandler, StartSubscriptionHandler)


class DoremiExecutor:
    def __init__(self) -> None:
        self.context = SubscriptionContext()
        self._start_subscription_handler = StartSubscriptionHandler(self.context)
        self._add_subscription_handler = AddSubscriptionHandler(self.context)
        self._add_topup_handler = AddTopUpHandler(self.context)
        self._print_renewal_details_handler = PrintRenewalDetailsHandler(self.context)

    def _execute_command(self, command: str, *args):
        """Main handler for all doremi commands

        Args:
            command (str): InputCommand
        """
        cmd = InputCommand(command)

        try:
            if cmd == InputCommand.START_SUBSCRIPTION:
                self._start_subscription_handler.handle(start_date=args[0])

            elif cmd == InputCommand.ADD_SUBSCRIPTION:
                self._add_subscription_handler.handle(
                    category=PlanCategory(args[0]), plan_type=PlanType(args[1])
                )
            elif cmd == InputCommand.ADD_TOPUP:
                # topup
                self._add_topup_handler.handle(
                    topup_type=TopUpType(args[0]), units=int(args[1])
                )
            else:
                self._print_renewal_details_handler.handle()

        except InvalidCommandError as e:
            self.context.results.append(str(e))

    def execute(self, command_lines: List[str]):
        """
        - Takes a list of command lines
        - Executes all commands and prints results

        Args:
            command_lines (List[str]): List of DoReMi commands
        """
        for command_line in command_lines:
            args = command_line.strip("\n").split(" ")
            self._execute_command(*args)
        
        self.print_results()

    def print_results(self):
        """Prints final results"""
        print("\n".join(self.context.results))
