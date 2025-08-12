from normo_backend.models import AgentState
from normo_backend.prompts import PDF_SELECTOR_SYSTEM_PROMPT
from normo_backend.utils import get_default_chat_model
from normo_backend.utils.trimer import extract_json

llm = get_default_chat_model(model="gpt-4o-mini", temperature=0.2)


def pdf_selector_agent(state: AgentState) -> AgentState:
    prompt = PDF_SELECTOR_SYSTEM_PROMPT.format(user_query=state.user_query)
    response = llm.invoke(prompt)
    state.pdf_names = extract_json(response.content)["pdf_names"]
    state.memory.append(
        {
            "role": "pdf_selector_agent",
            "content": state.pdf_names,
        }
    )
    return state
