from normo_backend.models import AgentState
from normo_backend.prompts import META_DATA_EXTRACTOR_SYSTEM_PROMPT
from normo_backend.utils import get_default_chat_model
from normo_backend.utils.trimer import extract_json


def meta_data_agent(state: AgentState) -> AgentState:
    prompt = META_DATA_EXTRACTOR_SYSTEM_PROMPT.format(user_query=state.user_query)
    response = get_default_chat_model(model="gpt-4o-mini", temperature=0.2).invoke(
        prompt
    )
    state.meta_data = extract_json(response.content)["meta_data"]
    state.memory.append(
        {
            "role": "meta_data_agent",
            "content": state.meta_data,
        }
    )
    return state
