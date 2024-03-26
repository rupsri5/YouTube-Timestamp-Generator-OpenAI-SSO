from typing import Optional

from app.openai_helper.models import GPTConfig
from app.openai_helper.prompts import SYSTEM_PROMPT_TIMESTAMP, USER_PROMPT_TIMESTAMP

from app.openai_helper.utility import create_chat_llm_chain


class ChainFactory:

    def __init__(self, config: Optional[GPTConfig] = None):
        if config is None:
            config = GPTConfig()
        self.config = config

    def timestamp_chain(self):
        return create_chat_llm_chain(
            system_template = SYSTEM_PROMPT_TIMESTAMP,
            user_template = USER_PROMPT_TIMESTAMP,
            system_variables = [],
            user_variables = ["transcript"],
            config = self.config
        )
