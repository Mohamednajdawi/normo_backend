from normo_backend.models import AgentState
from normo_backend.prompts import PLANNER_SYSTEM_PROMPT
from normo_backend.utils import get_default_chat_model
from normo_backend.utils.trimer import extract_json

llm = get_default_chat_model(model="gpt-4o-mini", temperature=0.2)


def planner_agent(state: AgentState) -> AgentState:
    prompt = PLANNER_SYSTEM_PROMPT.format(user_query=state.user_query)
    response = llm.invoke(prompt)
    state.steps = extract_json(response.content)["steps"]
    print(state.steps)
    return state
