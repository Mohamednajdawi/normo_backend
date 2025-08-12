from normo_backend.models import AgentState
from normo_backend.prompts import SUMMARIZER_SYSTEM_PROMPT
from normo_backend.utils import get_default_chat_model
from normo_backend.utils.trimer import extract_json

llm = get_default_chat_model(model="gpt-4o-mini", temperature=0.2)


def summarizer_agent(state: AgentState) -> AgentState:
    prompt = SUMMARIZER_SYSTEM_PROMPT.format(
        user_query=state.user_query, summary=state.summary
    )
    response = llm.invoke(prompt)
    state.summary = extract_json(response.content)["summary"]
    state.memory.append(
        {
            "role": "summarizer_agent",
            "content": state.summary,
        }
    )
    return state
