from dataclasses import dataclass

from core.history import HistoryManager
from core.ollama_client import OllamaClient
from core.chat_session import ChatSession
from commands.dispatcher import CommandDispatcher
from ui.console import ConsoleUI


@dataclass
class ApplicationContext:

    console: ConsoleUI

    history: HistoryManager

    ollama: OllamaClient

    chat: ChatSession

    dispatcher: CommandDispatcher