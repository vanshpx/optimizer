from datetime import timedelta
from typing import List
from core.models import StateSnapshot, Task, TaskStatus
from core.enums import DisruptionType
from core.events import DisruptionEvent

class MonitoringAgent:
    def detect_disruptions(self, state: StateSnapshot) -> List[DisruptionEvent]:
        disruptions = []
        current_time = state.current_time
        
        for task in state.itinerary.tasks:
            if task.status == TaskStatus.PLANNED:
                # If we are 15 mins past start time
                if current_time > task.start_time + timedelta(minutes=15):
                    print(f"[Monitoring] ⚠️ Potential Disruption: Task {task.id} late start.")
                    disruptions.append(DisruptionEvent(
                        type=DisruptionType.LATE_ARRIVAL,
                        task_id=task.id,
                        detected_at=current_time,
                        metadata={"severity": "HIGH"}
                    ))
        return disruptions
    
    def simulate_delay(self, minutes: int) -> DisruptionEvent:
        print(f"[Monitoring] 🚦 SIMULATION: Creating {minutes} min delay signal.")
        # Simulating external delay (Traffic)
        return DisruptionEvent(
            type=DisruptionType.DELAY,
            task_id=None,
            detected_at=None, # Filled by caller or now?
            # detected_at is datetime.
            # I need datetime.now()
            metadata={"delay_minutes": minutes, "severity": "MEDIUM"}
        )
