import asyncio
from datetime import datetime, timedelta
import sys

# Infrastructure
from infrastructure.event_bus import InfrastructureEventBus as EventBus
# Domain
from core.models import StateSnapshot, Itinerary, Task
from core.enums import TaskStatus, CompletionType
from core.events import DisruptionEvent
# Agents
from agents.state_agent import StateAgent
from agents.monitoring_agent import MonitoringAgent
from agents.reoptimization_agent import ReoptimizationAgent
from agents.companion_agent import CompanionAgent
from orchestrator.orchestrator import OrchestratorAgent

sys.stdout = open("e:/tbo/execution.log", "w", encoding="utf-8")

async def main():
    print("=== Agentic Itinerary System (Phase 4: Strict Domain) Initializing ===")
    
    bus = EventBus()
    
    start_time = datetime.now()
    initial_tasks = [
        Task(id="1", title="Breakfast at Tiffany's", start_time=start_time + timedelta(hours=1), end_time=start_time + timedelta(hours=2), location="Downtown"),
        Task(id="2", title="Museum Tour", start_time=start_time + timedelta(hours=3), end_time=start_time + timedelta(hours=5), location="Museum District"),
        Task(id="3", title="Dinner Reservation", start_time=start_time + timedelta(hours=6), end_time=start_time + timedelta(hours=8), location="Italian Restaurant"),
    ]
    initial_snapshot = StateSnapshot(
        current_time=start_time,
        itinerary=Itinerary(tasks=initial_tasks)
    )
    
    state_agent = StateAgent(initial_snapshot)
    monitor_agent = MonitoringAgent()
    planner_agent = ReoptimizationAgent()
    companion_agent = CompanionAgent()
    
    orchestrator = OrchestratorAgent(bus, state_agent, monitor_agent, planner_agent, companion_agent)
    
    print(f"=== System Ready. Start Time: {start_time.strftime('%H:%M')} ===")
    
    print("\n--- ⏩ Advancing Time by 2.5 Hours ---")
    state_agent.advance_time(150) 
    
    await orchestrator.process_cycle()
    
    s = state_agent.get_state_snapshot()
    # Find active/completed
    t1 = next((t for t in s.itinerary.tasks if t.id == "1"), None)
    if t1:
        print(f"Task 1 Status: {t1.status}")
    
    print("\n--- ✅ User Confirms Task 1 (With Rollback) ---")
    if t1 and t1.status == TaskStatus.MISSED:
        print("[Main] Task is MISSED. Rolling back first...")
        state_agent.rollback_implicit("1")
    state_agent.confirm_task("1")
    
    print("\n--- 💥 Injecting Major Disruption (45m Delay) ---")
    disruption = monitor_agent.simulate_delay(45)
    await bus.publish("INJECT_DISRUPTION", disruption)
    
    await orchestrator.process_cycle()
    
    final_state = state_agent.get_state_snapshot()
    print("\n=== Final Schedule ===")
    for t in final_state.itinerary.tasks:
        print(f"{t.start_time.strftime('%H:%M')} - {t.title} ({t.status})")

if __name__ == "__main__":
    asyncio.run(main())
