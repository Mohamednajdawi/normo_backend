from langgraph.graph import END, StateGraph

from normo_backend.agents import (meta_data_agent, pdf_selector_agent,
                                  planner_agent, summarizer_agent)
from normo_backend.models import AgentState


def create_workflow_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("pdf_selector", pdf_selector_agent)
    graph.add_node("meta_data_extractor", meta_data_agent)
    graph.add_node("summarizer", summarizer_agent)

    graph.set_entry_point("meta_data_extractor")
    graph.add_edge("meta_data_extractor", "planner")
    graph.add_conditional_edges(
        "planner",
        lambda state: state.steps[0],
        {
            "retrieve_pdfs": "pdf_selector",
            "summarize": "summarizer",
        },
    )
    graph.add_edge("pdf_selector", "planner")
    graph.add_edge("summarizer", END)

    return graph.compile()


graph = create_workflow_graph()
