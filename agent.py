"""
Daily Standup Summarizer Agent
Built with Strands Agents SDK + AWS Bedrock
"""

from strands import Agent, tool


@tool
def format_standup(done: str, doing: str, blockers: str) -> str:
    """
    Formats standup notes into a clean, structured daily standup report.

    Args:
        done: Tasks completed since last standup
        doing: Tasks currently in progress or planned for today
        blockers: Any blockers or issues preventing progress

    Returns:
        A formatted standup report string
    """
    blockers_text = blockers if blockers.strip() else "None"
    return (
        f"📋 **Daily Standup**\n\n"
        f"✅ **Done:**\n{done}\n\n"
        f"🔄 **Doing:**\n{doing}\n\n"
        f"🚧 **Blockers:**\n{blockers_text}"
    )


@tool
def summarize_notes(raw_notes: str) -> str:
    """
    Extracts key points from raw, unstructured work notes.

    Args:
        raw_notes: Unstructured notes or brain dump from the user

    Returns:
        A bullet-point summary of key points
    """
    lines = [line.strip() for line in raw_notes.strip().split("\n") if line.strip()]
    bullets = "\n".join(f"• {line}" for line in lines)
    return f"Key points extracted:\n{bullets}"


# Create the agent
agent = Agent(
    system_prompt="""You are a helpful daily standup assistant for software developers and professionals.

Your job is to help users create clear, concise daily standup updates from their messy notes or free-form text.

When a user gives you their raw notes or work updates:
1. Use the summarize_notes tool to extract key points if the input is unstructured
2. Use the format_standup tool to produce a clean standup report
3. Identify what was done, what is being worked on, and any blockers

Be concise, professional, and friendly. Keep standup updates short and to the point.
If the user doesn't mention blockers, assume there are none.""",
    tools=[format_standup, summarize_notes],
)


def main():
    print("🤖 Daily Standup Summarizer")
    print("=" * 40)
    print("Paste your notes or describe your work, and I'll format your standup.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if not user_input:
            continue

        print("\nAgent: ", end="", flush=True)
        response = agent(user_input)
        print(f"\n{response}\n")
        print("-" * 40)


if __name__ == "__main__":
    main()
