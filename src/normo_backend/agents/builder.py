from langgraph.graph import StateGraph

from normo_backend.agents import meta_data_agent, planner_agent
from normo_backend.models import AgentState


def create_workflow_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("meta_data_extractor", meta_data_agent)

    graph.set_entry_point("meta_data_extractor")
    graph.add_edge("meta_data_extractor", "planner")

    return graph.compile()


graph = create_workflow_graph()
